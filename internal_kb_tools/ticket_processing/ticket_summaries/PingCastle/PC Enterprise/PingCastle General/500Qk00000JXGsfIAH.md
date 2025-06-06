## Ticket Metadata
- **Ticket ID:** 500Qk00000JXGsfIAH
- **Case Number:** 429894
- **Status:** Closed - Resolved
- **Account/Company:** Diehl Stiftung & Co.
- **Contact Name:** Thomas Muench
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer requested guidance on how to permit users from child domains to access entities in PingCastle via Claims. Despite configuring claim permissions, users could log in but were unable to view domain reports, only seeing the Infrastructure Menu and parts of the Configuration menu.

## Environment Details
- **Claims Type:** `http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid`
- **Authorization Level:** Operator (view domain reports and edit action plans)

## Troubleshooting Steps
1. Verified the claim permission configuration for the entity.
2. Attempted to explicitly permit the group on a domain.
3. Checked if granting permissions on a user basis allowed access to the domain reports.
4. Escalated the issue for further investigation.

## Root Cause
The issue was identified as a bug in the PingCastle software that affected the permissions for users from child domains when using claims.

## Solution
The problem was resolved by updating PingCastle to version 3.3.0.5, which included a fix for the identified bug related to permissions on entities.

## Notes
- Ensure that users from child domains are granted permissions correctly through claims in future configurations.
- Always check for the latest software updates that may resolve known issues.
- If similar issues arise, consider escalating to development for potential bugs in the software.