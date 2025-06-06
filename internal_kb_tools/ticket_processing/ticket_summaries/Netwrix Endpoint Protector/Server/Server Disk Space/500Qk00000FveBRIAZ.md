## Ticket Metadata
- **Ticket ID:** 500Qk00000FveBRIAZ
- **Case Number:** 421383
- **Status:** Closed - Resolved
- **Account/Company:** DINERS CLUB PERÚ S.A.
- **Contact Name:** Stephanie Santisteban
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** 7.1

## Problem Description
The customer reported that the EPP server was displaying a critical low disk space warning, indicating that there was no free space available on the disk. This situation was affecting the server's functionality and performance.

## Environment Details
- **Disk Capacity:** 257.22 GB
- **Free Space Available:** 0 GB
- **Message Displayed:** "Your appliance is on critical low disk space, there is only 0 free available from 257.22 gb (0%). EPP Server functionality and performance may be severely affected..."

## Troubleshooting Steps
1. Verified the disk space usage on the EPP server.
2. Reviewed the logs to identify large files consuming disk space.
3. Suggested the customer use the Audit Log Backup feature to reduce the logs stored in the database.
4. Recommended deleting older system and audit log backups.
5. Advised tuning policies to reduce the incoming log count.

## Root Cause
The issue was caused by a large syslog file, which was over 250 GB in size. This file was consuming all available disk space, leading to the critical low disk space warning.

## Solution
The issue was resolved by removing the large syslog file from the backend. The logs were already backed up to the SIEM, and the customer only required the logs from the last three months on the EPP server, which were retained.

## Notes
- It is important to regularly monitor disk space usage and implement log retention policies to prevent similar issues in the future.
- Customers should be advised to back up logs to external systems like SIEM to avoid excessive disk usage on the EPP server.