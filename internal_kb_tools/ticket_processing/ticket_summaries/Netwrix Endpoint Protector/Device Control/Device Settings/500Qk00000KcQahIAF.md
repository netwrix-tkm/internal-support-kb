## Ticket Metadata
- **Ticket ID:** 500Qk00000KcQahIAF
- **Case Number:** 432132
- **Status:** Closed - Resolved
- **Account/Company:** Canada Guaranty
- **Contact Name:** Parinkumar Patel
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** Not specified

## Problem Description
The customer reported an inconsistency in the Data Loss Prevention (DLP) console after migrating to group-level settings from custom settings. The DLP console indicated that the Deep Packet Inspection (DPI) status was "ON," while the EPP client on the endpoint showed it as "disabled."

## Environment Details
- Migration from custom settings to group-level settings in the DLP console.
- Endpoints managed through Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Verified that the group settings matched the individual host settings.
2. Attempted to reproduce the issue by restoring custom computer settings to group settings.
3. Conducted tests to check if the settings reverted correctly to the group settings after restoration.
4. Engaged in communication with the customer to gather more information and confirm the issue.

## Root Cause
The root cause of the issue was not identified. The support team could not reproduce the reported behavior, indicating that the settings were functioning as intended during their tests.

## Solution
The issue was resolved by confirming that the DPI settings were correctly applied and functioning as expected. The support team communicated with the customer, and after a period of monitoring, the ticket was closed with no further feedback from the customer.

## Notes
- It is important to ensure that group settings are consistently applied across all endpoints after migration.
- Future cases involving similar discrepancies should involve thorough testing to confirm the behavior of settings post-migration.
- If issues arise again, consider checking for any potential caching issues or delays in settings propagation between the DLP console and the EPP client.