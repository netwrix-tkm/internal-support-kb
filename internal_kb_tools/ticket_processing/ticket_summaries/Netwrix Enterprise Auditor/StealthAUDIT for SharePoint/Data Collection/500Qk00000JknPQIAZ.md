## Ticket Metadata
- **Ticket ID:** 500Qk00000JknPQIAZ
- **Case Number:** 430483
- **Status:** Closed - Resolved
- **Account/Company:** Advent Health System
- **Contact Name:** Paul Williams
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported a disk I/O error during a system scan with the StealthAUDIT for SharePoint, specifically encountering the error code `IoErr (10)` and a message indicating a `System.Data.SQLite.SQLiteException`.

## Environment Details
- **Free Disk Space:**
  - C: 33GB+ free
  - D: 630GB+ free (NEA Install Directory & SharePoint Tier 2s)
- The account has proper access to Tier 2s.

## Troubleshooting Steps
1. Verified available disk space on both C and D drives.
2. Confirmed that the account used has the necessary permissions to access the Tier 2s.
3. Attempted to execute the scan again to reproduce the error.
4. Investigated the stack trace provided in the error message for potential causes.
5. Dropped the Tier 2s and initiated a rescanning process.

## Root Cause
The root cause of the disk I/O error was not definitively identified. However, it was suspected that there may have been a temporary issue with the SQLite database connection or schema validation during the scanning process.

## Solution
The issue was resolved by dropping the Tier 2s and performing a rescanning. This action cleared the error and allowed the scan to complete successfully.

## Notes
- It is advisable to monitor the system for similar disk I/O errors in the future.
- Ensure that there is sufficient disk space available before initiating scans.
- If similar issues arise, consider dropping and rescanning Tier 2s as a potential first step in troubleshooting.