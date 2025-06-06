## Ticket Metadata
- **Ticket ID:** 500Qk00000DNOwdIAH
- **Case Number:** 415614
- **Status:** Closed - Resolved
- **Account/Company:** Desktop - End user
- **Contact Name:** Alberto Mori
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their appliance was running low on disk space, with only 77.3 GB free out of 434.46 GB (18% remaining). This low disk space could severely affect the functionality and performance of the EPP Server.

## Environment Details
- **Appliance Type:** Netwrix Endpoint Protector
- **Disk Space Status:** 77.3 GB free from 434.46 GB total

## Troubleshooting Steps
1. Advised the customer to use the Audit Log Backup feature to reduce the logs stored in the database.
2. Suggested deleting older system and audit log backups.
3. Recommended tuning policies to reduce the incoming log count.
4. Cleared shadow files from the server to free up additional disk space.

## Root Cause
The root cause of the low disk space issue was the accumulation of logs and shadow files on the server, which had not been managed effectively.

## Solution
The issue was resolved by freeing up shadow files from the server, which significantly increased the available disk space. After this action, the server was reported to be mostly free of space issues.

## Notes
- It is important to regularly monitor disk space and manage log files to prevent similar issues in the future.
- Consider implementing automated log management policies to ensure that log accumulation does not lead to low disk space conditions.