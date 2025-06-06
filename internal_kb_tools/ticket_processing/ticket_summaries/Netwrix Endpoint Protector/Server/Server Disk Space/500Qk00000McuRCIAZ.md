## Ticket Metadata
- **Ticket ID:** 500Qk00000McuRCIAZ
- **Case Number:** 437927
- **Status:** Closed - Resolved
- **Account/Company:** HLB Gross Collins, P.C.
- **Contact Name:** Heather Worrall
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported issues with disk space on their Netwrix Endpoint Protector server, indicating they were running out of space and needed assistance with deleting unnecessary files or logs. The customer also inquired about the availability of an API for this purpose.

## Environment Details
- The EPP server is hosted by Netwrix.
- The customer was experiencing approximately 80% disk space usage.

## Troubleshooting Steps
1. The support engineer attempted to contact the customer via phone but did not receive a response.
2. The support engineer checked the backend of the EPP server for disk space usage.
3. The support engineer cleared some space in the backend, reducing disk space usage from 80% to approximately 52%.
4. The support engineer informed the customer about the periodic database backups that were consuming significant disk space.

## Root Cause
The primary cause of the disk space issue was identified as the accumulation of periodic database backups, which were taking up a considerable amount of space on the server.

## Solution
The support engineer cleared space in the backend, which resulted in a reduction of disk space usage. Additionally, the engineer recommended the following preventive measures:
- Utilize the **Audit Log Backup** functionality to archive logs and remove them from the EPP server. This feature can be enabled from **System Maintenance -> Audit Log Backup**.
- The customer was advised to apply this functionality to older logs to manage disk space effectively.

## Notes
- The support engineer noted that the periodic database backups could lead to a recurrence of the disk space issue in a few weeks or months if not managed properly.
- The customer was informed that there is currently no API available for managing these tasks, but it is a feature under consideration by the development team.