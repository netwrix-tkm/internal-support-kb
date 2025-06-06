## Ticket Metadata
- **Ticket ID:** 500Qk00000LkePoIAJ
- **Case Number:** 435443
- **Status:** Closed - Resolved
- **Account/Company:** Polsinelli
- **Contact Name:** Brandon Artist
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Reports
- **Version:** 11.6

## Problem Description
The customer reported that old file servers were appearing in reports, such as the stale content report, which distorted the amount of stale data in their environment. Additionally, there was missing activity data in the Activity Insight Console (AIC) related to file servers.

## Environment Details
- **AIC Version:** 11.6.0.12
- **Affected Servers:** 17 designated decommissioned file servers

## Troubleshooting Steps
1. Conducted a meeting with Brandon Artist to discuss the issue.
2. Followed the steps outlined in the Netwrix Help Center article on dropping data for decommissioned file servers.
3. Verified that the job was initiated to delete data for the specified 17 servers.
4. Checked the AIC for activity details and statistics, noting that activity details were not rendering.
5. Reviewed logs for potential issues but found them inconclusive.
6. Investigated the configuration settings in the Netwrix Enterprise Auditor (NEA) and Activity Insight Console (AIC) for any discrepancies.
7. Ran various jobs in NEA to ensure proper data collection and reporting.
8. Created a new job to remove old hosts and monitored its execution.

## Root Cause
The presence of old file servers in reports was due to the failure to remove data associated with decommissioned servers from the SQL server (Tier 1 database) and local databases (Tier 2). Additionally, the AIC was not rendering activity details due to configuration issues and potential data collection errors.

## Solution
The issue was resolved by:
1. Successfully executing the job to drop data for the 17 decommissioned file servers, which cleared the stale data from the reports.
2. Adjusting settings in the NEA and AIC to ensure proper reporting and data collection.
3. Creating and running a new job to remove old hosts, which successfully updated the database and cleared the old entries.
4. Ensuring that the AIC was configured correctly to display activity details, which began functioning after the adjustments.

## Notes
- It is important to regularly review and clean up decommissioned servers from the reporting databases to prevent similar issues in the future.
- Ensure that the AIC settings are correctly configured to render activity details, especially after making changes to the monitored hosts.
- For future cases, consider creating a checklist for verifying configurations in both NEA and AIC when dealing with decommissioned servers.