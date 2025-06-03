## Ticket Metadata
- **Ticket ID:** 500Qk00000MUjpSIAT
- **Case Number:** 437507
- **Status:** Closed - Resolved
- **Account/Company:** Oyster Bay Systems
- **Contact Name:** Andrew Temple
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2.4.2000 (client), 5.9.4.1 (server)

## Problem Description
After upgrading a client to version 6.2.4.2000, it was not reporting correctly. The client did not show the new version installed, and attempts to reinstall the agent were unsuccessful.

## Environment Details
- **Server Version:** 5.9.4.1
- **Client Version:** 6.2.4.2
- **Operating System:** Windows Server 2016
- **Security Software:** Eset Server Security (whitelisted EPP processes)
- **Firewall:** Communication ports opened

## Troubleshooting Steps
1. Verified the server and client versions.
2. Attempted to reinstall the client after removing it.
3. Used the ZAP tool to completely uninstall the client.
4. Stopped Eset Server Security to rule out interference.
5. Checked firewall settings to ensure communication was allowed.
6. Re-registered clients in the server console.
7. Analyzed logs and found the error: 
   ```
   ConnectedDevices request failed. cURL error is: 58, schannel: Failed to import cert file (memory blob), password is bad, proxy: false [CSoapClient::SendRequest SoapClient.cpp:339]
   ```
8. Reviewed the `options.ini` file and found it contained the wrong certificate path.

## Root Cause
The issue was caused by the incompatibility of the client with Windows Server 2016, which is no longer supported by the latest client versions. The server was missing necessary patches that caused the client to fail to connect properly.

## Solution
The customer was advised to revert to the previous client version (6.2.3.1010), which worked correctly. Additionally, it was communicated that support for Windows Server 2016 has been discontinued, and the customer may need to upgrade their operating system to continue using newer client versions.

## Notes
- Customers using Windows Server 2016 should be informed that they need to upgrade their OS to use builds from patch 5.9.4.1 and up.
- The product documentation will be updated to reflect the discontinuation of support for Windows Server 2016.
- Customers should continue using EPP Client version 5.9.4.0 for compatibility with older Windows versions.