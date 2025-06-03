```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BXkvOIAT
- **Case Number:** 411294
- **Status:** Closed - Resolved
- **Account/Company:** SingleSource Property Solutions / V300 DC+CAP
- **Contact Name:** Bryan Lantz
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 12.1

## Problem Description
The customer reported an issue where, upon logging into the EPP Portal with their admin account, they were automatically redirected to a password change page. The system did not recognize their current password, despite multiple verifications. After an admin reset the password, the new password also failed to work, while the old password remained functional.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **User Role:** Super Admin

## Troubleshooting Steps
1. The user attempted to log in multiple times with the correct password.
2. Another admin reset the user's EPP password.
3. The user attempted to log in with the new password, which failed.
4. The user’s EPP account was deleted and recreated with a temporary password.
5. The user attempted to log in with the temporary password, which also failed.
6. The user confirmed that the old password still worked and was no longer redirected to the password reset page.

## Root Cause
The issue was identified as a database inconsistency related to the Super Admin accounts, which caused the password reset functionality to malfunction.

## Solution
The technical support team made adjustments in the database for the Super Admin accounts to resolve the inconsistency. Following this, the account settings were verified, and two-factor authentication (2FA) was enabled for added security.

## Notes
- It is recommended to monitor Super Admin accounts for similar issues in the future.
- Ensure that any password resets are followed by a verification of account settings to prevent recurrence of similar issues.
- The ticket was left open for one week post-resolution to confirm that the issue did not reoccur.
```