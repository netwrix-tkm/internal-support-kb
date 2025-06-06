## Ticket Metadata
- **Ticket ID:** 500Qk00000DgwePIAR
- **Case Number:** 416361
- **Status:** Closed - Resolved
- **Account/Company:** MANCOSA
- **Contact Name:** ziyaad Rasool
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Sensitive Data
- **Version:** 11.6

## Problem Description
The customer reported a failure during the File System Seek Bulk Import process, accompanied by multiple error messages indicating issues with loading necessary libraries and a violation of a primary key constraint in the database.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems
- **Error Messages:**
  - Failed to read the list of static hosts for the job.
  - Unable to load libraries (CPasswordSDK.dll and libeay32.dll).
  - Violation of PRIMARY KEY constraint 'PK_SA_FSDLP_Matches'.

## Troubleshooting Steps
1. Reviewed error logs for detailed error messages related to the bulk import failure.
2. Attempted to identify missing libraries (CPasswordSDK.dll and libeay32.dll) in the specified directories.
3. Checked for duplicate entries in the database that could cause the primary key violation.
4. Dropped the DLP data for the affected host using the FS_SDD_DELETE job.
5. Deleted only DLP-related T2 database files.
6. Reran the SEEK scans to verify if the issue persisted.
7. Suggested resetting the affected host through the FSAA query > Maintenance > Reset Hosts.

## Root Cause
The root cause of the issue was identified as a violation of the primary key constraint in the database due to duplicate entries being attempted for insertion during the bulk import process. Additionally, the failure to load necessary libraries contributed to the import failure.

## Solution
The issue was resolved by:
- Dropping the DLP data for the affected host using the FS_SDD_DELETE job.
- Deleting the DLP-related T2 database files.
- Rerunning the SEEK scans to ensure successful import.
- It was also recommended to reset the affected host if similar issues arise in the future.

## Notes
- Ensure that all required libraries (CPasswordSDK.dll and libeay32.dll) are present in the specified directories to avoid loading issues.
- Monitor for duplicate entries in the database before performing bulk imports to prevent primary key constraint violations.
- For future bulk import failures, consider resetting the affected host as a potential solution.