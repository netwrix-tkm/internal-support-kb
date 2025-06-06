## Ticket Metadata
- **Ticket ID:** 500Qk00000GLWeqIAH
- **Case Number:** 422342
- **Status:** Closed - Resolved
- **Account/Company:** Massachusetts Property Insurance Underwriting Association
- **Contact Name:** Jonathan Candido
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported an issue where they were unable to add a new user to the Netwrix Enterprise Auditor console, despite having added the user as an admin in the Access settings.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.6

## Troubleshooting Steps
1. Confirmed that the user was added as an admin in the Access settings.
2. Reviewed the Netwrix Help Center documentation regarding Role Based Access.
3. Contacted the customer to verify if SQL roles had been created in SQL Management Studio.
4. Provided the customer with a link to the relevant documentation for configuring roles.

## Root Cause
The issue was caused by the absence of corresponding roles created within SQL Management Studio. Role Based Access requires that roles be established in SQL Management Studio before users can be assigned those roles in Enterprise Auditor.

## Solution
To resolve the issue, the following steps were taken:
1. Instructed the customer to create the necessary roles in SQL Management Studio.
2. Advised the customer to assign the created roles to the user both in SQL Management Studio and in Enterprise Auditor.
3. Provided a link to the Netwrix Help Center article for detailed guidance on configuring roles: [Configure Roles](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Settings/Access/RoleBased/ConfigureRoles.htm).

## Notes
- For future reference, ensure that corresponding roles are created in SQL Management Studio before attempting to assign users in Enterprise Auditor.
- It is important to verify role assignments in both SQL Management Studio and Enterprise Auditor to avoid similar issues.