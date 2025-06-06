## Ticket Metadata
- **Ticket ID:** 500Qk00000DJKbWIAX
- **Case Number:** 415553
- **Status:** Closed - Resolved
- **Account/Company:** AON Service Corporation
- **Contact Name:** Divyang Shah
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The account lockout job was not functioning as expected, resulting in the user account `strozllcpublicvreddy` being locked out repeatedly without detection by the lockout job.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General

## Troubleshooting Steps
1. Reviewed the existing account lockout job configuration.
2. Attempted to identify the cause of the repeated account lockouts.
3. Created a new job using SQL ViewCreation to pull all admin groups.
4. Developed a new report to list all users from each admin group.
5. Joined the `SA_ADInventory_UsersView` and `SA_ADInventory_GroupMembersView` using INNER JOIN on `PrincipalId` and `MemberPrincipalId`.
6. Selected relevant columns: `GroupNTAccount` from `SA_ADInventory_GroupMembersView` and `SamAccountName`, `ACCOUNTDISABLE` from `SA_ADInventory_UsersView`.
7. Applied a filter to show only disabled accounts: `[SourceTable1.ACCOUNTDISABLE] = True`.
8. Adjusted the report filter to ensure it displayed all admin groups.
9. Changed the report output format from PDF to CSV for better analysis.

## Root Cause
The initial account lockout job was not configured to adequately capture all relevant admin groups, leading to the failure in detecting the repeated lockouts for the specified user account.

## Solution
The issue was resolved by creating a new job that effectively pulled all admin groups and generated a report listing all users from these groups. The adjustments made to the SQL queries and filters allowed for comprehensive monitoring of account statuses, including disabled accounts, which helped in identifying the root cause of the lockouts.

## Notes
- Ensure that any future configurations of account lockout jobs include comprehensive checks for all relevant groups to avoid similar issues.
- Consider using CSV format for reports when dealing with large datasets for easier analysis and troubleshooting.