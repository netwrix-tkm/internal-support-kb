## Ticket Metadata
- **Ticket ID:** 500Qk00000OcdiUIAR
- **Case Number:** 443652
- **Status:** Closed - Resolved
- **Account/Company:** Denave India Pvt Ltd
- **Contact Name:** Amit Tomar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** 5.9.4.2

## Problem Description
The customer reported an issue with insufficient disk space on their server and requested assistance in freeing up space.

## Environment Details
- Database disk space was approximately 190 GB.
- The customer was using an older version of the client on some computers.

## Troubleshooting Steps
1. Opened a new ticket for the customer's request and inquired how they wanted assistance.
2. Conducted a remote session to assess disk usage and deleted some system backups.
3. Verified the date of the last Audit Log Backup and rescheduled it for logs older than 6 months.
4. Advised the customer to check disk space in the UI after the backup was completed.
5. Customer reported a "550 Internal Server Error" when logging in; scheduled another remote session to investigate.
6. During the second remote session, confirmed that there was no available disk space (huge MySQL usage - 149 GB).
7. Deleted additional internal backups and advised the customer to download and delete old backups from Audit Log Backup.
8. Suggested scheduling another backup for logs older than 1 month.
9. Pushed an upgrade of the client for some computers and advised monitoring due to the old client version.
10. Followed up with the customer to check if the provided instructions were helpful.
11. Discussed increasing disk space resources in the virtualization environment but later decided it was unnecessary.

## Root Cause
The primary cause of the issue was insufficient disk space due to large MySQL database usage and accumulation of old backups.

## Solution
The issue was resolved by:
- Deleting unnecessary internal backups.
- Advising the customer to manage their Audit Log Backups by downloading and deleting old logs.
- Rescheduling backups for logs older than 1 month.
- Successfully upgrading the client on some computers to ensure better performance.

## Notes
- It is recommended for customers to regularly monitor disk space and manage backups to prevent similar issues in the future.
- Consider configuring External Storage and enabling Limit Reporting Content Aware Protection to optimize disk usage.
- Always verify the version of the client software being used, especially if it is significantly outdated.