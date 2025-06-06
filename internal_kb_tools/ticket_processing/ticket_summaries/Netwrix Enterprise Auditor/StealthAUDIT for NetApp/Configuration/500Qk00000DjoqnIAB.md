## Ticket Metadata
- **Ticket ID:** 500Qk00000DjoqnIAB
- **Case Number:** 416460
- **Status:** Closed - Resolved
- **Account/Company:** Thales Group Australia
- **Contact Name:** Matthew Heaton-Harris
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported that FSAC jobs were failing with an error indicating that the scan could not be started due to an empty proxy host list or misconfiguration of proxies for the target host.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for NetApp

## Troubleshooting Steps
1. Verified the configuration of the proxy host list.
2. Checked for any blocked communication ports between the proxy server and the NetApp server.
3. Reviewed the credentials used for connection to ensure they had the necessary permissions to log in to the NetApp SVM.
4. Confirmed the status of the remote registry service on the target host.

## Root Cause
The issue was caused by multiple factors:
- Initially, communication ports were blocked between the proxy server and the NetApp server.
- The credentials used for the connection were not authorized to log in to the NetApp SVM.
- The remote registry service was not enabled on the target host.

## Solution
The issue was resolved by:
1. Unblocking the necessary communication ports between the proxy server and the NetApp server.
2. Updating the credentials to ensure they had the appropriate permissions to access the NetApp SVM.
3. Enabling the remote registry service on the target host.

## Notes
- Ensure that communication ports are open and properly configured before initiating scans.
- Always verify that the credentials used for connections have the necessary permissions.
- Check that the remote registry service is enabled on the target host to avoid similar issues in the future.