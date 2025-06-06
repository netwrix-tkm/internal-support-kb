## Ticket Metadata
- **Ticket ID:** 500Qk00000HRCuYIAX
- **Case Number:** 424991
- **Status:** Closed - Resolved
- **Account/Company:** Baldwin Risk Partners
- **Contact Name:** Ryan Oleary
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Inventory
- **Version:** 11.6

## Problem Description
The customer reported irregularities in their Netwrix Enterprise Auditor (NEA) instance, specifically that several users known to exist were not found in NEA or Active Inventory Collection (AIC) reports.

## Environment Details
- **Database:** StealthAUDIT
- **Active Directory (AD) Configuration:** Users were located in the Organizational Unit (OU) "Construction Risk Partners."

## Troubleshooting Steps
1. Executed a SQL query against the database to check for user records before the full AD collection:
   ```sql
   Use StealthAUDIT;
   select * from StealthAUDIT.dbo.SA_ADInventory_Principals where ObjectClass = 4 and SamAccountName like '%mike.grill%';
   ```
2. Searched the "ADInventory_UserView" in NEA using "DistinguishedName" to verify user presence before the full collection.
3. Changed the configuration setting for the "1-AD_Scan" Job:
   - Navigated to Jobs > ".Active Directory Inventory" > "1-AD_Scan" Job > "Configure" > "Queries" > "Query Properties" > "Configure" button > "Options."
   - Unchecked "Collect only updates since the last scan" to enable a full collection.
4. Ran the full collection, which took approximately 8-9 minutes.
5. Verified the presence of previously missing users in the database and AIC after the full collection.

## Root Cause
The issue was caused by the configuration of the "1-AD_Scan" Job, which was set to collect only updates since the last scan. This incremental collection did not capture all existing users, leading to the reported irregularities.

## Solution
The issue was resolved by performing a full Active Directory Inventory (ADI) scan. After changing the configuration to uncheck the incremental collection option, the previously missing users were successfully collected and appeared in both the database and AIC.

## Notes
- After resolving the issue, it is recommended to revert the configuration back to differential collection to optimize performance, as a full scan may not be necessary on a regular basis.
- Future cases should ensure that the configuration settings for AD scans are reviewed to prevent similar issues with missing user records.