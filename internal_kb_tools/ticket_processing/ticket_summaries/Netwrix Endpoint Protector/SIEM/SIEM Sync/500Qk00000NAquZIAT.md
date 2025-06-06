## Ticket Metadata
- **Ticket ID:** 500Qk00000NAquZIAT
- **Case Number:** 439607
- **Status:** Closed - Resolved
- **Account/Company:** PrivatBank
- **Contact Name:** CoreWin Tech
- **Product:** Netwrix Endpoint Protector
- **Component:** SIEM
- **Feature:** SIEM Sync
- **Version:** 3.1

## Problem Description
PrivatBank's SOC team inquired whether it was possible to transfer EPP logs to their SIEM with modified event file names. The issue arose because shadow copies sent to an S3 Bucket were renamed with a hash, making it difficult to correlate the logs with the actual shadow copies.

## Environment Details
- The customer configured an S3 Bucket for shadow copies.
- The EPP server automatically generates a hash for shadow copied files.

## Troubleshooting Steps
1. Confirmed whether the file names were changed on the S3 bucket.
2. Investigated if there were any manual file name changes recorded in the EPP logs.
3. Checked the EPP UI for any File Rename events.
4. Suggested using the SIEM's File Hash field to correlate logs with shadow copy names.

## Root Cause
The EPP server automatically creates a hash sum of the shadow copied files and does not log any manual file name changes. As a result, the logs sent to the SIEM retained the default file names, which did not match the renamed files in the S3 Bucket.

## Solution
The issue was resolved by advising the customer to utilize the File Hash field in their SIEM to correlate the logs with the shadow copy file names stored in the S3 Bucket. The customer confirmed that this approach would work for their needs.

## Notes
- There are no entries for the creation of the hash sum in the EPP logs, meaning these events will not show up as logs.
- Future inquiries regarding file name changes should consider the automatic hashing behavior of the EPP server.