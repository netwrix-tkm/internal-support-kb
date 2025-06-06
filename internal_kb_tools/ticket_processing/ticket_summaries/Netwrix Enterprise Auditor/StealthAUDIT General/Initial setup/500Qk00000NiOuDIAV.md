## Ticket Metadata
- **Ticket ID:** 500Qk00000NiOuDIAV
- **Case Number:** 441061
- **Status:** Closed - Resolved
- **Account/Company:** Broadview Federal Credit Union (Formally Capital Communications Federal Credit Union (CAP COM))
- **Contact Name:** Marc Payzant
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer required assistance in setting up the Entra ID within the Netwrix Enterprise Auditor platform.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Version:** 11.6

## Troubleshooting Steps
1. Initial communication established with the customer regarding the setup of Entra ID.
2. Scheduled meetings to discuss the setup process and requirements.
3. Attempted to run the `AADI_RegisterAzureAppAuth` job to create the Entra Inventory.
4. Executed PowerShell commands to install Microsoft Graph, NuGet, and the Azure Module.
5. Identified an error indicating that the user account could not communicate properly with the tenant, suspected to be related to Okta permissions.
6. Customer was advised to work with their internal team to resolve the permission issues.
7. Follow-up meetings were scheduled to continue troubleshooting after the internal team addressed the permissions.

## Root Cause
The initial issue was caused by account permission problems related to Okta, which prevented the user from properly communicating with the Azure tenant.

## Solution
The issue was resolved by running the `AADI_RegisterAzureAppAuth` job successfully after the customer resolved the Okta access issues. The customer confirmed that they could log into Entra directly, and the job executed without errors.

## Notes
- Ensure that user accounts have the necessary permissions to communicate with the Azure tenant before attempting to run the `AADI_RegisterAzureAppAuth` job.
- Future cases should verify the integration with identity providers like Okta to prevent similar permission-related issues.
- The customer expressed the need for further assistance with the Activity Monitor piece, which may require additional follow-up.