```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CZNVxIAP
- **Case Number:** 413777
- **Status:** Closed - Resolved
- **Account/Company:** Hydro Group Norway
- **Contact Name:** Saveetha Anesh
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Database
- **Version:** 11.5

## Problem Description
The customer reported that the bulk import for both the NHY and GLOBAL permission scans was failing.

## Environment Details
- The issue occurred on a Windows server environment using Netwrix Enterprise Auditor version 11.5.
- The bulk import jobs were set to run in Global Default mode.

## Troubleshooting Steps
1. Verified the Bulk Import job settings to ensure they were in Global Default mode.
2. Collected and reviewed the scan logs from the previous week.
3. Set the Bulk Import job to Debug mode to capture detailed logs.
4. Analyzed the logs for error messages related to the bulk import failures.
5. Identified specific errors:
   - **GLOBAL Domain:** "The specified path, file name, or both are too long."
   - **NHY Domain:** "SQL logic error unknown database StrucMap."
6. Suggested dropping the T2 databases for the affected hosts and proxies.
7. Recommended running repairs on the problematic servers.

## Root Cause
The bulk import failures were primarily due to:
- Long file paths exceeding Windows' maximum character limits (260 characters for file names and 248 for directory names).
- A SQL logic error indicating that the database "StrucMap" was unknown, likely due to insufficient database space.

## Solution
1. Dropped the T2 databases for the affected hosts and proxies.
2. Ran the FSAA-System Scans and Bulk Import jobs again after the repairs were completed.
3. Resolved the issues with the reports by deleting the "Reports" folder of the FSAA-Bulk Import.
4. Confirmed that the SQL team increased the Stealth Audit database size to accommodate the required data.

## Notes
- Ensure that job names for Bulk Import jobs are kept short to avoid path length issues in the future.
- Regularly monitor SQL database space to prevent similar issues related to database capacity.
- After making changes to the database or server configurations, always rerun the relevant jobs to verify that the issues are resolved.
```