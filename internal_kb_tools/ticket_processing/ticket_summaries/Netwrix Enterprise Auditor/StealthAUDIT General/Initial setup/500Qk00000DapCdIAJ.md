## Ticket Metadata
- **Ticket ID:** 500Qk00000DapCdIAJ
- **Case Number:** 416237
- **Status:** Closed - Resolved
- **Account/Company:** City of Norman
- **Contact Name:** Jeremy Kilgore
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer inquired whether they could use the same SQL Server and application server for Netwrix Enterprise Auditor (NEA) that they currently use for Netwrix Activity Monitor (NAM).

## Environment Details
- **Netwrix Activity Monitor (NAM)**: Currently in use.
- **Netwrix Enterprise Auditor (NEA)**: Version 11.6.

## Troubleshooting Steps
1. Reviewed the architecture and requirements for both Netwrix Activity Monitor and Netwrix Enterprise Auditor.
2. Consulted the official documentation regarding SQL Server requirements for Netwrix Enterprise Auditor.
3. Provided guidance on best practices for server configurations.

## Root Cause
The root cause of the inquiry was a misunderstanding regarding the database storage components of Netwrix Activity Monitor and Netwrix Enterprise Auditor. It was noted that NAM does not have a database storage component, while NEA requires its own SQL Server instance for optimal performance and data integrity.

## Solution
It was recommended that the customer should not use the same SQL Server instance for both Netwrix Activity Monitor and Netwrix Enterprise Auditor. Instead, they should set up a dedicated SQL Server instance for Netwrix Enterprise Auditor to ensure proper functionality and performance. The following documentation was referenced for further guidance:
- [Netwrix Enterprise Auditor v11.6 SQL Server Requirements](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Requirements/Overview.htm#sql_server_requirements)
- [Netwrix Enterprise Auditor v11.6 Installation & Configuration Overview](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/Application/Database.htm)

## Notes
- It is crucial to maintain separate SQL Server instances for different Netwrix products to avoid potential conflicts and ensure optimal performance.
- Future installations of Netwrix Enterprise Auditor should always follow the recommended server setup guidelines as outlined in the official documentation.