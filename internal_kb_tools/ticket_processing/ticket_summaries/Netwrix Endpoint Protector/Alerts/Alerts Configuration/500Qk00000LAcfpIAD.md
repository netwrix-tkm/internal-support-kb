## Ticket Metadata
- **Ticket ID:** 500Qk00000LAcfpIAD
- **Case Number:** 433853
- **Status:** Closed - Resolved
- **Account/Company:** Geico SpA
- **Contact Name:** Carlo Tafuni
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** 13.0

## Problem Description
The customer reported an issue with the email report configuration for the "New Device Control Event - FILE COPY - Daily copy 500 files" alert. They were receiving multiple reports for the same event, and there was an inconsistency in the information displayed in the Transfer Limit alerts, specifically regarding the presence of usernames in the alert messages.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Alert Type:** Transfer Limit Alerts

## Troubleshooting Steps
1. Conducted a remote session with the customer to better understand the issue.
2. Suggested the customer check the Transfer Limit Alerts in the Server UI to verify if the username was reported for those logs.
3. Advised the customer to compare the format of the alerts (with/without username) to identify any discrepancies.

## Root Cause
The root cause of the issue was identified as an inconsistency in the alert configuration, leading to some alerts displaying usernames while others did not. This inconsistency resulted in multiple reports being sent for the same event.

## Solution
The issue was resolved by guiding the customer to review and adjust the alert configuration settings in the Server UI. Ensuring that the alert format was consistent across all notifications helped eliminate the discrepancies in the username display and reduced the number of duplicate reports sent.

## Notes
- It is important for customers to regularly review their alert configurations to ensure consistency in the information being reported.
- Future cases involving alert configurations should include a check for the format and content of alerts to prevent similar issues.