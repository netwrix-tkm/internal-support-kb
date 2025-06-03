## Ticket Metadata
- **Ticket ID:** 500Qk00000LeKtgIAF
- **Case Number:** 435181
- **Status:** Closed - Resolved
- **Account/Company:** National Oil Well Varco (Formerly Varco)
- **Contact Name:** Bret Campbell
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync Error
- **Version:** Not specified

## Problem Description
The customer reported that while two users were successfully added to their Azure AD group and reflected in the Netwrix Endpoint Protector (EPP) on February 6, a third user added later that day was not synchronized into the corresponding group in EPP. Additionally, the "Last Synchronization" field in the EPP console was blank.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Sync Method:** Active Directory Sync

## Troubleshooting Steps
1. Verified the synchronization status and logs for any errors.
2. Checked the Azure AD group membership for the affected users.
3. Investigated the sync_aad.log file for any indications of issues.
4. Confirmed the sync interval settings.
5. Queried the database to check for any groups that had not been updated since the last successful sync.

## Root Cause
The synchronization error was caused by the inclusion of a group that had been deleted in Azure AD but not removed from the EPP's synchronization configuration. This discrepancy led to the sync process failing, preventing updates to group memberships.

## Solution
The issue was resolved by removing the deleted group from the EPP synchronization configuration. Once the group was removed, the synchronization process was able to complete successfully, and the third user was added to the corresponding group in EPP.

## Notes
- Ensure that any groups deleted in Azure AD are also removed from the EPP synchronization settings to prevent similar issues in the future.
- Regularly monitor the "Last Synchronization" field in the EPP console to catch synchronization issues early.
- Consider implementing alerts for synchronization failures to facilitate quicker resolution.