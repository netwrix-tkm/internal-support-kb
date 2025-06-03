## Ticket Metadata
- **Ticket ID:** 500Qk00000MfHppIAF
- **Case Number:** 438023
- **Status:** Closed - Resolved
- **Account/Company:** Rubyplay Limited
- **Contact Name:** CoreWin Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Allowlist / Denylist
- **Version:** 6.2.4.2 (Client), 5.9.4.1 (Server)

## Problem Description
The customer, RubyPlay, reported a false positive URL blocking issue where the URL `tunnel.googlezip.net` was blocked according to the Content Aware Report (CAP), despite not being listed in the URL Denylist.

## Environment Details
- **Client Version:** 6.2.4.2 (Windows)
- **Server Version:** 5.9.4.1
- **Operating System:** Windows 11 Pro (26100.3194)

## Troubleshooting Steps
1. Verified that the URL `tunnel.googlezip.net` was not present in the URL Denylist.
2. Checked the Content Aware Report (CAP) for details on the policy triggering the block.
3. Confirmed that the customer was using the latest server and client versions.
4. Suggested the customer enable specific DPI settings:
   - Stealthy DPI Driver
   - Bypass DPI Certificate Rejection by Third-Party Applications
5. Awaited feedback from the customer after enabling the recommended settings.

## Root Cause
The issue was identified as a false positive caused by the DPI (Deep Packet Inspection) settings not being properly configured, leading to incorrect blocking of the URL.

## Solution
The issue was resolved by configuring the DPI settings as recommended. The customer enabled the Stealthy DPI Driver and Bypass DPI Certificate Rejection options, which corrected the false positive URL blocking behavior.

## Notes
- Ensure that DPI settings are properly configured in future cases to prevent similar false positives.
- Regularly verify that the URL Denylist is up to date and that the latest software versions are being used to minimize issues.