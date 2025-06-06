## Ticket Metadata
- **Ticket ID:** 500Qk00000GzgQwIAJ
- **Case Number:** 423763
- **Status:** Closed - Resolved
- **Account/Company:** auDA
- **Contact Name:** Natalia Khobotova
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported an issue connecting Netwrix to their SharePoint Online (SPO) environment, receiving "ACCESS DENIED" errors during the connection attempts.

## Environment Details
- The customer does not have an on-premises Active Directory (AD).
- The Netwrix Enterprise Auditor (NEA) is installed on a standalone server that is not domain-joined.

## Troubleshooting Steps
1. Verified the configuration of the client secret for NEA authentication.
2. Created a self-signed certificate for SharePoint jobs.
3. Attempted to run SharePoint bulk import jobs, which failed due to missing database tables.
4. Checked the database using SQL Server Management Studio (SSMS) and confirmed that the required tables were not present.
5. Reviewed the working environment in the lab, where the necessary tables were available.

## Root Cause
The issue was identified as a product defect related to the absence of necessary database tables that should have been created during the Active Directory Import (ADI) job. Without an on-prem AD, these tables were not generated, leading to the "ACCESS DENIED" errors during the connection attempts.

## Solution
The R&D team provided scripts to manually create the missing tables and stored procedures in the SQL database. Once these scripts were executed, the SharePoint bulk import jobs were able to run successfully, resolving the connection issue.

## Notes
- Future customers without an on-prem AD should be informed that manual creation of specific database tables may be necessary to facilitate proper integration with SharePoint Online.
- Consider documenting the provided scripts and the process for creating the necessary tables as part of the knowledge base for similar cases.