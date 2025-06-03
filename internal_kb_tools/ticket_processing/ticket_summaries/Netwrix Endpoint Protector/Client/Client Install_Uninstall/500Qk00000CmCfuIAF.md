## Ticket Metadata
- **Ticket ID:** 500Qk00000CmCfuIAF
- **Case Number:** 414293
- **Status:** Closed - Resolved
- **Account/Company:** BizEquity
- **Contact Name:** James Barnes
- **Product:** Netwrix Endpoint Protector
- **Component:** Client Install/Uninstall
- **Feature:** Client Install/Uninstall
- **Version:** Not specified

## Problem Description
The customer reported that the Data Loss Prevention (DLP) feature, specifically DPI (Deep Packet Inspection), was not functioning after installation. Although DPI was enabled, the required certificate was not available and was not trusted.

## Environment Details
- Platform: Mac
- Management Tool: Jamf

## Troubleshooting Steps
1. Verified that DPI was enabled in the settings.
2. Attempted to upload and import the required certificate multiple times.
3. Uninstalled and reinstalled the Netwrix Endpoint Protector client several times.
4. Followed multiple guides for configuration, both manually and via Jamf.
5. Scheduled a remote session to further investigate the issue.

## Root Cause
The issue was identified as being related to the VPN settings. DPI was not functioning correctly because the intercept VPN was turned off, which prevented the proxy from being utilized on the Macs.

## Solution
The issue was resolved by:
- Turning on the intercept VPN.
- Allowing the proxy settings on the Macs.

This configuration change enabled the DPI feature to function as intended.

## Notes
- Ensure that the intercept VPN is enabled and proxy settings are correctly configured on all Macs where DPI is required.
- Future installations should verify VPN settings as part of the initial setup to prevent similar issues.