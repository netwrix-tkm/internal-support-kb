## Ticket Metadata
- **Ticket ID:** 500Qk00000PARLdIAP
- **Case Number:** 445143
- **Status:** Closed - Resolved
- **Account/Company:** Chapman and Cutler LLP
- **Contact Name:** Veronica Yessa
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer reported that all alerts had stopped working again after previously functioning correctly following a switch to cloud hosting earlier in the year. The alert history showed no entries, and although a test email was successfully sent, the expected alerts were not being received.

## Environment Details
- The issue occurred after the transition to a cloud-hosted environment.
- A significant number of alerts were pending and stuck in processing.

## Troubleshooting Steps
1. Verified the alert history, which showed no recent alerts.
2. Sent a test email through the mail setup, which was successful.
3. Updated alerts that were stuck in processing.
4. Deleted and rebuilt the alert cache.

## Root Cause
The root cause of the issue was identified as a large number of alerts being stuck in processing, which prevented new alerts from being generated and sent.

## Solution
The issue was resolved by updating the stuck alerts and deleting the existing alert cache, followed by rebuilding it. This process allowed the alerts to function correctly again, and the customer was informed that alerts should now be operational.

## Notes
- It is important to monitor alert processing regularly to prevent similar issues in the future.
- The customer was informed about a possible fix in version 5950 regarding alerts, which may be relevant for future cases involving alert malfunctions.