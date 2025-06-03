```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CclyIIAR
- **Case Number:** 413934
- **Status:** Closed - Resolved
- **Account/Company:** Alcatel-Lucent Enterprise
- **Contact Name:** ALE Team
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** N/A
- **Version:** Build 5930

## Problem Description
Some applications, including Android Studio and Maven, were reported to not function correctly when Data Protection Integration (DPI) was enabled.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Client Code:** Client
- **DPI Feature:** Stealthy DPI

## Troubleshooting Steps
1. Requested additional details from the customer regarding server and client versions.
2. Asked the customer to describe the specific issues encountered with DPI enabled versus disabled.
3. Suggested disabling the MTP (Media Transfer Protocol), saving the settings, and restarting the PC to check if it resolved the issue.
4. Scheduled a session to collect logs and further investigate the problem.

## Root Cause
The root cause was identified as compatibility issues with certain applications when DPI was enabled. Specifically, the applications were unable to function properly due to the DPI settings interfering with their operations.

## Solution
The issue was resolved by enabling the "Stealthy DPI" feature, which allowed the applications to function correctly without the interference caused by standard DPI settings. This solution was confirmed to work for the applications that were previously experiencing errors.

## Notes
- It is recommended to use the Stealthy DPI setting for applications that may have compatibility issues with standard DPI.
- If further issues arise with other applications, additional debugging sessions may be necessary to find the best configuration for the Alcatel environment.
```