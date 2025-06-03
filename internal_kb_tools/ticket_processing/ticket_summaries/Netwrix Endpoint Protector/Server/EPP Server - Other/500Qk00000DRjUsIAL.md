## Ticket Metadata
- **Ticket ID:** 500Qk00000DRjUsIAL
- **Case Number:** 415809
- **Status:** Closed - Resolved
- **Account/Company:** Disney Streaming Technology
- **Contact Name:** Giancarlo Alberti
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** 5.9.3.0

## Problem Description
The customer, Giancarlo Alberti, reported an issue with applying updates to the EPP appliance. Although the update process indicated that EPP Server 5.9.3.0 and EPP Server Hotfix 1.1 were successfully installed, the appliance continued to prompt for these updates upon subsequent checks.

## Environment Details
- **EPP Appliance Version:** 5.9.3.0
- **Hotfix Version:** 1.1

## Troubleshooting Steps
1. Verified the update installation logs to confirm that the updates were applied successfully.
2. Checked the appliance settings to ensure that the update notifications were configured correctly.
3. Attempted to manually reapply the updates to see if the issue persisted.
4. Restarted the EPP appliance to refresh the system and clear any potential caching issues.

## Root Cause
The issue was identified as a caching problem within the EPP appliance that caused it to incorrectly prompt for updates even after they had been successfully applied.

## Solution
The resolution involved applying the hotfix (Hotfix 1.1) to the EPP appliance, which addressed the caching issue. After the hotfix was successfully applied, the appliance no longer prompted for the updates, confirming that the issue was resolved.

## Notes
- Ensure that the EPP appliance is regularly updated to the latest version to avoid similar caching issues in the future.
- If similar update loops occur, check the update logs and consider applying any available hotfixes as a first troubleshooting step.