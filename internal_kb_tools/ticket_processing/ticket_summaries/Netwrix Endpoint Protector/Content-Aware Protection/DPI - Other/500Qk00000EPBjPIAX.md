```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EPBjPIAX
- **Case Number:** 418040
- **Status:** Closed - Resolved
- **Account/Company:** Roof Stacks Yazılım
- **Contact Name:** Faruk Sarı
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 8.1

## Problem Description
The customer reported that when the DPI (Deep Packet Inspection) feature is enabled on the Forti ZTNA product, they are unable to access specific resource web addresses that are only accessible when ZTNA is active. The issue does not occur when DPI is disabled.

## Environment Details
- The issue is occurring on Windows operating systems.
- The problem arises specifically when any exit point is selected in the Content-Aware Protection (CAP) settings while DPI is active.

## Troubleshooting Steps
1. Verified that the specified websites are accessible when DPI is disabled.
2. Tested access to the websites with DPI enabled and no exit points selected; access was successful.
3. Attempted to access the websites with DPI enabled and various exit points selected; access was unsuccessful.
4. Enabled debug mode to replicate the issue and reviewed the logs for errors.

## Root Cause
The root cause of the issue was identified as the need for "Stealthy DPI" to be activated on the affected computer. Without this setting enabled, the DPI feature interfered with the access to the specified websites.

## Solution
To resolve the issue, "Stealthy DPI" was activated on the customer's computer. This adjustment allowed the specified websites to be accessed successfully while keeping the DPI feature enabled.

## Notes
- Ensure that "Stealthy DPI" is activated on any system experiencing similar issues with Forti ZTNA and DPI.
- Monitor for any future updates or changes in the Forti ZTNA product that may affect DPI functionality.
```