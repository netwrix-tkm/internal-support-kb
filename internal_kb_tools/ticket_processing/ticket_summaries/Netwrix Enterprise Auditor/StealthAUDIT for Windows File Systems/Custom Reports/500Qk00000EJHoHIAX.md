## Ticket Metadata
- **Ticket ID:** 500Qk00000EJHoHIAX
- **Case Number:** 417793
- **Status:** Closed - Resolved
- **Account/Company:** ConocoPhillips Company
- **Contact Name:** Frank McNickle
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer requested assistance in generating a report that tracks permission changes specifically for the first level of folders within their file system.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector:** StealthAUDIT for Windows File Systems

## Troubleshooting Steps
1. Reviewed the customer's requirements for tracking permission changes.
2. Analyzed the FSAC_ActivityEvents table to identify relevant fields for filtering.
3. Created a SQLView job to filter permission changes based on specific criteria:
   - Filter for permission changes using `OperationDescription like 'Permission%'`.
   - Exclude file-level permission changes by filtering for folders with `ResourceTypeDescription = 'Folder'`.
   - Limit results to top-level and second-level folders using the path length condition.
   - Set a date range to capture changes from the last 7 days.

## Root Cause
The customer needed a method to track permission changes at the folder level, which was not readily available through existing reporting features.

## Solution
A SQLView job was implemented with the following SQL filter on the FSAC_ActivityEvents table:

```sql
OperationDescription like 'Permission%' -- Filter for Permission Changes
AND [ResourceTypeDescription] = 'Folder' -- Filter for folders
AND (
    LEN([Path]) - LEN(REPLACE([Path], '', '')) <= 2 -- Filter for top-level or second-level folders
)
AND CAST([AccessTime] AS DATE) >= CAST(GETDATE() - 7 AS DATE) -- Changes in the last 7 days
AND CAST([AccessTime] AS DATE) <= CAST(GETDATE() AS DATE)
```

This job successfully pulls permission changes for the top two levels of folders over the past week, accommodating the limitations of the FSAC scan and bulk import schedules.

## Notes
- The report generated will only reflect permission changes for the top two levels of folders and is limited to the last 7 days due to the scanning schedule.
- Future requests for similar reports should consider the same SQL filtering criteria to ensure accurate tracking of permission changes.