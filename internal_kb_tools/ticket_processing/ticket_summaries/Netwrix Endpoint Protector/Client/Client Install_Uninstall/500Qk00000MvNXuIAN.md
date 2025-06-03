## Ticket Metadata
- **Ticket ID:** 500Qk00000MvNXuIAN
- **Case Number:** 438789
- **Status:** Closed - Resolved
- **Account/Company:** Bridgecom Semiconductors GmbH
- **Contact Name:** Amy Zhang
- **Product:** Netwrix Endpoint Protector
- **Component:** Client Install/Uninstall
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer reported an issue where they were unable to install, uninstall, or repair the DLP version 5.9 on Windows 11. Additionally, they faced difficulties installing the new version 6.3. The error message indicated insufficient access to a specific registry key.

## Environment Details
- **Operating System:** Windows 11
- **Previous DLP Version:** 5.9
- **Attempted New Version:** 6.3

## Troubleshooting Steps
1. The customer was advised to attempt the installation while logged into the local administrator account.
2. A remote session was conducted where the support engineer took control of the customer's machine.
3. The ZAP tool was used to remove any remnants of the old Endpoint Protector appliance.
4. The archive and extracted folder were deleted using the SHIFT + Delete method.
5. The machine was restarted after the cleanup.
6. A new installation of the Endpoint Protector client was attempted.

## Root Cause
The issue was caused by remnants of a previous installation that had failed, which left behind registry entries and files that interfered with the installation of the new version.

## Solution
The problem was resolved by:
- Using the ZAP tool to completely remove any remnants of the old Endpoint Protector installation.
- Deleting the associated files and folders.
- Restarting the machine, which allowed the customer to successfully install the new version of Endpoint Protector without further issues.

## Notes
- Ensure that any previous installations are completely removed before attempting to install a new version of Endpoint Protector.
- If similar issues arise, consider using the ZAP tool for cleanup and verify that the user has sufficient permissions to access necessary registry keys.