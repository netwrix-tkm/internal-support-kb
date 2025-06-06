## Ticket Metadata
- **Ticket ID:** 500Qk00000JXXgbIAH
- **Case Number:** 429910
- **Status:** Closed - Resolved
- **Account/Company:** Addleshaw Goddard LLP
- **Contact Name:** Sean Reilly
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** 5.9.4.1

## Problem Description
After applying the update "5.9.4.1 - Product Maintenance - Netwrix Endpoint," the Single Sign-On (SSO) functionality for the management portal of Netwrix Endpoint Protector was broken. Admin users were unable to log in, as the system repeatedly prompted for account credentials without granting access.

## Environment Details
- **Login URL:** [https://endpointprotector/index.php/login](https://endpointprotector/index.php/login)
- **Server ID:** PBGU2VNR
- **Server IP:** 10.110.0.37

## Troubleshooting Steps
1. Verified the update was applied correctly.
2. Attempted to log in using different browsers to replicate the issue.
3. Checked sign-in logs, which indicated that admin users were logging in successfully but were not redirected to the management portal.
4. Reviewed server configurations and settings related to SSO.

## Root Cause
The issue was identified as a compatibility problem introduced by the recent update (5.9.4.1) that affected the SSO login process, preventing successful redirection to the management portal.

## Solution
The issue was resolved by rolling back the update to the previous stable version of the Netwrix Endpoint Protector. This restored the SSO functionality, allowing admin users to log in successfully to the management portal.

## Notes
- It is recommended to test updates in a staging environment before applying them to production to avoid similar issues.
- Monitor the release notes for future updates for any known issues related to SSO functionality.
- Ensure that backup procedures are in place to facilitate quick rollbacks in case of critical failures after updates.