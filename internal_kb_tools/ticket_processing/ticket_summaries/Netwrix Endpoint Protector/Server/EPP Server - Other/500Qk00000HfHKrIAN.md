```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HfHKrIAN
- **Case Number:** 425494
- **Status:** Closed - Resolved
- **Account/Company:** Government (Malta)
- **Contact Name:** Glenn Bilocca
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** Content Aware Protection
- **Version:** EPP Server version – 5.9.4.0, Client Version – 6.2.2.2005

## Problem Description
The customer reported difficulties in deploying the feature to disable the Print Screen and Snipping Tool functionalities through Content Aware Protection. Despite enabling the feature, it was not functioning as expected.

## Environment Details
- **EPP Server Version:** 5.9.4.0
- **Client Version:** 6.2.2.2005

## Troubleshooting Steps
1. Verified the configuration settings in the Content Aware Protection policy.
2. Suggested restarting the endpoint and updating the policies.
3. Conducted a meeting to reproduce the issue with the latest EPP client version.
4. Collected logs for further analysis.
5. Engaged the Engineering team for deeper investigation.
6. Attempted to block the Snipping Tool and Print Screen functionalities using denylist entries.

## Root Cause
The issue was identified as a bug where the Print Screen functionality was not being blocked due to additional processes (specifically `ScreenSketch.exe`, `ScreenClippingHost.exe`, and `GameBar.exe`) that were not initially included in the denylist.

## Solution
The issue was resolved by adding the following executables to the denylist with the wildcard parameter:
- `Snippingtool.exe`
- `ScreenSketch.exe`
- `ScreenClippingHost.exe`
- `GameBar.exe`

This configuration effectively blocked the Print Screen functionality as intended.

## Notes
- Ensure that all relevant processes are included in the denylist to prevent similar issues in the future.
- Always use the wildcard parameter (*) when adding applications to the denylist to ensure comprehensive blocking.
- Regularly check for updates from the Engineering team regarding any known bugs or issues with the software.
```