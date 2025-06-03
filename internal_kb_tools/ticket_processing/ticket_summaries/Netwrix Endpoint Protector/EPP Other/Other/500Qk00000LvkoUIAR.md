```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000LvkoUIAR
- **Case Number:** 435988
- **Status:** Closed - Resolved
- **Account/Company:** Helo.ai
- **Contact Name:** Qazi Amir
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Server: 5.9.4.1, Client: 6.2.4.0054

## Problem Description
The customer reported that Git was being blocked by a report-only policy in the Windows report policy settings. They requested assistance in configuring Git to work correctly without being blocked.

## Environment Details
- **Server Version:** 5.9.4.1
- **Client Version:** 6.2.4.0054

## Troubleshooting Steps
1. Verified that Git was being blocked by a report-only policy.
2. Enabled Stealthy DPI from Device Control -> Global Settings.
3. Tested Git functionality after enabling Stealthy DPI to confirm resolution.

## Root Cause
The issue was caused by a report-only policy that was blocking Git operations. The policy settings did not allow Git to function as intended.

## Solution
The issue was resolved by enabling Stealthy DPI from the Device Control settings. This adjustment allowed Git to bypass the restrictions imposed by the report-only policy, enabling it to function correctly.

## Notes
- Ensure that Stealthy DPI is enabled for applications that may be blocked by similar policies in the future.
- Monitor the CAP reporting issue under ticket no. 00434661 for any related concerns.
```