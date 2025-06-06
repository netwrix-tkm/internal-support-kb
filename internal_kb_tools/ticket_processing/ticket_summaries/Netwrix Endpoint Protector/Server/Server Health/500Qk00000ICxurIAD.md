## Ticket Metadata
- **Ticket ID:** 500Qk00000ICxurIAD
- **Case Number:** 426810
- **Status:** Closed - Resolved
- **Account/Company:** FcBrasil
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Health
- **Version:** 9.2

## Problem Description
The customer reported that they were unable to access the server, encountering a strange error. A screen capture of the error was attached to the ticket.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. The support engineer, Iosif Muntean, asked the customer if they had tried rebooting the virtual machine hosting the Endpoint Protector Server.
2. The customer confirmed they rebooted the VM, and the server appeared to be functioning normally afterward.
3. The ticket was kept open for monitoring in case the issue reoccurred.
4. Follow-up communications included inquiries about logs to diagnose the root cause of the initial error.

## Root Cause
The root cause was identified as a potential log rotation issue that filled the system partition. This likely caused the server to become inaccessible until the virtual machine was rebooted, which cleared the space and allowed the Endpoint Protector processes to restart.

## Solution
The issue was resolved by rebooting the virtual machine on which the Endpoint Protector Server was installed. After the reboot, the server returned to normal operation, and the issue did not reappear in the following days.

## Notes
- It is advisable to monitor the server's log rotation settings to prevent similar issues in the future.
- If the issue recurs, a remote session may be necessary to investigate the system logs for errors.