## Ticket Metadata
- **Ticket ID:** 500Qk00000FoGvOIAV
- **Case Number:** 421086
- **Status:** Closed - Resolved
- **Account/Company:** IBM - Etihad Airways
- **Contact Name:** Praveen Huilgol
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Reports
- **Version:** 11.5

## Problem Description
The customer requested the addition of two columns to the "Empty Groups" report for Active Directory (AD). The new columns were to include the group description and the "Managed By" details from AD to enhance clarity in the report.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Active Directory
- **Product Version:** 11.5

## Troubleshooting Steps
1. Verified the existing structure of the "Empty Groups" report.
2. Integrated the requested columns into the `SA_PS_EmptyGroups_View` by executing the following SQL commands:
   ```sql
   IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].SA_PS_EmptyGroups_View') AND type in (N'V'))
   DROP VIEW SA_PS_EmptyGroups_View

   GO

   CREATE VIEW [SA_PS_EmptyGroups_View] AS
   SELECT ege.[Domain], ege.[Group], gv.[Description], ege.[NT Name], dnM.Value AS [Managed By], ege.[PrincipalId], ege.[Member Of], ege.[Type], gv.WhenCreated, gv.WhenChanged
   FROM dbo.SA_AD_EmptyGroups_Empty ege
   LEFT JOIN dbo.SA_ADInventory_GroupsView gv ON gv.[PrincipalId] = ege.[PrincipalId]
   LEFT JOIN dbo.SA_ADInventory_DistinguishedNames dnM ON dnM.[PrincipalId] = gv.[ManagedByPrincipalId]
   WHERE (gv.Distinguishedname NOT LIKE '%CN=Users,DC=etihad,DC=local' AND gv.DistinguishedName NOT LIKE '%OU=Microsoft Exchange Security Groups,DC=etihad,DC=local')
   ```
3. Recreated the "Empty Group Details" table in the "Empty Groups" report to reflect the changes.

## Root Cause
The issue was due to the existing report configuration not including the requested columns for group description and managed by details, which limited the clarity of the report for the customer.

## Solution
The issue was resolved by modifying the SQL view `SA_PS_EmptyGroups_View` to include the new columns for group description and managed by details. Additionally, the "Empty Group Details" table was recreated in the report to ensure the changes were reflected correctly.

## Notes
- Ensure that any future modifications to reports are communicated clearly to avoid similar requests.
- Regularly review report configurations to ensure they meet user requirements and include all necessary details.