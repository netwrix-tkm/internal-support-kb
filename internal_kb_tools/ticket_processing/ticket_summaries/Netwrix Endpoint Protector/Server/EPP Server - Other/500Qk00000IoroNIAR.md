## Ticket Metadata
- **Ticket ID:** 500Qk00000IoroNIAR
- **Case Number:** 428198
- **Status:** Closed - Resolved
- **Account/Company:** Samsung Research America, Inc.
- **Contact Name:** Warren Huie
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** 1.1

## Problem Description
The customer reported that after rebooting the EPP server, the IP address was lost, and they were unable to update the network gateway address.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The support team reached out to the customer to schedule a remote session for troubleshooting.
2. The customer indicated that they had a similar issue on a development server and suggested transferring the case to another technician who was already addressing a related issue.
3. The support team investigated the server configuration and network settings.

## Root Cause
The issue was identified as missing network adapters from the EPP server, which prevented the server from maintaining its IP address after a reboot.

## Solution
The support team re-added the missing network adapters from the backend of the EPP server. After this action, the server was able to retain its IP address and the network gateway address could be updated successfully.

## Notes
- Ensure that network adapters are properly configured and present after server reboots to avoid similar issues in the future.
- It may be beneficial to document the configuration of network settings to facilitate quicker troubleshooting in case of similar incidents.