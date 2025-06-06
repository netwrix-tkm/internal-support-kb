```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000KLtlxIAD
- **Case Number:** 431422
- **Status:** Closed - Resolved
- **Account/Company:** Warner Brothers Sound Studio UK
- **Contact Name:** DLL Engineering
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported being unable to log in to their on-premise EPP server since the beginning of the year. All admin account logins resulted in incorrect login messages, and they did not have a local account to access the server.

## Environment Details
- The admin accounts are integrated with Active Directory.
- The server was experiencing a CIFs error related to log storage.

## Troubleshooting Steps
1. Verified the login attempts and confirmed that all admin accounts were locked out.
2. Checked the server GUI for error messages and identified a CIFs error indicating issues with log storage.
3. Attempted to access the server using different admin accounts from Active Directory.
4. Investigated the log storage server to determine if it was operational and reachable.

## Root Cause
The issue was caused by a CIFs error that prevented the EPP server from reaching the log storage server, which subsequently led to the locking out of all admin accounts.

## Solution
The issue was resolved during a remote session where the support technician was able to:
- Correct the CIFs configuration to restore connectivity to the log storage server.
- Unlock the admin accounts, allowing the customer to regain access to the EPP server.

## Notes
- Ensure that there is a local account available on the server for emergency access in case of similar issues in the future.
- Regularly monitor the connectivity to the log storage server to prevent account lockouts.
```