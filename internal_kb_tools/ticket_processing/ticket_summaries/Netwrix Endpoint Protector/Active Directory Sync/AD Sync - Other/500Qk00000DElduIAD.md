## Ticket Metadata
- **Ticket ID:** 500Qk00000DElduIAD
- **Case Number:** 415378
- **Status:** Closed - Resolved
- **Account/Company:** SSI Sviluppo Sistemi Informativi srl - Dis
- **Contact Name:** Massimo Chierici
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** NONE

## Problem Description
The customer was unable to synchronize Active Directory (AD) Administrators using the "Sync AD Administrators" button, receiving an error message stating "Group not found or no users present in group!" despite successful connection tests with AD.

## Environment Details
- The user account used for the AD connection had domain admin privileges.
- The group being synchronized was located in a custom AD Organizational Unit (OU).

## Troubleshooting Steps
1. Verified the group name syntax used for synchronization, including pure group name, Canonical Name, and Distinguished Name.
2. Tested the connection to AD using the "Test" button, which returned a successful connection message.
3. Attempted synchronization with various groups, including the built-in Domain Admins group.
4. Ensured that the user account had the necessary permissions and was a member of the specified group.
5. Consulted with R&D for further insights and potential solutions.

## Root Cause
The issue was caused by an incorrect format of the domain name in the Active Directory authentication settings. The customer had entered "ssi.local" instead of the required format "DC=ssi,DC=local". This misconfiguration prevented the synchronization process from recognizing the specified group.

## Solution
The issue was resolved by correcting the domain name format in the AD authentication settings to "DC=ssi,DC=local". After saving the changes, the customer was able to successfully synchronize the AD Administrators group.

## Notes
- Ensure that all settings are saved before attempting to sync AD Administrators.
- The Active Directory Administrators Group cannot include primary groups, as this is restricted by Microsoft.
- Always verify the syntax and format of the domain name when configuring AD authentication to avoid similar issues in the future.