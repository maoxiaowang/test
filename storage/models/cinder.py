# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.manager import Manager
from django.utils.translation import ugettext_lazy as _


class Backups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    volume_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    container = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    fail_reason = models.CharField(max_length=255, blank=True, null=True)
    service_metadata = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    object_count = models.IntegerField(blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backups'
        default_permissions = ()
        app_label = 'cinder'


class Cgsnapshots(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    consistencygroup = models.ForeignKey('Consistencygroups', models.DO_NOTHING)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cgsnapshots'
        default_permissions = ()
        app_label = 'cinder'


class Consistencygroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    volume_type_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    cgsnapshot_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consistencygroups'
        default_permissions = ()
        app_label = 'cinder'


class DriverInitiatorData(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    initiator = models.CharField(max_length=255)
    namespace = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'driver_initiator_data'
        unique_together = (('initiator', 'namespace', 'key'),)
        default_permissions = ()
        app_label = 'cinder'


class Encryption(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    cipher = models.CharField(max_length=255, blank=True, null=True)
    control_location = models.CharField(max_length=255)
    key_size = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255)
    volume_type_id = models.CharField(max_length=36)
    encryption_id = models.CharField(primary_key=True, max_length=36)

    class Meta:
        managed = False
        db_table = 'encryption'
        default_permissions = ()
        app_label = 'cinder'


class IscsiTargets(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    target_num = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iscsi_targets'
        default_permissions = ()
        app_label = 'cinder'


class MigrateVersion(models.Model):
    repository_id = models.CharField(primary_key=True, max_length=250)
    repository_path = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrate_version'
        default_permissions = ()
        app_label = 'cinder'


class QualityOfServiceSpecs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    specs = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quality_of_service_specs'
        default_permissions = ()
        app_label = 'cinder'


class QuotaClasses(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    hard_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quota_classes'
        default_permissions = ()
        app_label = 'cinder'


class QuotaUsages(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    in_use = models.IntegerField()
    reserved = models.IntegerField()
    until_refresh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quota_usages'
        default_permissions = ()
        app_label = 'cinder'


class Quotas(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255)
    hard_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotas'
        default_permissions = ()
        app_label = 'cinder'


class Reservations(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    usage = models.ForeignKey(QuotaUsages, models.DO_NOTHING)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    delta = models.IntegerField()
    expire = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservations'
        default_permissions = ()
        app_label = 'cinder'


class Services(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    binary = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    report_count = models.IntegerField()
    disabled = models.IntegerField(blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    disabled_reason = models.CharField(max_length=255, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'
        default_permissions = ()
        app_label = 'cinder'


class SnapshotMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    snapshot = models.ForeignKey('Snapshots', models.DO_NOTHING)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snapshot_metadata'
        default_permissions = ()
        app_label = 'cinder'


class Snapshots(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    progress = models.CharField(max_length=255, blank=True, null=True)
    volume_size = models.IntegerField(blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    provider_location = models.CharField(max_length=255, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=36, blank=True, null=True)
    volume_type_id = models.CharField(max_length=36, blank=True, null=True)
    cgsnapshot = models.ForeignKey(Cgsnapshots, models.DO_NOTHING, blank=True, null=True)
    provider_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snapshots'
        default_permissions = ()
        app_label = 'cinder'


class Transfers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    crypt_hash = models.CharField(max_length=255, blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfers'
        default_permissions = ()
        app_label = 'cinder'


class VolumeAdminMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_admin_metadata'
        default_permissions = ()
        app_label = 'cinder'


class VolumeAttachment(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING)
    attached_host = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    mountpoint = models.CharField(max_length=255, blank=True, null=True)
    attach_time = models.DateTimeField(blank=True, null=True)
    detach_time = models.DateTimeField(blank=True, null=True)
    attach_mode = models.CharField(max_length=36, blank=True, null=True)
    attach_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_attachment'
        default_permissions = ()
        app_label = 'cinder'


class VolumeGlanceMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING, blank=True, null=True)
    snapshot = models.ForeignKey(Snapshots, models.DO_NOTHING, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_glance_metadata'
        default_permissions = ()
        app_label = 'cinder'


class VolumeMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_metadata'
        default_permissions = ()
        app_label = 'cinder'


class VolumeTypeExtraSpecs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    volume_type = models.ForeignKey('VolumeTypes', models.DO_NOTHING)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_type_extra_specs'
        default_permissions = ()
        app_label = 'cinder'


class VolumeTypeProjects(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    volume_type = models.ForeignKey('VolumeTypes', models.DO_NOTHING, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_type_projects'
        unique_together = (('volume_type', 'project_id', 'deleted'),)
        default_permissions = ()
        app_label = 'cinder'


class VolumeTypes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    qos_specs = models.ForeignKey(QualityOfServiceSpecs, models.DO_NOTHING, blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_types'
        default_permissions = ()
        app_label = 'cinder'


class Volumes(models.Model, Manager):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    ec2_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    attach_status = models.CharField(max_length=255, blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    launched_at = models.DateTimeField(blank=True, null=True)
    terminated_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    provider_location = models.CharField(max_length=256, blank=True, null=True)
    provider_auth = models.CharField(max_length=256, blank=True, null=True)
    snapshot_id = models.CharField(max_length=36, blank=True, null=True)
    volume_type_id = models.CharField(max_length=36, blank=True, null=True)
    source_volid = models.CharField(max_length=36, blank=True, null=True)
    bootable = models.IntegerField(blank=True, null=True)
    provider_geometry = models.CharField(max_length=255, blank=True, null=True)
    field_name_id = models.CharField(db_column='_name_id', max_length=36, blank=True, null=True)  # Field renamed because it started with '_'.
    encryption_key_id = models.CharField(max_length=36, blank=True, null=True)
    migration_status = models.CharField(max_length=255, blank=True, null=True)
    replication_status = models.CharField(max_length=255, blank=True, null=True)
    replication_extended_status = models.CharField(max_length=255, blank=True, null=True)
    replication_driver_data = models.CharField(max_length=255, blank=True, null=True)
    consistencygroup = models.ForeignKey(Consistencygroups, models.DO_NOTHING, blank=True, null=True)
    provider_id = models.CharField(max_length=255, blank=True, null=True)
    multiattach = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volumes'
        # permissions = (
        #     ('list_volume', _('Can see volume list')),
        #     ('detail_volume', _('Can see volume detail')),
        #     ('add_volume', _('Can add volume')),
        #     ('change_volume', _('Can change volume')),
        #     ('delete_volume', _('Can delete volume')),
        # )
        default_permissions = ()
        app_label = 'cinder'
