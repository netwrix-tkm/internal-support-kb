## Ticket Metadata
- **Ticket ID:** 500Qk00000CIgZlIAL
- **Case Number:** 413026
- **Status:** Closed - Resolved
- **Account/Company:** AMVAC Chemical Corporation
- **Contact Name:** Brandon Flaming
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer requested assistance in obtaining a list of stale files from the 'Shares with Stale Content' report, which only displayed the number of stale files without providing the actual list.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems
- **Build Number:** 66

## Troubleshooting Steps
1. Advised the customer to check the FS_CleanupAssessment Job to retrieve the list of stale files.
2. The customer reported an error: "Invalid length parameter passed to the LEFT or SUBSTRING function."
3. Suggested the customer remove the "Value" entry from a .csv file located in the job folder and re-run the job.
4. Confirmed that the Active Directory Inventory job group and FileSystem jobs were executed.
5. The customer reported that the report was blank despite having stale files, indicating potential misconfiguration in job settings.
6. Requested the customer to provide the settings for the FS_CleanupAssessment job for further analysis.

## Root Cause
The initial issue stemmed from a misconfiguration in the FS_CleanupAssessment job settings, which prevented the retrieval of stale file data. The error encountered was related to SQL processing within the job.

## Solution
The issue was resolved when the customer re-ran all FileSystem jobs after making the necessary adjustments to the job settings. This allowed the customer to successfully pull up the list of stale files.

## Notes
- Ensure that all relevant jobs are executed before attempting to retrieve reports.
- If encountering SQL-related errors, check for misconfigurations in job settings and any problematic entries in associated .csv files.
- For future reference, advise customers to keep their job settings documented to facilitate troubleshooting.