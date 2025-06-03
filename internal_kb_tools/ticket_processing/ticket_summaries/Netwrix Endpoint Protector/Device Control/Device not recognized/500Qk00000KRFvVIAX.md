## Ticket Metadata
- **Ticket ID:** 500Qk00000KRFvVIAX
- **Case Number:** 431663
- **Status:** Closed - Resolved
- **Account/Company:** Dixon Advisory
- **Contact Name:** Nicolaas Coertze
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** 6.2.3.10 (initially reported version)

## Problem Description
The customer reported that multiple devices with the Netwrix client installed were not recognized by the server when searched. Despite attempts to reinstall the client, the devices remained unavailable or took an excessively long time to connect.

## Environment Details
- Initial client version: 6.2.3.10
- Downgraded client version: 5.5.1.6
- Latest client version installed for resolution: 6.2.3.1

## Troubleshooting Steps
1. Attempted to reinstall the client on affected devices.
2. Removed the new client version (6.2.3.10) and installed the old version (5.5.1.6) on affected devices.
3. Verified that affected devices came online and connected to the server after downgrading.
4. Upgraded affected devices from the old client (5.5.1.6) back to the new version (6.2.3.10), which resulted in a broken connection.
5. Upgraded unaffected devices from the old client to the new version, which was successful.
6. Connected to the computer, uninstalled the client (5.5.1.6) with the "Box Remove database and Logs" option selected, and restarted the computer.
7. Installed the latest version (6.2.3.1), which successfully established communication with the server.

## Root Cause
The root cause of the issue was not definitively identified. However, it was observed that the newer client version (6.2.3.10) caused connectivity issues on certain devices, while the older version (5.5.1.6) allowed for successful connections.

## Solution
The issue was resolved by performing the following steps:
1. Uninstalling the problematic client version (5.5.1.6) using the "Box Remove database and Logs" option.
2. Restarting the affected computer.
3. Installing the latest client version (6.2.3.1), which restored communication with the server.

## Notes
- Future installations of the client should be monitored closely, especially when upgrading from older versions to newer ones, as compatibility issues may arise.
- Consider scheduling remote sessions during overlapping business hours to facilitate troubleshooting, especially when dealing with time zone differences.