## Ticket Metadata
- **Ticket ID:** 500Qk00000DlqfRIAR
- **Case Number:** 416564
- **Status:** Closed - Resolved
- **Account/Company:** Wotton & Kearney
- **Contact Name:** Mahesh Belagali
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** 5.9.3.0

## Problem Description
The customer, Wotton & Kearney, reported an issue where they were unable to access EasyLock using the Master Password configured in the admin console during their proof of concept (POC) of Endpoint Protector.

## Environment Details
- **Server URL:** https://5dayext.hosted.endpointprotector.com
- **Server ID:** ZD35BCVQ
- **Client Version:** 6.2.2.1 EPP client
- **EasyLock Version:** Latest version at the time of the issue
- **Operating System:** Windows

## Troubleshooting Steps
1. Verified the Master Password configuration in the admin console.
2. Checked for any updates or patches for the EasyLock and EPP client.
3. Attempted to reset the Master Password and reconfigured it.
4. Tested access to EasyLock from different user accounts and machines.
5. Reviewed server logs for any error messages related to authentication.

## Root Cause
The issue was identified as a mismatch between the Master Password configured in the admin console and the password being entered by the user. This could have been due to a configuration error or a misunderstanding of the password requirements.

## Solution
The issue was resolved by confirming the correct Master Password with the customer and ensuring they were entering it correctly. After re-entering the password, the customer was able to access EasyLock without further issues.

## Notes
- Ensure that users are aware of the password requirements and any potential case sensitivity.
- Recommend documenting the Master Password securely to avoid similar issues in the future.
- Consider providing additional training or resources for users unfamiliar with the EasyLock access process.