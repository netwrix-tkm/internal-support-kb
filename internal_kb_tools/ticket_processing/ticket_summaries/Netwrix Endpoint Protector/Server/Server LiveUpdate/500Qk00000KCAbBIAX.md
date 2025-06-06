## Ticket Metadata
- **Ticket ID:** 500Qk00000KCAbBIAX
- **Case Number:** 431128
- **Status:** Closed - Resolved
- **Account/Company:** Quad Graphics
- **Contact Name:** Jacob Edwards
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server LiveUpdate
- **Version:** 5.9.4.1

## Problem Description
The customer encountered an issue while attempting to update the EPP Server, initially receiving ERROR 5 (checksum) and subsequently ERROR 2 (maximum retries). They required assistance to diagnose the problem further.

## Environment Details
- The update was attempted during a period when the update was not available for download.

## Troubleshooting Steps
1. Reviewed the error messages received during the update process (ERROR 5 and ERROR 2).
2. Confirmed that the update was attempted when it was not available for download.
3. Investigated backend configurations related to the update process.
4. Removed the problematic patch from the database, specifically from the `syscommands` and `live_update` tables.

## Root Cause
The issue was caused by the customer attempting to update the EPP Server during a time when the update was not available for download, leading to checksum errors and maximum retries.

## Solution
The issue was resolved by removing the patch from the backend database, specifically from the `syscommands` and `live_update` tables. This action allowed the customer to successfully update the server afterward.

## Notes
- Ensure that customers are informed about the availability of updates before attempting to install them to avoid similar issues in the future.
- Monitor the backend database for any residual issues related to updates to prevent recurrence of similar errors.