## Ticket Metadata
- **Ticket ID:** 500Qk00000OJESrIAP
- **Case Number:** 442701
- **Status:** Closed - Resolved
- **Account/Company:** Clootrack
- **Contact Name:** Ramesh B
- **Product:** Netwrix Endpoint Protector
- **Component:** Server Disk Space
- **Feature:** Server Disk Space
- **Version:** 22.04

## Problem Description
The customer reported that their appliance was running low on disk space, with only 17.07 GB free out of 139.11 GB (12%). This low disk space was affecting the functionality and performance of the EPP Server.

## Environment Details
- The server is hosted by Netwrix.
- The customer had over 30 million logs, with approximately 10 million logs from unidentified file types.

## Troubleshooting Steps
1. Obtained customer approval to access the backend and clear logs.
2. Cleared space from old backups.
3. Disabled file tracing and file shadowing as per customer consent.
4. Removed unnecessary options from Content Aware Protection (CAP) policies.
5. Scheduled an audit log backup to run every two weeks.
6. Advised the customer to run an audit log backup to further free up space and review their monitoring needs.

## Root Cause
The primary cause of the disk space issue was the accumulation of over 30 million logs, with a significant portion (10 million) related to unidentified file types. This excessive logging was not managed effectively, leading to insufficient disk space.

## Solution
The issue was resolved by:
- Clearing old backups and shadows to free up disk space.
- Optimizing CAP policies to reduce unnecessary logging.
- Scheduling regular audit log backups to maintain disk space.
- Providing guidance to the customer on managing their logging policies to prevent future occurrences.

## Notes
- It is recommended that the customer regularly monitor their log generation and adjust their logging policies to avoid similar disk space issues in the future.
- Consider implementing automated log management solutions to help manage log retention and deletion effectively.