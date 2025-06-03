## Ticket Metadata
- **Ticket ID:** 500Qk00000JQsgAIAT
- **Case Number:** 429725
- **Status:** Closed - Resolved
- **Account/Company:** Canada Guaranty
- **Contact Name:** Parinkumar Patel
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Settings
- **Version:** Not specified

## Problem Description
The customer reported that when attempting to apply Data Loss Prevention (DLP) settings at the Group level for their hosts, the settings were not inherited by the hosts as expected. This required the customer to manually change settings on each host, which was not ideal.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector environment.
- The customer was transitioning from custom settings for individual computers to group settings.

## Troubleshooting Steps
1. Reviewed the DLP settings applied at the Group level.
2. Confirmed that the hosts were correctly assigned to the group.
3. Explained the inheritance mechanism of settings in the Endpoint Protector (EPP).
4. Identified that custom settings were still in place on the hosts.

## Root Cause
The issue was caused by the presence of custom settings on the hosts, which prevented the group-level DLP settings from being inherited. The custom settings needed to be restored to global settings for the inheritance to function correctly.

## Solution
The resolution involved guiding the customer to:
- Remove or reset the custom settings on the hosts.
- Ensure that the group-level DLP settings were correctly configured.
- Confirm that the hosts were set to inherit settings from the group.

Once the custom settings were restored to global settings, the group-level DLP settings were successfully inherited by the hosts.

## Notes
- It is important to ensure that custom settings are cleared or reset before applying group settings to avoid inheritance issues.
- Future transitions from custom to group settings should be planned carefully to prevent similar issues.