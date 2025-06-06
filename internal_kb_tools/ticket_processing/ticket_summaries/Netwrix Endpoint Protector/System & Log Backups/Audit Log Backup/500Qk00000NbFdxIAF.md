## Ticket Metadata
- **Ticket ID:** 500Qk00000NbFdxIAF
- **Case Number:** 440697
- **Status:** Closed - Resolved
- **Account/Company:** Ventura Pranas
- **Contact Name:** Thanushree N
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** Audit Log Backup
- **Version:** Not specified

## Problem Description
The customer reported an error related to log backups, which was accompanied by a screenshot indicating the issue. The system was experiencing high usage of the `/var/eppfiles` partition due to excessive shadow files and mailer backups.

## Environment Details
- The backend showed 19 GB in shadow files and 4.5 GB in the mailer.
- A snapshot of the VM was performed on April 3, 2025.

## Troubleshooting Steps
1. Connected to the backend to assess the storage usage.
2. Identified that the `/var/eppfiles` partition was using 25% of its capacity.
3. Deleted shadow files, some backups, and the mailer to free up space.
4. Scheduled a follow-up session to continue the cleanup process.

## Root Cause
The issue was caused by an accumulation of shadow files and mailer backups, which led to excessive usage of the `/var/eppfiles` partition. This was exacerbated by the recent snapshot of the VM, which likely retained additional data.

## Solution
The issue was resolved by:
- Deleting the unnecessary shadow files and mailer backups.
- After cleanup, the usage of the `/var/eppfiles` partition was reduced to 25%, which alleviated the error reported by the customer.

## Notes
- It is important to regularly monitor the storage usage of the `/var/eppfiles` partition to prevent similar issues in the future.
- Consider implementing automated cleanup processes for shadow files and mailer backups to maintain optimal performance and storage efficiency.