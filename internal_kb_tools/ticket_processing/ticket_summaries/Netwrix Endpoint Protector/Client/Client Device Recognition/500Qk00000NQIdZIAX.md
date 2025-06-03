## Ticket Metadata
- **Ticket ID:** 500Qk00000NQIdZIAX
- **Case Number:** 440288
- **Status:** Closed - Resolved
- **Account/Company:** Rhino Rack Australia
- **Contact Name:** Matt Harris
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** 5.9.3.0 (upgraded to 5.9.4.1)

## Problem Description
The Australian Criminal Intelligence Commission reported an issue where the Endpoint Protector (EPP) client installed on a Windows 11 virtual machine was preventing access to additional virtual hard drives (D: and E:). The C: drive was accessible, and virtual CDROM drives were unaffected. Users received a "D: is not accessible. Access is Denied" error message when attempting to access the blocked drives.

## Environment Details
- **EPP Version:** 5.9.3.0
- **EPP Client Version:** 6.2.2.1
- **Operating System:** Windows 11
- **Environment Type:** Offline

## Troubleshooting Steps
1. Verified that the EPP client showed no devices as being blocked.
2. Checked the EPP console logs for any blocked devices related to the virtual machine.
3. Attempted to disable the EPP client using a temporary offline password, which did not resolve the issue.
4. Uninstalled the EPP client, which restored access to the blocked drives.
5. Discussed upgrading to the latest version of EPP to see if it would resolve the issue.

## Root Cause
The issue was caused by a compatibility problem between the EPP client version 6.2.2.1 and the virtual hard drives on the Windows 11 virtual machine. The EPP client was incorrectly blocking access to the additional drives despite no devices being set to block in the configuration.

## Solution
The issue was resolved by upgrading the EPP server and client to the latest versions. The upgrade process involved:
1. Creating a VM snapshot for safety.
2. Applying the following patches sequentially:
   - From EPP 5.9.3.0 to EPP 5.9.4.0
   - From EPP 5.9.4.0 to EPP 5.9.4.1
3. After the upgrade, the virtual hard drives were accessible without restrictions.

## Notes
- Always create a VM snapshot before performing upgrades to ensure a rollback point.
- When applying patches, upload only one at a time and wait for it to finish before proceeding with the next.
- Monitor the EPP console logs after upgrades to confirm that no devices are being incorrectly blocked.