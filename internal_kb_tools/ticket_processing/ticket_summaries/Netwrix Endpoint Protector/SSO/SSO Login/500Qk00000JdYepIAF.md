## Ticket Metadata
- **Ticket ID:** 500Qk00000JdYepIAF
- **Case Number:** 430160
- **Status:** Closed - Resolved
- **Account/Company:** TrustingSocial
- **Contact Name:** Linh Hoang
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** GA 5.9.4.1

## Problem Description
After updating to GA 5.9.4.1, the customer reported that SSO login to the NEP portal was not functioning. Users experienced a looping issue at the Azure login page, preventing access to the portal. The issue arose the morning following the update, despite successful logins immediately after the update.

## Environment Details
- **Integration:** Azure for SSO
- **Affected Component:** NEP portal

## Troubleshooting Steps
1. Verified the update process to ensure it completed successfully.
2. Attempted to replicate the SSO login issue in a controlled environment.
3. Checked Azure integration settings for any discrepancies post-update.
4. Reviewed logs for any error messages or anomalies during the login process.
5. Conducted a remote session with the customer to observe the issue firsthand.

## Root Cause
The issue was identified as a backend procedure failure (specifically backend procedure no. 68) that occurred after the update, which disrupted the SSO functionality.

## Solution
The resolution involved executing the necessary backend procedure to restore proper SSO functionality. After applying the fix, users were able to log in to the NEP portal without encountering the looping issue.

## Notes
- Ensure to monitor SSO functionality closely after future updates to catch any similar issues early.
- It may be beneficial to document any backend procedures that are critical for SSO operations to facilitate quicker resolutions in the future.