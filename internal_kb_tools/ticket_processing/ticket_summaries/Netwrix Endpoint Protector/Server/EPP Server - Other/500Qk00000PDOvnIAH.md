## Ticket Metadata
- **Ticket ID:** 500Qk00000PDOvnIAH
- **Case Number:** 445315
- **Status:** Closed - Resolved
- **Account/Company:** Konfio Limited
- **Contact Name:** Gibrann Montero
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** N/A
- **Version:** N/A

## Problem Description
The customer reported an issue with the settings inheritance hierarchy in Netwrix Endpoint Protector. After modifying a setting at the Computer Settings level, reverting it back to match the Group Setting caused the new group-level changes to not apply to the endpoint. The customer sought a way to restore the normal settings inheritance without deleting and reinstalling the agent.

## Environment Details
- **Hierarchy of Settings:** General Settings → Group Settings → Computer Settings
- **Issue observed:** Changes made at the Computer Settings level disrupt the inheritance of settings from Group Settings.

## Troubleshooting Steps
1. Verified the settings hierarchy as per the documentation.
2. Modified a setting (e.g., "DPI") at the Computer Settings level to confirm it overrides Group Settings.
3. Reverted the Computer Setting back to match the Group Setting.
4. Attempted to apply new changes at the Group Settings level to check if they would take effect.
5. Explored options for restoring settings inheritance without agent reinstallation.

## Root Cause
The issue was identified as a disruption in the settings inheritance mechanism after any modification was made at the Computer Settings level. Even after reverting the changes, the system did not restore the expected inheritance behavior.

## Solution
The issue was resolved by utilizing the built-in functionality to restore settings to the previous hierarchy. The customer was instructed to navigate to:
```
Device Control -> Computers -> Manage Settings -> Restore Global Settings (located at the bottom of the page).
```
This action successfully restored the normal settings inheritance for the endpoint.

## Notes
- It is important to inform users that any direct modifications at the Computer Settings level can disrupt the inheritance of settings from Group and General Settings.
- Users should be aware of the restore functionality available in the management interface to reset settings inheritance without needing to reinstall the agent.