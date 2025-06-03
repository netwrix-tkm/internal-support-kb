## Ticket Metadata
- **Ticket ID:** 500Qk00000ItadCIAR
- **Case Number:** 428432
- **Status:** Closed - Resolved
- **Account/Company:** Sheridan&Co
- **Contact Name:** Peter Longley
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync Error
- **Version:** Not specified

## Problem Description
The customer reported that their client secret with Azure Active Directory had expired, and the system did not provide a warning prior to the expiration. Although a new secret was created, there was no option to update it in the Endpoint Synchronization settings, preventing the addition of new users and posing a risk of data leakage.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature Affected:** Active Directory Synchronization

## Troubleshooting Steps
1. Confirmed the expiration of the client secret and the inability to update it in the synchronization settings.
2. Communicated with the server team to verify if the configuration could be edited or if a complete reconfiguration was necessary.
3. Suggested the customer check the User Manual for steps on configuring Azure AD.
4. Advised the customer to delete the current synchronization configuration and recreate it to accommodate the new secret.

## Root Cause
The issue was caused by the expiration of the client secret used for Azure Active Directory synchronization, which was not flagged by the system prior to its expiration.

## Solution
The issue was resolved by instructing the customer to delete the existing synchronization configuration and recreate it using the new client secret. Detailed steps for this process were provided from the User Manual, specifically referencing the configuration section for Azure AD.

## Notes
- It is important for users to regularly monitor the status of their client secrets to prevent unexpected expirations.
- Future implementations should consider implementing alerts for upcoming expirations of critical credentials to avoid similar issues.
- Ensure that users have access to the User Manual for reference on configuration procedures.