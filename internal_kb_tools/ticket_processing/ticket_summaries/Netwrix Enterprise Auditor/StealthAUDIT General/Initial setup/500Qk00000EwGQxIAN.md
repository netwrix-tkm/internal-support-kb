## Ticket Metadata
- **Ticket ID:** 500Qk00000EwGQxIAN
- **Case Number:** 419108
- **Status:** Closed - Resolved
- **Account/Company:** New York Times
- **Contact Name:** Ted Bagby
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer requested assistance in setting up an end-to-end File Server scan job within the Netwrix Enterprise Auditor.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.5

## Troubleshooting Steps
1. Clarified the customer's definition of "end-to-end File server" through a phone call.
2. Reviewed the File System settings to ensure proper configuration.
3. Added the correct server to the Host List.
4. Identified that the Active Directory Inventory (ADI) group was being pulled from the wrong Domain Controller (DC).
5. Updated the configuration to pull the ADI group from the correct server/DC.
6. Set up a schedule for the File System and ADI job to start automatically.

## Root Cause
The issue was primarily caused by the Active Directory Inventory group being configured to pull data from an incorrect Domain Controller, which prevented the successful setup of the File Server scan job.

## Solution
The issue was resolved by:
- Correctly configuring the File System settings and adding the appropriate server to the Host List.
- Updating the Active Directory Inventory group to pull from the correct Domain Controller.
- Establishing an automatic schedule for the File System and ADI job to ensure it runs as intended.

## Notes
- Ensure that the correct Domain Controller is selected when setting up Active Directory Inventory groups to avoid similar issues in the future.
- Regularly review and verify File System settings to ensure they align with the intended configuration.