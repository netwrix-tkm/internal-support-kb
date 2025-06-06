## Ticket Metadata
- **Ticket ID:** 500Qk00000ETqMaIAL
- **Case Number:** 418237
- **Status:** Closed - Resolved
- **Account/Company:** AIQON Servicos em Informatica LTDA - MSP
- **Contact Name:** Rafael Zacarias
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SQL
- **Feature:** Configuration
- **Version:** 11.6

## Problem Description
The customer reported encountering an "Invalid Object Name" error while attempting to run several SQL-related jobs. They were unable to identify the cause despite reviewing the documentation.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **SQL Server:** SKYLINE

## Troubleshooting Steps
1. Reviewed documentation for potential misconfigurations.
2. Attempted to run SQL jobs without success, consistently receiving the "Invalid Object Name" error.
3. Investigated SQL Collection job settings for any discrepancies.

## Root Cause
The issue was identified as errors occurring in the SQL Collection jobs, which were likely due to incorrect configuration of audit settings.

## Solution
To resolve the issue, the following steps were taken:
- Installed the Sensitive Data Discovery add-on to the NEA Console server.
- Created a host list that included only the SQL server "SKYLINE" for running SQL jobs.
- Initiated the Database0.CollectionSQL group, which resulted in successful job executions.

## Notes
- Ensure that the SQL server is correctly configured in the host list to avoid similar issues in the future.
- Regularly review and update audit settings to prevent configuration-related errors.