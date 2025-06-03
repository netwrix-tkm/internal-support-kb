## Ticket Metadata
- **Ticket ID:** 500Qk00000KLqbEIAT
- **Case Number:** 431430
- **Status:** Closed - Resolved
- **Account/Company:** ZS Associates India Pvt. Ltd.
- **Contact Name:** Harshvardhan Mithapelli
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** None

## Problem Description
A user was unable to access the website `cp-prod.secretservercloud.com`, receiving an error message stating: "Your Session has expired, please log in again." The issue was resolved temporarily by disabling the Endpoint Protector (EPP), but the user still faced access issues when EPP was enabled.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5941
- **No logs were generated** for the user to analyze the issue further.

## Troubleshooting Steps
1. The user reported the issue and provided logs and a screenshot of the error.
2. Attempts to whitelist the website's URL were made, but they did not resolve the issue.
3. The support team escalated the issue internally for further analysis.
4. A session was scheduled to assist the user after upgrading to the latest version (6.2.4.2).
5. The support team collected additional logs from the user's system for further investigation.

## Root Cause
The root cause of the issue was not definitively identified. However, it was noted that there were no logs generated in the CAP portal, which made it difficult to analyze the behavior of the Endpoint Protector in this scenario.

## Solution
The issue was resolved by whitelisting the URL `cp-prod.secretservercloud.com` in the Endpoint Protector settings. After this action, the user was able to access the website without further issues.

## Notes
- It is important to ensure that URLs are whitelisted in the Endpoint Protector to prevent similar access issues in the future.
- Future cases should consider checking for log generation in the CAP portal to aid in troubleshooting.
- If users report similar issues, verify if disabling EPP resolves the problem, and consider whitelisting the affected URLs as a potential solution.