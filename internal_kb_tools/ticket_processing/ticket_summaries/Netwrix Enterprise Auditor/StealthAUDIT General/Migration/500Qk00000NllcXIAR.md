## Ticket Metadata
- **Ticket ID:** 500Qk00000NllcXIAR
- **Case Number:** 441125
- **Status:** Closed - Resolved
- **Account/Company:** GroupM
- **Contact Name:** Vinay Singh
- **Product:** Netwrix Enterprise Auditor
- **Component:** Database Migration
- **Feature:** Migration
- **Version:** 11.6

## Problem Description
The customer requested assistance with the migration of the Netwrix Enterprise Auditor (NEA) 11.6 database to a new SQL server. After confirming the successful restoration of the NEA database, an error occurred when attempting to change the storage profile in the Enterprise Auditor console, stating "remote server refused connection."

## Environment Details
- New SQL Server configured to accept connections on port 1433.
- Original StealthAudit database was in read-only mode during the migration process.

## Troubleshooting Steps
1. Confirmed SQL server settings with the DBA team to ensure it was configured to accept connections on port 1433.
2. Executed `Test-NetConnection` command from the Enterprise Auditor server to the new SQL server on port 1433, which was successful.
3. Created a .udl file to test the connection to the SQL server directly, which resulted in the same connection error and an SSL/TLS connection issue.
4. Successfully connected to the old SQL server using the .udl file.
5. Attempted to disable TLS 1.0 and TLS 1.1 on the Enterprise Auditor server, but the connection error persisted.
6. Installed OleDB 18 Provider on the Netwrix Enterprise Auditor server.
7. Tested the connection via the Enterprise Auditor console, which was successful but failed to retrieve the list of databases due to missing `VIEW ANY DEFINITION` permission on the 'master' database.
8. Provided the `VIEW ANY DEFINITION` permission for the `ad_wwgrm.stb_ai` account.
9. Successfully connected to the new SQL server and retrieved the list of databases after granting the necessary permissions.
10. Updated the storage profile for the Netwrix Access Analyzer (Enterprise Auditor) and confirmed a successful connection to Published Reports.
11. Updated certificate binding for port 481 (AIC service port) using the latest certificate to secure the Access Information Center (AIC) web page.
12. Uninstalled and reinstalled AIC version 11.6.0.37, providing connection information for the new SQL database during installation.
13. Switched the database connection format from UPN to NetBIOS name format for successful connection.
14. Increased the SQL server timeout to allow the AIC to finalize the indexing script against the new SQL database.

## Root Cause
The initial connection issues were caused by a combination of blocked SQL server ports, SSL/TLS configuration issues, and insufficient permissions for the user account attempting to access the new SQL server.

## Solution
The issue was resolved by:
- Installing the correct OleDB provider.
- Granting the necessary permissions to the user account.
- Updating the AIC configuration to use the correct database connection format and ensuring the correct certificate binding was applied.
- Increasing the SQL server timeout to allow the indexing script to complete successfully.

## Notes
- Ensure that the SQL server is configured to accept connections on the appropriate ports and that necessary permissions are granted to user accounts before migration.
- Always verify SSL/TLS settings and connection formats when migrating databases to avoid similar issues in the future.
- Follow up with the customer after migration to confirm that the new SQL database is functioning correctly and that the old SQL server can be decommissioned.