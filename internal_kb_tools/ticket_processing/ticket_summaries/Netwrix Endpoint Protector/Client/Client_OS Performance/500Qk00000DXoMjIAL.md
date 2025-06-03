## Ticket Metadata
- **Ticket ID:** 500Qk00000DXoMjIAL
- **Case Number:** 416100
- **Status:** Closed - Resolved
- **Account/Company:** Haleon
- **Contact Name:** Matthew Corner
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** Not specified

## Problem Description
A colleague reported a significant decrease in file transfer speed while transferring a large number of files to USB storage. This issue arose after receiving a pop-up alert indicating that they had hit the daily file transfer limit, which is set to monitor-only mode.

## Environment Details
- The issue occurred on a system using Netwrix Endpoint Protector.
- The specific logs from the Endpoint Protector (EPP) were to be provided for further analysis.

## Troubleshooting Steps
1. Reviewed the pop-up alert indicating the daily file transfer limit was reached.
2. Analyzed the file transfer speed before and after the alert was received.
3. Investigated the EPP logs for any related entries that could indicate throttling or restrictions.
4. Attempted to identify any settings related to file transfer limits within the Endpoint Protector configuration.

## Root Cause
The root cause of the issue was identified as the file transfer threshold settings within the Netwrix Endpoint Protector, which were inadvertently limiting the transfer speed after the daily limit was reached.

## Solution
The issue was resolved by disabling the file transfer threshold settings in the Netwrix Endpoint Protector. This action allowed the colleague to resume normal file transfer speeds without restrictions.

## Notes
- It is important to monitor file transfer settings to prevent unintentional throttling, especially during large file transfers.
- Future users should be aware of the daily file transfer limits and consider adjusting these settings if frequent large transfers are necessary.