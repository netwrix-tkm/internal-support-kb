## Ticket Metadata
- **Ticket ID:** 500Qk00000IbQafIAF
- **Case Number:** 427766
- **Status:** Closed - Resolved
- **Account/Company:** PeopleStrong
- **Contact Name:** Rohit Nawani
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Custom Content (custom PII)
- **Version:** NONE

## Problem Description
The customer requested assistance in creating a Data Loss Prevention (DLP) policy to monitor data transfer logs for WhatsApp and Google Drive, specifically through browser activity. They sought confirmation on the feasibility of detecting data transfers in browsers using DLP and guidance on creating a context-aware policy for this purpose.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** Content-Aware Protection for monitoring data transfers.

## Troubleshooting Steps
1. Confirmed the capabilities of the Netwrix Endpoint Protector regarding DLP policies for WhatsApp and Google Drive.
2. Explained the limitations of enforcing Content Aware Protection on the web version of WhatsApp due to end-to-end encryption.
3. Suggested a workaround for WhatsApp by blocking the `web.whatsapp` domain under "Deep Packet Inspection" > "Denylists" and applying the Content Aware Policy on the WhatsApp Desktop Application.
4. Provided instructions for creating and enforcing a Content Aware Protection Policy for Google Drive, including selecting web browsers as exit points.

## Root Cause
The inability to enforce a Content Aware Protection policy on the web version of WhatsApp was due to the end-to-end encryption of files uploaded through the platform, which prevents monitoring of data transfers.

## Solution
The issue was resolved by:
- Advising the customer to block the `web.whatsapp` domain to prevent data transfers through the web version of WhatsApp.
- Guiding them on how to apply the Content Aware Policy on the WhatsApp Desktop Application to monitor and control file types.
- Providing detailed steps and a video demonstration for creating a Content Aware Protection Policy for Google Drive, ensuring that web browsers were selected as exit points.

## Notes
- It is important to note that while DLP policies can be effectively applied to Google Drive, the web version of WhatsApp cannot be monitored due to encryption. 
- Future users should be aware of the limitations of DLP in environments where end-to-end encryption is utilized, particularly with messaging applications.