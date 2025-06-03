## Ticket Metadata
- **Ticket ID:** 500Qk00000ORVnDIAX
- **Case Number:** 443182
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Faruk Sarı
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Predefined Content (PII)
- **Version:** Server version 5.9.4.2, Client version 6.2.4.2

## Problem Description
The customer reported an issue with the detection of Turkish ID numbers (TCIDs) when sent in the body of emails using the new Outlook application. While TCIDs in file attachments were detected and blocked as expected, those written directly in the email body were not detected, leading to successful email delivery.

## Environment Details
- **Server Version:** 5.9.4.2 (upgraded from 5.9.4.1)
- **Client Version:** 6.2.4.2
- **CAP with DPI and Text Inspection:** Enabled and functioning for file attachments.

## Troubleshooting Steps
1. Verified that CAP with DPI and Text Inspection was enabled.
2. Conducted tests using both the old and new Outlook applications.
3. Sent TCIDs in various formats (PDF, TXT, and directly in the email body) to observe detection behavior.
4. Enabled Debug mode and repeated tests to check for any changes in detection.
5. Gathered logs and screen recordings to document the behavior.

## Root Cause
The issue was identified as a known limitation of the current Netwrix Endpoint Protector client when used with the new Outlook application. TCIDs in the email body are not detected or blocked, while those in attachments are handled correctly.

## Solution
The customer was informed that the inability to detect TCIDs in the email body when using the new Outlook is a known limitation. They were advised to continue using the old Outlook application for critical TCID detection until a new client version is released that addresses this limitation. The case was closed upon customer confirmation.

## Notes
- A new client version (5.9.4.3) is expected to be released in the second half of May, which will include an updated EPP Add-in that works with Microsoft user accounts and aims to resolve this limitation.
- It is recommended to monitor Netwrix Endpoint Protector release notes for updates regarding content inspection in the new Outlook application.
- Inform end users and stakeholders about the current limitation and recommend using the old Outlook if TCID detection in email bodies is critical.