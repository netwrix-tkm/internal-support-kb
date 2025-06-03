## Ticket Metadata
- **Ticket ID:** 500Qk00000GcbYPIAZ
- **Case Number:** 422927
- **Status:** Closed - Resolved
- **Account/Company:** Syapse
- **Contact Name:** Silvio Barretta
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported that they were not receiving their EPP Content Alert emails, which is a recurring issue that typically requires support intervention to resolve.

## Environment Details
- **Platform:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Verified the email alert settings in the Netwrix Endpoint Protector configuration.
2. Checked the email server logs for any errors or issues related to email delivery.
3. Attempted to manually trigger the alert emails to see if they would be sent.
4. Cleared the email queue to remove any stuck messages.
5. Rebuilt the alerts cache to ensure that all alert configurations were up to date.

## Root Cause
The root cause of the issue was not explicitly identified in the case details. However, it was likely related to a backlog in the email queue or a corruption in the alerts cache that prevented the emails from being sent.

## Solution
The issue was resolved by performing the following actions:
- Cleared the mailer to remove any stuck or queued emails.
- Rebuilt the alerts cache to refresh the alert configurations and ensure proper functionality.

## Notes
- It is advisable to monitor the email alert system regularly to catch similar issues early.
- If the problem recurs, consider checking for any updates or patches for the Netwrix Endpoint Protector that may address email delivery issues.
- Document any changes made to the configuration for future reference.