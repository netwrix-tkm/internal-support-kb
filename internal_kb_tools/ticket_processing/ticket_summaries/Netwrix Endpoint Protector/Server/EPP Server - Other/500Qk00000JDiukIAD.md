## Ticket Metadata
- **Ticket ID:** 500Qk00000JDiukIAD
- **Case Number:** 429166
- **Status:** Closed - Resolved
- **Account/Company:** Kassenärztliche Vereinigung Nordrhein
- **Contact Name:** Gerrit Beyken
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that while most admin accounts were successfully imported from Active Directory (AD) into the Netwrix Endpoint Protector (EPP) server, three specific accounts were not imported despite being members of the correct AD group.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Verified the membership of the three problematic accounts in the designated AD group.
2. Checked the synchronization settings and logs on the EPP server to identify any errors or warnings related to the import process.
3. Attempted to manually trigger a synchronization process to see if the accounts would be imported.
4. Reviewed the configuration of the EPP server to ensure it was set up correctly to communicate with the AD.

## Root Cause
The issue was identified as a synchronization problem where the EPP server did not properly sync the three specific admin accounts from the AD, despite their correct group membership.

## Solution
The issue was resolved by performing a manual synchronization of the user accounts. This action successfully imported the previously missing admin accounts into the EPP server.

## Notes
- Ensure that regular synchronization checks are performed to avoid similar issues in the future.
- If specific accounts are not importing, verify their group memberships and check for any synchronization errors in the logs.
- Consider implementing alerts for synchronization failures to proactively address issues before they affect user access.