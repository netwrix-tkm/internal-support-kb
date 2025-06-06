## Ticket Metadata
- **Ticket ID:** 500Qk00000EUvyXIAT
- **Case Number:** 418281
- **Status:** Closed - Resolved
- **Account/Company:** Westpac Banking Corporation
- **Contact Name:** Mark Chambers
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported errors during the scheduled FSAC import jobs for additional Isilon access zones. The main error encountered was related to a system exception indicating an abort received while retrying.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.5

## Troubleshooting Steps
1. Reviewed the error logs to identify the specific error message.
2. Analyzed the configuration of the FSAC import jobs and the Isilon access zones.
3. Checked for any existing deadlocks or timeout issues in the database.
4. Attempted to adjust the command timeout settings to see if it would alleviate the issue.

## Root Cause
The issue was identified as a timeout problem during the import process, likely due to the database not responding in a timely manner, leading to aborts during retries.

## Solution
The issue was resolved by increasing the command timeout parameter to 6 hours (360 minutes) in the storage global settings. This adjustment allowed the import jobs to complete successfully without encountering the abort error.

## Notes
- It is recommended to monitor the performance of the import jobs after making such changes to ensure that the timeout settings are appropriate for the workload.
- Future configurations should consider the expected volume of data and adjust timeout settings accordingly to prevent similar issues.