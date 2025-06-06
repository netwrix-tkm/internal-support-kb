## Ticket Metadata
- **Ticket ID:** 500Qk00000IkqdxIAB
- **Case Number:** 428004
- **Status:** Closed - Resolved
- **Account/Company:** Assystem Energy & Infrastructure Limited
- **Contact Name:** James Allen
- **Product:** Netwrix Enterprise Auditor
- **Component:** Active Directory
- **Feature:** Database
- **Version:** 11.6

## Problem Description
The customer requested a modification to the AD_StaleUsers job report to display stale users who have not logged on for the last 30 days, instead of the default 60 days.

## Environment Details
- The issue pertains to the Netwrix Enterprise Auditor platform, specifically the Active Directory Inventory solution.

## Troubleshooting Steps
1. Reviewed the SQL query for the "AD_StaleUsers" job, which joins data from `ADInventory_UsersView` and `ADInventory_ExceptionsView`.
2. Identified that the `ADInventory_ExceptionsView` is populated by the "3-AD_Exceptions" job, which uses a parameter called `@STALE_THRESHOLD` to determine stale users based on a 60-day threshold.
3. Provided instructions to the customer on how to change the `@STALE_THRESHOLD` parameter from 60 to 30 days:
   - Navigate to ".Active Directory Inventory" solution > "3-AD_Exceptions" job > "Analysis" > select "Stale Users" analysis.
   - Select "Analysis Configuration".
   - Locate the `@STALE_THRESHOLD` variable and change its value from 60 to 30.
   - Run the ".Active Directory Inventory" and "Active Directory" jobs to update the data.
4. Followed up with the customer to confirm the changes and check the results.

## Root Cause
The default configuration of the AD_StaleUsers job was set to identify users who had not logged on for 60 days. The SQL query used for this job was not initially configured to allow for easy modification of the stale user threshold.

## Solution
The issue was resolved by guiding the customer through the process of modifying the `@STALE_THRESHOLD` parameter in the "3-AD_Exceptions" job configuration. After the parameter was changed to 30 days and the relevant jobs were run, the customer confirmed that the report now accurately reflected users who had not logged on for the last 30 days.

## Notes
- Ensure that the ".Active Directory Inventory" job is run regularly, as it is the primary source of AD information for the "Active Directory" solution.
- This case highlights the importance of understanding the underlying SQL queries and job configurations in Netwrix Enterprise Auditor to effectively address customer requests for report modifications.