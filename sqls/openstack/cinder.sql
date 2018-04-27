CREATE TABLE `driver_initiator_data` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `initiator` varchar(255) NOT NULL,
  `namespace` varchar(255) NOT NULL,
  `key` varchar(255) NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `initiator` (`initiator`,`namespace`,`key`),
  KEY `ix_driver_initiator_data_initiator` (`initiator`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `quota_classes` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) DEFAULT NULL,
  `resource` varchar(255) DEFAULT NULL,
  `hard_limit` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_quota_classes_class_name` (`class_name`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

CREATE TABLE `quota_usages` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` varchar(255) DEFAULT NULL,
  `resource` varchar(255) DEFAULT NULL,
  `in_use` int(11) NOT NULL,
  `reserved` int(11) NOT NULL,
  `until_refresh` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_quota_usages_project_id` (`project_id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

CREATE TABLE `reservations` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `usage_id` int(11) NOT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `resource` varchar(255) DEFAULT NULL,
  `delta` int(11) NOT NULL,
  `expire` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usage_id` (`usage_id`),
  KEY `ix_reservations_project_id` (`project_id`),
  KEY `reservations_deleted_expire_idx` (`deleted`,`expire`),
  CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`usage_id`) REFERENCES `quota_usages` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=855 DEFAULT CHARSET=utf8;

CREATE TABLE `backups` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `volume_id` varchar(36) NOT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `host` varchar(255) DEFAULT NULL,
  `availability_zone` varchar(255) DEFAULT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `display_description` varchar(255) DEFAULT NULL,
  `container` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `fail_reason` varchar(255) DEFAULT NULL,
  `service_metadata` varchar(255) DEFAULT NULL,
  `service` varchar(255) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `object_count` int(11) DEFAULT NULL,
  `parent_id` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `consistencygroups` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `host` varchar(255) DEFAULT NULL,
  `availability_zone` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `volume_type_id` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `cgsnapshot_id` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `cgsnapshots` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `consistencygroup_id` varchar(36) NOT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `consistencygroup_id` (`consistencygroup_id`),
  CONSTRAINT `cgsnapshots_ibfk_1` FOREIGN KEY (`consistencygroup_id`) REFERENCES `consistencygroups` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `encryption` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `cipher` varchar(255) DEFAULT NULL,
  `control_location` varchar(255) NOT NULL,
  `key_size` int(11) DEFAULT NULL,
  `provider` varchar(255) NOT NULL,
  `volume_type_id` varchar(36) NOT NULL,
  `encryption_id` varchar(36) NOT NULL,
  PRIMARY KEY (`encryption_id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `migrate_version` (
  `repository_id` varchar(250) NOT NULL,
  `repository_path` text DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`repository_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `quality_of_service_specs` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `specs_id` varchar(36) DEFAULT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `specs_id` (`specs_id`),
  CONSTRAINT `quality_of_service_specs_ibfk_1` FOREIGN KEY (`specs_id`) REFERENCES `quality_of_service_specs` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `volume_types` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `qos_specs_id` varchar(36) DEFAULT NULL,
  `is_public` tinyint(1) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `qos_specs_id` (`qos_specs_id`),
  CONSTRAINT `volume_types_ibfk_1` FOREIGN KEY (`qos_specs_id`) REFERENCES `quality_of_service_specs` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `volume_type_extra_specs` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `volume_type_id` varchar(36) NOT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_type_extra_specs_ibfk_1` (`volume_type_id`),
  CONSTRAINT `volume_type_extra_specs_ibfk_1` FOREIGN KEY (`volume_type_id`) REFERENCES `volume_types` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

CREATE TABLE `volume_type_projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `volume_type_id` varchar(36) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `volume_type_id` (`volume_type_id`,`project_id`,`deleted`),
  CONSTRAINT `volume_type_projects_ibfk_1` FOREIGN KEY (`volume_type_id`) REFERENCES `volume_types` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `quotas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `resource` varchar(255) NOT NULL,
  `hard_limit` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `services` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` varchar(255) DEFAULT NULL,
  `binary` varchar(255) DEFAULT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `report_count` int(11) NOT NULL,
  `disabled` tinyint(1) DEFAULT NULL,
  `availability_zone` varchar(255) DEFAULT NULL,
  `disabled_reason` varchar(255) DEFAULT NULL,
  `modified_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1)),
  CONSTRAINT `CONSTRAINT_2` CHECK (`disabled` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

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

CREATE TABLE `volume_metadata` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `volume_id` varchar(36) NOT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_id` (`volume_id`),
  CONSTRAINT `volume_metadata_ibfk_1` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=667 DEFAULT CHARSET=utf8;


CREATE TABLE `iscsi_targets` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `target_num` int(11) DEFAULT NULL,
  `host` varchar(255) DEFAULT NULL,
  `volume_id` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_id` (`volume_id`),
  CONSTRAINT `iscsi_targets_ibfk_1` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `transfers` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `volume_id` varchar(36) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `crypt_hash` varchar(255) DEFAULT NULL,
  `expires_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_id` (`volume_id`),
  CONSTRAINT `transfers_ibfk_1` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `volume_admin_metadata` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `volume_id` varchar(36) NOT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_id` (`volume_id`),
  CONSTRAINT `volume_admin_metadata_ibfk_1` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;

CREATE TABLE `volume_attachment` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `volume_id` varchar(36) NOT NULL,
  `attached_host` varchar(255) DEFAULT NULL,
  `instance_uuid` varchar(36) DEFAULT NULL,
  `mountpoint` varchar(255) DEFAULT NULL,
  `attach_time` datetime DEFAULT NULL,
  `detach_time` datetime DEFAULT NULL,
  `attach_mode` varchar(36) DEFAULT NULL,
  `attach_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_id` (`volume_id`),
  CONSTRAINT `volume_attachment_ibfk_1` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `snapshots` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` varchar(36) NOT NULL,
  `volume_id` varchar(36) NOT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `project_id` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `progress` varchar(255) DEFAULT NULL,
  `volume_size` int(11) DEFAULT NULL,
  `scheduled_at` datetime DEFAULT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `display_description` varchar(255) DEFAULT NULL,
  `provider_location` varchar(255) DEFAULT NULL,
  `encryption_key_id` varchar(36) DEFAULT NULL,
  `volume_type_id` varchar(36) DEFAULT NULL,
  `cgsnapshot_id` varchar(36) DEFAULT NULL,
  `provider_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `snapshots_volume_id_fkey` (`volume_id`),
  KEY `cgsnapshot_id` (`cgsnapshot_id`),
  CONSTRAINT `snapshots_ibfk_1` FOREIGN KEY (`cgsnapshot_id`) REFERENCES `cgsnapshots` (`id`),
  CONSTRAINT `snapshots_volume_id_fkey` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `snapshot_metadata` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `snapshot_id` varchar(36) NOT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `snapshot_id` (`snapshot_id`),
  CONSTRAINT `snapshot_metadata_ibfk_1` FOREIGN KEY (`snapshot_id`) REFERENCES `snapshots` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `volume_glance_metadata` (
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `volume_id` varchar(36) DEFAULT NULL,
  `snapshot_id` varchar(36) DEFAULT NULL,
  `key` varchar(255) DEFAULT NULL,
  `value` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `volume_id` (`volume_id`),
  KEY `snapshot_id` (`snapshot_id`),
  CONSTRAINT `volume_glance_metadata_ibfk_1` FOREIGN KEY (`volume_id`) REFERENCES `volumes` (`id`),
  CONSTRAINT `volume_glance_metadata_ibfk_2` FOREIGN KEY (`snapshot_id`) REFERENCES `snapshots` (`id`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`deleted` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=1501 DEFAULT CHARSET=utf8;
