## Ticket Metadata
- **Ticket ID:** 500Qk00000GaIRrIAN
- **Case Number:** 422823
- **Status:** Closed - Resolved
- **Account/Company:** Ambarella
- **Contact Name:** Andrea Camurri
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** Ubuntu 20.04, 22.04, 24.04

## Problem Description
The customer requested updated client installers for Ubuntu versions 20.04, 22.04, and 24.04. It was reported that the Ubuntu 24 agent was not checking in with the server.

## Environment Details
- **Operating Systems:** Ubuntu 20.04, 22.04, 24.04
- **Product Version:** Netwrix Endpoint Protector

## Troubleshooting Steps
1. Customer reported the issue regarding the Ubuntu 24 agent not checking in with the server.
2. A remote session was scheduled to investigate the issue further.
3. During the investigation, the `options.sh` file was identified as a potential source of the problem.

## Root Cause
The issue was traced back to a misconfiguration in the `options.sh` file, which prevented the Ubuntu 24 agent from properly communicating with the server.

## Solution
The problem was resolved by editing the `options.sh` file to correct the configuration settings, allowing the Ubuntu 24 agent to check in with the server successfully.

## Notes
- Ensure that the `options.sh` file is properly configured for future installations of the Ubuntu agent to avoid similar issues.
- Regularly verify agent connectivity after updates to ensure they are functioning as expected.