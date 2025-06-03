## Ticket Metadata
- **Ticket ID:** 500Qk00000BjpstIAB
- **Case Number:** 411679
- **Status:** Closed - Resolved
- **Account/Company:** Shakta Technologies Pvt Ltd
- **Contact Name:** Lokesh N
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Predefined Content (PII)
- **Version:** Not specified

## Problem Description
The customer reported issues with email alerts not being received after implementing a WhatsApp blocking policy for PII documents. Additionally, alerts were not triggered when sending PII-related text messages, and there were issues with the SMTP mail server.

## Environment Details
- The EPP server was configured to send alerts using the email address `root@eppserver`, which was not recognized as a valid user by the mail server.
- The customer was using a relay for email delivery.

## Troubleshooting Steps
1. Verified the email server settings and confirmed the use of `root@eppserver` as the sender.
2. Engaged with R&D to investigate the "unable to qualify my own domain name" error, indicating misconfigured hostname settings.
3. Conducted multiple remote sessions to troubleshoot the email alert issues.
4. Performed an uninstall and reinstall of the EPP software to restore communication with the server.
5. Changed the ownership of the Mailer folder from `root` to `www-data`.
6. Cleared pending emails from the database and restarted mailer alerts.
7. Verified the mail.log to confirm that emails were being sent.
8. Conducted tests with multiple devices to ensure alerts were received.

## Root Cause
The root cause of the issue was identified as the use of an invalid email address (`root@eppserver`) for sending alerts, which was rejected by the mail server due to it not being a fully qualified user. Additionally, there were connection timeout errors with the relay due to security settings.

## Solution
The issue was resolved by:
- Changing the ownership of the Mailer folder to `www-data`, which allowed the alerts to be sent successfully.
- Reconfiguring the email server settings and ensuring that valid email addresses were used for sending alerts.
- Conducting tests that confirmed alerts were being received correctly after the changes were made.

## Notes
- It is crucial to ensure that valid email addresses are configured for sending alerts to avoid issues with mail server rejections.
- Future configurations should consider using a custom sender address to prevent similar issues with the default `root@eppserver` address.
- The customer was advised to monitor the alerts and report any further issues before closing the ticket.