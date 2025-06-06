## Ticket Metadata
- **Ticket ID:** 500Qk00000HqVYzIAN
- **Case Number:** 425868
- **Status:** Closed - Resolved
- **Account/Company:** PrivatBank
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** Not specified

## Problem Description
PrivatBank reported that EPP (Endpoint Protector) administrators were unable to access the console due to the Two Factor Authenticator not functioning correctly. The issue was traced to an incorrect server time, which was ahead by one minute.

## Environment Details
- The EPP appliance was not configured to synchronize time with an external NTP (Network Time Protocol) server, leading to authentication failures.

## Troubleshooting Steps
1. Verified the server time settings on the EPP appliance.
2. Identified that the time was set forward by one minute.
3. Attempted to connect to the EPP backend for manual time adjustment.
4. Inquired about the configuration of the NTP server (pool.ntp.org) and its accessibility within the customer's network.
5. Confirmed that UDP port 123 needed to be allowed for NTP traffic.

## Root Cause
The root cause of the issue was that the EPP appliance was not allowed to access the NTP server (pool.ntp.org), preventing it from synchronizing its time correctly. This misconfiguration led to the Two Factor Authenticator failing to validate user access.

## Solution
- A remote session was conducted to manually set the correct time on the EPP appliance.
- Advised the customer to allow access to the NTP server (109.91.184.21) in their network settings to ensure proper time synchronization in the future.

## Notes
- It is crucial for the EPP appliance to have access to a reliable NTP server to avoid similar issues with time-sensitive operations like Two Factor Authentication.
- Ensure that UDP port 123 is open in the firewall settings to allow NTP traffic.
- Future configurations should include regular checks on time synchronization settings to prevent recurrence of this issue.