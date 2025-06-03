## Ticket Metadata
- **Ticket ID:** 500Qk00000DkTvaIAF
- **Case Number:** 416498
- **Status:** Closed - Resolved
- **Account/Company:** Airpak
- **Contact Name:** Stefania Oltean
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** NONE

## Problem Description
The customer inquired about the support for various file types in Content Aware Policies, specifically for SQL Server, Oracle, and Amazon Aurora databases. They needed confirmation on whether certain file types were supported.

## Environment Details
- **File Types in Question:**
  - SQL Server: .mdf, .ldf, .ndf, .bak, .trc, .sql, .dmp
  - Oracle: .dbf, .ctl, .dmp, .log, .pdb, .sql, .spc
  - Amazon Aurora (MySQL and PostgreSQL): .sql, .cnf, .dmp, .frm, .conf, .backup, .pg_dump

## Troubleshooting Steps
1. Reviewed an internal list of supported file types for Content Aware Policies.
2. Confirmed support for the following file types:
   - SQL Server: .sql, .dmp
   - Oracle: .dbf, .dmp, .pdb, .sql
   - Amazon Aurora (MySQL): .sql, .dmp
   - Amazon Aurora (PostgreSQL): .sql, .backup
3. Identified unsupported file types: .ldf, .ndf, .bak, .trc, .ctl, .log, .spc, .cnf, .frm, .conf, .pg_dump.

## Root Cause
The inquiry stemmed from a lack of clarity regarding the support status of specific file types in Content Aware Policies, leading to confusion for the customer.

## Solution
The issue was resolved by providing a comprehensive list of supported and unsupported file types for SQL Server, Oracle, and Amazon Aurora databases. The customer was informed that the following file types are supported:
- SQL Server: .sql, .dmp
- Oracle: .dbf, .dmp, .pdb, .sql
- Amazon Aurora (MySQL): .sql, .dmp
- Amazon Aurora (PostgreSQL): .sql, .backup

The unsupported file types were also clearly communicated to the customer.

## Notes
- Ensure that future inquiries regarding file type support are accompanied by a detailed list of supported and unsupported types to avoid confusion.
- Regularly update internal documentation to reflect any changes in supported file types for Content Aware Policies.