## Ticket Metadata
- **Ticket ID:** 500Qk00000LYlWgIAL
- **Case Number:** 434916
- **Status:** Closed - Resolved
- **Account/Company:** Edelman Financial Engines
- **Contact Name:** Jim Manalo
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Migration
- **Version:** 11.6

## Problem Description
The customer requested assistance in migrating several Netwrix servers to a new domain. This included reconfiguring software, URL paths, and certificates, with a preference for making changes after 6 PM PST.

## Environment Details
The following servers were involved in the migration:
- **DC1-SB-SD01**
  - Netwrix PostgreSQL v14
  - Netwrix Threat Manager (StealthDepend)
  
- **DC1-SB-SI01**
  - Threat Prevention (StealthIntercept)
  
- **DC1-SB-SMP01**
  - Netwrix Access Information Center
  - Netwrix Activity Monitor
  - Netwrix Enterprise Auditor
  - Netwrix Sensitive Data Discovery Add-On
  
- **DC1-SB-SQL01**
  - SQL Server 2019
  
- **DC2-SB-SMP01**
  - Netwrix Enterprise Auditor File System Scanning
  - Netwrix Sensitive Data Discovery Add-On

## Troubleshooting Steps
1. Confirmed the customer's requirements for migrating NTP, NTM, NAM, NEA, and the associated SQL server to the new domain.
2. Reviewed SWAT posts related to each Netwrix product for migration guidance.
3. Successfully migrated Netwrix Threat Manager (NTM) and documented the process in ticket 00436543.
4. Awaited responses from the development team regarding the migration of the SQL server, which contained databases for NEA and NTP.
5. Completed migrations for all Netwrix products as documented in the following tickets:
   - Netwrix Threat Manager Migration: 00436543
   - Netwrix Threat Prevention Migration: 00435527
   - Netwrix Threat Prevention Upgrade: 00436235
   - Netwrix Enterprise Auditor, Netwrix Activity Monitor, Access Information Center, and NEA Reporting Module: 00435206

## Root Cause
The issue stemmed from the need to migrate multiple Netwrix applications and their associated SQL server from one domain to another while maintaining their configurations and data integrity.

## Solution
The migration was successfully completed by following the documented procedures for each Netwrix product. The necessary configurations, URL paths, and certificates were updated to reflect the new domain settings. All migrations were verified and confirmed to be operational post-migration.

## Notes
- Ensure to schedule migrations during off-peak hours to minimize disruption.
- Always back up configurations and databases before initiating a migration.
- Future migrations should reference the completed tickets for detailed procedures and lessons learned.