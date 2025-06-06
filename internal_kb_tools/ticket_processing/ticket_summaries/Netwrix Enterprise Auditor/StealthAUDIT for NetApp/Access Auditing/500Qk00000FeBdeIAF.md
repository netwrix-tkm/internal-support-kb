## Ticket Metadata
- **Ticket ID:** 500Qk00000FeBdeIAF
- **Case Number:** 420745
- **Status:** Closed - Resolved
- **Account/Company:** ORIX
- **Contact Name:** Jayne Daulong
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Access Auditing
- **Version:** 11.6

## Problem Description
The customer requested assistance in verifying the files located in the folder `D:FSAADA6PNETAPP1B`, which corresponds to a decommissioned NetApp filer. They were looking to clear up space by potentially deleting this folder.

## Environment Details
- **Location:** United States (Texas)
- **Decommissioned Host:** DA6PNETAPP1B (NetApp filer)

## Troubleshooting Steps
1. Reviewed the status of the NetApp filer to confirm it was decommissioned.
2. Discussed the implications of deleting the folder with the customer.
3. Clarified whether the folder was an alias for any active servers.

## Root Cause
The initial concern was whether the folder could be deleted since it belonged to a decommissioned host. However, it was later discovered that the folder was an alias for an active server, which influenced the decision to retain it.

## Solution
The issue was resolved by confirming that if the host had indeed been decommissioned and would no longer be scanned, it would be acceptable to delete the folder. However, upon further investigation, the customer realized that the folder was an alias for an active server and decided to leave it as is.

## Notes
- Always verify if a folder is an alias for an active server before proceeding with deletion.
- Ensure clear communication with the customer regarding the implications of deleting files or folders associated with decommissioned hosts.