## Ticket Metadata
- **Ticket ID:** 500Qk00000MIcyHIAT
- **Case Number:** 436986
- **Status:** Closed - Resolved
- **Account/Company:** Morton Community Bank
- **Contact Name:** Skye Jackson
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** Not specified

## Problem Description
A user, Kris Hall (username: KDHall, email: kris.hall@mortonbank.com), who previously appeared in the admin panel via Active Directory (AD) Sync, was missing. A manual sync did not resolve the issue, and attempts to add the user manually were unsuccessful.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Sync Method:** Active Directory Sync

## Troubleshooting Steps
1. Conducted a remote session to investigate the issue.
2. Attempted a manual sync of the user without success.
3. Changed database flags for the user:
   - Set "deleted" flag to `0`
   - Set "is_active" flag to `1`
   - Set "is_super_admin" flag to `1`

## Root Cause
The user was marked as deleted and inactive in the database, which prevented the user from appearing in the admin panel and accessing the EPP UI.

## Solution
During the remote session, the database flags for the user were updated to reflect that the user was not deleted and was active. After these changes, the customer confirmed that Kris Hall was able to access the EPP UI successfully.

## Notes
- Ensure that user accounts are not mistakenly marked as deleted or inactive in the database to prevent similar issues in the future.
- Regularly verify the synchronization process to ensure all users are correctly reflected in the admin panel.