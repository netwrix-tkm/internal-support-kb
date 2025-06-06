## Ticket Metadata
- **Ticket ID:** 500Qk00000GsoJbIAJ
- **Case Number:** 423583
- **Status:** Closed - Resolved
- **Account/Company:** ServiceNow
- **Contact Name:** Arpitha Shetty
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** Not specified

## Problem Description
The customer reported that the Single Sign-On (SSO) login functionality was not working following a service outage.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature Affected:** SSO Login

## Troubleshooting Steps
1. Verified the SSO configuration settings on the server.
2. Attempted to log in using SSO credentials to reproduce the issue.
3. Checked server logs for any error messages related to SSO authentication.
4. Disabled SSO from the server's backend to assess if the issue persisted without SSO.
5. Reconfigured SSO settings on the server.

## Root Cause
The issue was identified as a misconfiguration in the SSO settings that occurred after the service outage.

## Solution
The problem was resolved by:
- Disabling SSO from the server's backend.
- Reconfiguring and setting up SSO again, which restored the login functionality.

## Notes
- Ensure to verify SSO configurations after any service outages to prevent similar issues.
- Document any changes made during troubleshooting for future reference.