## Ticket Metadata
- **Ticket ID:** 500Qk00000OplaBIAR
- **Case Number:** 444153
- **Status:** Closed - Resolved
- **Account/Company:** XacBank
- **Contact Name:** Amartur Byambaa
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** 06.05

## Problem Description
The customer reported that their system was running low on disk space, with only 240.88 GB free out of 950.23 GB (approximately 25%). This low disk space was affecting the functionality and performance of the Endpoint Protector (EPP) Server.

## Environment Details
- The issue was related to insufficient hardware resources, specifically disk space on the server hosting the Netwrix Endpoint Protector.

## Troubleshooting Steps
1. Confirmed the low disk space issue reported by the customer.
2. Deleted file shadows older than 120 days.
3. Removed some older system and audit log backups.
4. Advised the customer against using file shadowing for all users/actions to prevent excessive disk space usage.
5. Awaited customer availability for further remote support (RS) sessions.

## Root Cause
The root cause of the issue was identified as insufficient disk space due to the accumulation of file shadows and backups over time, which were not being managed effectively.

## Solution
The issue was resolved by:
- Deleting file shadows older than 120 days.
- Removing some older system and audit log backups to free up disk space.
- Advising the customer on best practices for managing file shadowing to prevent future occurrences of low disk space.

## Notes
- It is important for customers to regularly manage their file shadows and backups to avoid running into disk space issues.
- Customers should be advised to tune their policies to reduce the incoming log count, which can help in managing disk space more effectively in the future.