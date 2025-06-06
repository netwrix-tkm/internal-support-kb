```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CRzRxIAL
- **Case Number:** 413502
- **Status:** Closed - Resolved
- **Account/Company:** NIC Inc
- **Contact Name:** Bobby Williams
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Unix
- **Feature:** Reports
- **Version:** 11.5

## Problem Description
The customer reported that the Linux sudoers report was truncating data for the column `GROUPMEMBERS` to fit the database field, which hindered their ability to provide complete information to auditors.

## Environment Details
- The issue occurred in a Netwrix Enterprise Auditor environment, specifically using the StealthAUDIT for Unix component.
- The database field for `GROUPMEMBERS` was initially set to a character limit of 250.

## Troubleshooting Steps
1. The support team requested the output from a PowerShell script to gather information about the installed applications and their versions.
2. The customer was asked to provide an export of the job in question and any relevant images.
3. The support team confirmed the account name associated with the ticket to ensure proper linkage to previous tickets.
4. The support team suggested increasing the character limit for the `GROUPMEMBERS` column in the database.

## Root Cause
The truncation of data was caused by the character limit of the `GROUPMEMBERS` column being set to 250 characters, which was insufficient for the data being collected.

## Solution
The issue was resolved by increasing the character limit for the `GROUPMEMBERS` column from 250 to 400 characters. This adjustment allowed the report to capture and display all necessary data without truncation.

## Notes
- It is important to monitor character limits for database fields when dealing with variable-length data to prevent truncation issues.
- Future configurations should consider potential data growth to avoid similar issues.
- The customer can reopen the case within 30 days if any related errors occur after closure.
```