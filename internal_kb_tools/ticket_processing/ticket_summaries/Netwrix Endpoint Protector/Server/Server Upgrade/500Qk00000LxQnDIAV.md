## Ticket Metadata
- **Ticket ID:** 500Qk00000LxQnDIAV
- **Case Number:** 435998
- **Status:** Closed - Resolved
- **Account/Company:** Nestor Nestor Diculescu Kingston Petersen (NNDKP)
- **Contact Name:** Cristian Nastase
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer requested guidance on the procedure for migrating from a virtual appliance based on Ubuntu 14.04 LTS, which is End of Life (EOL), to a new virtual appliance based on Ubuntu 22.04 LTS.

## Environment Details
- **Old Server OS:** Ubuntu 14.04 LTS
- **New Server OS:** Ubuntu 22.04 LTS
- **Backup Method:** SQL import

## Troubleshooting Steps
1. Conducted a remote session with the client.
2. Created a backup copy from the old server through the backend.
3. Successfully imported the backup onto the new server.
4. Verified that users, computers, and server maintenance settings were intact on the new server.
5. Asked the client to monitor the new server for any issues.

## Root Cause
The issue stemmed from the need to migrate from an outdated operating system (Ubuntu 14.04 LTS) to a supported version (Ubuntu 22.04 LTS). The migration process required careful handling of backups to ensure data integrity and system functionality.

## Solution
The issue was resolved by:
- Performing a backup of the old server.
- Importing the backup into the new server using SQL.
- Confirming that all necessary configurations and data were correctly migrated and functional on the new server.

The client confirmed that the migration was successful and that everything was working as expected.

## Notes
- Ensure that clients are aware of the EOL status of their operating systems to avoid similar migration issues in the future.
- It is advisable to monitor the new server post-migration for any unforeseen issues.
- Future migrations should consider the size of the backup to avoid errors such as "Request Entity Too Large" during the import process.