## Ticket Metadata
- **Ticket ID:** 500Qk00000KcJNwIAN
- **Case Number:** 432127
- **Status:** Closed - Resolved
- **Account/Company:** Chemline
- **Contact Name:** Javaign Vinson
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported an issue with resetting their password for the Netwrix Endpoint Protector. Despite multiple attempts to reset the password and save it in various password management tools, the customer was unable to log in.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** EPP Other

## Troubleshooting Steps
1. The customer attempted to reset the password multiple times.
2. The customer saved the new password in Notepad, Keeper Enterprise, and their browser.
3. The support team reset the password to a default value.
4. The support team communicated with the customer regarding the potential overwriting of the root user account.

## Root Cause
The issue was identified as a result of the customer overwriting the root user account with their own account. This caused login issues due to the root account's specific exceptions for login that may not apply to standard user accounts.

## Solution
The support team reset the password to a default value, which allowed the customer to regain access. Additionally, it was recommended that the customer create a separate account for themselves and rename the current one to "root," which could be disabled to prevent access issues in the future.

## Notes
- It is important to avoid overwriting the root user account with standard user accounts to prevent login issues.
- Future users should be advised to create separate accounts for administrative tasks rather than modifying the root account.