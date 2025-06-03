## Ticket Metadata
- **Ticket ID:** 500Qk00000HwpgHIAR
- **Case Number:** 426169
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Denis Pasca
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked

## Problem Description
The customer reported that uploads of sensitive files were not being blocked when using WhatsApp Web, Telegram Web, and Facebook Messenger Web. The files were successfully blocked when sent through Slack, indicating that the issue was not with the files themselves. The customer expected uploads through the browser to be blocked regardless of the exit points for the messaging apps.

## Environment Details
- The issue was replicated on both Windows and Mac machines.
- The only log generated was the DPI Bypass log, with logs for Telegram being the only ones recorded in the production environment.

## Troubleshooting Steps
1. Verified that the exit points for WhatsApp Web, Telegram Web, and Facebook Messenger Web were activated in the policies.
2. Checked the logs for any indications of file uploads being blocked.
3. Confirmed that uploads were being blocked in Slack, ruling out issues with the files themselves.
4. Investigated the encryption status of the web applications in question.

## Root Cause
The root cause of the issue was identified as the end-to-end encryption employed by WhatsApp Web, Telegram Web, and Facebook Messenger Web. This encryption prevents the Netwrix Endpoint Protector from inspecting files being uploaded through these platforms, rendering the exit points ineffective for monitoring uploads.

## Solution
The recommended solution was to block access to WhatsApp Web, Telegram Web, and Facebook Messenger Web using a URL Denylist. This approach would prevent users from accessing these services altogether, thereby eliminating the risk of sensitive file uploads.

## Notes
- It is important to note that while the exit points are available for desktop applications, they do not function for web applications due to encryption.
- Users may still trigger alerts on desktop applications, but this is not applicable to the web versions.
- Most browser chat applications utilize end-to-end encryption, which may limit the effectiveness of monitoring tools like Netwrix Endpoint Protector for uploads through these platforms.