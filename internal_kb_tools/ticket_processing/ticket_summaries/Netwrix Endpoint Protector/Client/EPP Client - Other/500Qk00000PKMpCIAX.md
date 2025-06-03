## Ticket Metadata
- **Ticket ID:** 500Qk00000PKMpCIAX
- **Case Number:** 445555
- **Status:** Closed - Resolved
- **Account/Company:** Mordor Intelligence Pvt. Ltd.
- **Contact Name:** mohammad.azam Azam
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** 6.2.4.2

## Problem Description
After updating the Netwrix Endpoint Protector client from version 6.0.1.6 to 6.2.4.1, several laptops displayed a black screen upon user login following a failed update.

## Environment Details
- **Operating System:** Windows 11
- **Affected Devices:** Initially 6 laptops reported the issue.

## Troubleshooting Steps
1. Gathered initial details from the customer regarding the issue.
2. Confirmed the upgrade method (EPP and Intune) and client versions.
3. Asked the customer what occurs after the black screen.
4. Requested a remote session to test the latest client.
5. Provided the customer with an offline patch for the new client (6.2.4.2).
6. Instructed the customer to film the laptop behavior after the black screen.
7. Followed up on the installation of the 6.2.4.2 client and whether the black screen issue persisted.
8. Suggested testing with the release candidate for version 5.9.4.3.
9. Advised the customer to delete old upgrade jobs and create new ones after a failed installation.

## Root Cause
The black screen issue was identified as a result of the failed update to client version 6.2.4.1, which caused instability in the system.

## Solution
The issue was resolved by successfully installing the offline patch for the client version 6.2.4.2. The customer confirmed that the black screen issue no longer occurred after this installation.

## Notes
- Ensure to monitor the installation process closely when upgrading clients to avoid similar issues.
- Advise customers to keep a backup of their current client version before proceeding with updates.
- If issues arise post-update, consider rolling back to a previous stable version before applying the latest updates.