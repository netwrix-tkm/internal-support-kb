## Ticket Metadata
- **Ticket ID:** 500Qk00000FfdrEIAR
- **Case Number:** 420824
- **Status:** Closed - Resolved
- **Account/Company:** CoreWin Distributor
- **Contact Name:** Danylo Didenko
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer, PrivatBank, reported an issue with EPP licensing where updating the Linux client from version 2.4.2.1 to 2.4.3.1 resulted in the creation of duplicate clients in the console. The new client appeared unlicensed and lacked information, while the license remained attached to the previous version.

## Environment Details
- **Client Versions:** 2.4.2.1 and 2.4.3.1
- **Operating System:** Linux

## Troubleshooting Steps
1. Verified the client version before and after the update.
2. Checked the EPP console for duplicate client entries.
3. Observed the licensing status of both the old and new clients.
4. Attempted to release the license from the old client to see if it would attach to the new client.
5. Reviewed screenshots provided by the customer to confirm the issue.

## Root Cause
The issue was caused by the lack of available licenses when the client was updated. The new client was created as a duplicate in the console because the license was still attached to the previous version, preventing proper communication with the EPP server.

## Solution
The issue was resolved when the customer received additional licenses. This allowed the new client to properly attach to a license and communicate with the EPP server, eliminating the duplication issue. The ticket was temporarily closed until the issue could potentially reoccur.

## Notes
- Ensure that clients have sufficient licenses before performing updates to avoid duplication issues.
- Monitor the licensing status after updates to prevent similar occurrences in the future.