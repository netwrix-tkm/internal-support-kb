## Ticket Metadata
- **Ticket ID:** 500Qk00000KjfmiIAB
- **Case Number:** 432588
- **Status:** Closed - Resolved
- **Account/Company:** Woodmen of the World Life Insurance Society
- **Contact Name:** Jeremy Kaiser
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported that after adding a new SQL database to the scan, the reports generated displayed "No data available" for some entries, while others showed data.

## Environment Details
- **Product Version:** 11.6.0.74
- The customer was not on the latest version of Netwrix Enterprise Auditor, which had released patches related to database performance.

## Troubleshooting Steps
1. Launched Netwrix Enterprise Auditor (NEA).
2. Navigated to the Database node under the job folder.
3. Accessed the SQL folder and then the Permission folder.
4. Created a new folder for the custom report.
5. Observed that some reports displayed data while others were missing data.
6. Discussed the issue with the DBA, who suggested that NEA might not consistently write data to the table.
7. Recommended the customer upgrade to the latest version of NEA to resolve potential performance issues.

## Root Cause
The root cause of the issue was identified as the customer's use of an outdated version of Netwrix Enterprise Auditor, which lacked recent patches that addressed database performance and data writing consistency.

## Solution
The resolution involved advising the customer to upgrade to the latest version of Netwrix Enterprise Auditor. The customer was informed that further investigation could be conducted after the upgrade was completed.

## Notes
- It is crucial for customers to keep their software updated to benefit from performance improvements and bug fixes.
- Future cases involving missing data in reports should first check the software version and recommend an upgrade if the customer is not on the latest release.