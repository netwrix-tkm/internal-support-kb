## Ticket Metadata
- **Ticket ID:** 500Qk00000CmCuPIAV
- **Case Number:** 414285
- **Status:** Closed - Resolved
- **Account/Company:** Kannan International Pvt Ltd. (former BrainValley Software Private Limited)
- **Contact Name:** Vasantha Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** Not specified

## Problem Description
The customer reported confusion regarding the reporting of file transfers, specifically when sending files via Gmail. The reports indicated a "chrome destination" with the type listed as "webbrowser," leading to uncertainty about whether files were transferred via email or simply opened in a web browser.

## Environment Details
- The customer had enabled Data Loss Prevention (DPI) but had not enabled the Endpoint Protector (EPP) network extension on the machines.

## Troubleshooting Steps
1. The customer was advised to enable the EPP network extension on all computers using a Mobile Device Management (MDM) tool.
2. A meeting was scheduled to install a new EPP Client and investigate the issue further.
3. The customer provided log files for analysis.
4. Communication was maintained with the customer to clarify the expected behavior of the EPP Client.

## Root Cause
The issue reported by the customer was not a malfunction but rather a misunderstanding of how the EPP Client operates. The EPP Client does not report email sender and receiver information for attachments when editing drafts without a recipient.

## Solution
The confusion was clarified by explaining that the EPP Client's behavior was expected. The customer was informed that:
- The email sender will always be reported.
- The email receiver will not be available for attachments when editing a draft without a recipient.
- The logs would show file transfers but not the sender/receiver details for certain scenarios.

## Notes
- Ensure that the EPP network extension is enabled on all machines to improve reporting accuracy.
- Educate users on the limitations of the EPP Client regarding email monitoring, especially concerning drafts and attachments.
- Future cases should verify the configuration of the EPP Client and the network extension settings to prevent similar misunderstandings.