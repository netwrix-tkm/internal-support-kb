## Ticket Metadata
- **Ticket ID:** 500Qk00000GvnUIIAZ
- **Case Number:** 423720
- **Status:** Closed - Resolved
- **Account/Company:** Post Holdings, Inc.
- **Contact Name:** Justin Cahill
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Activity Auditing
- **Version:** 11.6

## Problem Description
After upgrading to Netwrix Enterprise Auditor (NEA) version 11.6.0.112 and clearing the tier 1/2 databases for SharePoint, the customer reported no activity being recorded within Teams Channels for users. The activity records in the database showed a NULL resource ID, which prevented them from appearing in the Access Information Center (AIC).

## Environment Details
- **Netwrix Access Information Center:** 11.6.0.25
- **Netwrix Activity Monitor:** 7.0.3175
- **Netwrix Activity Monitor Agent 64-bit:** 7.0.3175
- **Netwrix Enterprise Auditor:** 11.6.0.112
- **Netwrix Sensitive Data Discovery Add-On:** 11.6.0.13

## Troubleshooting Steps
1. Upgraded NEA to version 11.6.0.112.
2. Cleared all tables and SQLite databases related to SharePoint.
3. Ran SPAA (SharePoint Activity Auditing) and SPAC (SharePoint Activity Collection) jobs.
4. Verified that the resource ID of activity records was NULL.
5. Investigated if the SPAA/SPSEEK scans included the paths of SPAC.
6. Checked for specific event IDs in the SA_SPAC_ActivityEventsView.

## Root Cause
The issue was likely caused by running a SPAC scan that collected activity from SharePoint resources that had not yet been scanned with SPAA or SPSEEK. This resulted in activity records being created without associated resource IDs, leading to their absence in the AIC.

## Solution
The customer performed several updates and data drops, which resolved the issue. Although the exact cause of the resolution was unclear, it was noted that the customer had successfully run multiple SPAA and SPSEEK jobs after the data drops, which likely corrected the NULL resource ID problem.

## Notes
- It is important to ensure that SP resources are scanned with SPAA or SPSEEK before reviewing activity in the AIC to avoid NULL resource IDs.
- If similar issues arise in the future, verify that the relevant resources are included in the permission scans and that the necessary scans have been completed successfully.