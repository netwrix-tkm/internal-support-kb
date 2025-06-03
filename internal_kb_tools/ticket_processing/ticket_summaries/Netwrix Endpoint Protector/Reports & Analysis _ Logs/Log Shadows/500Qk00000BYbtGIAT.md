## Ticket Metadata
- **Ticket ID:** 500Qk00000BYbtGIAT
- **Case Number:** 411332
- **Status:** Closed - Resolved
- **Account/Company:** RoundRobin Tech Services
- **Contact Name:** Rajesh Makwana
- **Product:** Netwrix Endpoint Protector
- **Component:** Reports & Analysis / Logs
- **Feature:** Log Shadows
- **Version:** Not specified

## Problem Description
The customer reported an issue with their on-premises Data Loss Prevention (DLP) server, specifically with the Device Control module configured for File Tracing. They noted that while a device was detected as connected, the file activity log was not being displayed on the DLP server.

## Environment Details
- On-premises DLP server image
- Device Control module configured for:
  - Windows Portable Device (Media Transfer Protocol)
  - Android Smartphone (Media Transfer Protocol)
  - Smartphone (USB Sync)
  - Smartphone (Windows CE)
  - Bluetooth Smartphone

## Troubleshooting Steps
1. Confirmed the configuration of the DLP server and Device Control module.
2. Verified the connection status of the devices in question.
3. Checked if file tracing for the specified device categories was supported by the DLP server.
4. Investigated if the log files were stuck in quarantine.
5. Engaged with the development team regarding potential issues with the CAP driver not loading.

## Root Cause
The issue was identified as a problem related to the CAP driver, which was not loading correctly. This prevented the DLP server from capturing file activity logs for the connected devices.

## Solution
The resolution involved clearing the current installation of the DLP server and performing a fresh installation using the ZapEPP tool to ensure all remnants of the previous installation were removed. After the fresh installation, the file tracing functionality for the specified device categories was successfully restored.

## Notes
- Ensure that the CAP driver is properly loaded during installation to avoid similar issues in the future.
- Regularly check for updates or patches for the DLP server and Device Control module to maintain compatibility with connected devices.
- If issues persist, consider using diagnostic tools to monitor driver loading and file tracing functionality.