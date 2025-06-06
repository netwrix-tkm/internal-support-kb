## Ticket Metadata
- **Ticket ID:** 500Qk00000BYYgsIAH
- **Case Number:** 411329
- **Status:** Closed - Resolved
- **Account/Company:** Hitachi Systems India Pvt. Ltd.
- **Contact Name:** Divya Ramachandran S
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** NONE

## Problem Description
The customer requested assistance with the pre-checks and post-checks required for upgrading their CoSoSys server, along with the procedure steps to carry out the upgrade.

## Environment Details
- The server is part of the Netwrix Endpoint Protector platform.
- The customer inquired about the implications of server space usage on the upgrade process.

## Troubleshooting Steps
1. Advised the customer to create a VM snapshot before proceeding with the upgrade to ensure a safe rollback point.
2. Instructed the customer to check the server's space usage in "Appliance > Server Information" and ensure it is below 70%.
3. Provided steps to update the server via "Dashboard" -> "Live Update":
   - Check for available updates.
   - Select the update and apply it, noting the server version it applies to.
4. Confirmed that communication with clients running lower versions would not be affected by the upgrade, specifically up to three versions lower.
5. Suggested releasing licenses from "System Configuration > System Licenses" post-upgrade to verify client communication.
6. Recommended updating the EPP clients from "System Configuration > Client software upgrade" after the server upgrade.

## Root Cause
The inquiry was primarily about ensuring a smooth upgrade process for the CoSoSys server, with concerns about server space and client communication compatibility.

## Solution
The issue was resolved by providing detailed instructions for both pre-upgrade checks (such as creating a VM snapshot and checking server space) and post-upgrade steps (including license management and client updates). The customer was reassured that the upgrade would not disrupt communication with clients running older versions.

## Notes
- It is crucial to maintain server space below 70% to avoid potential issues during the upgrade process.
- Always confirm the server version compatibility with client versions before proceeding with upgrades.
- Document any specific items that need to be backed up prior to the upgrade, especially if the server is physical.