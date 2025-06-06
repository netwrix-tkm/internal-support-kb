## Ticket Metadata
- **Ticket ID:** 500Qk00000MKGjxIAH
- **Case Number:** 437077
- **Status:** Closed - Resolved
- **Account/Company:** Waves Audio Ltd. (Israel)
- **Contact Name:** Rotem Dadon
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported an issue with their on-premise EPP server, which became unresponsive after a reboot initiated via the web UI. The server was still reachable via ping, but the customer did not have access to the root user credentials.

## Environment Details
- Two EPP servers: 
  - Old on-premise server hosted on VMware
  - New server located in the Netwrix datacenter
- The issue occurred during a client migration process from the old server to the new one.

## Troubleshooting Steps
1. Customer attempted to reboot the server via the web UI.
2. Confirmed that the server was reachable via ping.
3. Customer reached out for support due to lack of root access and unresponsiveness of the web UI.
4. A remote session was scheduled to investigate the issue further.

## Root Cause
The root cause of the issue was identified as a disk corruption on the partition `/dev/sda4`, which rendered the server unresponsive.

## Solution
The issue was resolved by running the following command during the remote session:
```bash
e2fsck /dev/sda4
```
This command checked and repaired the corrupted filesystem on the specified partition, restoring access to the server.

## Notes
- Ensure that root user credentials are securely stored and accessible for future troubleshooting.
- Regularly monitor disk health to prevent similar issues from arising.
- Consider implementing a backup strategy to facilitate recovery in case of disk corruption.