## Ticket Metadata
- **Ticket ID:** 500Qk00000NnAtqIAF
- **Case Number:** 441224
- **Status:** Closed - Resolved
- **Account/Company:** Impulse telecom (@impulse-telecom.com) - MX
- **Contact Name:** Edgar Onesto
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer needed to install the Endpoint Protector (EPP) on devices located in different branches with different network segments. They required static routes on the server to establish effective communication between the EPP server and clients.

## Environment Details
- The company has a Data Loss Prevention (DLP) service in place.
- Communication between branches is established via VPN.
- Previous configurations for static routes were lost due to migration and backup issues.

## Troubleshooting Steps
1. Proposed using a Public IP or DNS for the EPP server to allow clients to connect.
2. Suggested using an internal IP, ensuring all computers within the network could reach that IP or connect via VPN.
3. Discussed creating an Access Control List (ACL) in the firewall to allow outside traffic.
4. Engaged in email communications to clarify requirements and gather additional information from the customer.
5. Scheduled a remote session to further investigate the issue and assist with configuration.

## Root Cause
The issue stemmed from the loss of previously configured static routes due to migration and backup processes, which prevented effective communication between the EPP server and clients across different network segments.

## Solution
The resolution involved:
- Confirming the use of an internal IP for the EPP server, ensuring that all devices on the network could connect to it.
- Implementing a VPN solution to facilitate communication between different network segments.
- Creating an ACL in the firewall to allow necessary traffic to and from the EPP server.

## Notes
- It is crucial to maintain documentation of network configurations to prevent loss during migrations or backups.
- Future installations of EPP across different network segments should consider the security implications of using Public IPs and ensure that internal IPs and VPNs are properly configured to maintain secure communication.