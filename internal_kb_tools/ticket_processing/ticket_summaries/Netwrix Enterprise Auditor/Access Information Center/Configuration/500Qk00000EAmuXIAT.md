## Ticket Metadata
- **Ticket ID:** 500Qk00000EAmuXIAT
- **Case Number:** 417555
- **Status:** Closed - Resolved
- **Account/Company:** PERN S.A.
- **Contact Name:** Support Appeal
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
After upgrading the Enterprise Auditor core and Access Information Center to version 11.6, the customer reported several issues with the Access Information Center (AIC) portal, including:
- Polish translation not functioning for "Manage Access" and "Access Request."
- Admin users from Active Directory (AD) unable to log in to the portal, with only the built-in admin account working.
- The "Change Owner" option missing from the portal, preventing owners from changing access to resources.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 11.6.0.21

## Troubleshooting Steps
1. Reviewed the logs sent from the client environment.
2. Confirmed that the issues arose post-upgrade to version 11.6.
3. Investigated the configuration settings in the AIC.
4. Checked the AD group settings related to AIC permissions.

## Root Cause
The root cause of the issues was identified as an incorrect configuration in the AIC settings. Specifically, the setting that allows AD groups to make changes in AIC was not enabled.

## Solution
To resolve the issue, the following change was made in the AIC configuration file:
```xml
<add key="ADServiceAllowChanges" value="False" /> 
```
This line was changed to:
```xml
<add key="ADServiceAllowChanges" value="True" />
```
After making this change, the issues with admin logins and the missing "Change Owner" option were resolved.

## Notes
- Ensure that AD groups are properly configured to allow changes in AIC settings after any upgrades to prevent similar issues in the future.
- It is advisable to test all functionalities post-upgrade to identify any configuration-related issues early on.