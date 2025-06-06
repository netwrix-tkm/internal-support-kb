## Ticket Metadata
- **Ticket ID:** 500Qk00000GpAljIAF
- **Case Number:** 423395
- **Status:** Closed - Resolved
- **Account/Company:** REIF Bauunternehmung GmbH & Co. KG
- **Contact Name:** Jonas Stöpfel
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** External Storage - FTP/Samba
- **Version:** NONE

## Problem Description
The customer reported that their disk storage was running out of space. They had connected external storage but suspected that old data was not being automatically moved as intended.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **External Storage Type:** FTP/Samba

## Troubleshooting Steps
1. Verified the connection to the external storage.
2. Checked the configuration settings for automated data movement.
3. Reviewed logs for any errors related to data transfer.
4. Attempted to manually clear old data but found it was not effective.
5. Removed shadows older than 90 days.

## Root Cause
The issue was caused by the accumulation of shadow copies that were not being cleared automatically, leading to the depletion of available disk space.

## Solution
The problem was resolved by manually clearing the shadow copies that were older than 90 days. This action freed up significant disk space and allowed the system to function normally.

## Notes
- It is important to regularly monitor and manage shadow copies to prevent similar issues in the future.
- Consider setting up automated tasks for clearing old shadows to maintain optimal storage levels.