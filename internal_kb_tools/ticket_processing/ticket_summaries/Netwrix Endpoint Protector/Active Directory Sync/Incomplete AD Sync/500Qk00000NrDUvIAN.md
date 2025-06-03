## Ticket Metadata
- **Ticket ID:** 500Qk00000NrDUvIAN
- **Case Number:** 441419
- **Status:** Closed - Resolved
- **Account/Company:** Landeshauptstadt Hannover
- **Contact Name:** Lukas Rust
- **Product:** Netwrix Endpoint Protector
- **Component:** Active Directory Sync
- **Feature:** Incomplete AD Sync
- **Version:** NONE

## Problem Description
The customer reported that not all users were being synchronized to the Administrative Group in Netwrix Endpoint Protector, despite being correctly assigned in Active Directory (AD).

## Environment Details
- The issue involved synchronization between Active Directory and Netwrix Endpoint Protector.
- The users in question were part of the same AD groups as those that were successfully imported.

## Troubleshooting Steps
1. Requested confirmation from the customer regarding whether the users not imported were part of the same AD groups as those that were imported.
2. Asked the customer to provide a screenshot of the AD groups showing the users that were imported versus those that were not.
3. Scheduled a remote session with the customer to observe the behavior live.
4. During the remote session, checked the backend of the Endpoint Protector server for any discrepancies.
5. Identified that the administrators who were not synchronized had been previously deleted from the Endpoint Protector server.

## Root Cause
The root cause of the issue was that the administrators who were not being synchronized had been deleted from the Endpoint Protector server, which prevented their import during the synchronization process.

## Solution
The solution involved restoring the deleted administrators from the backend of the Endpoint Protector server. After restoring, the customer performed another synchronization, which successfully imported the administrators, making them visible in the Endpoint Protector UI.

## Notes
- Ensure that a backup or snapshot of the Endpoint Protector appliance is created before making any changes to the backend.
- Future cases involving incomplete AD sync should first check if the users in question have been deleted from the Endpoint Protector server.
- Always confirm that the users are part of the same AD groups before proceeding with deeper troubleshooting.