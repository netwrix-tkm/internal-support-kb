## Ticket Metadata
- **Ticket ID:** 500Qk00000NnqzVIAR
- **Case Number:** 441249
- **Status:** Closed - Resolved
- **Account/Company:** Hawaii Pacific Health
- **Contact Name:** Steven Schiesl
- **Product:** Netwrix Access Analyzer
- **Component:** Data Migration
- **Feature:** Data Collection
- **Version:** 12.0

## Problem Description
The customer installed Netwrix Access Analyzer 12.0 and encountered an issue where the "Create Schema" job, specifically the "Data Migration" task, was taking an excessively long time to complete. After running for approximately 83 hours, the customer stopped the job and sought clarification on whether such a duration was normal and how to estimate the time required for completion.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Windows File Systems

## Troubleshooting Steps
1. The customer initially ran the "Create Schema" job, which included the "Data Migration" SQL script.
2. After 83 hours, the job was stopped due to concerns about its duration.
3. The support team consulted with Product Management and Development teams to analyze the situation.
4. The team identified that the Foreign Key (FK) constraints on two tables were likely causing delays.
5. The FK constraints on the following tables were temporarily disabled:
   - `SA_FSAA_ResourcesScanTypeDetails`
   - `SA_FSAA_ResourceMap`
6. After disabling the constraints, the "Data Migration" task completed quickly.
7. The FK constraints were then re-applied to the tables.

## Root Cause
The prolonged duration of the "Data Migration" task was attributed to the Foreign Key constraints on the involved tables, which were causing performance bottlenecks during the migration process.

## Solution
To resolve the issue, the following steps were taken:
1. Temporarily disable the FK constraints on the tables involved in the migration:
   ```sql
   ALTER TABLE SA_FSAA_ResourcesScanTypeDetails NOCHECK CONSTRAINT ALL;
   ALTER TABLE SA_FSAA_ResourceMap NOCHECK CONSTRAINT ALL;
   ```
2. Run the "Data Migration" task, which completed successfully and quickly after the constraints were disabled.
3. Re-enable the FK constraints after the migration was completed:
   ```sql
   ALTER TABLE SA_FSAA_ResourcesScanTypeDetails WITH CHECK CHECK CONSTRAINT ALL;
   ALTER TABLE SA_FSAA_ResourceMap WITH CHECK CHECK CONSTRAINT ALL;
   ```

## Notes
- It is advisable to monitor the performance of the "Data Migration" task in future instances, especially when dealing with large datasets.
- Consider disabling FK constraints during lengthy migration processes to improve performance, but ensure they are re-enabled afterward to maintain data integrity.
- If similar issues arise, check the SQL execution plan for the running queries to identify potential bottlenecks.