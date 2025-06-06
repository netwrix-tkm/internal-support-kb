```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000NLZrxIAH
- **Case Number:** 440018
- **Status:** Closed - Resolved
- **Account/Company:** E-Data Teknoloji Pazarlama
- **Contact Name:** Yunus ICIN
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer requested assistance in separating the communication ports for the console and client connections in the Netwrix Endpoint Protector. They wanted to use port 443 for console access while configuring a different port for client-server communication.

## Environment Details
- The issue was related to the configuration of the Netwrix Endpoint Protector appliance.
- The customer was using a virtualization environment (VMWare, HyperV, AWS, Azure, GoogleCloud).

## Troubleshooting Steps
1. Connected remotely with the customer to change the IP port settings.
2. Initially encountered issues during testing.
3. Accessed the `/etc/sysctl.conf` file and added the following line:
   ```bash
   net.ipv4.ip_nonlocal_bind = 1
   ```
4. Retested the connection after making the configuration change.

## Root Cause
The initial inability to separate the ports was due to the default system settings that did not allow binding to non-local addresses. The configuration in `sysctl.conf` needed to be adjusted to enable this functionality.

## Solution
The issue was resolved by:
- Modifying the `sysctl.conf` file to include `net.ipv4.ip_nonlocal_bind = 1`.
- Successfully changing the port for client communication to 8443 while retaining port 443 for console access.
- Confirming that the client could connect successfully after the changes were made.

## Notes
- Ensure that a snapshot of the Endpoint Protector appliance is taken before making significant changes to the configuration. This serves as a backup to revert to the original settings if needed.
- Always verify SSH access and have necessary tools (e.g., Putty, Zoom) ready for remote sessions to facilitate troubleshooting.
- Future requests for port changes should follow a similar procedure, ensuring that the `sysctl.conf` settings are reviewed and adjusted as necessary.
```