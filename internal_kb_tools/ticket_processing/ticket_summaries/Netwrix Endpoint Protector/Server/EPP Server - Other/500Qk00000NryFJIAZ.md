## Ticket Metadata
- **Ticket ID:** 500Qk00000NryFJIAZ
- **Case Number:** 441482
- **Status:** Closed - Resolved
- **Account/Company:** Student Transportation of America
- **Contact Name:** James Schmidt
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer, James Schmidt, reported that he was unable to log in to the Netwrix Endpoint Protector (EPP) Console.

## Environment Details
- The EPP server was hosted in the cloud, with the original access URL provided as: `https://qec6p8e.hosted.endpointprotector.com/index.php/`.

## Troubleshooting Steps
1. A remote session was scheduled to assist with resetting the password.
2. Investigation revealed that Active Directory (AD) administrators were unable to sync on the server.
3. It was identified that there were local administrators with the same username as the AD admins.
4. The local admins with conflicting usernames were removed to allow for proper synchronization.

## Root Cause
The issue was caused by the presence of local administrators on the server who had the same usernames as the Active Directory administrators, preventing the AD admins from syncing properly.

## Solution
The issue was resolved by removing the local administrators that had conflicting usernames. Once these accounts were removed, the AD administrators were able to sync successfully, allowing James to log in to the EPP Console.

## Notes
- Ensure that there are no local accounts with the same usernames as AD accounts to prevent similar login issues in the future.
- Regularly verify synchronization between AD and local accounts to avoid conflicts that could lead to authentication issues.