## Ticket Metadata
- **Ticket ID:** 500Qk00000LJZsQIAX
- **Case Number:** 434301
- **Status:** Closed - Resolved
- **Account/Company:** FC Brasil
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** SIEM
- **Feature:** SIEM Sync
- **Version:** Not specified

## Problem Description
The customer, CIANDT, was migrating from Splunk to SecOps for their SIEM integration. They reported that while logs were successfully being sent to Splunk, no logs were being forwarded to SecOps. The customer inquired whether the Endpoint Protector (EPP) could send logs to both SIEMs simultaneously.

## Environment Details
- The customer was using two SIEM solutions: Splunk (operational) and SecOps (non-operational).
- The customer provided screenshots of their configuration and granted access to their backend for troubleshooting.

## Troubleshooting Steps
1. Reviewed the customer's configuration screenshots.
2. Accessed the backend to check the connection to SecOps.
3. Noted that broadcast messages were being generated continuously, preventing command execution.
4. Stopped the broadcast messages from displaying on the console.
5. Inquired about testing the connection to the customer's SIEM server configured with UDP.

## Root Cause
The issue was determined to be on the customer's side. During a meeting, it was discovered that the configuration or setup for SecOps was not correctly implemented, leading to the failure in log forwarding.

## Solution
The customer confirmed that they resolved the issue on their end. Specific steps taken by the customer were not detailed, but they acknowledged that the problem was not related to the Netwrix product.

## Notes
- It is important to ensure that both SIEM solutions are correctly configured to receive logs from the EPP.
- For future cases, if broadcast messages are overwhelming the console, consider stopping the service and adjusting the journald configuration as follows:
  ```bash
  service nginx stop
  Edit /etc/systemd/journald.conf
  #Change ForwardToWall=yes to ForwardToWall=no
  systemctl restart systemd-journald
  service nginx start
  ```
- Always verify the connection to the SIEM server using tools like `telnet` or `tcpdump` to diagnose connectivity issues, especially when using UDP.