## Ticket Metadata
- **Ticket ID:** 500Qk00000FZqzJIAT
- **Case Number:** 420586
- **Status:** Closed - Resolved
- **Account/Company:** Allstate Insurance Company
- **Contact Name:** Stealth Audit
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for AzureAD
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer reported an "Access Denied" error when attempting to connect to Azure AD Inventory scan from the server Y0185-APP0443-S. The error message indicated that the connection using the specified Application ID was denied.

## Environment Details
- **Platform:** Azure AD
- **Connection URL:** [ALLSTATE365.ONMICROSOFT.COM](https://ALLSTATE365.ONMICROSOFT.COM)
- **Authentication Method:** Application (client) ID and Client Secret

## Troubleshooting Steps
1. Verified the connection URL and Application ID used for authentication.
2. Confirmed the credentials being used were correct and up-to-date.
3. Requested confirmation of the Client Secret from the Active Directory Integration (ADI) team.
4. Checked for any PowerShell requirements for Azure AD/Entra ID.
5. Reviewed the configuration settings for the Azure AD connection in the Netwrix product.

## Root Cause
The issue was caused by an incorrect configuration of the credential profile. The system was set up to use an unsupported authentication method (modern authentication with a certificate) instead of the required Application (client) ID and Client Secret.

## Solution
The issue was resolved by reconfiguring the credential profile to use the correct authentication method. The customer was instructed to ensure that only the Application (client) ID and Client Secret value were used for authentication, as modern authentication with a certificate is not supported by the Azure AD Inventory DC.

## Notes
- Ensure that future configurations for Azure AD connections strictly adhere to the supported authentication methods.
- It is important to verify the credentials and their configuration before attempting to connect to Azure AD to avoid similar access issues.