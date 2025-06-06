```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CbRYeIAN
- **Case Number:** 413862
- **Status:** Closed - Resolved
- **Account/Company:** Westpac Banking Corporation
- **Contact Name:** Mark Chambers
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Resource Audit
- **Version:** 11.5.0.165

## Problem Description
The customer reported an issue with the Activity Monitor in Netwrix Enterprise Auditor, where the Activity Details for a share (ServerShare_1) incorrectly displayed users accessing a child share (ServerShare_2) even when the "Include subfolders" option was unchecked. The customer sought clarification on whether the Activity Details window would show activity from the parent share and its immediate child shares.

## Environment Details
- **StealthAUDIT Version:** 11.5.0.165
- **AIC Version:** 11.5.0.103
- **Resource Type:** Isilon

## Troubleshooting Steps
1. Confirmed the versions of StealthAUDIT and AIC with the customer.
2. Attempted to reproduce the issue in a lab environment using Netwrix Enterprise Auditor 11.6.
3. Clarified the resource type scanned (Isilon) and requested additional details about the SAM version.
4. Suggested upgrading to the latest build of AIC (11.5.0.276) to see if it resolved the issue.
5. Reviewed SQL database entries using the SA_FSAC_ActivityEventsView table for accuracy.

## Root Cause
The issue was identified as a bug in the AIC version 11.5 that caused it to display activity from the top-level share and the next level down, regardless of the "Include subfolders" setting. This behavior was not related to SAM or Isilon events.

## Solution
The customer was advised to upgrade the AIC to the latest build of version 11.5. The customer confirmed that they would validate whether the upgrade resolves the issue. They also noted that they could access the correct data through their Power BI report, indicating that the underlying data was accurate despite the display issue.

## Notes
- The issue may be resolved in version 11.6, but the customer was unable to upgrade at the time of the case.
- It is recommended to always check for the latest builds of both StealthAUDIT and AIC when encountering similar issues.
- The customer successfully accessed the necessary data through SQL queries, which can be a useful workaround until the display issue is resolved.
```