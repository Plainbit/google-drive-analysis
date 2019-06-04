from sqlalchemy import Table, Column, String, MetaData, Integer

_metadata = MetaData()

global_db_username_mapping = Table(
    'username_mapping', _metadata,
    Column('username', String),
    Column('directory_path', String),
)

device_db_db_device_files = Table(
    'device_files', _metadata,
    Column('doc_id', String),
    Column('device_id', String),
    Column('filename', String),
    Column('path', String),
    Column('modified', Integer),
    Column('size', Integer),
    Column('checksum', String),
)

device_db_db_external_devices = Table(
    'external_devices', _metadata,
    Column('device_id', String),
    Column('doc_id', String),
    Column('label', String),
    Column('upload_time', Integer),
    Column('device_discovery_action', Integer),
    Column('usb_type', Integer),
    Column('parent_device_id', String),
)

snapshot_db_cloud_entry = Table(
    'cloud_entry', _metadata,
    Column('doc_id', String),
    Column('filename', String),
    Column('modified', String),
    Column('created', Integer),
    Column('acl_role', Integer),
    Column('doc_type', Integer),
    Column('removed', String),
    Column('size', String),
    Column('checksum', String),
    Column('shared', String),
    Column('resource_type', String),
    Column('original_size', String),
    Column('original_checksum', String),
    Column('down_sample_status', String),
)

snapshot_db_cloud_relations = Table(
    'cloud_relations', _metadata,
    Column('child_doc_id', String),
    Column('parent_doc_id', String),
)

snapshot_db_local_entry = Table(
    'local_entry', _metadata,
    Column('inode', Integer),
    Column('volume', String),
    Column('modified', Integer),
    Column('checksum', String),
    Column('size', Integer),
    Column('is_folder', Integer),
)

snapshot_db_local_relations = Table(
    'local_relations', _metadata,
    Column('child_inode', Integer),
    Column('chile_volume', String),
    Column('parent_inode', Integer),
    Column('parent_volume', String),
)

snapshot_db_mapping = Table(
    'mapping', _metadata,
    Column('inode', Integer),
    Column('volume', String),
    Column('path', String),
)

snapshot_db_volume_info = Table(
    'volume_info', _metadata,
    Column('volume', String),
    Column('full_path', String),
    Column('uuid', String),
    Column('label', String),
    Column('size', Integer),
    Column('filesystem', String),
    Column('model', String),
    Column('device_type', String),
    Column('device_file', String),
    Column('device_number', Integer),
)

sync_config_db_data = Table(
    'data', _metadata,
    Column('entry_key', String),
    Column('data_key', String),
    Column('data_value', String),
)
