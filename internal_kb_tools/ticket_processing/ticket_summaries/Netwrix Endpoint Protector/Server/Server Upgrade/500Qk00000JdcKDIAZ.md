## Ticket Metadata
- **Ticket ID:** 500Qk00000JdcKDIAZ
- **Case Number:** 430162
- **Status:** Closed - Resolved
- **Account/Company:** Leonhard Lang GmbH
- **Contact Name:** Paul Dibiasi
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.1

## Problem Description
The customer attempted to install the latest update (version 5.9.4.1) via Live-Update but encountered "ERROR 2" during the installation process, prompting them to contact support for assistance.

## Environment Details
- The customer recently enforced new Firewall Rules for the Endpoint Protector Server.
- Port 80 to [liveupdate.endpointprotector.com](https://liveupdate.endpointprotector.com) is open, and no blocks were detected.

## Troubleshooting Steps
1. Verified that the Firewall Rules were correctly configured to allow traffic on Port 80 to the Live Update server.
2. Checked for any network blocks or restrictions that could prevent the update from being downloaded.
3. Confirmed that the Live Update service was operational and accessible from the customer's network.

## Root Cause
The issue was related to the recent enforcement of Firewall Rules, which may have inadvertently affected the update process despite Port 80 being open. The specific cause of "ERROR 2" was not explicitly identified but was likely linked to network connectivity issues during the update attempt.

## Solution
The issue was resolved by ensuring that the Firewall Rules allowed all necessary traffic for the Live Update process. After confirming the configuration, the customer was able to successfully complete the update to version 5.9.4.1 without encountering further errors.

## Notes
- It is important to review Firewall Rules thoroughly when implementing changes to ensure that all required ports and services are accessible for updates.
- Future updates should be monitored closely, especially after any changes to network configurations, to prevent similar issues from arising.