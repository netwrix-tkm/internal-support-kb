## Ticket Metadata
- **Ticket ID:** 500Qk00000IliJWIAZ
- **Case Number:** 428058
- **Status:** Closed - Resolved
- **Account/Company:** OUHSC
- **Contact Name:** Chisum Thompson
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that the storage space on their EPP server had reached a critical threshold, with only 11.32 GB free available from a total of 49.04 GB (23%). This situation posed a risk to the functionality and performance of the EPP server.

## Environment Details
- **Server Type:** EPP Server
- **Total Disk Space:** 49.04 GB
- **Free Disk Space:** 11.32 GB
- **Additional Disk Space Available:** 2 TB on a secondary partition

## Troubleshooting Steps
1. **Initial Assessment:** Reviewed the current disk space usage and confirmed the warning threshold was reached.
2. **Remote Session:** Scheduled a remote session with the customer to investigate further.
3. **Commands Execution:** Botond had previously run commands to reduce storage usage, but the remaining space decreased further.
4. **Disk Space Clearing:** During the remote session, the following actions were taken:
   - Vacuumed the journal, freeing up 4.1 GB.
   - Cleared artifacts and cache, reducing occupied space from 34 GB to 11 GB.
5. **Log File Relocation:** The PHP error log file was relocated to the secondary partition, which had almost 2 TB of space, clearing an additional 10 GB from the system disk partition.

## Root Cause
The root cause of the low disk space was identified as excessive accumulation of cache and journal files, which were not being managed effectively, leading to rapid consumption of available disk space.

## Solution
The issue was resolved by relocating the PHP error log file to a secondary partition with ample space, which cleared 10 GB from the system disk. Additionally, regular maintenance actions such as vacuuming the journal and clearing cache were performed to manage disk space more effectively.

## Notes
- It is recommended to monitor disk space usage regularly and consider implementing limits on how much space can be occupied by cache and journal files.
- If the issue recurs, further investigation with the DevOps team may be necessary to explore options for extending the system disk partition or optimizing file storage practices.
- Follow-up with the customer in two weeks to check if the issue persists and to reassess the storage management strategy.