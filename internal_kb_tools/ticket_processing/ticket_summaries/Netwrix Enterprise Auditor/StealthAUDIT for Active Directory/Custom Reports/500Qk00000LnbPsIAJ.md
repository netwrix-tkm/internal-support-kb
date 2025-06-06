## Ticket Metadata
- **Ticket ID:** 500Qk00000LnbPsIAJ
- **Case Number:** 435617
- **Status:** Closed - Resolved
- **Account/Company:** Fair Isaac Corporation (FICO)
- **Contact Name:** Chandan Trikha
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer reported that the "All Groups" report does not include groups from certain Organizational Units (OUs) in Active Directory (AD). Additionally, they requested assistance in creating a job to generate a report containing specific fields for user accounts in AD.

## Environment Details
- The customer utilizes custom reports that fetch data via SQL view from a database table containing data from AD about Active Directory Groups and their types.

## Troubleshooting Steps
1. Investigated the absence of groups in the specified OUs with the AD team.
2. Confirmed that there were no AD groups (Security or Distribution) present in the OUs in question.
3. Discussed the customer's requirements for a report containing specific user account fields.
4. Created a new SQL view to include the OU information for user accounts.

## Root Cause
The root cause of the issue was identified as the absence of any AD groups in the specified OUs. The customer was under the impression that the data was not being fetched correctly, but the data simply did not exist in AD.

## Solution
To resolve the issue, the following steps were taken:
1. Created a SQL view using the following command:
   ```sql
   CREATE VIEW SA_ADInventory_UsersView_Custom AS
   SELECT
     DomainName,
     SamAccountName,
     DisplayName,
     DistinguishedName,
     IsDeleted,
     EmployeeId,
     WhenCreated,
     WhenChanged,
     LastLogonTimestamp,
     AccountExpires,
     PwdLastSetDate,
     ACCOUNTDISABLE,
     REPLACE(SUBSTRING(DistinguishedName, CHARINDEX('OU=', DistinguishedName), LEN(DistinguishedName)), 'DN=', '') AS OU
   FROM
     [StealthAudit].[dbo].[SA_ADInventory_UsersView];
   ```
2. In the Job Analysis Part, created a script to drop the existing view if it exists:
   ```sql
   IF EXISTS (SELECT * FROM sys.views WHERE object_id = OBJECT_ID('SA_ADInventory_UsersView_Custom'))
   BEGIN
     DROP VIEW SA_ADInventory_UsersView_Custom;
   END
   ```
3. Created a report based on the newly populated data.
4. Rearranged the job tasks to ensure the drop view command is executed first, followed by creating the view and then generating the report.

## Notes
- Ensure that the presence of groups in the specified OUs is verified before creating reports to avoid similar confusion in the future.
- The customer’s boss was unavailable for follow-up during the week of the resolution; ensure to check in with them for any additional requirements or confirmations.