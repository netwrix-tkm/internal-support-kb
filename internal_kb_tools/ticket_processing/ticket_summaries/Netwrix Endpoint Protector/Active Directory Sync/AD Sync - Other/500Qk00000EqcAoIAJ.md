## Ticket Metadata
- **Ticket ID:** 500Qk00000EqcAoIAJ
- **Case Number:** 418981
- **Status:** Closed - Resolved
- **Account/Company:** Barthelmeß EDV-Service GmbH
- **Contact Name:** Alexander Barthelmess
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** Not specified

## Problem Description
The customer reported that the default Active Directory group "Domain Users" does not appear in the list of users under Device Control -> Users, preventing them from applying user policies to this group.

## Environment Details
- The Active Directory Sync feature is functioning correctly, as other groups and users are syncing without issues.
- Linked devices have been successfully unblocked.

## Troubleshooting Steps
1. Verified that the Active Directory Sync was operational and syncing other groups correctly.
2. Attempted to sync users from the "Domain Users" primary group.
3. Recommended creating a new group for user policies, but the customer was reluctant to manually add users to this new group.
4. Suggested adding devices to a custom class to allow access for all users.

## Root Cause
The issue arose due to a limitation in the Netwrix Endpoint Protector (EPP) that prevents syncing users from a primary group like "Domain Users." This limitation restricts the visibility of the group in the Device Control user list.

## Solution
The resolution involved advising the customer to create a custom class for devices, which would allow access for all users without needing to manually add them to a new group. This approach circumvented the limitation of syncing from the primary group.

## Notes
- It is important to note that syncing from primary groups is not supported in EPP due to inherent limitations.
- For future cases, consider recommending the use of custom classes for broader user access when dealing with similar group visibility issues.