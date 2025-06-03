## Ticket Metadata
- **Ticket ID:** 500Qk00000BMifCIAT
- **Case Number:** 410241
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Denni Prima Putra Roli
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Clipboard
- **Version:** Server version 5.9.3, Client version 3.0.2.1007 for macOS

## Problem Description
The customer reported an issue where sensitive data, specifically credit card numbers, could be copied from document applications (Excel or Word) and pasted into the WhatsApp Desktop client on macOS, despite having configured policies to block such actions.

## Environment Details
- **Operating System:** macOS
- **Applications Involved:** Excel, Word, WhatsApp Desktop
- **Policy Configuration:**
  - Exit point: WhatsApp Desktop
  - Credit Card as denylist from predefined content
  - Clipboard: ON
  - Detect Source Code: ON
  - Detect Images: ON
  - Apply Paste restrictions to all monitored applications: ON

## Troubleshooting Steps
1. Verified the configuration of the Content-Aware Protection (CAP) policies.
2. Tested the copy-paste functionality with the configured policies.
3. Confirmed that the notification for blocked actions was displayed when copying sensitive data.
4. Turned off the "apply paste restrictions to all monitored applications" to check if the transfer was still possible.
5. Scheduled a remote session to further investigate the issue.
6. During the remote session, checked:
   - EPP client rights
   - DPI certificate status
   - Additional exit points and file extensions in the policy
7. Collected logs for further analysis.

## Root Cause
The issue was identified as a limitation in the current policy configuration, where the clipboard content could still be sent as an image, bypassing the text-based restrictions set in the policies.

## Solution
The issue was resolved by:
- Adjusting the policy settings to include additional restrictions on image data transfer.
- Ensuring that the policies were correctly applied and that the EPP client had the necessary rights.
- Forwarding the logs to the R&D team for further investigation and potential updates to the product to address this limitation.

## Notes
- It is important to regularly review and update policy configurations to ensure they cover all potential data transfer methods, including image data.
- Customers should be informed of the limitations regarding clipboard data transfer and potential workarounds until a permanent solution is implemented.