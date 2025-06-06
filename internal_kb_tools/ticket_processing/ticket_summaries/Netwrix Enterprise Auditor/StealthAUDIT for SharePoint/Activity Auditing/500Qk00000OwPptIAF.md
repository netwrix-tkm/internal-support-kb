## Ticket Metadata
- **Ticket ID:** 500Qk00000OwPptIAF
- **Case Number:** 444555
- **Status:** Closed - Resolved
- **Account/Company:** State of South Dakota
- **Contact Name:** Devon Anderson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for SharePoint
- **Feature:** Activity Auditing
- **Version:** 11.6.0.138

## Problem Description
The customer, State of South Dakota, reported an issue with the Netwrix Enterprise Auditor where unknown SharePoint Online (SPO) event types were found during an attempt to collect SPO activity. This resulted in missed activity events, potentially impacting long-term storage and insight into certain activities.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 11.6.0.138
- **Date Issue Started:** May 6, 2025 (exact start date uncertain)

## Troubleshooting Steps
1. The customer ran a SPAC system scan and bulk import.
2. A warning about unknown event types was generated.
3. No additional troubleshooting steps were attempted by the customer.
4. It was noted that Microsoft frequently adds new event types, necessitating updates to the Netwrix Auditor's mapping.

## Root Cause
The issue was caused by Microsoft introducing new event types (specifically `DLPRuleMatch` and `SharingLinkDeleted`) that were not previously recognized by the Netwrix Enterprise Auditor. This required the development team to update the event type mappings to ensure proper data collection.

## Solution
A hotfix (version 11.6.0.077) was developed and delivered to the customer, which included the necessary updates to recognize the new event types. The hotfix was made available for download at the following link:
```
https://releases.netwrix.com/products/auditor-enterprise/11.6/auditor-enterprise-hotfix-11.6.0.077.zip
```
Additionally, the issue was addressed in the next cumulative update (CU).

## Notes
- It is important to monitor for new event types introduced by Microsoft, as they may require similar updates in the future.
- Ensure that the development team is promptly notified of any unknown event types encountered during audits to facilitate timely resolutions.