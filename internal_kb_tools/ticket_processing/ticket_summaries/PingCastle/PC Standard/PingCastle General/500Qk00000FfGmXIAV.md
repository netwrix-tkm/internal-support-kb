## Ticket Metadata
- **Ticket ID:** 500Qk00000FfGmXIAV
- **Case Number:** 420784
- **Status:** Closed - Resolved
- **Account/Company:** Decathlon
- **Contact Name:** Mohamed SAKHO
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer requested assistance on how to export the HTML audit report to a specific path instead of the default configuration. Additionally, they inquired about setting up SMTP to automatically send the report via email.

## Environment Details
- **Platform:** PingCastle
- **Product Version:** 3.2.0.1

## Troubleshooting Steps
1. Reviewed the customer's request regarding exporting reports and SMTP configuration.
2. Investigated potential issues with SMTP settings and certificate requirements.
3. Confirmed the configuration of the SMTP server and its associated certificates.

## Root Cause
The issue was identified as a certificate problem linked to the customer's SMTP server, which was preventing the successful sending of emails.

## Solution
The problem was resolved by installing the necessary certificate on the server running PingCastle. Once the certificate was properly installed, the email functionality for sending reports worked as intended.

## Notes
- Ensure that the SMTP server has the correct certificates installed to avoid similar issues in the future.
- It may be beneficial to document the steps for configuring SMTP and exporting reports for future reference.