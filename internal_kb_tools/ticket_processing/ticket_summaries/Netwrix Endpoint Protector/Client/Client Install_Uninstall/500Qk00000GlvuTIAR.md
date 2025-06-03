## Ticket Metadata
- **Ticket ID:** 500Qk00000GlvuTIAR
- **Case Number:** 423241
- **Status:** Closed - Resolved
- **Account/Company:** HQLAx
- **Contact Name:** Yacine BOUMEKIK
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer reported that after installing the Endpoint Protector (EP) and the associated certificate on a macOS 15 MacBook, the expected pop-up to install the transparent proxy did not appear. This issue prevented the detection of sensitive file uploads in the EP dashboard.

## Environment Details
- **Operating System:** macOS 15
- **Previous OS Version:** macOS 14
- The issue did not occur on MacBooks where EP was installed prior to upgrading to macOS 15.

## Troubleshooting Steps
1. Verified the installation of EP and the certificate on the macOS 15 device.
2. Attempted to trigger the transparent proxy pop-up multiple times.
3. Restarted the MacBook twice to see if the pop-up would appear.
4. Added the device to the policy in an attempt to trigger the pop-up.
5. Conducted a meeting to discuss the issue and potential solutions.

## Root Cause
The root cause was identified as a problem during the migration from macOS 14 to macOS 15, which likely disrupted the installation process of the transparent proxy.

## Solution
The issue was resolved by performing a full wipe and re-installation of macOS 15. After this process, the transparent proxy installation worked correctly, and the pop-up appeared as expected.

## Notes
- It is advisable to ensure that all installations and upgrades are performed cleanly to avoid migration issues.
- Future installations of EP on macOS 15 should be monitored closely, especially if the device was previously upgraded from an earlier macOS version.