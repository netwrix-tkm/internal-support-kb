## Ticket Metadata
- **Ticket ID:** 500Qk00000GAqvPIAT
- **Case Number:** 421894
- **Status:** Closed - Resolved
- **Account/Company:** TrustingSocial
- **Contact Name:** Dang Duong
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** NONE

## Problem Description
The customer requested the ability for Endpoint Protector to automatically apply policies for users by syncing groups from Azure Active Directory (Azure AD). They were currently applying policies manually, which was inefficient.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Sync Source:** Azure Active Directory

## Troubleshooting Steps
1. Reviewed the current configuration of Endpoint Protector and its integration with Azure AD.
2. Confirmed that manual policy application was the only method currently in use.
3. Investigated the capabilities of the Active Directory Sync feature within Endpoint Protector.
4. Checked for any existing documentation or settings related to automatic policy application based on Azure AD group membership.

## Root Cause
The issue stemmed from a lack of understanding of the capabilities of the Active Directory Sync feature in Endpoint Protector. The customer was unaware that the system could be configured to automatically apply policies based on Azure AD group memberships.

## Solution
The resolution involved guiding the customer on how to configure the Active Directory Sync feature in Endpoint Protector to enable automatic policy application. This included:
- Setting up the synchronization between Azure AD and Endpoint Protector.
- Ensuring that the policies in Endpoint Protector were linked to the appropriate Azure AD groups.
- Testing the configuration to confirm that adding a user to a group in Azure AD resulted in the corresponding policy being applied automatically.

## Notes
- It is important for users to familiarize themselves with the capabilities of the Active Directory Sync feature to leverage automatic policy management effectively.
- Future users should ensure that their Azure AD groups are correctly configured and linked to the appropriate policies in Endpoint Protector to avoid manual policy application.