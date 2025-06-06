## Ticket Metadata
- **Ticket ID:** 500Qk00000KYiCpIAL
- **Case Number:** 431916
- **Status:** Closed - Resolved
- **Account/Company:** Northern Bank & Trust Company
- **Contact Name:** Sean Oliver
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that the Netwrix Enterprise Auditor was unable to connect to SharePoint, despite having a valid key. The error messages indicated issues with negotiating a connection to the SharePoint farm and server.

## Environment Details
- SharePoint URL: [nbtc0.sharepoint.com](https://nbtc0.sharepoint.com)
- Connection attempts were made using PowerShell to test connectivity.

## Troubleshooting Steps
1. Verified the validity of the connection key.
2. Attempted to connect to SharePoint using PowerShell command:
   ```powershell
   test-netconnection nbtc0.sharepoint.com -port 443
   ```
   This confirmed that a TCP connection could be established.
3. Configured a new connection profile for SharePoint.
4. Manually provisioned all required SharePoint online permissions as per the documentation.
5. Added the Azure hostname to a newly created host list.
6. Assigned the same host and connection profile settings to all child objects.
7. Successfully executed a job for a one-level scan.

## Root Cause
The issue was caused by the absence of a properly configured connection profile and the lack of necessary permissions for the Azure account to access SharePoint.

## Solution
The issue was resolved by:
- Creating and configuring a new connection profile.
- Manually provisioning the Azure account with all required permissions as detailed in the Netwrix documentation.
- Adding the Azure hostname to a host list and ensuring all child objects inherited the correct settings.
- Successfully running the SharePoint scan job after these configurations.

## Notes
- Ensure that all necessary permissions are provisioned for Azure accounts when configuring connections to SharePoint.
- Regularly review and update connection profiles to prevent similar issues in the future.