## Ticket Metadata
- **Ticket ID:** 500Qk00000LkpOQIAZ
- **Case Number:** 435453
- **Status:** Closed - Resolved
- **Account/Company:** Delaware Department of Corrections
- **Contact Name:** Patrick Adams
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The customer requested assistance with licensing counts for user accounts in the Netwrix Enterprise Auditor environment.

## Environment Details
- **Netwrix Enterprise Auditor (NEA):** 11.5.0.177
- **Netwrix Access Information Center (AIC):** 11.5.0.112
- **Netwrix Activity Monitor (NAM):** 6.0.928

## Troubleshooting Steps
1. Confirmed the versions of the Stealth applications running in the environment.
2. Created a new report based on the `SA_ADInventory_UsersView`.
3. Applied filters for `IsDeleted`, `DistinguishedName`, `ACCOUNTDISABLE`, and `OU=DoC`.
4. Retrieved a result set of approximately 3,900 users.

## Root Cause
The issue stemmed from the need to accurately count and report on user accounts, specifically those that were deleted or disabled, which required the creation of a custom report.

## Solution
The issue was resolved by creating a custom report in the Netwrix Enterprise Auditor using the `SA_ADInventory_UsersView`. The report was filtered to include only relevant user accounts, allowing for an accurate licensing count.

## Notes
- Ensure that future reports are created with the appropriate filters to avoid discrepancies in user account counts.
- Refer to the following documentation for guidance on report creation:
  - [Creating a Report](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Report/Create.htm#copy_an_existing_report)
  - [Report Configuration Wizard](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Report/Wizard/Widgets.htm#grid)