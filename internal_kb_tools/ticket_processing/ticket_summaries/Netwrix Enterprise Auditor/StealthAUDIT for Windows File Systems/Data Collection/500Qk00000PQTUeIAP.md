## Ticket Metadata
- **Ticket ID:** 500Qk00000PQTUeIAP
- **Case Number:** 445870
- **Status:** Closed - Resolved
- **Account/Company:** Hawaii Pacific Health
- **Contact Name:** Steven Schiesl
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 12.0

## Problem Description
A substantial number of deleted files and folders were not being accurately reflected in the database, with entries displaying NULL values instead of marking the deleted items as such.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector:** StealthAUDIT for Windows File Systems
- **Product Version:** 12.0

## Troubleshooting Steps
1. Used StealthAUDIT for Windows File Systems version 12.0 within the Netwrix Enterprise Auditor platform.
2. Deleted a substantial number of files and folders from the monitored file system.
3. Checked the database entries for the deleted files and folders.
4. Observed that the database displayed NULL values for the entries and did not mark the files and folders as deleted.

## Root Cause
The issue was identified as a temporary glitch in the data collection process, which resulted in the database not updating correctly to reflect the deletions.

## Solution
The issue was resolved by restarting the scans within the Netwrix Enterprise Auditor platform, which allowed the database to refresh and correctly update the status of the deleted files and folders.

## Notes
- It is advisable to periodically restart scans if similar issues arise to ensure that the database reflects the most current state of the monitored file system.
- Users should monitor the database entries after significant deletions to confirm that the data is being updated correctly.