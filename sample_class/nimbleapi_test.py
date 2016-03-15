from pprint import pprint
from nimbleapi.nimbleapi import nimbleapi

# INITIATE CONNECTION TO NIMBLE ARRAY
nimble = nimbleapi(hostname = 'testnimble.something.com', username = 'admin', password = 'admin')

# TEST READ FUNCTIONS ON ALL DATA FROM THE NIMBLE
nimble.access_control_records_read()
nimble.arrays_read()
nimble.audit_log_read()
nimble.initiator_group_read()
nimble.initiator_read()
nimble.performance_policies_read()
nimble.pools_read()
nimble.protection_schedules_read()
nimble.protection_templates_read()
nimble.replication_partners_read()
nimble.snapshot_collections_read()
# nimble.snapshots_read() # TAKES A BIT OF TIME DEPENDING ON YOUR VOLUME/SNAPSHOT COUNT
nimble.volume_collections_read()
nimble.volume_read()

##################################################################

# CREATE INITIATOR GROUP
nimble.initiator_group_create(initiator_group_name = 'ucs-prrhev01')

# ADD INITIATORS TO INITIATOR GROUP
nimble.initiator_create(initiator_group_name = 'ucs-prrhev01', alias = 'ucs-prrhev01-vhba0', wwpn = '20:00:00:25:b5:fa:e3:01')
nimble.initiator_create(initiator_group_name = 'ucs-prrhev01', alias = 'ucs-prrhev01-vhba1', wwpn = '20:00:00:25:b5:fb:e3:01')

# CREATE PERFORMANCE POLICY
nimble.performance_policies_create(name = 'custom-rhev', description = 'custom-prrhev01', block_size = 16384, compress = True, cache = True, cache_policy = 'normal', space_policy = 'offline')

##################################################################

# CREATE BOOT VOLUME
nimble.volume_create(volume_name = 'ucs-prrhev01-boot', volume_size = 102400, performance_policy_name = 'custom-rhev')

# ADD INITIATOR GROUP AS LUN-ID 0 (BOOT)
nimble.access_control_records_create(volume_name = 'ucs-prrhev01-boot', initiator_group_name = 'ucs-prrhev01', boot_volume = True)

# TAKE A SNAPSHOT OF THE NEW BOOT VOLUME
nimble.snapshots_create(volume_name = 'ucs-prrhev01-boot', snapshot_name = 'date-time-reason')

##################################################################

# CREATE KVM/RHEV/VMWARE DATASTORE (5TB)    
nimble.volume_create(volume_name = 'rhev-datastore01', volume_size = 5242880, performance_policy_name = 'custom-rhev')

# ADD INITIATOR GROUP; LUN-ID IS AUTO INCREMENTED STARTING AT 1
nimble.access_control_records_create(volume_name = 'rhev-datastore01', initiator_group_name = 'ucs-prrhev01')

# CREATE VOLUME COLLECTION
new_volume_collection_id = nimble.volume_collections_create(name = 'vc-rhev-datastore01', description = 'generated volume collection')

# ADD OUR DATASTORE VOLUME TO THE VOLUME COLLECTION
nimble.volume_update('rhev-datastore01', volcoll_id = new_volume_collection_id)

# SETUP HOURLY REPLICATION OF THE DATASTORE
nimble.protection_schedules_create(name = 'hourly-replication', description = 'hourly-replication', volcoll_or_prottmpl_id = new_volume_collection_id, period = 1, period_unit = 'hours', num_retain = 3, downstream_partner = 'backupnimble.something.com', num_retain_replica = 12)

# TAKE A MANUAL SNAPSHOT OF THE VOLUME COLLECTION
nimble.snapshot_collections_create(volume_collection_name = 'vc-rhev-datastore01', replicate = True, name = 'snapshot-collection-name', description = 'snapshot-collection-description')

##################################################################

# You get the idea... When I get some more time i'll add a full test up and down.

# remove snapshot collection 
# remove protection schedule  
# remove volume from volume collection  
# offline volume 
# delete volume  

# remove snapshot  
# remove initiator groups
# offline volume  
# delete volume  

# remove performance policy  
# remove initiators  
# remove initiator group  