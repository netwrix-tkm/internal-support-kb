## Ticket Metadata
- **Ticket ID:** 500Qk00000MKlkYIAT
- **Case Number:** 437110
- **Status:** Closed - Resolved
- **Account/Company:** Ropes and Gray LLC
- **Contact Name:** Matt Joyce
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** 5.9.4.0

## Problem Description
The customer reported that their on-premises Endpoint Protector (EPP) appliance was running low on disk space, with only 80.1 GB free out of 257.22 GB (31% remaining). This low disk space was affecting the functionality and performance of the EPP server.

## Environment Details
- **Platform:** On-premises
- **Operating System:** Not specified, but the issue pertains to the EPP server environment.

## Troubleshooting Steps
1. Joined a remote session to assess the disk space issue.
2. Checked the partition for `/var/eppfiles/*` and identified that `/var/eppfiles/shadows/` was consuming 149 GB.
3. Customer requested the deletion of shadow files.
4. Deleted shadow files that were 180 and 60 days old.
5. Verified that `/var/eppfiles/shadows/` was reduced to 4 KB.
6. Closed the case upon customer request.

## Root Cause
The root cause of the low disk space was the accumulation of old shadow files in the `/var/eppfiles/shadows/` directory, which had not been deleted over time, leading to significant disk space consumption.

## Solution
The issue was resolved by:
- Deleting the old shadow files (specifically those that were 180 and 60 days old) from the `/var/eppfiles/shadows/` directory, which freed up a substantial amount of disk space.

## Notes
- It is recommended to regularly monitor and manage the disk space on the EPP server to prevent similar issues in the future.
- Implementing a scheduled task to automatically delete old shadow files could help maintain adequate disk space.
- Customers should be advised to use the Audit Log Backup feature to manage logs stored in the database effectively.