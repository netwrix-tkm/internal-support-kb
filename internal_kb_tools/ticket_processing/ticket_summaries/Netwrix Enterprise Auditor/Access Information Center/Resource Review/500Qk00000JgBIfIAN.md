## Ticket Metadata
- **Ticket ID:** 500Qk00000JgBIfIAN
- **Case Number:** 430286
- **Status:** Closed - Resolved
- **Account/Company:** Extron Electronics
- **Contact Name:** Kevin Winkleman
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Resource Review
- **Version:** 11.6

## Problem Description
The customer reported that during testing of the Netwrix Resource Audit section, the domain admin group was included in the file share access review. They requested a way to exclude the "domain admins" group from the resource audit to prevent data owners from seeing service accounts in the review.

## Environment Details
- **Product Version:** 11.6.0.117
- **Build Number:** 6.0.117

## Troubleshooting Steps
1. Reviewed the customer's request to exclude the domain admin group from the resource audit.
2. Provided documentation on custom search-based reports and filters available in Netwrix Auditor.
3. Discussed the limitations of the current system regarding visibility of resource owners.
4. Confirmed that the case was tagged correctly as an Enterprise Auditor issue.

## Root Cause
The root cause of the issue was identified as a limitation in the Netwrix Enterprise Auditor system. Resource owners inherently have full visibility into the resources they own, which includes all groups and users associated with those resources.

## Solution
The issue was resolved by clarifying that it is not possible to exclude the domain admin group from the resource audit reports. The system is designed to provide resource owners with complete visibility into their resources, including all associated groups.

## Notes
- It is important to communicate to customers that resource owners will always have full visibility into their resources, and exclusions are not supported in the current version of the software.
- Future inquiries regarding similar exclusions should be directed to the limitations of the product's design.