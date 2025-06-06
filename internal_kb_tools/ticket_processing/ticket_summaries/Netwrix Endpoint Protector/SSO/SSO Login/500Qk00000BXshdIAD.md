```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BXshdIAD
- **Case Number:** 411312
- **Status:** Closed - Resolved
- **Account/Company:** Viskase Companies
- **Contact Name:** System Contact from Website
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** Not specified

## Problem Description
The customer reported being locked out of their admin account after setting up Okta Single Sign-On (SSO). They were unable to regain access using their admin credentials.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **SSO Provider:** Okta

## Troubleshooting Steps
1. The support engineer, Flaviu Moldovan, reached out to the customer to schedule a remote session for troubleshooting.
2. A remote session was scheduled for June 7, 2024, at 12:30 PM CDT.
3. During the remote session, the following actions were taken:
   - Disabled Okta SSO from the backend.
   - Updated the user's role to Super Admin.
   - Re-enabled Okta SSO.

## Root Cause
The issue was caused by the configuration of Okta SSO, which prevented the admin user from accessing their account. Disabling Okta allowed the support team to modify the user role without interference from the SSO settings.

## Solution
The issue was resolved by:
- Disabling Okta SSO temporarily.
- Changing the user's role to Super Admin to restore access.
- Re-enabling Okta SSO after the changes were made.

## Notes
- Ensure that admin accounts are properly configured before implementing SSO solutions to avoid lockout scenarios.
- It may be beneficial to have a backup admin account that is not tied to SSO for emergency access.
```