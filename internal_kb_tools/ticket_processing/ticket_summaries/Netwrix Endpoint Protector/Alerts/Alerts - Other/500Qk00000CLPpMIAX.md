```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CLPpMIAX
- **Case Number:** 413169
- **Status:** Closed - Resolved
- **Account/Company:** Chapman and Cutler LLP
- **Contact Name:** Veronica Yessa
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer reported that they were not receiving alerts for USB-related activity, which had been functioning previously. They confirmed that no changes were made to the alert configurations.

## Environment Details
- The issue was specifically related to alerts configured for USB device control activities.

## Troubleshooting Steps
1. Reviewed the alert configurations for USB-related activities.
2. Recreated the "Artifact Received" alert to test its functionality.
3. Successfully triggered the recreated alert.
4. Recreated the remaining alerts and requested the customer to test them on their end.

## Root Cause
The root cause was identified as a malfunction in the alert system, which required the alerts to be recreated to restore their functionality.

## Solution
The issue was resolved by:
- Recreating the "Artifact Received" alert, which successfully triggered when tested.
- Recreating all other alerts related to USB activities, which were then confirmed to be functioning correctly after customer testing.

## Notes
- The customer mentioned that they would be out of the office until December 19, 2024, and requested to hold any further testing until their return.
- A separate ticket (00428173) was raised for an ongoing issue with the System License Alert not triggering at the new threshold of 70%.
```