## Ticket Metadata
- **Ticket ID:** 500Qk00000FVmfdIAD
- **Case Number:** 420409
- **Status:** Closed - Resolved
- **Account/Company:** Stensul
- **Contact Name:** Agustin Llovet
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** 5.9.4.0 (Server), 6.2.3.1 (Windows), 3.0.3.1 (macOS)

## Problem Description
After updating the Netwrix server and endpoints to enhance security, users reported issues with web browsing, specifically:
- Difficulty loading certain web pages
- "WebSocket" connection issues, causing some pages to fail to load entirely

## Environment Details
- Server Version: 5.9.4.0
- Endpoint Versions: 
  - Windows: 6.2.3.1
  - macOS: 3.0.3.1
- Most affected devices were Macs; no issues reported on Windows devices.

## Troubleshooting Steps
1. Conducted preliminary investigations to rule out connectivity and web application issues.
2. Disabled Deep Packet Inspection (DPI) on two devices, which temporarily resolved the web browsing issues.
3. Communicated with Netwrix support for further assistance and potential solutions.

## Root Cause
The issues were identified as being related to the Deep Packet Inspection (DPI) feature of the Netwrix Endpoint Protector, which interfered with web browsing functionality, particularly for WebSocket connections.

## Solution
The recommended solution involved uninstalling the current EPP Client from affected machines and installing a test build provided by Netwrix support. This test build was expected to resolve the web browsing issues. However, as a temporary workaround, disabling DPI allowed users to access previously blocked websites.

## Notes
- Users were advised to keep DPI disabled until the test build could be evaluated.
- If the test build resolves the issue, it may be deployed more widely through the Client Software Upgrade feature in the dashboard.
- Future updates should be monitored closely for similar issues, especially concerning DPI settings and their impact on web browsing.