## Ticket Metadata
- **Ticket ID:** 500Qk00000NQvbiIAD
- **Case Number:** 440315
- **Status:** Closed - Resolved
- **Account/Company:** Massachusetts Property Insurance Underwriting Association
- **Contact Name:** Mawloda Khudaynazar
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that their Stealthbits scanner was not returning any results despite having configured activity monitoring on all folders within FS01 and the Financial folder.

## Environment Details
- The customer is using version 11.6 of the Netwrix Enterprise Auditor.
- The FileSystem job runs every 2 weeks, while the special HR VP job and another job run monthly.

## Troubleshooting Steps
1. Confirmed that the FileSystem job runs every 2 weeks and the HR VP job runs monthly.
2. Reviewed the "Departments HR_VP Activity" report and found only one row of data for March 4, 2025.
3. Recommended the customer perform four actions worth of test activity in the "E:DepartmentsHR_VP%" department and maintain a record of this activity.
4. Verified that the `SA_FSAC_ActivityEvents` table was populated with data on the April 7 run, returning over 300,000 rows when queried.
5. Checked the WHERE clause against the `SA_FSAC_ActivityEventsView`, confirming it returned the same single row found in the monthly report.

## Root Cause
The issue was identified as a lack of activity being recorded in the "Departments HR_VP Activity" report, which was due to insufficient test activity being performed in the monitored folders.

## Solution
The customer was advised to conduct test activities in the specified department and confirm that these activities were recorded in the report for April 2025. This approach ensured that the data collection process was functioning correctly, and the report would reflect the expected results.

## Notes
- It is important for users to perform sufficient test activities in monitored folders to ensure that the data collection and reporting features of the Netwrix Auditor work as intended.
- Future users experiencing similar issues should verify the configuration of their jobs and ensure that activity is being generated and recorded properly.