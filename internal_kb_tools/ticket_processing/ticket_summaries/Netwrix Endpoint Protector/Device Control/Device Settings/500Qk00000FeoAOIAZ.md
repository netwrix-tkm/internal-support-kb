## Ticket Metadata
- **Ticket ID:** 500Qk00000FeoAOIAZ
- **Case Number:** 420766
- **Status:** Closed - Resolved
- **Account/Company:** CoSoSys Solution
- **Contact Name:** Seong Yun Jeong
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** 5.9.4.0 (macOS 15.0 Beta)

## Problem Description
The customer reported multiple issues with Endpoint Protector version 5.9.4.0 while using macOS 15.0 Beta, specifically regarding the functionality of device control settings. The issues included:
- iPhones being able to charge despite access being denied.
- Wi-Fi not being blocked when a wired network connection was present.
- USB modems not being blocked even when access was denied.

## Environment Details
- **Operating System:** macOS 15.0 Beta
- **Endpoint Protector Version:** 5.9.4.0

## Troubleshooting Steps
1. Confirmed the settings for denying access to iPhones and USB modems.
2. Verified the "block Wi-Fi if wired network connection is present" option was enabled.
3. Rebooted the Mac and reapplied the policies from the client.
4. Collected logs and terminal outputs using the commands:
   - `sudo ifconfig`
   - `sudo /usr/sbin/networksetup -listnetworkserviceorder`
5. Provided a test build to the customer to address the Wi-Fi blocking issue.

## Root Cause
The issues were primarily due to a bug in the Endpoint Protector software that affected the detection of network connections on macOS 15.0 Beta. Specifically:
- The iPhone charging behavior was due to the timing of how the Endpoint Protector agent interacts with the USB port, which sometimes allowed charging despite access being denied.
- The Wi-Fi blocking issue was related to the software not correctly detecting the wired Ethernet connection when using certain USB adapters (e.g., AX88772D).
- The USB modem continued to function because the software did not enforce the deny access policy correctly when the modem was connected.

## Solution
The resolution involved:
- Providing a test build (version 3.0.4.0007) that improved the detection of the Ethernet connection, allowing the Wi-Fi blocking feature to work as intended.
- Clarifying the functionality of the "deny access" and "deny access but allow charging" settings to the customer, explaining that while "deny access" attempts to block charging, it does not guarantee it due to potential conflicts with other software.

## Notes
- The test build provided is not intended for mass deployment and should be used for testing purposes only.
- Customers should be informed that while the "deny access" feature aims to block charging, it may not always be effective due to external factors.
- Future users should ensure they are using compatible hardware with the Endpoint Protector to avoid similar issues with device detection.