## Ticket Metadata
- **Ticket ID:** 500Qk00000NmYjlIAF
- **Case Number:** 441199
- **Status:** Closed - Resolved
- **Account/Company:** Censys
- **Contact Name:** Armando Basurto Moreno
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Groups
- **Version:** 5.9.4

## Problem Description
The customer, Armando Basurto from Censys, reported issues after migrating their server to a new instance. They were unable to deploy the Endpoint Protector module across the organization due to uncertainties regarding its functionality, specifically concerning the import of users and computers.

## Environment Details
- The customer had recently migrated their server to a new instance.
- The Endpoint Protector (EPP) server settings were confirmed to be correct, but only groups were imported, while users and computers were not.

## Troubleshooting Steps
1. Conducted a remote session with the customer to review the EPP server settings.
2. Verified that the EPP server settings were correct.
3. Recommended the customer check the Azure settings for proper configuration.
   - Provided links to relevant documentation:
     - [EPP Directory Services Overview](https://helpcenter.netwrix.com/bundle/EndpointProtector_5.9.4/page/Content/EndpointProtector/Admin/DirectoryServices/Overview.htm)
     - [API Permission Configuration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis)
4. Instructed the customer to re-sync after making the necessary Azure settings adjustments.

## Root Cause
The issue stemmed from the Azure Active Directory (AD) configuration, specifically regarding how users were being mapped during synchronization. The settings in Azure were not correctly configured to ensure that users were imported into the appropriate groups.

## Solution
The customer successfully added groups to the Azure application and performed a new synchronization, which resulted in users appearing in their respective groups. However, all users were initially assigned to the "Default Department." The support engineer advised the customer to maintain the Default Department and utilize groups for departmental separation.

## Notes
- It is important to ensure that the Azure AD settings are correctly configured to prevent issues with user mapping during synchronization.
- The "Map on-premises users" feature in Azure AD should be enabled or disabled based on the specific hybrid environment setup to avoid duplicate usernames.
- Future users should be advised to check both EPP server settings and Azure configurations when facing similar issues.