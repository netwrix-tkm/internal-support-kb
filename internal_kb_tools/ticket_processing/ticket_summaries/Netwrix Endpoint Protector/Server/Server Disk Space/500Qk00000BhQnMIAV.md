## Ticket Metadata
- **Ticket ID:** 500Qk00000BhQnMIAV
- **Case Number:** 411601
- **Status:** Closed - Resolved
- **Account/Company:** Haleon
- **Contact Name:** Sudhir Baral
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their appliance was running low on disk space, with only 6.91 GB free out of 19.52 GB (approximately 35% available). This low disk space could severely affect the functionality and performance of the Endpoint Protector (EPP) Server.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Advised the customer to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Suggested deleting older system and audit log backups to free up space.
3. Recommended tuning policies to reduce the incoming log count.
4. Scheduled a meeting with the customer to discuss the issue further.

## Root Cause
The root cause of the issue was identified as insufficient disk space due to the accumulation of logs and backups over time, which was not being managed effectively.

## Solution
The issue was resolved after the customer implemented the following actions:
- Utilized the Audit Log Backup feature to manage and reduce the volume of logs stored.
- Deleted older system and audit log backups.
- Adjusted policies to limit the incoming log count.
After these actions, the warning message regarding low disk space was no longer appearing in the console.

## Notes
- It is important for users to regularly monitor disk space and manage log files to prevent similar issues in the future.
- Consider implementing automated log management policies to ensure that disk space does not become a recurring issue.