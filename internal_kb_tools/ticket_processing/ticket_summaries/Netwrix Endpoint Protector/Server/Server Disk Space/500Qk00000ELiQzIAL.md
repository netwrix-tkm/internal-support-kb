## Ticket Metadata
- **Ticket ID:** 500Qk00000ELiQzIAL
- **Case Number:** 417886
- **Status:** Closed - Resolved
- **Account/Company:** Haleon
- **Contact Name:** Sudhir Baral
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their appliance was running low on disk space, with only 6.93 GB free from a total of 19.52 GB (approximately 35% available). This low disk space was affecting the functionality and performance of the EPP Server.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The customer was advised to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Suggested deleting older system and audit log backups to free up space.
3. Recommended tuning policies to reduce the incoming log count.
4. The customer requested assistance to remove log space and indicated that they needed more time to conclude the log rotation process and retention workflow.

## Root Cause
The root cause of the issue was identified as insufficient disk space due to the accumulation of audit logs and system backups, which were not being managed effectively.

## Solution
The issue was resolved by freeing up disk space on the root partition. This involved:
- Implementing the Audit Log Backup to manage log storage.
- Deleting older backups that were no longer needed.
- Adjusting log retention policies to prevent future occurrences of low disk space.

## Notes
- It is important for users to regularly monitor disk space and manage log retention to avoid similar issues in the future.
- Consider implementing automated log rotation and retention policies to maintain optimal disk space usage.