## Ticket Metadata
- **Ticket ID:** 500Qk00000COaMnIAL
- **Case Number:** 413328
- **Status:** Closed - Resolved
- **Account/Company:** Finastra
- **Contact Name:** József Friedel
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** Not specified

## Problem Description
The customer, József Friedel, reported an issue with removing the CoSoSys Endpoint Protector (EPP) agent from macOS devices using their MDM solution, Kandji. The removal process was initiated using a Unix executable, but it failed due to a password prompt during the uninstallation.

## Environment Details
- **MDM Solution:** Kandji
- **Operating System:** macOS
- **EPP Agent:** CoSoSys Endpoint Protector

## Troubleshooting Steps
1. The customer downloaded the `remove-epp` Unix executable and packaged it into a `.pkg` file.
2. The package was deployed to a test device in the `/Applications/Utilities` folder.
3. The post-install script was executed, which resulted in a password prompt during the uninstallation process.

## Root Cause
The uninstallation script for the CoSoSys Endpoint Protector agent requires a password for uninstall protection, which was not provided in the script. This requirement caused the uninstall process to abort when the password was not entered.

## Solution
The support team provided the customer with an alternative uninstall tool that does not require a password. The tool can be found at the following link:
```
http://download.endpointprotector.com/Support_files/remove-epp_mac_nopwd.command.zip
```
This tool allows for the uninstallation of the EPP agent without user intervention, enabling mass action through the MDM solution.

## Notes
- Ensure that any future scripts or tools used for uninstallation of the EPP agent are verified to not require user input, especially passwords, to facilitate automated processes.
- It is advisable to test the uninstallation process on a small number of devices before deploying it widely to ensure compatibility and functionality.