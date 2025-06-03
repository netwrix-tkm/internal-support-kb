## Ticket Metadata
- **Ticket ID:** 500Qk00000MeuGbIAJ
- **Case Number:** 438016
- **Status:** Closed - Resolved
- **Account/Company:** Gemeinde Weyhe
- **Contact Name:** Jens Balk
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Rights
- **Version:** NONE

## Problem Description
The customer reported that a PC was no longer receiving policies from the Endpoint Protector. A reinstallation of the software did not resolve the issue, and the debug mode could not be activated.

## Environment Details
- Multiple PCs were affected, with the last policies received dating back to late January 2025.
- The server ID was confirmed as LYWBJ6RF, with an IP address of 192.168.106.59.

## Troubleshooting Steps
1. The customer provided a log report indicating that numerous PCs had not received policies for an extended period.
2. The support engineer requested logs from one of the affected computers.
3. The support engineer identified certificate issues in the logs that were preventing client communication.
4. The clients were re-registered to establish communication with the server.

## Root Cause
The issue was identified as a communication failure between the clients and the Endpoint Protector server due to certificate issues.

## Solution
The resolution involved re-registering the clients, which restored their ability to communicate with the Endpoint Protector server and receive policies.

## Notes
- Ensure that certificate issues are checked when clients are unable to communicate with the Endpoint Protector server.
- Regular monitoring of policy reception on client machines can help identify similar issues early.