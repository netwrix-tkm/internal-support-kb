## Ticket Metadata
- **Ticket ID:** 500Qk00000OoabxIAB
- **Case Number:** 444100
- **Status:** Closed - Resolved
- **Account/Company:** Ernst & Young USA
- **Contact Name:** Doug Russell
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** N/A
- **Version:** 7.1

## Problem Description
The customer requested a process to daily purge client records that have checked in but are no longer active. They aimed to maintain up-to-date reporting.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Navigate to **Device Control** -> **Computers**.
2. Select **Filters**.
3. Set **Status = Offline** and apply the filter.
4. Rearrange the **Last Seen** column to display the oldest records first.
5. Select the checkbox next to **Computer Name** to select all computers on the current page.
6. At the bottom of the page, select **Delete** to remove the selected records.

## Root Cause
The issue stemmed from the accumulation of stale client records that had not checked in for an extended period, leading to outdated reporting.

## Solution
The problem was resolved by providing the customer with a step-by-step guide to filter and delete offline client records manually. This process allows for regular maintenance of the records, ensuring that only active clients are reported.

## Notes
- It is recommended to perform this purging process regularly to keep the reporting accurate.
- Consider automating this process in the future if the volume of stale records becomes unmanageable.