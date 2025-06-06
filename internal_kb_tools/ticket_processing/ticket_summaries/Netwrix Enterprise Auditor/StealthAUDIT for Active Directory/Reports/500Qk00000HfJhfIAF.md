## Ticket Metadata
- **Ticket ID:** 500Qk00000HfJhfIAF
- **Case Number:** 425507
- **Status:** Closed - Resolved
- **Account/Company:** Caxton Alternative Management LP
- **Contact Name:** Rick Schaktman
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer reported that a daily activity report for a specific folder was sending stale data, showing activity from over a week ago instead of the expected daily updates. The analysis preview displayed blank data, while the results table contained outdated information.

## Environment Details
- The issue was related to the Netwrix Enterprise Auditor (NEA) and Netwrix Activity Monitor (NAM) configurations.
- The report was configured to filter data from the SQL view `SA_FSAC_DailyActivityView`.

## Troubleshooting Steps
1. Reviewed the logs provided by the customer for any signs of issues with the NEA job.
2. Verified the configuration of NAM to ensure it was set up to collect the desired data.
3. Attempted to search for data in NAM but found it only in the raw agent logs.
4. Checked the SQL database and confirmed that fresh data was present in `SA_FSAC_DailyActivityView`.
5. Analyzed the filtering logic of the analysis task that creates the report, which was filtering for `isoutlookinterval|Yesterday|`.
6. Conducted a test change to the configuration and planned to monitor the results the following day.

## Root Cause
The root cause of the issue was identified as the filtering logic in the analysis task. The task was designed to filter data based on the previous day's activity. If there was no new activity, the table would remain blank, leading to the appearance of stale data in the report until fresh data was available.

## Solution
The issue was resolved by confirming that the report was functioning as intended, with the stale data being a result of no new activity being recorded. The customer was offered to modify the filter for more reliable results, but they did not schedule a follow-up meeting to implement this change. The ticket was closed after the customer indicated they no longer needed assistance.

## Notes
- It is important to ensure that the filtering logic in reports is configured correctly to avoid confusion with stale data.
- Future users should be aware that if no new activity is recorded, the report will not clear previous data, which may lead to misunderstandings about the report's accuracy.
- Regular monitoring of report configurations and data collection settings is recommended to ensure optimal performance.