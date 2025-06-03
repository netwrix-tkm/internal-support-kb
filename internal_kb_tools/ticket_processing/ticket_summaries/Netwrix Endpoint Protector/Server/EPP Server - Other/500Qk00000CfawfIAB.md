## Ticket Metadata
- **Ticket ID:** 500Qk00000CfawfIAB
- **Case Number:** 414080
- **Status:** Closed - Resolved
- **Account/Company:** Netweb Software Pvt. Ltd.
- **Contact Name:** Khalid Saiyed
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** 5.1

## Problem Description
After applying a server hotfix (adv-2024-002), the server's IP address changed from a static IP to a DHCP-assigned IP. The customer was unable to revert the IP address back to its original static configuration.

## Environment Details
- The issue occurred on a server running Netwrix Endpoint Protector.
- The customer reported that the same IP address pool was functioning correctly across their network.

## Troubleshooting Steps
1. The customer attempted to change the IP address back to static multiple times but was unsuccessful.
2. Netwrix support suggested accessing the EPP appliance to change the IP settings from DHCP to static.
3. The customer was advised to check the gateway address and ensure it was correct.
4. A server reboot was recommended before attempting to change the IP again.
5. The customer was instructed to match the first "Name Server" entry with the Default Gateway.
6. A remote session was scheduled for further assistance.

## Root Cause
The root cause of the issue was identified as a failure of the EPP server to accept the static IP configuration after the hotfix was applied. This was likely due to misconfiguration of network settings or conflicts with DHCP settings.

## Solution
During the remote session, the support engineer guided the customer through the following steps:
1. Verified the network configuration settings on the EPP appliance.
2. Ensured that the gateway address was correctly set to the firewall's IP, which serves as the LAN gateway.
3. Confirmed that the Name Server IP matched the Default Gateway.
4. Successfully changed the IP address back to the original static configuration.

The issue was resolved, and the customer was advised to monitor the system for any further issues.

## Notes
- It is important to ensure that the network settings are correctly configured before applying hotfixes to avoid similar issues.
- Customers should be advised to have a network specialist available when dealing with IP configuration issues, especially after updates or changes to the system.
- Monitoring the system after changes is crucial to ensure stability and functionality.