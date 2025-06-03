# Ticket Summary for Support Case

## Ticket Metadata
- **Ticket ID:** 500Qk00000ItBWjIAN
- **Case Number:** 428409
- **Status:** Closed - Resolved
- **Account/Company:** J M BAXI GROUP
- **Contact Name:** Prasanth Ganesan
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Other
- **Version:** None

## Problem Description
The customer reported issues with two websites that were being blocked by the Netwrix Endpoint Protector (EPP) client, specifically when applying the Content Aware Protection (CAP) policy. The affected websites were:
1. [business.moneycorp.com/exchange-currency](https://business.moneycorp.com/exchange-currency) - A currency conversion tool that stopped functioning when the CAP policy was applied.
2. [figma.com/files/team](https://figma.com/files/team) - This website did not load correctly after logging in when the CAP policy was applied.

## Environment Details
- The issues were observed on machines with the EPP client installed.
- The CAP policy was applied to the affected machines.

## Troubleshooting Steps
1. Conducted a remote session with the customer to investigate the issues.
2. Reviewed logs from the EPP client to identify any blocked URLs (no logs were generated for the Figma website).
3. Removed the machines from the CAP policy, which allowed the websites to function correctly.
4. Enabled "DPI Bypass" for the affected machines during the remote session.
5. Added the domains to the whitelist as a temporary measure.

## Root Cause
The root cause of the issue was identified as the CAP policy interfering with the functionality of specific web tools on the affected websites. The EPP client was blocking necessary processes without generating logs, making it difficult to diagnose the problem initially.

## Solution
The issue was resolved by:
- Enabling "DPI Bypass" on the affected machines, which allowed the tools on the websites to function correctly.
- Adding the necessary domains to the whitelist to prevent future blocking of legitimate processes.

## Notes
- It is important to ensure that "DPI Bypass" is enabled whenever similar issues arise with web applications being blocked by the EPP client.
- Always check and update the DPI whitelist dictionaries when modifying the Content Aware Policy to avoid unintended blocking of legitimate applications.
- Future cases should be handled independently to avoid confusion, especially when multiple issues are reported simultaneously.