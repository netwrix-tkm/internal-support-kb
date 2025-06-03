## Ticket Metadata
- **Ticket ID:** 500Qk00000GLRqTIAX
- **Case Number:** 422343
- **Status:** Closed - Resolved
- **Account/Company:** BayPort Credit Union
- **Contact Name:** Zac Cornett
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
After importing administrators from Active Directory (AD), users were unable to log in with their accounts.

## Environment Details
- The issue occurred in the Netwrix Endpoint Protector environment.
- The customer was using a service account for AD authentication.

## Troubleshooting Steps
1. Verified that the correct passwords were being used for the AD accounts.
2. Checked if the AD authentication settings were properly configured.
3. Attempted to log in with local accounts and confirmed they were failing as well.
4. Investigated whether the AD authentication had ever worked for the customer.
5. Reviewed the AD authentication settings and account privileges.
6. Suggested using a Domain Administrator account for AD authentication.
7. Tested various configurations for AD authentication, including account suffix and username formats.
8. Confirmed that client certificate validation was required by the customer's AD setup.

## Root Cause
The root cause of the login issues was identified as:
- Client Certificate Authorization was enabled on the AD, which prevented successful authentication.
- Local accounts were not created with AD authentication ignored, leading to login failures.

## Solution
The issue was resolved by:
- Disabling Client Certificate Authorization on the AD.
- Using the recommended AD formatting in the system settings.
- Ensuring that local accounts were created with AD authentication ignored, allowing them to log in successfully.

## Notes
- Ensure that Client Certificate Authorization is disabled if it is not required by the AD setup.
- When configuring AD authentication, always verify the correct formatting of usernames and account suffixes.
- For future cases, consider testing with a Domain Administrator account to rule out permission issues.