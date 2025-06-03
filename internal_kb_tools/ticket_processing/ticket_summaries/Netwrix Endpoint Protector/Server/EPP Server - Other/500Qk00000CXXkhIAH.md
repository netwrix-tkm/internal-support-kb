```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CXXkhIAH
- **Case Number:** 413663
- **Status:** Closed - Resolved
- **Account/Company:** Digital Asset Holdings
- **Contact Name:** Oscar Valle
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** Backup Process
- **Version:** Not specified

## Problem Description
The customer reported that the backup process was stuck at 99% while attempting to apply an update.

## Environment Details
- The backup process was hosted on Netwrix's datacenters.
- The customer indicated that the backup had been running for over 3 hours.

## Troubleshooting Steps
1. Inquired about the duration the backup had been stuck at 99%.
2. Asked if a snapshot of the appliance was created before the upgrade.
3. Suggested reloading the web console to check the status of the backup.
4. Proposed a remote session to check disk space and backend access.
5. Engaged the server team to find a way to stop the backup process.
6. Suggested that the customer could proceed with applying the update despite the backup being stuck.

## Root Cause
The backup process was unable to complete, likely due to a combination of factors including potential disk space issues and the inability to stop a running backup process.

## Solution
- The support team removed the backup request and status from the backend.
- Engaged with the DevOps team to resolve the security upgrade issue.
- Confirmed that the customer could proceed with the update since two snapshots were taken daily, making the backup unnecessary.

## Notes
- It is important to monitor the backup process closely, especially when large databases are involved.
- Future cases should consider checking disk space and system resources before initiating backups.
- If a backup process becomes unresponsive, it may require backend intervention to resolve.
```