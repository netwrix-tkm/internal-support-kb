## Ticket Metadata
- **Ticket ID:** 500Qk00000KvpWyIAJ
- **Case Number:** 433159
- **Status:** Closed - Resolved
- **Account/Company:** FcBrasil
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** System & Log Backups
- **Feature:** System Backup
- **Version:** 7.1

## Problem Description
The customer reported that a system backup was stuck at 99%. They required a backend check to resolve the issue and were advised not to use the problematic backup. Instead, they planned to utilize VM or backup v2 while seeking a resolution for the stuck backup.

## Environment Details
- **Backup Type:** System Backup
- **Customer Availability:** January 26th and 27th, 14h BRT

## Troubleshooting Steps
1. Instructed the customer not to use the stuck backup.
2. Recommended using VM or backup v2 as alternatives.
3. Conducted a backend check to identify the cause of the stuck backup.
4. Cleared the stuck status message from the system.

## Root Cause
The issue was caused by a stuck status message within the backup system, which prevented the backup from completing successfully.

## Solution
The issue was resolved by cleaning out the stuck status message, allowing the backup process to resume normal operations.

## Notes
- Ensure that customers are advised to avoid using backups that are reported as stuck.
- It may be beneficial to periodically check the status of backups to prevent similar issues from occurring in the future.
- Consider reviewing external repositories as part of routine maintenance to ensure all backups are functioning correctly.