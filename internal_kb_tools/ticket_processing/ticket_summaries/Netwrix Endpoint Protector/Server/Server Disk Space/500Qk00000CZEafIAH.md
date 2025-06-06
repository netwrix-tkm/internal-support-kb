```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CZEafIAH
- **Case Number:** 413745
- **Status:** Closed - Resolved
- **Account/Company:** NHS Hampshire, Isle of Wight and Southampton
- **Contact Name:** Dave Andrews
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported receiving a low disk space warning on their Netwrix Endpoint Protector appliance, which is provisioned on Hyper-V with a dynamically expanding disk of maximum capacity 3TB. The warning indicated that functionality may be severely affected.

## Environment Details
- **Platform:** Hyper-V
- **Disk Type:** Dynamically expanding disk with a maximum capacity of 3TB

## Troubleshooting Steps
1. Acknowledged the issue and initiated an internal investigation.
2. Communicated with the customer to gather availability for a remote session.
3. Scheduled a remote session to extend the disk space from the backend of the server.
4. Conducted the remote session to increase the disk space.

## Root Cause
The low disk space warning was caused by the dynamically expanding disk reaching its maximum capacity, which was not adequately managed or monitored.

## Solution
During the remote session, the disk space of the EPP server was successfully increased, resolving the low disk space warning. The customer was informed that the issue was resolved and the case was closed.

## Notes
- It is important to monitor disk space usage regularly, especially when using dynamically expanding disks, to prevent similar issues in the future.
- Consider converting to a static provisioned disk if consistent disk space issues arise, as this may provide more predictable performance and management.
```