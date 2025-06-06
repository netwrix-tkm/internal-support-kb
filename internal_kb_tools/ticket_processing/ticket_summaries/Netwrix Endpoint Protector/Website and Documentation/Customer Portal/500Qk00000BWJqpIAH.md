## Ticket Metadata
- **Ticket ID:** 500Qk00000BWJqpIAH
- **Case Number:** 411220
- **Status:** Closed - Resolved
- **Account/Company:** KEURO Besitz GmbH & Co. EDV-Dienstleistungs KG
- **Contact Name:** Benjamin Gutberlet
- **Product:** Netwrix Endpoint Protector
- **Component:** Website and Documentation
- **Feature:** Customer Portal
- **Version:** NONE

## Problem Description
During a proof of concept (POC), the customer reported that the Content Aware logs for file uploads via web browsers were not reaching the server. They attempted to upload a PDF file using both Edge and Chrome browsers on Windows, but no logs were generated for these events.

## Environment Details
- Browsers used: Microsoft Edge and Google Chrome
- Websites tested: wetransfer.com and dlptest.com
- Operating System: Windows
- Content Aware policy: Set to "Report Only"
- DPI (Deep Packet Inspection): Enabled with an allowlist that did not include the tested domains.

## Troubleshooting Steps
1. Confirmed that the Content Aware policy was applied to all users and computers.
2. Verified that the PDF file type was selected in the policy.
3. Attempted file uploads on both Edge and Chrome.
4. Noted the error "Server responded with 0 code" during the upload process on dlptest.com.
5. Checked the DPI log file, which showed no data.
6. Suggested restarting the computer and checking for crash reports related to sslsplit in the Windows Event Viewer.
7. Inquired if the browsers were using a proxy and confirmed the port number (8077).

## Root Cause
The issue was identified as being related to the proxy configuration. The DPI allowlist did not include the proxy port (8077), which prevented the logs from being captured correctly.

## Solution
The resolution involved adding the proxy port (8077) to the DPI allowlist under "Content Aware Protection > Deep Packet Inspection." After this adjustment, the logs for file uploads were successfully captured, and the customer confirmed that they could see the uploads in the logs.

## Notes
- Ensure that any proxies in use are included in the DPI allowlist to avoid similar issues in the future.
- When troubleshooting log capture issues, always verify proxy settings and configurations, as they can significantly impact logging functionality.