## Ticket Metadata
- **Ticket ID:** 500Qk00000FVHlXIAX
- **Case Number:** 420386
- **Status:** Closed - Resolved
- **Account/Company:** Bridgecom Semiconductors GmbH
- **Contact Name:** Amy Zhang
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer reported intermittent network issues where Microsoft Teams would lose connectivity while Outlook continued to function normally. Webpages would fail to load occasionally, although ping tests were successful. The network would only return to normal after restarting the computer.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5940
- **Age:** 14.9 days

## Troubleshooting Steps
1. Verified network connectivity using ping tests, which returned successful results.
2. Checked the functionality of Outlook, which was able to send and receive emails without issues.
3. Investigated potential conflicts with Data Loss Prevention (DLP) policies as suggested by the customer.
4. Explored settings related to the Netwrix Endpoint Protector to identify any misconfigurations.

## Root Cause
The root cause of the issue was identified as a conflict with the Deep Packet Inspection (DPI) settings within the Netwrix Endpoint Protector. Specifically, the DPI was affecting the network performance of certain applications, leading to the observed connectivity issues.

## Solution
The issue was resolved by activating the "Stealthy DPI" feature within the Netwrix Endpoint Protector. This adjustment allowed for improved network performance and stability, eliminating the connectivity problems experienced by the customer.

## Notes
- It is recommended to monitor the performance of the Stealthy DPI feature to ensure it continues to meet the network requirements.
- Future cases involving similar symptoms should consider checking DPI settings as a potential root cause.
- Customers should be advised to restart their computers as a temporary workaround if they experience similar issues before a permanent solution is applied.