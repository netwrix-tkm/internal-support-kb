## Ticket Metadata
- **Ticket ID:** 500Qk00000HDSPjIAP
- **Case Number:** 424439
- **Status:** Closed - Resolved
- **Account/Company:** El Aguila Compania de Seguros
- **Contact Name:** Aaron Soto
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** Not specified

## Problem Description
The customer reported issues with offline and unlicensed computers appearing in the Netwrix Endpoint Protector console. Despite attempts to delete these entries, they reappeared shortly after, indicating that the deletion process was ineffective.

## Environment Details
- The issue involves the use of the Active Directory (AD) Sync feature, which may be contributing to the persistence of the offline and unlicensed computers in the console.

## Troubleshooting Steps
1. Verified the list of computers in the console to identify offline and unlicensed entries.
2. Attempted to delete the identified computers from the console.
3. Monitored the console after deletion to confirm if the computers reappeared.
4. Suggested checking the status of the computers in Active Directory to determine if they were still active.

## Root Cause
The root cause of the issue was identified as the Active Directory Sync feature. The computers that were being deleted were still active in Active Directory, which caused them to reappear in the Netwrix Endpoint Protector console after deletion.

## Solution
The resolution involved advising the customer to check the status of the computers in Active Directory. If the computers were still active in AD, they would need to be removed or deactivated there to prevent them from reappearing in the Netwrix Endpoint Protector console after deletion.

## Notes
- Ensure that any computers intended for deletion are also inactive in Active Directory to avoid reappearance in the console.
- Regularly review the synchronization settings and the status of devices in Active Directory to maintain an accurate list in the Netwrix Endpoint Protector console.