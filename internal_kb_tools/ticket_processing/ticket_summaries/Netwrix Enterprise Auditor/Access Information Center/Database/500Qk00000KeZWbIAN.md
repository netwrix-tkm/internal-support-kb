## Ticket Metadata
- **Ticket ID:** 500Qk00000KeZWbIAN
- **Case Number:** 432286
- **Status:** Closed - Resolved
- **Account/Company:** Nexidia
- **Contact Name:** Angie Sawyer
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Database
- **Version:** 11.6

## Problem Description
The customer reported being unable to log in to the Access Information Center (AIC) due to an error stating "Unable to use the SQL Server Database provided." This issue arose after multiple database changes were made, including the dropping of several AIC tables.

## Environment Details
- **Database Version:** SQL Server
- **Backup Date:** January 6th, 2025
- **Recent Changes:** Multiple tables were removed as part of a cleanup process.

## Troubleshooting Steps
1. Verified the presence of AIC tables in the database.
2. Restored AIC tables from a backup dated January 6th.
3. Noted the appearance of duplicate entries for resource owners after restoration.
4. Investigated the missing `SA_AIC_AuditEvents` table, which was crucial for AIC functionality.
5. Reviewed logs to confirm successful logins prior to the error reoccurrence.
6. Deleted the `SA_AIC_AuditEvents` table to resolve the login issue.
7. Attempted to restore the table again, which led to the original error reappearing.

## Root Cause
The root cause of the issue was identified as the deletion of the `SA_AIC_AuditEvents` table, which was necessary for the AIC to function correctly. The table was inadvertently dropped during a cleanup process, leading to the inability to log in and subsequent errors regarding null values in the database.

## Solution
The issue was resolved by deleting the problematic `SA_AIC_AuditEvents` table and then logging into the AIC without it. Upon logging in, the AIC created a new instance of the table, allowing the customer to regain access. 

## Notes
- After restoring tables from backup, the customer experienced duplicate entries for resource owners, which were greyed out and could not be removed. This may require further investigation.
- It is crucial to ensure that all necessary tables are retained during database cleanup processes to prevent similar issues in the future.
- Future database changes should be carefully documented, and backups should be verified to ensure critical tables are not lost.