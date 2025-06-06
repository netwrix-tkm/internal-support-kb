## Ticket Metadata
- **Ticket ID:** 500Qk00000NPSwqIAH
- **Case Number:** 440265
- **Status:** Closed - Resolved
- **Account/Company:** Oak Hill Advisors
- **Contact Name:** Zinoviy Langer
- **Product:** Netwrix Enterprise Auditor
- **Component:** Reporting Console
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer requested guidance on how to perform a file share review using Netwrix Enterprise Auditor. They needed reports in CSV format that included specific fields (timestamp, SAM account name, and file share path) which were previously available in the decommissioned Netwrix Auditor but not in the current version.

## Environment Details
- The customer has FSAA (File Share Access Audit) scans configured.
- The Access Information Center (AIC) is installed but not fully utilized for reporting.

## Troubleshooting Steps
1. Discussed the customer's requirements for the report format and fields needed.
2. Provided documentation on creating custom reports and using the SQLViewCreation tool.
3. Explained the access restrictions in the NEA console and how they affect user permissions.
4. Offered a remote session to assist with report configuration due to access issues.

## Root Cause
The issue stemmed from the transition from Netwrix Auditor to Netwrix Enterprise Auditor, where certain report fields were no longer available in the new reporting format. Additionally, access configuration issues led to the customer being locked out of the reporting console.

## Solution
- Provided detailed instructions on how to create custom reports using the SQLViewCreation tool.
- Clarified the differences between the Access Information Center and the reporting console.
- Ensured the customer understood how to manage user permissions to avoid lockouts in the future.

## Notes
- It is crucial to ensure that all necessary users, especially admins, are included in the access list to prevent lockouts.
- The customer was advised to reach out for further assistance if they encountered additional issues or needed help with report creation.
- Documentation links provided for future reference:
  - [SQLViewCreation Overview](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Analysis/SQLViewCreation/Overview.htm)
  - [Creating Custom Reports](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Report/Create.htm#Create)