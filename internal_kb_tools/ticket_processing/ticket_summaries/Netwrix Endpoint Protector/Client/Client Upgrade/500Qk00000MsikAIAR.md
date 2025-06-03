## Ticket Metadata
- **Ticket ID:** 500Qk00000MsikAIAR
- **Case Number:** 438652
- **Status:** Closed - Resolved
- **Account/Company:** BeeWaTec AG
- **Contact Name:** Alexander Mack
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** NONE

## Problem Description
The customer reported that when attempting to upgrade client software to the latest version, only 39 licensed clients were displayed when selecting "all," despite the License Manager indicating around 190 clients.

## Environment Details
- The issue occurred within the Netwrix Endpoint Protector platform.
- The customer had a mix of operating systems, including Windows, Ubuntu, and MAC devices.

## Troubleshooting Steps
1. The support engineer requested the customer to check the System Configuration under System Licensing to verify if all 190 seats were occupied.
2. The customer was advised to consider the operating systems of the clients, as the upgrade selection might be limited by OS compatibility.
3. The support engineer noted that some clients might already have the latest version installed, which would reduce the number of available endpoints for upgrade.

## Root Cause
The issue was identified as a potential bug in the client software upgrade process, which initially limited the visibility of clients eligible for upgrade.

## Solution
The customer reported that after selecting version 6.2.4.2, all 193 clients became visible for the upgrade process. The upgrade was initiated successfully, with 90 clients upgraded without issues.

## Notes
- It is important to ensure that the correct version is selected during the upgrade process to avoid similar visibility issues in the future.
- Customers should be reminded to check for any clients that may already have the latest version installed, as this can affect the number of clients available for upgrade.