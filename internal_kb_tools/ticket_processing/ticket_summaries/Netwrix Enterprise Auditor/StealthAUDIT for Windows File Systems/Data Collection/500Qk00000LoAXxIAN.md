## Ticket Metadata
- **Ticket ID:** 500Qk00000LoAXxIAN
- **Case Number:** 435648
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Gregory Meyer
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.5

## Problem Description
The customer reported that during a scan of their RCH facility, which was supposed to cover 30,375 servers, only 12,453 servers were reported as scanned in the ACCESS table. They required assistance to resolve this discrepancy.

## Environment Details
- The scanning process took over 2 days to complete.
- The system was configured to use 11 proxy hosts for scanning.
- The job was set to collect permissions only.

## Troubleshooting Steps
1. Verified the job statistics to confirm the number of servers scanned.
2. Checked the logs for errors and warnings related to the scanning process.
3. Increased the thread count for concurrent scanning operations from 9 to 20 threads.
4. Analyzed the database for potential connection issues and data capture failures.
5. Reviewed network traffic and backup processes that could interfere with scanning.
6. Consulted documentation on improving local file system permission scan performance.

## Root Cause
The issue was primarily caused by connection failures during the scanning process, which resulted in the inability to commit row data to the database. This was exacerbated by network traffic and potential interference from backup processes (notably VEEAM).

## Solution
To resolve the issue, the following actions were taken:
- Increased the number of concurrent worker threads from 9 to 20 to enhance scanning performance.
- Adjusted the configuration settings in the XML file to optimize thread management.
- Conducted additional analysis to ensure that the scanning job was correctly capturing and logging data.

## Notes
- Future scans should consider monitoring network traffic and backup schedules to minimize interference.
- It is advisable to regularly review and adjust thread counts based on the scale of the scanning operation to improve performance.
- Ensure that all proxy hosts are functioning correctly and reporting scanning activity to avoid discrepancies in server counts.