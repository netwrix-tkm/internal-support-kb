## Ticket Metadata
- **Ticket ID:** 500Qk00000KyajTIAR
- **Case Number:** 433304
- **Status:** Closed - Resolved
- **Account/Company:** Techbull Softtech Pvt Ltd
- **Contact Name:** Sai Nachiappan
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** Not specified

## Problem Description
The customer reported that after configuring the SMTP settings for email alerts, they were not receiving any emails, including test emails. Despite changing SSL and TLS settings, the issue persisted.

## Environment Details
- The machine had no internet connection, which was a critical factor affecting email delivery.

## Troubleshooting Steps
1. Verified SMTP configuration settings.
2. Attempted to send test emails to check functionality.
3. Changed SSL and TLS settings to ensure compatibility.
4. Identified that the machine lacked an internet connection.

## Root Cause
The root cause of the issue was identified as the lack of an internet connection on the machine, which prevented the SMTP server from sending emails.

## Solution
The solution involved providing an internet connection to the machine. Once the internet was established, the email alerts functioned correctly, and the customer confirmed that the issue was resolved.

## Notes
- Ensure that machines intended to send email alerts have a stable internet connection.
- Future configurations should include a check for internet connectivity as a preliminary step to avoid similar issues.