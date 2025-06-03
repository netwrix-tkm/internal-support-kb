## Ticket Metadata
- **Ticket ID:** 500Qk00000DBsLnIAL
- **Case Number:** 415281
- **Status:** Closed - Resolved
- **Account/Company:** Florida Lottery
- **Contact Name:** Anthony Davis
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** Not specified

## Problem Description
The customer reported that after renewing and applying their license for Endpoint Protector, devices were not being recognized by the system. The devices appeared offline, and the last seen date did not update.

## Environment Details
- The issue occurred after a year without a license renewal.
- The configuration file for Nginx was initially set up for port separation, which was not applicable in this case.

## Troubleshooting Steps
1. Verified the license was successfully applied.
2. Checked the configuration of the `epp.nginx.conf` file for proper settings.
3. Attempted to connect EPP clients to the server.
4. Regenerated the server certificate stack and rebooted the server.
5. Reviewed logs for any errors related to client-server communication.
6. Conducted remote sessions to diagnose the issue further.

## Root Cause
The root cause of the issue was identified as a misconfiguration in the `epp.nginx.conf` file, which was set for port separation despite the customer not having that setup. This led to the EPP clients being unable to connect to the server.

## Solution
The issue was resolved by changing the `epp.nginx.conf` file from port separation to a normal configuration. After this change, the EPP clients successfully connected to the server, and their status updated accordingly.

## Notes
- Ensure that the configuration files are correctly set up according to the customer's environment to avoid similar issues in the future.
- Always verify whether port separation is required before applying configurations related to it.
- Document any changes made to configuration files and maintain backups for rollback if necessary.