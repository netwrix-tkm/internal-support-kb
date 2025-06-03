## Ticket Metadata
- **Ticket ID:** 500Qk00000JiwJzIAJ
- **Case Number:** 430412
- **Status:** Closed - Resolved
- **Account/Company:** King's Own Institute
- **Contact Name:** Brian KANG
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5941

## Problem Description
The customer reported an inability to access the server, receiving a "500 Internal Server Error" message. The error indicated that something was broken on the server.

## Environment Details
- The issue was related to the MySQL service, which was not starting due to a filled `/var/lib/mysql` partition.

## Troubleshooting Steps
1. Confirmed that the `/var/lib/mysql` partition was filled, preventing MySQL from starting.
2. Stopped all related services.
3. Backed up data from `/var/lib/mysql` and `/var/eppfiles/mysql` to a newly-created temporary disk.
4. Extended the disk space to 200 GB.
5. Removed the last three partitions (the two original partitions and the extended partition).
6. Created a new ext4 partition to replace the three previous partitions and restored the backed-up data.
7. Updated the MySQL configuration file (`/etc/mysql/my.cnf`) to point to `/var/eppfiles/mysql` instead of `/var/lib/mysql`.
8. Modified the AppArmor profile to include the new MySQL data directory.
9. Created a symlink from `/var/lib/mysql` to `/var/eppfiles/mysql`.
10. Restarted the services.
11. Verified that the EPP Server was functioning correctly in the UI.

## Root Cause
The root cause of the issue was the `/var/lib/mysql` partition being completely filled, which prevented the MySQL service from starting.

## Solution
The issue was resolved by clearing disk space and reconfiguring the MySQL service to use a different directory (`/var/eppfiles/mysql`) that had sufficient space. This involved backing up existing data, creating a new partition, and updating configuration files accordingly.

## Notes
- Ensure regular monitoring of disk space on critical partitions to prevent similar issues in the future.
- Consider implementing alerts for disk usage thresholds to proactively manage storage before it becomes a problem.