# coding=utf-8
"""
Convert DDL to model
"""
import re

example_ddl = '''
CREATE TABLE `volumes` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `ec2_id` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `host` varchar(255) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `availability_zone` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `attach_status` varchar(255) DEFAULT NULL,
  `scheduled_at` datetime DEFAULT NULL,
  `launched_at` datetime DEFAULT NULL,
  `terminated_at` datetime DEFAULT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `display_description` varchar(255) DEFAULT NULL,
  `provider_location` varchar(256) DEFAULT NULL,
  `provider_auth` varchar(256) DEFAULT NULL,
  `snapshot_id` varchar(36) DEFAULT NULL,
  `volume_type_id` varchar(36) DEFAULT NULL,
  `source_volid` varchar(36) DEFAULT NULL,
  `bootable` tinyint(1) DEFAULT NULL,
  `provider_geometry` varchar(255) DEFAULT NULL,
  `_name_id` varchar(36) DEFAULT NULL,
  `encryption_key_id` varchar(36) DEFAULT NULL,
  `migration_status` varchar(255) DEFAULT NULL,
  `replication_status` varchar(255) DEFAULT NULL,
  `replication_extended_status` varchar(255) DEFAULT NULL,
  `replication_driver_data` varchar(255) DEFAULT NULL,
  `consistencygroup_id` varchar(36) DEFAULT NULL,
  `provider_id` varchar(255) DEFAULT NULL,
  `multiattach` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `consistencygroup_id` (`consistencygroup_id`),
  CONSTRAINT `volumes_ibfk_1` FOREIGN KEY (`consistencygroup_id`) REFERENCES `consistencygroups` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''



class NoPrimaryKeyFound(Exception):
    pass


class PrimaryKeyTypeError(Exception):
    pass


class TypeMappingError(Exception):
    pass


def type_mapping(type_name):
    mapping = (
        ('varchar', 'CharField'),
        ('datetime', 'DateTimeField'),
        ('tinyint', 'SmallIntegerField'),
        ('int', 'IntegerField'),
    )
    for item in mapping:
        if item[0] == type_name:
            return item[1]
    raise TypeMappingError


def get_type(type_str):
    # like 'varchar(255)' >> ('varchar', '100'), 'datetime' >> ('datetime', '')
    return re.findall('^(.*?)\(?(\d+)?\)?$', type_str)


def clean(string):
    return string.replace('(', '').replace(')', '').replace('`', '').strip()


def convert(ddl):
    assert isinstance(ddl, str) and ddl.strip().upper().startswith('CREATE TABLE')
    items = re.findall(r'CREATE TABLE\s+`?(.*?)`?\s+\((.*)\)', ddl, re.I | re.S)
    if not items:
        assert ValueError('Incorrect sql format')
    db_name = items[0][0]
    items = items[0][1]

    lines = [line.strip(',').strip() for line in items.splitlines() if line]
    fields = list()

    # get primary key and its types
    pk_name = ''
    pk_type = ()
    for line in lines:
        sl = line.split()
        if len(sl[0]) > 1 and sl[0].upper() == 'PRIMARY' and sl[1].upper() == 'KEY':
            pk_name = clean(sl[2])
    if not pk_name:
        raise NoPrimaryKeyFound
    for line in lines:
        sl = line.split()
        # find primary key
        if clean(sl[0]) == pk_name:
            pk_type_re = get_type(sl[1])
            if pk_type_re:
                pk_type = pk_type_re[0]
    if not pk_type:
        raise PrimaryKeyTypeError

    # generate model
    for line in lines:
        sl = line.split()

        r = ''  # item line

        if sl[0].upper() == 'CONSTRAINT':
            # foreign key or/and check
            if len(sl) > 3 and sl[2] == 'FOREIGN' and sl[3] == 'KEY':
                pass
            if len(sl) > 2 and sl[2] == 'CHECK':
                # deleting_state = (('deleted', 1), ('not_deleted', 0))
                # state = models.IntegerField(choices=deleting_state,
                #                               max_length=32,
                #                              verbose_name=_(deleteing state))
                pass
            # TODO: handle constraint key
            print('[M] %s' % line)
        elif sl[0].upper() == 'KEY':
            # not handle
            continue
        elif sl[0].upper() == 'PRIMARY' and sl[1] == 'KEY':
            # not handle
            continue
        else:
            # for ordinary item
            default_value = None
            for i, item in enumerate(sl):
                if item.upper() == 'DEFAULT':
                    default_value = sl[i+1]
                    break

            other = ''
            if default_value:
                if default_value.upper() == 'NULL':
                    default_value = 'None'
                other += ', default=%s' % default_value

            if clean(sl[0]) == pk_name:
                # primary key
                other += ', primary_key=True'
            if pk_type[1] != '':
                other += ', max_length=%s' % pk_type[1]

            _ = {
                'name': clean(sl[0]),
                'data_type': type_mapping(pk_type[0]),
                'vn': clean(sl[0]),
                'other': other
            }

            r = "%(name)s = models.%(data_type)s(verbose_name=_('%(vn)s')%(other)s)" % _

        if r:
            fields.append(r)

    # class Meta
    result = 'class %s(models.Model):\n' % db_name.capitalize()
    fields = ' '*4 + '\n    '.join(fields)
    meta_class = '\n' + ' '*4 + 'class Meta:\n' + ' '*8 + "db_table='%s'" % db_name
    print(result + fields + '\n' + meta_class)


if __name__ == '__main__':
    convert(example_ddl)
