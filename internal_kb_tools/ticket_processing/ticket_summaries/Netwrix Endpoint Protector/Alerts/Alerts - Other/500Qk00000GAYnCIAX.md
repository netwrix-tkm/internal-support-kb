## Ticket Metadata
- **Ticket ID:** 500Qk00000GAYnCIAX
- **Case Number:** 421873
- **Status:** Closed - Resolved
- **Account/Company:** IsSolutions - EC
- **Contact Name:** Roque Macias
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer reported that the Firefox browser was unable to establish a secure connection due to interference from Netwrix Endpoint Protector NetDLP.

## Environment Details
- **Browser:** Firefox
- **Security Software:** Netwrix Endpoint Protector NetDLP

## Troubleshooting Steps
1. Verified the issue by attempting to connect to secure websites using Firefox.
2. Checked the configuration settings of Netwrix Endpoint Protector for any restrictions on secure connections.
3. Attempted to disable Netwrix Endpoint Protector temporarily to confirm if it was the source of the issue.
4. Explored the DPI (Deep Packet Inspection) settings within Netwrix Endpoint Protector.

## Root Cause
The issue was identified as being caused by the Deep Packet Inspection (DPI) feature of Netwrix Endpoint Protector, which was preventing Firefox from establishing secure connections.

## Solution
The issue was resolved by activating the DPI bypass feature within Netwrix Endpoint Protector, allowing Firefox to successfully establish secure connections.

## Notes
- Ensure that the DPI bypass is configured correctly for applications that require secure connections to avoid similar issues in the future.
- Regularly review the settings of Netwrix Endpoint Protector to ensure compatibility with commonly used applications.