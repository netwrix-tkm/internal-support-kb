```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BULogIAH
- **Case Number:** 411120
- **Status:** Closed - Resolved
- **Account/Company:** OUHSC
- **Contact Name:** Chris Melton
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** Not specified

## Problem Description
The customer reported a disk space warning on their Netwrix Endpoint Protector appliance, indicating that the appliance was running low on disk space with only 15.56 GB free out of 49.09 GB (32%). The warning suggested that server functionality and performance could be severely affected.

## Environment Details
- The appliance is a virtual machine (VM) with a total disk capacity of 2TB.
- The root partition was limited to 50GB.

## Troubleshooting Steps
1. The customer was advised to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Older system and audit log backups were suggested for deletion.
3. Policies were recommended to be tuned to reduce the incoming log count.
4. A remote session was scheduled to investigate the disk space issue further.
5. During the remote session, it was confirmed that the Audit Log Backup did not clear any significant space.
6. The customer was informed about the possibility of reallocating partitions from the existing 2TB drive.

## Root Cause
The root cause of the disk space issue was identified as the insufficient allocation of space to the root partition, which was only 50GB despite the appliance having a total of 2TB available. This led to the appliance running low on disk space.

## Solution
- The disk space was cleared by setting a limit on PHP logs.
- It was determined that there was no need to add extra space; instead, the existing partitions could be reallocated to increase the root partition size.
- The customer was advised to continue using the Audit Log Backup and to monitor the disk space usage regularly.

## Notes
- It is important for users to monitor disk space regularly and to configure log retention policies appropriately to avoid similar issues in the future.
- Customers should be aware that increasing the root partition may require technical assistance and should plan for potential downtime during the process.
```