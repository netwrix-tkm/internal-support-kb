## Ticket Metadata
- **Ticket ID:** 500Qk00000EyvRaIAJ
- **Case Number:** 419228
- **Status:** Closed - Resolved
- **Account/Company:** Haleon
- **Contact Name:** Sudhir Baral
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** Server version 5.9.4.0; Client version 6.2.3.1

## Problem Description
The customer reported that endpoints were hanging during the installation of the new EPP Windows (64-bit version) - Version: 6.2.3.1 via Intune. Users were required to perform a hard reboot to regain access to their laptops, which was not an acceptable user experience.

## Environment Details
- **Production Server ID:** 8YZN4MPO
- **Server Version:** 5.9.4.0
- **Client Version:** 6.2.3.1

## Troubleshooting Steps
1. The customer was advised to check if "Advanced Printer and MTP Scanning" was enabled under "Device Control > Global Settings > File Tracing and Shadowing."
2. It was recommended to disable the aforementioned setting during the upgrade process to prevent conflicts.
3. A call was scheduled to discuss the issue further and explore additional troubleshooting options.

## Root Cause
The issue was identified as a conflict during the installation process of the client version 6.2.3.1, which caused the endpoints to hang.

## Solution
The problem was resolved by upgrading to the new client version 6.2.3.1010, which addressed the installation issues experienced with version 6.2.3.1.

## Notes
- It is advisable to disable "Advanced Printer and MTP Scanning" during client upgrades to avoid similar issues in the future.
- Always ensure that the latest client version is deployed to prevent known issues from affecting user experience.