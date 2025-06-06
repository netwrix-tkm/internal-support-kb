## Ticket Metadata
- **Ticket ID:** 500Qk00000GIxBiIAL
- **Case Number:** 422238
- **Status:** Closed - Resolved
- **Account/Company:** Hawaii Pacific Health
- **Contact Name:** Steven Schiesl
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Proxy
- **Version:** 11.6.0.13

## Problem Description
The customer reported that some Sensitive Data scans were failing with a warning message stating, "Cannot scan, SDD Differential Scan needs bulk import," despite previous bulk imports showing success.

## Environment Details
- **Hosts Involved:** DRF-ERNIE2, PALIMOMI, HARBORCOURT
- **Current Versions of Applications:**
  - Netwrix Enterprise Auditor (NEA): 11.6.0.89
  - NEA Sensitive Data (SDD): 11.6.0.13
  - NEA Proxy: 11.6.0.89

## Troubleshooting Steps
1. Reviewed FSAA logs for the host DRF-ERNIE2, which showed current FSAA and FSAC but no SDD logs.
2. Attempted to replicate the issue in a lab environment but was unsuccessful.
3. Noted that the issue seemed to arise from improper scan completion (job termination) that corrupted the Tier2 databases.
4. Ran the following jobs:
   - Jobs > Z.Sandbox > FS_DropTables (specifically dropping FSDLP Tables)
   - Jobs > FileSystem > 3.Prep > 0-Create Schema
5. Manually deleted the Tier 2 *DLP* (SQLite) databases from both the NEA FSSA path and the Proxy host FSAA folder path.
6. Monitored subsequent scans for success.

## Root Cause
The issue was identified as being caused by improper scan completion, which led to corruption in the Tier2 databases. This corruption prevented the SDD scans from running correctly.

## Solution
The issue was resolved by:
- Dropping the corrupted Tier2 databases.
- Recreating the necessary schema.
- Running zero-level SDD scans until all completed successfully.
- Ensuring that the databases were synchronized between the Proxy and NEA host.

## Notes
- It is important to monitor the completion of scans closely, especially after bulk imports.
- Future scans should be verified for success before considering the job complete.
- If similar issues arise, consider checking for database corruption and performing the steps outlined above to reset the environment.