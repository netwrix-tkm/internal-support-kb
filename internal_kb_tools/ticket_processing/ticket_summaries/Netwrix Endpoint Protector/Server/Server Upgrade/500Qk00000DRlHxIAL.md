## Ticket Metadata
- **Ticket ID:** 500Qk00000DRlHxIAL
- **Case Number:** 415811
- **Status:** Closed - Resolved
- **Account/Company:** Arista Networks, Inc.
- **Contact Name:** Bharani M
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** N/A

## Problem Description
The customer, Arista Networks, Inc., reported the need to migrate from Ubuntu 18, which is End of Life (EoL), to Ubuntu 22.04. They requested assistance for a scheduled call to perform the migration and transfer the database.

## Environment Details
- Current Operating System: Ubuntu 18 (EoL)
- Target Operating System: Ubuntu 22.04
- Product in Use: Netwrix Endpoint Protector

## Troubleshooting Steps
1. Confirmed the current operating system version and its EoL status.
2. Discussed the migration requirements with the customer.
3. Scheduled a call for the migration process.
4. Utilized sysbackup v2 for the migration and database transfer.

## Root Cause
The issue stemmed from the use of an outdated operating system (Ubuntu 18), which is no longer supported, necessitating an upgrade to ensure continued security and functionality.

## Solution
The migration was successfully executed using sysbackup v2, which facilitated the transfer of the database to the new server running Ubuntu 22.04. The process was completed during the scheduled call with the customer.

## Notes
- Ensure to verify the operating system support status before planning upgrades.
- Recommend scheduling migration calls well in advance to accommodate customer availability.
- Future migrations should consider using sysbackup v2 or similar tools for efficiency.