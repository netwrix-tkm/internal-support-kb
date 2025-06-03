## Ticket Metadata
- **Ticket ID:** 500Qk00000MaYEiIAN
- **Case Number:** 437811
- **Status:** Closed - Resolved
- **Account/Company:** Metalex Manufacturing, Inc
- **Contact Name:** Nicholas Wagner
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Predefined Content (PII)
- **Version:** Latest server version with older epp client

## Problem Description
A user reported being blocked from printing an email with no option to remediate the issue. The CAP logs indicated a non-existent policy called "Browser Printing" and referenced "Predefined Content" that was not being used as an Item Type. The user was not attempting to print from a browser.

## Environment Details
- The customer was using the latest server version of Netwrix Endpoint Protector but had an older version of the Endpoint Protection (epp) client installed.

## Troubleshooting Steps
1. Reviewed CAP logs to identify any relevant policies affecting printing.
2. Confirmed the server version was up to date while the epp client was outdated.
3. Suggested upgrading the epp client to the latest version.
4. Recommended rebooting the computer after the client upgrade.
5. Awaited confirmation from the customer regarding the reproducibility of the issue post-upgrade.

## Root Cause
The issue was caused by the use of an outdated epp client that was incompatible with the latest server version, leading to unexpected behavior when attempting to print.

## Solution
The problem was resolved by upgrading the epp client to the latest version. After the upgrade and a subsequent reboot of the computer, the user was able to print without encountering the blocking issue.

## Notes
- Ensure that clients are regularly updated to maintain compatibility with the server version.
- Monitor CAP logs for any unusual policies that may affect user operations, especially when they are not applicable to the current environment.