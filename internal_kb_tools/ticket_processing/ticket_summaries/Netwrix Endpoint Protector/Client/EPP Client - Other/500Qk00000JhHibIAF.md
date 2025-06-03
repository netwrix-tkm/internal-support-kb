## Ticket Metadata
- **Ticket ID:** 500Qk00000JhHibIAF
- **Case Number:** 430309
- **Status:** Closed - Resolved
- **Account/Company:** Laykon Distributor
- **Contact Name:** Yağız Özkütük
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer reported that after completing client installations, the computers appeared offline in the management panel despite successful ping communication between the server and clients. Policy changes were detected by the clients, and all necessary permissions were granted.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Client Communication:** Successful ping between server and clients
- **Policy Detection:** Changes made to policies were detected by clients

## Troubleshooting Steps
1. Verified successful ping communication between the server and clients.
2. Checked if policy changes were being detected by the clients.
3. Confirmed that all necessary permissions were granted to the clients.
4. Investigated potential network issues or firewall settings that could affect client visibility.

## Root Cause
The issue was caused by the firewall settings on the client machines, which were blocking the necessary communication for the clients to appear online in the management panel.

## Solution
The problem was resolved when the customer added an exception in the firewall settings, allowing the necessary traffic for the Netwrix Endpoint Protector clients to communicate properly with the server.

## Notes
- Ensure that firewall settings are configured correctly during client installations to prevent similar issues in the future.
- It may be beneficial to provide customers with guidelines on configuring firewall exceptions for Netwrix products during the installation process.