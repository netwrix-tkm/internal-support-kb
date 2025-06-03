## Ticket Metadata
- **Ticket ID:** 500Qk00000JFcmnIAD
- **Case Number:** 429184
- **Status:** Closed - Resolved
- **Account/Company:** Satcom Infotech
- **Contact Name:** Sai Nachiappan
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** NONE

## Problem Description
Linux agents running version 22.04 were unable to access the internet when Deep Packet Inspection (DPI) was enabled. Disabling DPI allowed internet access, indicating a conflict when DPI was active.

## Environment Details
- **Operating System:** Linux 22.04
- **DPI Feature:** Enabled/Disabled toggle affecting internet access

## Troubleshooting Steps
1. Verified the internet connectivity on Linux agents with DPI disabled.
2. Analyzed logs which indicated that client requests were timing out when DPI was enabled.
3. Attempted to change the IP address of the server to see if it resolved the connectivity issue.

## Root Cause
The issue was identified as a timeout occurring in client requests when DPI was enabled, suggesting that the DPI settings were interfering with the network traffic.

## Solution
The issue was resolved by changing the IP address of the server. After the IP change, the Linux agents were able to access the internet with DPI enabled.

## Notes
- Ensure that any changes to server IP addresses are documented and communicated to all relevant stakeholders.
- Monitor the performance of DPI settings in future configurations to prevent similar issues from arising.