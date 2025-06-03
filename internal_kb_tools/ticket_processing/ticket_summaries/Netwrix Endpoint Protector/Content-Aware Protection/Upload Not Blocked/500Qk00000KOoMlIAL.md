## Ticket Metadata
- **Ticket ID:** 500Qk00000KOoMlIAL
- **Case Number:** 431552
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Prasanth Ganesan
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** NONE

## Problem Description
The customer reported that during a Proof of Concept (POC), the EPP client was successfully installed on an Ubuntu 22.04 machine. However, the configured policy to monitor file upload activities did not generate reports, and when the policy was changed to Block & Report, file uploads were still not blocked.

## Environment Details
- **Operating System:** Ubuntu 22.04
- **EPP Client:** Installed successfully

## Troubleshooting Steps
1. Verified the installation of the EPP client on the Ubuntu machine.
2. Configured the policy to "Reports only" to monitor file uploads.
3. Observed that file uploads were occurring without report generation.
4. Changed the policy action to "Block & Report" to prevent file uploads.
5. Confirmed that file uploads were still not blocked and reports were not generated.

## Root Cause
The root cause of the issue was not explicitly identified in the case details. However, it was implied that there may have been a misconfiguration in the policy settings or a compatibility issue with the EPP client on the Ubuntu 22.04 platform.

## Solution
The issue was resolved by providing the correct EPP client download link for Ubuntu devices, which may have included necessary updates or configurations that were missing in the initial installation. The customer acknowledged the resolution and requested the ticket to be closed.

## Notes
- Ensure that the EPP client is compatible with the operating system version being used.
- Always verify policy configurations after installation to ensure they are set correctly for the desired actions.
- Document any specific configurations or settings that were successful in resolving similar issues for future reference.