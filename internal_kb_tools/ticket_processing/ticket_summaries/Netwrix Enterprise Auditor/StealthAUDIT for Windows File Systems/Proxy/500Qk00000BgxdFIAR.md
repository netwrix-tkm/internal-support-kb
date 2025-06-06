## Ticket Metadata
- **Ticket ID:** 500Qk00000BgxdFIAR
- **Case Number:** 411562
- **Status:** Closed - Resolved
- **Account/Company:** Borbet GmbH
- **Contact Name:** Waldemar Sartison
- **Product:** Netwrix Enterprise Auditor
- **Component:** FSAA Proxy
- **Feature:** Proxy
- **Version:** 11.6

## Problem Description
After updating the FSAA proxy on all three proxy servers from version 11.5 to 11.6, the customer encountered an error message indicating that the scan session could not be initialized with any proxy host.

## Environment Details
- **Proxy Servers:** Three FSAA proxy servers
- **Previous Version:** 11.5
- **Current Version:** 11.6

## Troubleshooting Steps
1. Confirmed that the FSAA Proxy Service was running.
2. Verified that the necessary ports were open as per the documentation.
3. Requested and reviewed proxy logs from the customer.
4. Identified an error in the logs related to expired server certificates and authentication failures.
5. Suggested changing the applet mechanism settings in FSAA Query > Applet Settings.

## Root Cause
The issue was caused by an incorrect configuration of the applet mechanism settings after the update to version 11.6, which led to authentication failures and the inability to initialize scan sessions.

## Solution
The issue was resolved by changing the applet mechanism setting to "Require applet to be running as a service on target (does not deploy or launch applet)" from the previous setting of "MSTask Task Scheduler." Additionally, the FSAA Proxy was reinstalled on one of the proxy servers, and the same settings were applied for the FS SEEK scans. After these changes, the scans were verified to be functioning correctly.

## Notes
- Ensure that the applet mechanism settings are correctly configured after any updates to avoid similar issues in the future.
- Regularly check for expired certificates and update them as necessary to prevent authentication errors.