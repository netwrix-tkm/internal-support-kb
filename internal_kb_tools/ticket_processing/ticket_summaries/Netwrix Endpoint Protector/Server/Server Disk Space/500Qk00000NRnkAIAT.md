## Ticket Metadata
- **Ticket ID:** 500Qk00000NRnkAIAT
- **Case Number:** 440379
- **Status:** Closed - Resolved
- **Account/Company:** Cleerly
- **Contact Name:** Josh Luttrell
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that the system volume was at 73% utilization and they were unable to reduce this usage despite offloading all log archives older than three months. They were also uncertain about safely removing file shadows to free up additional space.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Hosting:** AWS (Amazon Web Services)

## Troubleshooting Steps
1. Requested customer approval to access the backend of the server for cleanup.
2. Cleared the system partition occupied by inodes and journals.
3. Informed the customer that the EPP UI may take 15-20 minutes to reflect the actual disk space after cleanup.
4. Verified the disk space utilization after cleanup.

## Root Cause
The high disk usage was primarily due to the accumulation of inodes and journals within the system partition, which can occur over time as logs and other temporary files are generated.

## Solution
After obtaining customer approval, the support team performed a cleanup of the system partition, specifically targeting inodes and journals. This action successfully reduced the disk usage from 73% to 58%, resolving the issue without deleting any logs or shadows that were necessary for the customer.

## Notes
- It is normal for the system partition to be occupied 40-60% of the time. Alerts may trigger due to log rotation malfunctions or other factors.
- If disk space issues arise again, the customer can contact support for assistance.
- Increasing the size of the system partition would require a new server request and data migration, which is generally not recommended due to the rarity of space issues.