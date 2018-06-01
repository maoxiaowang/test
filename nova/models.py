# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgentBuilds(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hypervisor = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    architecture = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    md5hash = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_builds'
        unique_together = (('hypervisor', 'os', 'architecture', 'deleted'),)
        default_permissions = ()


class AggregateHosts(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    aggregate = models.ForeignKey('Aggregates', models.DO_NOTHING)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aggregate_hosts'
        unique_together = (('host', 'aggregate', 'deleted'),)
        default_permissions = ()


class AggregateMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    aggregate = models.ForeignKey('Aggregates', models.DO_NOTHING)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aggregate_metadata'
        unique_together = (('aggregate', 'key', 'deleted'),)
        default_permissions = ()


class Aggregates(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aggregates'
        default_permissions = ()


class BlockDeviceMapping(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    delete_on_termination = models.IntegerField(blank=True, null=True)
    snapshot_id = models.CharField(max_length=36, blank=True, null=True)
    volume_id = models.CharField(max_length=36, blank=True, null=True)
    volume_size = models.IntegerField(blank=True, null=True)
    no_device = models.IntegerField(blank=True, null=True)
    connection_info = models.TextField(blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=255, blank=True, null=True)
    destination_type = models.CharField(max_length=255, blank=True, null=True)
    guest_format = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    disk_bus = models.CharField(max_length=255, blank=True, null=True)
    boot_index = models.IntegerField(blank=True, null=True)
    image_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_device_mapping'
        default_permissions = ()


class BwUsageCache(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    start_period = models.DateTimeField()
    last_refreshed = models.DateTimeField(blank=True, null=True)
    bw_in = models.BigIntegerField(blank=True, null=True)
    bw_out = models.BigIntegerField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    last_ctr_in = models.BigIntegerField(blank=True, null=True)
    last_ctr_out = models.BigIntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bw_usage_cache'
        default_permissions = ()


class Cells(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    api_url = models.CharField(max_length=255, blank=True, null=True)
    weight_offset = models.FloatField(blank=True, null=True)
    weight_scale = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_parent = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    transport_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cells'
        unique_together = (('name', 'deleted'),)
        default_permissions = ()


class Certificates(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificates'
        default_permissions = ()


class ComputeNodes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    vcpus = models.IntegerField()
    memory_mb = models.IntegerField()
    local_gb = models.IntegerField()
    vcpus_used = models.IntegerField()
    memory_mb_used = models.IntegerField()
    local_gb_used = models.IntegerField()
    hypervisor_type = models.TextField()
    hypervisor_version = models.IntegerField()
    cpu_info = models.TextField()
    disk_available_least = models.IntegerField(blank=True, null=True)
    free_ram_mb = models.IntegerField(blank=True, null=True)
    free_disk_gb = models.IntegerField(blank=True, null=True)
    current_workload = models.IntegerField(blank=True, null=True)
    running_vms = models.IntegerField(blank=True, null=True)
    hypervisor_hostname = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    host_ip = models.CharField(max_length=39, blank=True, null=True)
    supported_instances = models.TextField(blank=True, null=True)
    pci_stats = models.TextField(blank=True, null=True)
    metrics = models.TextField(blank=True, null=True)
    extra_resources = models.TextField(blank=True, null=True)
    stats = models.TextField(blank=True, null=True)
    numa_topology = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compute_nodes'
        unique_together = (('host', 'hypervisor_hostname', 'deleted'),)
        default_permissions = ()


class ConsolePools(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=39, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    console_type = models.CharField(max_length=255, blank=True, null=True)
    public_hostname = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    compute_host = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'console_pools'
        unique_together = (('host', 'console_type', 'compute_host', 'deleted'),)
        default_permissions = ()


class Consoles(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    pool = models.ForeignKey(ConsolePools, models.DO_NOTHING, blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consoles'
        default_permissions = ()


class DnsDomains(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    domain = models.CharField(primary_key=True, max_length=255)
    scope = models.CharField(max_length=255, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dns_domains'
        default_permissions = ()


class FixedIps(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=39, blank=True, null=True)
    network_id = models.IntegerField(blank=True, null=True)
    allocated = models.IntegerField(blank=True, null=True)
    leased = models.IntegerField(blank=True, null=True)
    reserved = models.IntegerField(blank=True, null=True)
    virtual_interface_id = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_ips'
        unique_together = (('address', 'deleted'),)
        default_permissions = ()


class FloatingIps(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=39, blank=True, null=True)
    fixed_ip_id = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    auto_assigned = models.IntegerField(blank=True, null=True)
    pool = models.CharField(max_length=255, blank=True, null=True)
    interface = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'floating_ips'
        unique_together = (('address', 'deleted'),)
        default_permissions = ()


class InstanceActions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    request_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_actions'
        default_permissions = ()


class InstanceActionsEvents(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    action = models.ForeignKey(InstanceActions, models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_actions_events'
        default_permissions = ()


class InstanceExtra(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid')
    numa_topology = models.TextField(blank=True, null=True)
    pci_requests = models.TextField(blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    vcpu_model = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_extra'
        default_permissions = ()


class InstanceFaults(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    code = models.IntegerField()
    message = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_faults'
        default_permissions = ()


class InstanceGroupMember(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    instance_id = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey('InstanceGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'instance_group_member'
        default_permissions = ()


class InstanceGroupPolicy(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    policy = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey('InstanceGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'instance_group_policy'
        default_permissions = ()


class InstanceGroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_groups'
        unique_together = (('uuid', 'deleted'),)
        default_permissions = ()


class InstanceIdMappings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_id_mappings'
        default_permissions = ()


class InstanceInfoCaches(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    network_info = models.TextField(blank=True, null=True)
    # instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', unique=True)
    instance_uuid = models.OneToOneField(to='Instances', on_delete=models.DO_NOTHING, to_field='uuid')
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_info_caches'
        default_permissions = ()


class InstanceMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_metadata'
        default_permissions = ()


class InstanceSystemMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_uuid = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance_uuid')
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_system_metadata'
        default_permissions = ()


class InstanceTypeExtraSpecs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_type = models.ForeignKey('InstanceTypes', models.DO_NOTHING)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_type_extra_specs'
        unique_together = (('instance_type', 'key', 'deleted'),)
        default_permissions = ()


class InstanceTypeProjects(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_type = models.ForeignKey('InstanceTypes', models.DO_NOTHING)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_type_projects'
        unique_together = (('instance_type', 'project_id', 'deleted'),)
        default_permissions = ()


class InstanceTypes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    memory_mb = models.IntegerField()
    vcpus = models.IntegerField()
    swap = models.IntegerField()
    vcpu_weight = models.IntegerField(blank=True, null=True)
    flavorid = models.CharField(max_length=255, blank=True, null=True)
    rxtx_factor = models.FloatField(blank=True, null=True)
    root_gb = models.IntegerField(blank=True, null=True)
    ephemeral_gb = models.IntegerField(blank=True, null=True)
    disabled = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_types'
        unique_together = (('name', 'deleted'), ('flavorid', 'deleted'),)
        default_permissions = ()


class Instances(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    internal_id = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    image_ref = models.CharField(max_length=255, blank=True, null=True)
    kernel_id = models.CharField(max_length=255, blank=True, null=True)
    ramdisk_id = models.CharField(max_length=255, blank=True, null=True)
    launch_index = models.IntegerField(blank=True, null=True)
    key_name = models.CharField(max_length=255, blank=True, null=True)
    key_data = models.TextField(blank=True, null=True)
    power_state = models.IntegerField(blank=True, null=True)
    vm_state = models.CharField(max_length=255, blank=True, null=True)
    memory_mb = models.IntegerField(blank=True, null=True)
    vcpus = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)
    reservation_id = models.CharField(max_length=255, blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    launched_at = models.DateTimeField(blank=True, null=True)
    terminated_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    locked = models.IntegerField(blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    launched_on = models.TextField(blank=True, null=True)
    instance_type_id = models.IntegerField(blank=True, null=True)
    vm_mode = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)
    architecture = models.CharField(max_length=255, blank=True, null=True)
    root_device_name = models.CharField(max_length=255, blank=True, null=True)
    access_ip_v4 = models.CharField(max_length=39, blank=True, null=True)
    access_ip_v6 = models.CharField(max_length=39, blank=True, null=True)
    config_drive = models.CharField(max_length=255, blank=True, null=True)
    task_state = models.CharField(max_length=255, blank=True, null=True)
    default_ephemeral_device = models.CharField(max_length=255, blank=True, null=True)
    default_swap_device = models.CharField(max_length=255, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    auto_disk_config = models.IntegerField(blank=True, null=True)
    shutdown_terminate = models.IntegerField(blank=True, null=True)
    disable_terminate = models.IntegerField(blank=True, null=True)
    root_gb = models.IntegerField(blank=True, null=True)
    ephemeral_gb = models.IntegerField(blank=True, null=True)
    cell_name = models.CharField(max_length=255, blank=True, null=True)
    node = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    locked_by = models.CharField(max_length=5, blank=True, null=True)
    cleaned = models.IntegerField(blank=True, null=True)
    ephemeral_key_uuid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instances'
        default_permissions = ()


class IscsiTargets(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    target_num = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    volume = models.ForeignKey('Volumes', models.DO_NOTHING, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iscsi_targets'
        default_permissions = ()


class KeyPairs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'key_pairs'
        unique_together = (('user_id', 'name', 'deleted'),)
        default_permissions = ()


class MigrateVersion(models.Model):
    repository_id = models.CharField(primary_key=True, max_length=250)
    repository_path = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrate_version'
        default_permissions = ()


class Migrations(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    source_compute = models.CharField(max_length=255, blank=True, null=True)
    dest_compute = models.CharField(max_length=255, blank=True, null=True)
    dest_host = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.ForeignKey(Instances, models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    old_instance_type_id = models.IntegerField(blank=True, null=True)
    new_instance_type_id = models.IntegerField(blank=True, null=True)
    source_node = models.CharField(max_length=255, blank=True, null=True)
    dest_node = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrations'
        default_permissions = ()


class Networks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    injected = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)
    netmask = models.CharField(max_length=39, blank=True, null=True)
    bridge = models.CharField(max_length=255, blank=True, null=True)
    gateway = models.CharField(max_length=39, blank=True, null=True)
    broadcast = models.CharField(max_length=39, blank=True, null=True)
    dns1 = models.CharField(max_length=39, blank=True, null=True)
    vlan = models.IntegerField(blank=True, null=True)
    vpn_public_address = models.CharField(max_length=39, blank=True, null=True)
    vpn_public_port = models.IntegerField(blank=True, null=True)
    vpn_private_address = models.CharField(max_length=39, blank=True, null=True)
    dhcp_start = models.CharField(max_length=39, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    cidr_v6 = models.CharField(max_length=43, blank=True, null=True)
    gateway_v6 = models.CharField(max_length=39, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    netmask_v6 = models.CharField(max_length=39, blank=True, null=True)
    bridge_interface = models.CharField(max_length=255, blank=True, null=True)
    multi_host = models.IntegerField(blank=True, null=True)
    dns2 = models.CharField(max_length=39, blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    rxtx_base = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    mtu = models.IntegerField(blank=True, null=True)
    dhcp_server = models.CharField(max_length=39, blank=True, null=True)
    enable_dhcp = models.IntegerField(blank=True, null=True)
    share_address = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'networks'
        unique_together = (('vlan', 'deleted'),)
        default_permissions = ()


class PciDevices(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    compute_node = models.ForeignKey(ComputeNodes, models.DO_NOTHING)
    address = models.CharField(max_length=12)
    product_id = models.CharField(max_length=4)
    vendor_id = models.CharField(max_length=4)
    dev_type = models.CharField(max_length=8)
    dev_id = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255)
    status = models.CharField(max_length=36)
    extra_info = models.TextField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    request_id = models.CharField(max_length=36, blank=True, null=True)
    numa_node = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pci_devices'
        unique_together = (('compute_node', 'address', 'deleted'),)
        default_permissions = ()


class ProjectUserQuotas(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255)
    project_id = models.CharField(max_length=255)
    resource = models.CharField(max_length=255)
    hard_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_user_quotas'
        unique_together = (('user_id', 'project_id', 'resource', 'deleted'),)
        default_permissions = ()


class ProviderFwRules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    protocol = models.CharField(max_length=5, blank=True, null=True)
    from_port = models.IntegerField(blank=True, null=True)
    to_port = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_fw_rules'
        default_permissions = ()


class QuotaClasses(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    hard_limit = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quota_classes'
        default_permissions = ()


class QuotaUsages(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255)
    in_use = models.IntegerField()
    reserved = models.IntegerField()
    until_refresh = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quota_usages'
        default_permissions = ()


class Quotas(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255)
    hard_limit = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotas'
        unique_together = (('project_id', 'resource', 'deleted'),)
        default_permissions = ()


class Reservations(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    usage = models.ForeignKey(QuotaUsages, models.DO_NOTHING)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    delta = models.IntegerField()
    expire = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservations'
        default_permissions = ()


class S3Images(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's3_images'
        default_permissions = ()


class SecurityGroupDefaultRules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    protocol = models.CharField(max_length=5, blank=True, null=True)
    from_port = models.IntegerField(blank=True, null=True)
    to_port = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_group_default_rules'
        default_permissions = ()


class SecurityGroupInstanceAssociation(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    security_group = models.ForeignKey('SecurityGroups', models.DO_NOTHING, blank=True, null=True)
    instance_uuid = models.ForeignKey(Instances, models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_group_instance_association'
        default_permissions = ()


class SecurityGroupRules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    parent_group = models.ForeignKey('SecurityGroups', models.DO_NOTHING, blank=True, null=True,
                                     related_name='security_groups_parent_set')
    protocol = models.CharField(max_length=255, blank=True, null=True)
    from_port = models.IntegerField(blank=True, null=True)
    to_port = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)
    group = models.ForeignKey('SecurityGroups', models.DO_NOTHING, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_group_rules'
        default_permissions = ()


class SecurityGroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_groups'
        unique_together = (('project_id', 'name', 'deleted'),)
        default_permissions = ()


class Services(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    binary = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    report_count = models.IntegerField()
    disabled = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    disabled_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'
        unique_together = (('host', 'topic', 'deleted'), ('host', 'binary', 'deleted'),)
        default_permissions = ()


class ShadowAgentBuilds(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    hypervisor = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    architecture = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    md5hash = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_agent_builds'
        default_permissions = ()


class ShadowAggregateHosts(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    aggregate_id = models.IntegerField()
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_aggregate_hosts'
        default_permissions = ()


class ShadowAggregateMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    aggregate_id = models.IntegerField()
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_aggregate_metadata'
        default_permissions = ()


class ShadowAggregates(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_aggregates'
        default_permissions = ()


class ShadowBlockDeviceMapping(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    delete_on_termination = models.IntegerField(blank=True, null=True)
    snapshot_id = models.CharField(max_length=36, blank=True, null=True)
    volume_id = models.CharField(max_length=36, blank=True, null=True)
    volume_size = models.IntegerField(blank=True, null=True)
    no_device = models.IntegerField(blank=True, null=True)
    connection_info = models.TextField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=255, blank=True, null=True)
    destination_type = models.CharField(max_length=255, blank=True, null=True)
    guest_format = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    disk_bus = models.CharField(max_length=255, blank=True, null=True)
    boot_index = models.IntegerField(blank=True, null=True)
    image_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_block_device_mapping'
        default_permissions = ()


class ShadowBwUsageCache(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    start_period = models.DateTimeField()
    last_refreshed = models.DateTimeField(blank=True, null=True)
    bw_in = models.BigIntegerField(blank=True, null=True)
    bw_out = models.BigIntegerField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    last_ctr_in = models.BigIntegerField(blank=True, null=True)
    last_ctr_out = models.BigIntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_bw_usage_cache'
        default_permissions = ()


class ShadowCells(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    api_url = models.CharField(max_length=255, blank=True, null=True)
    weight_offset = models.FloatField(blank=True, null=True)
    weight_scale = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_parent = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    transport_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shadow_cells'
        default_permissions = ()


class ShadowCertificates(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_certificates'
        default_permissions = ()


class ShadowComputeNodes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    vcpus = models.IntegerField()
    memory_mb = models.IntegerField()
    local_gb = models.IntegerField()
    vcpus_used = models.IntegerField()
    memory_mb_used = models.IntegerField()
    local_gb_used = models.IntegerField()
    hypervisor_type = models.TextField()
    hypervisor_version = models.IntegerField()
    cpu_info = models.TextField()
    disk_available_least = models.IntegerField(blank=True, null=True)
    free_ram_mb = models.IntegerField(blank=True, null=True)
    free_disk_gb = models.IntegerField(blank=True, null=True)
    current_workload = models.IntegerField(blank=True, null=True)
    running_vms = models.IntegerField(blank=True, null=True)
    hypervisor_hostname = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    host_ip = models.CharField(max_length=39, blank=True, null=True)
    supported_instances = models.TextField(blank=True, null=True)
    pci_stats = models.TextField(blank=True, null=True)
    metrics = models.TextField(blank=True, null=True)
    extra_resources = models.TextField(blank=True, null=True)
    stats = models.TextField(blank=True, null=True)
    numa_topology = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_compute_nodes'
        default_permissions = ()


class ShadowConsolePools(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=39, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    console_type = models.CharField(max_length=255, blank=True, null=True)
    public_hostname = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    compute_host = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_console_pools'
        default_permissions = ()


class ShadowConsoles(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    pool_id = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_consoles'
        default_permissions = ()


class ShadowDnsDomains(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    domain = models.CharField(primary_key=True, max_length=255)
    scope = models.CharField(max_length=255, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_dns_domains'
        default_permissions = ()


class ShadowFixedIps(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=39, blank=True, null=True)
    network_id = models.IntegerField(blank=True, null=True)
    allocated = models.IntegerField(blank=True, null=True)
    leased = models.IntegerField(blank=True, null=True)
    reserved = models.IntegerField(blank=True, null=True)
    virtual_interface_id = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_fixed_ips'
        default_permissions = ()


class ShadowFloatingIps(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=39, blank=True, null=True)
    fixed_ip_id = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    auto_assigned = models.IntegerField(blank=True, null=True)
    pool = models.CharField(max_length=255, blank=True, null=True)
    interface = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_floating_ips'
        default_permissions = ()


class ShadowInstanceActions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    request_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_actions'
        default_permissions = ()


class ShadowInstanceActionsEvents(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_actions_events'
        default_permissions = ()


class ShadowInstanceExtra(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36)
    numa_topology = models.TextField(blank=True, null=True)
    pci_requests = models.TextField(blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    vcpu_model = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_extra'
        default_permissions = ()


class ShadowInstanceFaults(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    code = models.IntegerField()
    message = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_faults'
        default_permissions = ()


class ShadowInstanceGroupMember(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    instance_id = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shadow_instance_group_member'
        default_permissions = ()


class ShadowInstanceGroupPolicy(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    policy = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shadow_instance_group_policy'
        default_permissions = ()


class ShadowInstanceGroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_groups'
        default_permissions = ()


class ShadowInstanceIdMappings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_id_mappings'
        default_permissions = ()


class ShadowInstanceInfoCaches(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    network_info = models.TextField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_info_caches'
        default_permissions = ()


class ShadowInstanceMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_metadata'
        default_permissions = ()


class ShadowInstanceSystemMetadata(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_system_metadata'
        default_permissions = ()


class ShadowInstanceTypeExtraSpecs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_type_id = models.IntegerField()
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_type_extra_specs'
        default_permissions = ()


class ShadowInstanceTypeProjects(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    instance_type_id = models.IntegerField()
    project_id = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_type_projects'
        default_permissions = ()


class ShadowInstanceTypes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    memory_mb = models.IntegerField()
    vcpus = models.IntegerField()
    swap = models.IntegerField()
    vcpu_weight = models.IntegerField(blank=True, null=True)
    flavorid = models.CharField(max_length=255, blank=True, null=True)
    rxtx_factor = models.FloatField(blank=True, null=True)
    root_gb = models.IntegerField(blank=True, null=True)
    ephemeral_gb = models.IntegerField(blank=True, null=True)
    disabled = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instance_types'
        default_permissions = ()


class ShadowInstances(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    internal_id = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    image_ref = models.CharField(max_length=255, blank=True, null=True)
    kernel_id = models.CharField(max_length=255, blank=True, null=True)
    ramdisk_id = models.CharField(max_length=255, blank=True, null=True)
    launch_index = models.IntegerField(blank=True, null=True)
    key_name = models.CharField(max_length=255, blank=True, null=True)
    key_data = models.TextField(blank=True, null=True)
    power_state = models.IntegerField(blank=True, null=True)
    vm_state = models.CharField(max_length=255, blank=True, null=True)
    memory_mb = models.IntegerField(blank=True, null=True)
    vcpus = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)
    reservation_id = models.CharField(max_length=255, blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    launched_at = models.DateTimeField(blank=True, null=True)
    terminated_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    locked = models.IntegerField(blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    launched_on = models.TextField(blank=True, null=True)
    instance_type_id = models.IntegerField(blank=True, null=True)
    vm_mode = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=36)
    architecture = models.CharField(max_length=255, blank=True, null=True)
    root_device_name = models.CharField(max_length=255, blank=True, null=True)
    access_ip_v4 = models.CharField(max_length=39, blank=True, null=True)
    access_ip_v6 = models.CharField(max_length=39, blank=True, null=True)
    config_drive = models.CharField(max_length=255, blank=True, null=True)
    task_state = models.CharField(max_length=255, blank=True, null=True)
    default_ephemeral_device = models.CharField(max_length=255, blank=True, null=True)
    default_swap_device = models.CharField(max_length=255, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    auto_disk_config = models.IntegerField(blank=True, null=True)
    shutdown_terminate = models.IntegerField(blank=True, null=True)
    disable_terminate = models.IntegerField(blank=True, null=True)
    root_gb = models.IntegerField(blank=True, null=True)
    ephemeral_gb = models.IntegerField(blank=True, null=True)
    cell_name = models.CharField(max_length=255, blank=True, null=True)
    node = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    locked_by = models.CharField(max_length=5, blank=True, null=True)
    cleaned = models.IntegerField(blank=True, null=True)
    ephemeral_key_uuid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_instances'
        default_permissions = ()


class ShadowIscsiTargets(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    target_num = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    volume_id = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_iscsi_targets'
        default_permissions = ()


class ShadowKeyPairs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'shadow_key_pairs'
        default_permissions = ()


class ShadowMigrateVersion(models.Model):
    repository_id = models.CharField(primary_key=True, max_length=250)
    repository_path = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_migrate_version'
        default_permissions = ()


class ShadowMigrations(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    source_compute = models.CharField(max_length=255, blank=True, null=True)
    dest_compute = models.CharField(max_length=255, blank=True, null=True)
    dest_host = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    old_instance_type_id = models.IntegerField(blank=True, null=True)
    new_instance_type_id = models.IntegerField(blank=True, null=True)
    source_node = models.CharField(max_length=255, blank=True, null=True)
    dest_node = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_migrations'
        default_permissions = ()


class ShadowNetworks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    injected = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)
    netmask = models.CharField(max_length=39, blank=True, null=True)
    bridge = models.CharField(max_length=255, blank=True, null=True)
    gateway = models.CharField(max_length=39, blank=True, null=True)
    broadcast = models.CharField(max_length=39, blank=True, null=True)
    dns1 = models.CharField(max_length=39, blank=True, null=True)
    vlan = models.IntegerField(blank=True, null=True)
    vpn_public_address = models.CharField(max_length=39, blank=True, null=True)
    vpn_public_port = models.IntegerField(blank=True, null=True)
    vpn_private_address = models.CharField(max_length=39, blank=True, null=True)
    dhcp_start = models.CharField(max_length=39, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    cidr_v6 = models.CharField(max_length=43, blank=True, null=True)
    gateway_v6 = models.CharField(max_length=39, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    netmask_v6 = models.CharField(max_length=39, blank=True, null=True)
    bridge_interface = models.CharField(max_length=255, blank=True, null=True)
    multi_host = models.IntegerField(blank=True, null=True)
    dns2 = models.CharField(max_length=39, blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    rxtx_base = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    mtu = models.IntegerField(blank=True, null=True)
    dhcp_server = models.CharField(max_length=39, blank=True, null=True)
    enable_dhcp = models.IntegerField(blank=True, null=True)
    share_address = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_networks'
        default_permissions = ()


class ShadowPciDevices(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField()
    compute_node_id = models.IntegerField()
    address = models.CharField(max_length=12)
    product_id = models.CharField(max_length=4, blank=True, null=True)
    vendor_id = models.CharField(max_length=4, blank=True, null=True)
    dev_type = models.CharField(max_length=8, blank=True, null=True)
    dev_id = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255)
    status = models.CharField(max_length=36)
    extra_info = models.TextField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    request_id = models.CharField(max_length=36, blank=True, null=True)
    numa_node = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_pci_devices'
        default_permissions = ()


class ShadowProjectUserQuotas(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255)
    project_id = models.CharField(max_length=255)
    resource = models.CharField(max_length=255)
    hard_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_project_user_quotas'
        default_permissions = ()


class ShadowProviderFwRules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    protocol = models.CharField(max_length=5, blank=True, null=True)
    from_port = models.IntegerField(blank=True, null=True)
    to_port = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_provider_fw_rules'
        default_permissions = ()


class ShadowQuotaClasses(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    hard_limit = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_quota_classes'
        default_permissions = ()


class ShadowQuotaUsages(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    in_use = models.IntegerField()
    reserved = models.IntegerField()
    until_refresh = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_quota_usages'
        default_permissions = ()


class ShadowQuotas(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255)
    hard_limit = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_quotas'
        default_permissions = ()


class ShadowReservations(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    usage_id = models.IntegerField()
    project_id = models.CharField(max_length=255, blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    delta = models.IntegerField()
    expire = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_reservations'
        default_permissions = ()


class ShadowS3Images(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_s3_images'
        default_permissions = ()


class ShadowSecurityGroupDefaultRules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    protocol = models.CharField(max_length=5, blank=True, null=True)
    from_port = models.IntegerField(blank=True, null=True)
    to_port = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_security_group_default_rules'
        default_permissions = ()


class ShadowSecurityGroupInstanceAssociation(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    security_group_id = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_security_group_instance_association'
        default_permissions = ()


class ShadowSecurityGroupRules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    parent_group_id = models.IntegerField(blank=True, null=True)
    protocol = models.CharField(max_length=255, blank=True, null=True)
    from_port = models.IntegerField(blank=True, null=True)
    to_port = models.IntegerField(blank=True, null=True)
    cidr = models.CharField(max_length=43, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_security_group_rules'
        default_permissions = ()


class ShadowSecurityGroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_security_groups'
        default_permissions = ()


class ShadowServices(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    binary = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    report_count = models.IntegerField()
    disabled = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    disabled_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_services'
        default_permissions = ()


class ShadowSnapshotIdMappings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_snapshot_id_mappings'
        default_permissions = ()


class ShadowSnapshots(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    volume_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    progress = models.CharField(max_length=255, blank=True, null=True)
    volume_size = models.IntegerField(blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_snapshots'
        default_permissions = ()


class ShadowTaskLog(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    task_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    period_beginning = models.DateTimeField()
    period_ending = models.DateTimeField()
    message = models.CharField(max_length=255)
    task_items = models.IntegerField(blank=True, null=True)
    errors = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_task_log'
        default_permissions = ()


class ShadowVirtualInterfaces(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    network_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_virtual_interfaces'
        default_permissions = ()


class ShadowVolumeIdMappings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_volume_id_mappings'
        default_permissions = ()


class ShadowVolumeUsageCache(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    volume_id = models.CharField(max_length=36)
    tot_last_refreshed = models.DateTimeField(blank=True, null=True)
    tot_reads = models.BigIntegerField(blank=True, null=True)
    tot_read_bytes = models.BigIntegerField(blank=True, null=True)
    tot_writes = models.BigIntegerField(blank=True, null=True)
    tot_write_bytes = models.BigIntegerField(blank=True, null=True)
    curr_last_refreshed = models.DateTimeField(blank=True, null=True)
    curr_reads = models.BigIntegerField(blank=True, null=True)
    curr_read_bytes = models.BigIntegerField(blank=True, null=True)
    curr_writes = models.BigIntegerField(blank=True, null=True)
    curr_write_bytes = models.BigIntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_volume_usage_cache'
        default_permissions = ()


class ShadowVolumes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    ec2_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    mountpoint = models.CharField(max_length=255, blank=True, null=True)
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
    volume_type_id = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    attach_time = models.DateTimeField(blank=True, null=True)
    deleted = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shadow_volumes'
        default_permissions = ()


class SnapshotIdMappings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snapshot_id_mappings'
        default_permissions = ()


class Snapshots(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    volume_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    progress = models.CharField(max_length=255, blank=True, null=True)
    volume_size = models.IntegerField(blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display_description = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snapshots'
        default_permissions = ()


class Tags(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=36)
    tag = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'tags'
        unique_together = (('resource_id', 'tag'),)
        default_permissions = ()


class TaskLog(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    task_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    period_beginning = models.DateTimeField()
    period_ending = models.DateTimeField()
    message = models.CharField(max_length=255)
    task_items = models.IntegerField(blank=True, null=True)
    errors = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_log'
        unique_together = (('task_name', 'host', 'period_beginning', 'period_ending'),)
        default_permissions = ()


class VirtualInterfaces(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    network_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    instance_uuid = models.ForeignKey(Instances, models.DO_NOTHING, db_column='instance_uuid', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'virtual_interfaces'
        unique_together = (('address', 'deleted'),)
        default_permissions = ()


class VolumeIdMappings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_id_mappings'
        default_permissions = ()


class VolumeUsageCache(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    volume_id = models.CharField(max_length=36)
    tot_last_refreshed = models.DateTimeField(blank=True, null=True)
    tot_reads = models.BigIntegerField(blank=True, null=True)
    tot_read_bytes = models.BigIntegerField(blank=True, null=True)
    tot_writes = models.BigIntegerField(blank=True, null=True)
    tot_write_bytes = models.BigIntegerField(blank=True, null=True)
    curr_last_refreshed = models.DateTimeField(blank=True, null=True)
    curr_reads = models.BigIntegerField(blank=True, null=True)
    curr_read_bytes = models.BigIntegerField(blank=True, null=True)
    curr_writes = models.BigIntegerField(blank=True, null=True)
    curr_write_bytes = models.BigIntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_usage_cache'
        default_permissions = ()


class Volumes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    ec2_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    availability_zone = models.CharField(max_length=255, blank=True, null=True)
    mountpoint = models.CharField(max_length=255, blank=True, null=True)
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
    volume_type_id = models.IntegerField(blank=True, null=True)
    instance_uuid = models.CharField(max_length=36, blank=True, null=True)
    attach_time = models.DateTimeField(blank=True, null=True)
    deleted = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volumes'
        default_permissions = ()
