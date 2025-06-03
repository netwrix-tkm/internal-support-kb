## Ticket Metadata
- **Ticket ID:** 500Qk00000BjzfJIAR
- **Case Number:** 411696
- **Status:** Closed - Resolved
- **Account/Company:** St. Vinzenz Klinik Pfronten
- **Contact Name:** Felix Behrendt
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** N/A
- **Version:** N/A

## Problem Description
The customer reported that all USB keyboards on newly received PCs with Windows 11 were being blocked by the Netwrix Endpoint Protector (EPP) software. This issue did not occur with the same hardware running Windows 10.

## Environment Details
- Operating System: Windows 11
- Hardware: HP ProDesk PCs
- EPP Version: Not specified, but the last update on the EPP server was in March 2024.

## Troubleshooting Steps
1. Confirmed that additional keyboards were blocked in the device control settings.
2. Suggested reinstalling the EPP client to recognize the USB keyboard as the primary device.
3. Customer attempted to uninstall the EPP client, including database and log deletion, followed by a fresh installation.
4. Verified that the computers were new and had not been previously updated from Windows 10.
5. Checked for the activation of the Minifilter option in the EPP settings.
6. Conducted a remote session to further investigate the issue.

## Root Cause
The issue was identified as a compatibility problem between the EPP client and the new Windows 11 operating system, which caused the software to misidentify the primary USB keyboard.

## Solution
The problem was resolved by ensuring that the Minifilter option was activated in the EPP settings. During a remote session, the support engineer confirmed the settings and provided guidance on how to properly configure the EPP client for Windows 11.

## Notes
- It is important to ensure that the Minifilter option is enabled for new installations of EPP on Windows 11.
- Customers should be advised to check for compatibility issues when transitioning to new operating systems.
- The internal tool used during the remote session is only to be used by administrators and must be deleted after use.