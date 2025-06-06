## Ticket Metadata
- **Ticket ID:** 500Qk00000FigkVIAR
- **Case Number:** 420950
- **Status:** Closed - Resolved
- **Account/Company:** Flex
- **Contact Name:** Thiagarajoo Segaran
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** System Backup
- **Version:** Not specified

## Problem Description
The customer reported that their appliance was on critical low disk space, with only 1.5GB remaining. They requested a cleanup to ensure the functionality and performance of the EPP server.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Disk Space Status:** Critical low disk space (1.5GB remaining)

## Troubleshooting Steps
1. Assessed the current disk space usage on the appliance.
2. Identified logs that were queued to be sent to the SIEM (Security Information and Event Management) system.
3. Confirmed that the customer had not been using the SIEM for an extended period.
4. Attempted to clear unnecessary files and logs to free up disk space.

## Root Cause
The issue was caused by an accumulation of logs that were queued for transmission to the SIEM, which had not been utilized by the customer for a long time. This led to the depletion of available disk space.

## Solution
The issue was resolved by removing the queued logs that were no longer needed. This cleanup action successfully freed up disk space, restoring the appliance's functionality and performance.

## Notes
- It is advisable for customers to regularly monitor disk space and perform cleanups to prevent similar issues.
- Customers should be informed about the importance of managing log retention settings, especially if they are not actively using SIEM solutions.