## Ticket Metadata
- **Ticket ID:** 500Qk00000OxrthIAB
- **Case Number:** 444614
- **Status:** Closed - Resolved
- **Account/Company:** Sphinxtec Co.,Ltd.
- **Contact Name:** Support Sphinxtec
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SQL
- **Feature:** Configuration
- **Version:** 12.0

## Problem Description
The customer inquired whether SQL Server activities could be scanned and imported into the database by Netwrix Access Analyzer (NAA) without enabling database auditing on their SQL Server.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for SQL
- **Product Version:** 12.0

## Troubleshooting Steps
1. Reviewed the customer's request regarding SQL Server auditing without enabling DB auditing.
2. Consulted the Netwrix documentation to verify capabilities related to SQL Server auditing.
3. Confirmed the current limitations of NAA in relation to SQL Server auditing.

## Root Cause
It was determined that the current version of Netwrix Enterprise Auditor does not support auditing SQL Server activities without enabling database auditing on the SQL Server itself.

## Solution
The issue was resolved by providing the customer with documentation that clearly states the limitations of the NAA regarding SQL Server auditing. The customer was informed that it is currently not possible to audit the database without enabling auditing on SQL Server.

## Notes
- Customers should be made aware that enabling database auditing on SQL Server is a prerequisite for using NAA to audit SQL Server activities.
- For future reference, the following documentation links were provided to the customer:
  - [Enterprise Auditor Requirements for SQL Database](https://helpcenter.netwrix.com/bundle/AccessAnalyzer_12.0/page/Content/EnterpriseAuditor/Requirements/Target/DatabaseSQL.htm)
  - [SQL Server Activity Configuration](https://helpcenter.netwrix.com/bundle/AccessAnalyzer_12.0/page/Content/Config/SQLServer/Activity.htm)
  - [Adding SQL Server to Monitored Hosts](https://helpcenter.netwrix.com/bundle/ActivityMonitor_8.0/page/Content/ActivityMonitor/Admin/MonitoredHosts/Add/SQLServer.htm)