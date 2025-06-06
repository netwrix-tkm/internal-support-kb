## Ticket Metadata
- **Ticket ID:** 500Qk00000LUSxGIAX
- **Case Number:** 434682
- **Status:** Closed - Resolved
- **Account/Company:** Astra Rafael Comsys Pvt. Ltd.
- **Contact Name:** Dushaynth Dushyanth
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer reported that a server configured with a static IP address was behaving as if it were using DHCP, resulting in an automatic change of the IP address.

## Environment Details
- The server in question had two network cards, but only one was connected to the network at the time of the issue.

## Troubleshooting Steps
1. Verified the static IP configuration on the server.
2. Identified that the second network card was not connected to the network.
3. Connected the second network card to the network.
4. Instructed the customer to monitor the server for any changes in the IP address.

## Root Cause
The issue was caused by the second network card being disconnected from the network, which likely led the server to revert to DHCP behavior due to network configuration settings.

## Solution
The issue was resolved by connecting the second network card to the network. After this action, the customer was advised to observe the server to confirm that the static IP address remained unchanged.

## Notes
- Ensure that all network cards are properly connected when configuring static IP addresses to avoid similar issues in the future.
- It may be beneficial to document the network configuration settings for future reference and troubleshooting.