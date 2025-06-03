```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GmSdXIAV
- **Case Number:** 423293
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Csilla Torok
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** 5.9.4.1 (fix included in this version)

## Problem Description
The customer reported that the EPP DEV agent was preventing access to web pages and Slack. Uninstalling the agent allowed access, but reinstalling it caused the issue to reoccur.

## Environment Details
- **Platform:** macOS
- **Agent Type:** DEV agent

## Troubleshooting Steps
1. The customer uninstalled the EPP agent, regaining access to web pages and Slack.
2. Upon reinstalling the agent, the issue reappeared.
3. Support requested logs from the affected machine.
4. Engineers analyzed the logs and identified that the DPI certificate was imported but not marked as trusted in the keychain.
5. Support provided links to download a test build of the EPP Client and instructions to reimport the DPI certificate and mark it as trusted.
6. The customer confirmed that the issue persisted after initial troubleshooting steps.
7. A test build was sent to the customer, which resolved the issue.

## Root Cause
The root cause was identified as the DPI certificate not being marked as trusted in the macOS keychain, which led to the EPP DEV agent blocking access to web pages and Slack.

## Solution
The issue was resolved by providing a test build of the EPP Client that included a fix for the DPI certificate handling. The customer was instructed to reimport the DPI certificate and ensure it was marked as trusted. This fix will be included in the official 5.9.4.1 server version.

## Notes
- Ensure that DPI certificates are marked as trusted in the keychain to prevent similar issues in the future.
- The fix provided in the test build will be included in the next official release, so customers should be advised to update to version 5.9.4.1 when available.
```