## Ticket Metadata
- **Ticket ID:** 500Qk00000CpoYaIAJ
- **Case Number:** 414481
- **Status:** Closed - Resolved
- **Account/Company:** Leonhard Lang GmbH
- **Contact Name:** Paul Dibiasi
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.0

## Problem Description
The customer reported issues while attempting to install the 5.9.3.0 Hotfix #1.1 update. Although the installation process indicated success (both via Live Update and offline), the update continued to appear in the "available updates" list, suggesting it had not been installed. The customer sought confirmation on whether the hotfix was indeed installed and if the issue could be ignored.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Attempted installation of the hotfix via both Live Update and offline methods.
2. Verified the installation status by checking the "available updates" list.
3. Restarted the server and logged in again to check if the update status changed.

## Root Cause
The issue was identified as a known behavior of the Endpoint Protector software, where the hotfix remains listed in the "available updates" even after a successful installation. This was not indicative of a failure in the installation process.

## Solution
The support team confirmed that the hotfix was successfully applied to the EPP server. They advised the customer to ignore the hotfix listed in the software update list, as it would be removed in the upcoming release of Endpoint Protector v5.9.4.0.

## Notes
- Customers experiencing similar issues should be informed that the appearance of installed updates in the "available updates" list is a known issue and does not affect the functionality of the installed hotfix.
- It is recommended to keep the software updated to the latest version to avoid such discrepancies in the future.