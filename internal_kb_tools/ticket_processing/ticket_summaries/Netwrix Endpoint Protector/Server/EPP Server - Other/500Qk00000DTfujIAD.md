```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000DTfujIAD
- **Case Number:** 415896
- **Status:** Closed - Resolved
- **Account/Company:** Booking.com
- **Contact Name:** Serhat Demir
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server
- **Feature:** Automatic License Release
- **Version:** Not specified

## Problem Description
The customer reported that the Automatic Release License feature was not functioning as expected. Endpoints that had not been online for over 90 days still retained licenses, leading to discrepancies in license status displayed in the Device Control -> Computers section.

## Environment Details
- The issue was observed on multiple endpoints within the Netwrix Endpoint Protector environment.
- The Automatic Release License feature was enabled.

## Troubleshooting Steps
1. Confirmed the Automatic Release License feature was enabled.
2. Collected logs from the license release job during remote sessions.
3. Reviewed the database entries for the affected computers to check their license status.
4. Ran SQL queries to update the license status for computers incorrectly marked as licensed.
5. Conducted multiple remote sessions with the customer to gather additional data and logs.

## Root Cause
The root cause was identified as a failure in the automatic license release script, which did not properly update the license status for certain endpoints. This was due to a flag in the database (`trialversion` from the `clientmachine` table) not being set correctly for machines that should have been marked as unlicensed.

## Solution
The issue was resolved by executing a specific SQL query that updated the `trialversion` flag for the affected computers, ensuring that their license status was accurately reflected in the system. This query was run during a remote session with the customer, and the license status was confirmed to be updated correctly afterward.

## Notes
- It is important to monitor the automatic license release process regularly to ensure it functions as intended.
- Customers should be informed that manual intervention may be necessary if the automatic process fails, and a workaround (SQL query) can be provided to correct the license status.
- Future updates to the software may address the underlying issues with the automatic release process, so keep an eye on release notes for improvements.
```