## Ticket Metadata
- **Ticket ID:** 500Qk00000JdzDZIAZ
- **Case Number:** 430182
- **Status:** Closed - Resolved
- **Account/Company:** Regina Maria
- **Contact Name:** Cristian Voicu
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** AD Sync - Other
- **Version:** 5.9.4.1

## Problem Description
The Regina Maria team reported an issue where they were unable to add a new EPP admin to the Active Directory (AD) Administrators Group via AD Sync. The error was indicated by the message: "Am mai incercat sa adaug un nou coleg ca admin in platforma via AD Sync, dar nu functioneaza."

## Environment Details
- **Server Version:** 5.9.4.1

## Troubleshooting Steps
1. Verified the server version and compatibility with Active Directory.
2. Checked the configuration settings for Active Directory Sync.
3. Reviewed the permissions of the user attempting to add the new admin.
4. Conducted a remote session to observe the issue in real-time.
5. Attempted to manually add the user to the AD Administrators Group to replicate the issue.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the Active Directory Sync settings, which prevented the proper synchronization of user roles and permissions.

## Solution
The issue was resolved during a remote session by:
- Correcting the configuration settings for Active Directory Sync.
- Ensuring that the user had the necessary permissions to add new admins.
- Performing a successful test to confirm that the new EPP admin could be added to the AD Administrators Group without further issues.

## Notes
- Ensure that all users attempting to modify AD groups have the appropriate permissions.
- Regularly review and update the Active Directory Sync settings to prevent similar issues in the future.
- Document any changes made to the configuration for future reference.