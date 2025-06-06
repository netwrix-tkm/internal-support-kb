## Ticket Metadata
- **Ticket ID:** 500Qk00000OwQxCIAV
- **Case Number:** 444553
- **Status:** Closed - Resolved
- **Account/Company:** Kootenai Health
- **Contact Name:** Devon Anderson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Access Auditing
- **Version:** 11.6.0.138

## Problem Description
The customer, Kootenai Health, reported encountering unknown SharePoint Online (SPO) event types while attempting to collect SPO activity. This issue resulted in missed activity events, which could hinder long-term storage and insight into specific activities.

## Environment Details
- **Data Source Affected:** SharePoint Activity Scans
- **Current Version:** 11.6.0.138

## Troubleshooting Steps
1. Identified unknown event types: `CommentDeleted` and `UserExpirationChanged`.
2. Gathered screenshots of the unknown event types for documentation.
3. Noted that this is a common occurrence due to Microsoft adding or changing event types, requiring mapping by the Netwrix NAA development team.
4. Escalated the issue to the development team for mapping the new event types.

## Root Cause
The root cause of the issue was identified as Microsoft introducing new event types that were not previously mapped in the Netwrix Enterprise Auditor, leading to the inability to collect certain SPO activity events.

## Solution
A hotfix (version 11.6.0.077) was made available to address the issue. This hotfix included the necessary mappings for the new event types, allowing the Netwrix Enterprise Auditor to properly collect SPO activity. The hotfix was sent to Professional Services for deployment.

## Notes
- It is important to monitor for similar issues in the future, as Microsoft frequently updates event types.
- Ensure that the development team is promptly notified of any new event types to facilitate timely updates and prevent data collection gaps.
- The hotfix can be downloaded from the following link: [Hotfix 11.6.0.077](https://releases.netwrix.com/products/auditor-enterprise/11.6/auditor-enterprise-hotfix-11.6.0.077.zip).