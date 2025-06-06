```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000IujPtIAJ
- **Case Number:** 428473
- **Status:** Closed - Resolved
- **Account/Company:** Samsung - SRI Bangalore
- **Contact Name:** Mohammed Shafi
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported a disk space issue on their server and requested assistance in deleting server logs to free up space. They specifically requested a disk addition rather than an extension, indicating a need for additional storage capacity.

## Environment Details
- The server had two disks: /dev/sda (1 TB) containing the EPP Server and /dev/sdb (1 TB) which was empty.
- The customer wanted to extend the storage for /var/eppfiles, which resided on /dev/sda5.

## Troubleshooting Steps
1. Initial communication with the customer to gather details about the server and the disk usage.
2. Requested access to the EPP Server to investigate what was consuming disk space.
3. Confirmed the URL and Server ID for accessing the EPP UI.
4. Identified that the customer did not want a disk extension but an addition of another disk.
5. Engaged DevOps to perform the necessary actions for adding the new disk.

## Root Cause
The root cause of the issue was insufficient disk space on the existing server due to the need for additional storage for logs and other data. The customer required a configuration that allowed for the addition of a new disk rather than extending the existing one.

## Solution
- The DevOps team, led by Catalin, added the new disk (/dev/sdb) next to the existing one.
- A new LVM (Logical Volume Manager) group was created, and /dev/sdb1 was configured as an LVM volume.
- The existing data from /var/eppfiles was migrated to the new volume using `rsync`.
- The original /dev/sda5 was also configured as an LVM volume and added to the existing LVM group.
- The LVM volume was extended to utilize the space from both disks, effectively increasing the available storage to approximately 2 TB.

## Notes
- Ensure that any future requests for disk space consider whether the customer prefers a disk addition or extension.
- Always confirm the server configuration and requirements before proceeding with changes to avoid miscommunication.
- Regular monitoring of disk usage can help prevent similar issues from arising in the future.
```