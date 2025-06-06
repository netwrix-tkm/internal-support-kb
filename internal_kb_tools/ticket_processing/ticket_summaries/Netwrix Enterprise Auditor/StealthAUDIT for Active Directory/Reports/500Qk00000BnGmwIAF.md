## Ticket Metadata
- **Ticket ID:** 500Qk00000BnGmwIAF
- **Case Number:** 411850
- **Status:** Closed - Resolved
- **Account/Company:** University of Kansas Medical Center - Remote campus
- **Contact Name:** Jason Rule
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Reports
- **Version:** 11.5

## Problem Description
The customer requested assistance in creating a group change report for a specific Active Directory group and sending it to an email address. Additionally, they wanted to discuss setting up activity details monitoring for a folder located under `C:\Program Files`.

## Environment Details
- **StealthAUDIT (SA):** 11.5.0.205
- **StealthAUDIT Access Information Center (AIC):** 11.5.0.120
- **SA Sensitive Data (SDD):** 11.5.0.65
- **Netwrix Activity Monitor (NAM):** Version not specified, but SAM Agent Services were visible.

## Troubleshooting Steps
1. Confirmed the versions of the Stealth applications running in the environment.
2. Created a job based on a prior job group to filter group membership changes using the following SQL query:
   ```sql
   IF EXISTS (SELECT * FROM sys.objects WHERE object_id = object_id(N'[dbo].[SA_PP_Groups]') AND TYPE in (N'U'))
     DROP TABLE [SA_PP_Groups]
   SELECT * Into [SA_PP_Groups]
   From SA_AD_Changes_GroupMembershipChanges
   Where [Group] like '%PP-%' And [when discovered] >= DATEADD(day, -1, GETDATE())
   ```
3. Updated URL settings for securing the web console in Netwrix Enterprise Auditor and Access Information Center.
4. Discussed the need to update email recipients for the new PP-Groups report based on the `SA_AD_Changes_GroupMembershipChanges` table.

## Root Cause
The issue stemmed from the need for a customized report that was not readily available in the existing reporting features of the Netwrix Enterprise Auditor. The customer required specific filtering based on group membership changes.

## Solution
The issue was resolved by creating a custom SQL job that filtered group membership changes and setting up the necessary configurations to secure the web console. The email recipients for the report were also updated accordingly. A follow-up call was scheduled to ensure all requirements were met and to discuss the monitoring of the specified folder.

## Notes
- Ensure that the SQL job is regularly reviewed and updated as needed to reflect any changes in group structures.
- Future requests for similar reports should consider the existing canned reports under Jobs > Active Directory > 6.Activity > Group Usage as a starting point.
- Always confirm the versions of the applications in use to ensure compatibility with the requested features.