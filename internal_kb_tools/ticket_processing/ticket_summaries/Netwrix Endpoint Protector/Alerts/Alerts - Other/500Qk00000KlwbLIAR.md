## Ticket Metadata
- **Ticket ID:** 500Qk00000KlwbLIAR
- **Case Number:** 432748
- **Status:** Closed - Resolved
- **Account/Company:** Callzilla
- **Contact Name:** Daniel Florez
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** 3.1

## Problem Description
The customer reported that after configuring a custom notification, clients were unable to see it or receive notifications when violating system-aware parameters. The customer expressed urgency in resolving this issue to facilitate a massive deployment of the agent.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector platform.

## Troubleshooting Steps
1. Verified the configuration of the custom notification template and its association with the policy.
2. Checked the client settings to ensure notifications were enabled.
3. Investigated the client mode settings to determine if they were affecting notification delivery.

## Root Cause
The notifications were not sent because the client mode was set to silent, preventing any alerts from being displayed to the users.

## Solution
The issue was resolved by changing the client mode from silent to an active mode that allows notifications to be displayed. This adjustment enabled the clients to receive the configured notifications as intended.

## Notes
- Ensure that client mode settings are reviewed during the configuration of notifications to avoid similar issues in the future.
- It is advisable to test notification settings in a controlled environment before a large-scale deployment to confirm that alerts are functioning as expected.