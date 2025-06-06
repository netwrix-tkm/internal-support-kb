## Ticket Metadata
- **Ticket ID:** 500Qk00000KjcbuIAB
- **Case Number:** 432579
- **Status:** Closed - Resolved
- **Account/Company:** Stanford University
- **Contact Name:** Spencer Chinn
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported receiving an alert indicating that their system was running low on disk space, despite system information showing available space. They expressed concern about potential performance impacts on their production system.

## Environment Details
- **Disk Space System:** 8.8G - 19% from 50G
- **Disk Space EPP Server:** 155G - 64% from 258G
- **Logs on Disk:** 4.0K
- **Shadows on Disk:** 8.0K

## Troubleshooting Steps
1. Reviewed the alert message indicating low disk space.
2. Verified the disk space usage on the system and EPP server.
3. Suggested cleaning up database backups.
4. Provided instructions on setting up audit log backups.

## Root Cause
The alert was triggered due to the accumulation of logs and backups, which consumed significant disk space, leading to a discrepancy between the reported available space and the actual usage impacting system performance.

## Solution
The issue was resolved by:
- Cleaning up some database backups to free up disk space.
- Setting up audit log backups to manage log retention and prevent future alerts regarding low disk space.

## Notes
- It is important to regularly monitor disk space usage and perform maintenance on backups and logs to avoid similar issues.
- Customers should be advised to tune their policies to reduce incoming log counts, which can help manage disk space more effectively.