## Ticket Metadata
- **Ticket ID:** 500Qk00000HaORtIAN
- **Case Number:** 425311
- **Status:** Closed - Resolved
- **Account/Company:** Marsh & McLennan Companies
- **Contact Name:** Kay Groth
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for AzureAD
- **Feature:** Database
- **Version:** 11.6

## Problem Description
The customer encountered an error related to Azure Active Directory Inventory (AADI) during a database operation. The error message indicated a violation of a UNIQUE KEY constraint, preventing the insertion of a duplicate key into the `dbo.SA_AzureADInventory_Principals` table.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for AzureAD
- **Product Version:** 11.6

## Troubleshooting Steps
1. The customer attempted to diagnose the issue but did not find a resolution.
2. Instead of further troubleshooting, the customer opted to remove the Azure ADI tables using the built-in data collector.
3. The customer then reran the Entra ID jobs.

## Root Cause
The root cause of the issue was identified as a UNIQUE KEY constraint violation in the `dbo.SA_AzureADInventory_Principals` table, specifically due to an attempt to insert a duplicate key value (5f98a142-32c6-43ba-a80a-9f850b5444db). The exact reason for the duplication was not diagnosed.

## Solution
The issue was resolved by the customer removing the Azure ADI tables and rerunning the Entra ID jobs. This action cleared the duplicate entries and allowed the database operations to proceed without errors.

## Notes
- It is advisable to monitor for similar UNIQUE KEY constraint violations in the future, especially after upgrades or changes to the database schema.
- Consider implementing checks to prevent duplicate entries before attempting to insert data into the database to avoid similar issues.