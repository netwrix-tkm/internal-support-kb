## Ticket Metadata
- **Ticket ID:** 500Qk00000PMkdjIAD
- **Case Number:** 445675
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Andy Bridson
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client
- **Feature:** EPP Client - Other
- **Version:** 1.0

## Problem Description
The customer reported that the Netwrix Endpoint Protector (EPP) Client was preventing successful Single Sign-On (SSO) sign-in to the Proton VPN via Okta. The sign-in process worked correctly when the EPP Client was uninstalled.

## Environment Details
- **VPN Client:** Proton VPN
- **SSO Provider:** Okta
- **EPP Client Version:** 1.0

## Troubleshooting Steps
1. Verified the issue by attempting to sign in to Proton VPN with the EPP Client installed, which failed.
2. Confirmed that the sign-in was successful when the EPP Client was removed.
3. Investigated potential configurations within the EPP Client that could affect VPN access.
4. Explored settings related to Deep Packet Inspection (DPI) within the EPP Client.

## Root Cause
The issue was identified as a conflict between the EPP Client's default settings and the Proton VPN's SSO authentication process. Specifically, the EPP Client's DPI settings were interfering with the VPN's ability to authenticate users via Okta.

## Solution
The issue was resolved by enabling the "Stealthy DPI Driver" feature within the EPP Client. After this adjustment, the user was able to successfully log in to Proton VPN using SSO.

## Notes
- Customers experiencing similar issues with VPN clients and EPP should consider enabling the Stealthy DPI Driver as a potential solution.
- It is advisable to document any changes made to EPP settings for future reference and troubleshooting.
- Ensure that affected users are informed about the changes to avoid confusion regarding VPN access.