# Ticket Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000HiTKhIAN
- **Case Number:** 425670
- **Status:** Closed - Resolved
- **Account/Company:** Healthcare Fraud Shield
- **Contact Name:** Karl Strobach
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported issues with alerts not being sent to email, despite previous configurations appearing correct.

## Environment Details
- The mailer folder was deleted and re-created.
- The customer was using an email address that appeared multiple times in the recipient list.

## Troubleshooting Steps
1. Deleted and re-created the mailer folder; confirmed that test emails were sent successfully.
2. Scheduled multiple remote sessions to troubleshoot the issue due to customer availability.
3. Re-created the alerts cache during a remote session.
4. Conducted tests using telnet to the SMTP server, which was successful.
5. Reviewed logs (syslog and mail.log) and identified connection refused error messages.
6. Engaged R&D for further investigation and recommendations.

## Root Cause
The issue was identified as a problem with the alert creation process, specifically related to the "Check all" checkbox in the Administrator section, which caused alerts to not be sent correctly.

## Solution
- The engineering team provided a workaround: 
  - Edit the alerts, uncheck all Administrators, and save the alert without any Administrators.
  - Then, edit again and manually check each Administrator that needs to receive the alert without using the "Check all" checkbox.
- The customer confirmed that the issue was resolved after implementing the workaround, and alerts began to come through as expected.

## Notes
- Ensure that the "Check all" checkbox functionality is reviewed in future updates to prevent similar issues.
- Monitor for any changes in email server settings or configurations that could affect alert delivery.
- Always verify the recipient list for duplicates, as this can complicate alert delivery.