## Ticket Metadata
- **Ticket ID:** 500Qk00000CbnhCIAR
- **Case Number:** 413868
- **Status:** Closed - Resolved
- **Account/Company:** Queensland Treasury
- **Contact Name:** Finn Ruth-Duffy
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The Queensland Treasury was planning a V2 Backup and Migration from an older server model to a newer one, along with an upgrade from version 9.6.1 to 9.6.3, including a hotfix. They requested support for the migration process scheduled for July 10th or 11th, 2024, at 1900 AEST.

## Environment Details
- **Old Server Version:** 9.6.1
- **New Server Version:** 9.6.3 (to be upgraded)
- **Trial License:** The new server was operating under a trial license during the setup.

## Troubleshooting Steps
1. Confirmed the scheduled migration date and time with the customer.
2. Provided guidance on the necessary steps for the migration process.
3. Assisted in setting up the new server, including creating admin accounts.
4. Investigated the issue of the new server not displaying the library of uploaded patches.
5. Suggested that the server needed internet access to receive a server ID for updates.
6. Clarified that a live update might be required to access the offline patch library.

## Root Cause
The new server was not displaying the library of uploaded patches due to it being under a trial license and lacking internet access to receive a server ID. This prevented the server from accessing the necessary updates.

## Solution
The issue was resolved by confirming that the new server needed to be online temporarily to receive a server ID. Once the server was online, it could access the necessary updates, including the offline patch library. The support engineer provided the required port (port 80) and address (https://liveupdate.endpointprotector.com) for the live update function.

## Notes
- Ensure that the server has internet access during the initial setup to receive updates and server IDs.
- If using a trial license, be aware that certain functionalities may be limited.
- It is important to verify that both servers are on the same UI version before migration to avoid compatibility issues.