## Ticket Metadata
- **Ticket ID:** 500Qk00000PEyAoIAL
- **Case Number:** 445391
- **Status:** Closed - Resolved
- **Account/Company:** Colegio Oficial de Farmacéuticos de Madrid
- **Contact Name:** Pablo Martin
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Disk Space
- **Version:** Not specified

## Problem Description
The customer reported that their Endpoint Protector appliance was running low on disk space, with only 28.81 GB free out of 257.22 GB (11%). They were advised to use the Audit Log Backup feature to reduce the logs stored in the database, delete older backups, and tune policies to reduce incoming log counts. The customer attempted to free up space in the Audit Log Backup section but was unsuccessful.

## Environment Details
- The appliance was running Netwrix Endpoint Protector.
- The customer had a significant amount of shadow files occupying disk space.

## Troubleshooting Steps
1. Connected remotely to the customer's system to assess the situation.
2. Checked the backend and identified approximately 168 GB of shadow files occupying disk space.
3. Confirmed with the customer that the shadow files had been copied to external storage.
4. Deleted the identified shadow files to free up disk space.
5. Recreated the oshadow and capshadow files accordingly.
6. Tested the functionality on the UI side to ensure everything was working as expected.

## Root Cause
The issue was caused by an accumulation of unnecessary shadow files that were not deleted, leading to a significant reduction in available disk space.

## Solution
The issue was resolved by deleting the 168 GB of unnecessary shadow files. After deletion, the oshadow and capshadow files were recreated, and the system was tested to confirm that it was functioning properly.

## Notes
- It is important to regularly monitor disk space and manage shadow files to prevent similar issues in the future.
- Customers should be advised to utilize external storage options for backups and to routinely delete old backups to maintain optimal disk space usage.