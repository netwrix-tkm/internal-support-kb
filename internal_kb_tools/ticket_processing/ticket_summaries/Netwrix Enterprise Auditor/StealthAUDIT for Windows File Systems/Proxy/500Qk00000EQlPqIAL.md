```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EQlPqIAL
- **Case Number:** 418104
- **Status:** Closed - Resolved
- **Account/Company:** Bank of America Corporation
- **Contact Name:** Gregory Meyer
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Proxy
- **Version:** 11.5

## Problem Description
After upgrading to version 11.5, the customer reported numerous FSAA scan errors, specifically the error message indicating that a session had "gone away."

## Environment Details
- The issue was observed in the context of the Netwrix Enterprise Auditor platform, utilizing StealthAUDIT for Windows File Systems.
- The customer had multiple FSAA proxies in their environment.

## Troubleshooting Steps
1. Reviewed logs provided by the customer to identify potential issues.
2. Verified the versions of the FSAA proxies in the customer's environment.
3. Discovered that some proxies were running an outdated version (9.0).
4. Noted that there were too many simultaneous connections to proxy hosts.
5. Suggested the customer update the proxies via the Update proxy job or manually.
6. Attempted to provide the latest proxy version to the customer, but download issues occurred due to company restrictions.
7. Advised the customer to have someone else download the proxy for testing.

## Root Cause
The issue was caused by:
- Some FSAA proxies running an outdated version (9.0) instead of the latest version (11.5).
- An excessive number of simultaneous connections to the proxy hosts, which contributed to the session errors.

## Solution
- Upgraded all FSAA proxy hosts to the latest version (11.5).
- Conducted a test FSAA system scan on one of the affected hosts, which was successful.
- Recommended adjusting the performance settings for the FSAA system scan job by lowering the thread count if the error reoccurs.

## Notes
- If similar errors arise in the future, ensure that all FSAA proxies are updated to the latest version.
- Monitor the number of simultaneous connections to proxy hosts to prevent overload.
- Consider adjusting performance settings if issues persist after upgrades.
```