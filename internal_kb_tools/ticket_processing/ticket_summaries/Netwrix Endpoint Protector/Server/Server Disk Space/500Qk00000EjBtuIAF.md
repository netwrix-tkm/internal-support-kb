## Ticket Metadata
- **Ticket ID:** 500Qk00000EjBtuIAF
- **Case Number:** 418702
- **Status:** Closed - Resolved
- **Account/Company:** Infibeam Avenues Limited / CCAvenue
- **Contact Name:** Amrut Nadgiri
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported a disk space issue on their EPP server, indicating that the server was running low on disk space with only 10.01 GB free out of 49.09 GB (20% remaining). This low disk space could severely affect the functionality and performance of the EPP server.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Advised the customer to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Suggested deleting older system and audit log backups to free up space.
3. Recommended tuning policies to reduce the incoming log count.

## Root Cause
The root cause of the issue was identified as insufficient disk space on the EPP server, primarily due to the accumulation of logs and backups over time.

## Solution
The issue was resolved by clearing disk space through the following actions:
- The customer utilized the Audit Log Backup feature to manage and reduce the volume of logs stored.
- Older system and audit log backups were deleted, which significantly increased the available disk space.

## Notes
- It is important for users to regularly monitor disk space and manage log files to prevent similar issues in the future.
- Consider implementing automated log management policies to help maintain optimal disk space levels.