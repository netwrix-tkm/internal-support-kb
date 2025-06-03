## Ticket Metadata
- **Ticket ID:** 500Qk00000McWJzIAN
- **Case Number:** 437895
- **Status:** Closed - Resolved
- **Account/Company:** KEURO Besitz GmbH & Co. EDV-Dienstleistungs KG
- **Contact Name:** Benjamin Gutberlet
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts Configuration
- **Version:** Not specified

## Problem Description
The customer reported that one of their administrators was receiving emails indicating that a transfer limit had been reached, despite not having set up any alerts for this event. The customer was unable to locate the specific setting in the Endpoint Protector console to view this alert or check which files had been transferred.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector platform.
- The alerts were being sent to all administrators, even those without a mailbox.

## Troubleshooting Steps
1. Confirmed that the customer had not set up any alerts in the Alerts -> Device Control Alerts section.
2. Informed the customer that the transfer limit alert is enabled by default in the Transfer Limit section and is intended to notify all administrators.
3. Suggested disabling the Transfer Limit Reached Alert to check if the daily report was still being received.
4. Provided guidance on where to find the transfer limit settings and how to check which files were transferred.

## Root Cause
The root cause of the issue was identified as the default behavior of the Netwrix Endpoint Protector, where the Transfer Limit Reached Alert is automatically enabled for all administrators. This was not a misconfiguration but rather the intended functionality of the system.

## Solution
The issue was resolved by informing the customer about the default settings of the Transfer Limit alert. The customer was advised that they could disable the global alert if they wished, but they could still set up individual alerts for the transfer limit even after disabling the global setting. Additionally, the customer was guided on how to access the reports to check which files had been transferred.

## Notes
- It is important for administrators to be aware that transfer limit alerts are sent by default to all admins and that this behavior is intended.
- Future inquiries regarding transfer limit alerts should clarify that these alerts can be managed separately from other alert configurations in the system.
- Customers should be informed that disabling the global alert does not prevent them from setting up specific alerts for transfer limits in the future.