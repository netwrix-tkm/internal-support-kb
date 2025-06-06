## Ticket Metadata
- **Ticket ID:** 500Qk00000CaKfiIAF
- **Case Number:** 413819
- **Status:** Closed - Resolved
- **Account/Company:** Royal Bank of Canada (RBC)
- **Contact Name:** Justin Olson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that several file-level scans were failing due to multiple "out of memory" errors and insufficient storage warnings, despite having adequate free space on the proxy servers.

## Environment Details
- **Proxy Server Storage:**
  - C: Drive: 100 GB free
  - Data Drives: Over 1 TB free
- **Product Version:** 11.6

## Troubleshooting Steps
1. Reviewed logs uploaded by the customer to identify the cause of the errors.
2. Confirmed available storage on proxy servers.
3. Escalated the issue to the engineering team for further investigation.
4. Suggested disabling antivirus temporarily, as it was interfering with the scans.
5. Collected memory dump files for analysis to diagnose potential memory leaks.
6. Identified that the issue was related to a product defect.

## Root Cause
The issue was determined to be a product defect related to a memory leak within the Netwrix Enterprise Auditor, which caused the scans to fail with out-of-memory errors despite sufficient storage being available.

## Solution
A hotfix was developed and made available to resolve the memory leak issue. The customer was directed to the following Knowledge Base article for the hotfix: [Hotfix KB Article](https://nwxcorp.lightning.force.com/lightning/r/General__kav/ka0Qk0000004vsXIAQ/view).

## Notes
- It is recommended to monitor memory usage during scans to identify potential leaks early.
- Ensure that antivirus software is configured to allow scans to run without interference.
- Future cases involving similar symptoms should consider checking for memory leaks and available storage as initial troubleshooting steps.