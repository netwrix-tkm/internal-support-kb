## Ticket Metadata
- **Ticket ID:** 500Qk00000MqRfOIAV
- **Case Number:** 438545
- **Status:** Closed - Resolved
- **Account/Company:** Prudential Investment Managers (M&G Investments SA)
- **Contact Name:** Warren Stevens
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Migration
- **Version:** 11.6

## Problem Description
The customer, Warren Stevens, requested assistance with migrating from a NetApp file server to a Windows file server while retaining the activity data collected by the Netwrix Auditor. The new file server would have the same name as the old one, and the customer was looking for guidance on how to re-link the auditor to the new server.

## Environment Details
- Current setup involves a NetApp file server.
- Migration target is a Windows file server with shares.
- The customer has been copying data from the NetApp server to the new Windows server and plans to go live next month.

## Troubleshooting Steps
1. Reviewed the previous ticket (00370902) for context on the feature request.
2. Confirmed that the feature request regarding migration capabilities is still under consideration for future updates.
3. Discussed the implications of migrating data between different collectors and the potential issues that may arise.
4. Suggested that the customer add and re-scan the new server separately instead of attempting to migrate data directly.
5. Provided a comprehensive list of tables and views used by the File Server collector for future reference.

## Root Cause
The inability to safely migrate data between two distinct collectors was identified as the primary issue. The different intake sources (NetApp vs. Windows file server) complicate direct data migration, leading to potential data integrity issues.

## Solution
The recommended solution was to:
- Perform a clean setup for the new Windows file server.
- Remove old data from the previous setup to avoid duplication.
- Re-scan the new server to ensure accurate data collection.
- For activity data retention, the customer was advised to refer to specific tables in the SQL database, particularly the `SA_FSAC_DailyResourceActivityView`, for querying activity details.

## Notes
- The customer expressed concerns about duplicating data and preserving resource ownership during the migration process. It was clarified that ownership would need to be re-established due to the change in objects.
- A guide for adding the new Windows file server to the activity monitor was provided to assist the customer in the setup process.
- The customer was encouraged to create a Power BI dashboard to connect to the old database for reporting purposes, ensuring they have access to historical activity data if needed.