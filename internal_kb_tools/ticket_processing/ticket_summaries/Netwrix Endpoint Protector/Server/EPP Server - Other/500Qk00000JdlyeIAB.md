```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000JdlyeIAB
- **Case Number:** 430176
- **Status:** Closed - Resolved
- **Account/Company:** Mordor Intelligence Pvt. Ltd.
- **Contact Name:** Mohammad Azam
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** Content Aware Protection
- **Version:** NONE

## Problem Description
The customer reported that Gmail was accessible only when the VPN was enabled. When the VPN was turned off, Gmail was blocked, indicating an issue with the Content Aware Protection (CAP) policy.

## Environment Details
- The Browsec VPN was installed as a plugin in the Chrome web browser.
- The CAP policy was configured to block the domain "mail.google.com".

## Troubleshooting Steps
1. Confirmed that the affected endpoints were part of a Content Aware Protection policy.
2. Verified that the policy type was set to "Outside Network".
3. Enabled the Stealthy DPI Driver on the affected endpoints.
4. Conducted a remote session to further investigate the issue.
5. Identified that the Browsec VPN was overriding the EPP SSL Certificate, making Deep Packet Inspection (DPI) ineffective.
6. Suggested adding port 1022 under "Deep Packet Inspection Ports & Settings" > "Custom Ports".

## Root Cause
The Browsec VPN was overriding the Endpoint Protector's SSL Certificate, which rendered the Content Aware Protection policy ineffective when the VPN was enabled. This caused the DPI to fail in blocking Gmail as intended.

## Solution
The issue was resolved by adding port 1022 to the "Deep Packet Inspection Ports & Settings" under "Custom Ports". This adjustment allowed the Endpoint Protector to function correctly even when the Browsec VPN was active.

## Notes
- Ensure that any VPN used does not interfere with the Endpoint Protector's SSL Certificate.
- Future configurations should consider the impact of browser-based VPNs on security policies.
- Always verify the correct ports are configured for DPI settings to avoid similar issues.
```