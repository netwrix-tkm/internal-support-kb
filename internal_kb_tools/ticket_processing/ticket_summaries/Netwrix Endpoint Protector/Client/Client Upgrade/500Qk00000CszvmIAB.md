## Ticket Metadata
- **Ticket ID:** 500Qk00000CszvmIAB
- **Case Number:** 414645
- **Status:** Closed - Resolved
- **Account/Company:** Savills Investment Management (Germany) GmbH
- **Contact Name:** Werner Kessel
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2.2.1006

## Problem Description
The customer, Werner Kessel, reported issues with updating the EPP client from the EPP Server. He was uncertain whether the new client included specific add-ons and if the filename format was necessary for installation.

## Environment Details
- Previous client version: EPPClientSetup.6.2.2.1006_x86_64
- New client filename: EPPClientSetup_x86_64.msi
- Customer prefers not to install add-ons for Outlook, Internet Explorer, and Lotus Notes.

## Troubleshooting Steps
1. Customer downloaded the client from the EPP Server and the Netwrix security center.
2. Customer checked if the new client included the add-ons.
3. Customer inquired if the additional information in the filename was necessary for installation.

## Root Cause
The issue stemmed from the customer downloading an outdated version of the client from the EPP Server, which did not reflect the latest updates and configurations.

## Solution
- A remote session was scheduled to inject the new EPP Clients onto the EPP Server.
- After the injection, the customer was able to download the updated EPP Client from the EPP UI, allowing him to choose whether to include the add-ons in the installation package.

## Notes
- Ensure that the latest client version is available on the EPP Server to avoid similar issues in the future.
- Customers should be informed that the filename format may not be critical, but using the correct version is essential for successful installation.