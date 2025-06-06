## Ticket Metadata
- **Ticket ID:** 500Qk00000JsYEjIAN
- **Case Number:** 430695
- **Status:** Closed - Resolved
- **Account/Company:** Cenibra
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** 5.9.4.1

## Problem Description
The customer reported that Single Sign-On (SSO) functionality stopped working, resulting in login loops on the login page. Additionally, the server was reported as inaccessible.

## Environment Details
- EPP Server Version: 5.9.4.1
- The customer was using Microsoft Azure for SSO configuration.

## Troubleshooting Steps
1. Scheduled a Zoom meeting with the customer for further investigation.
2. Requested the customer to create a snapshot of the current EPP server.
3. Joined the Zoom session and verified that the customer successfully created the snapshot.
4. Attempted to log into the EPP console using the SSO account, which failed.
5. Disabled SSO login via the backend to troubleshoot access issues.
6. Successfully logged into the EPP console using the root account.
7. Reconfigured the login process using Microsoft Azure.
8. Confirmed that the customer was still unable to log in using SSO but could access the console with the root account.
9. Advised the customer to update the security certificates related to SSO.
10. Left the ticket open while awaiting the customer's update on the security certificates.

## Root Cause
The issue was identified as being related to outdated or incorrect security certificates, which affected the SSO functionality.

## Solution
The customer updated the security certificates, after which they were able to successfully log in using the SSO account. The support team performed application fix steps to assist in the resolution.

## Notes
- Ensure that security certificates are regularly updated to prevent similar SSO issues in the future.
- It is advisable to verify the SSO configuration settings in Microsoft Azure if similar login issues arise.