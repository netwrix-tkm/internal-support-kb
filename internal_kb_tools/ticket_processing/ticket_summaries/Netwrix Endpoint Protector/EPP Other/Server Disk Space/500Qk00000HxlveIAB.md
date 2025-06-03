```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000HxlveIAB
- **Case Number:** 426257
- **Status:** Closed - Resolved
- **Account/Company:** OUHSC
- **Contact Name:** Chisum Thompson
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Server Disk Space
- **Version:** 5941

## Problem Description
The customer reported discrepancies in the license count for Endpoint Protector, specifically a mismatch between the number of licensed endpoints displayed in different sections of the application. They were nearing their license limit and sought clarification on the licensing mechanism, particularly regarding the Automatic Release License feature.

## Environment Details
- The customer did not have the Automatic Release License feature enabled.
- The discrepancy was noted between the counts in:
  - **System Configuration > System Licensing**
  - **Device Control > Computers**

## Troubleshooting Steps
1. The customer exported the license count from **System Configuration > System Licensing**, which showed 10,001 licensed endpoints.
2. They filtered and exported the list from **Device Control > Computers**, which indicated 12,525 records, later reduced to 10,806 after removing duplicates.
3. They checked the last online status of devices in both sections, noting inconsistencies in the counts.
4. A remote session was scheduled to investigate the issue further.

## Root Cause
The issue was identified as a filtering problem related to how licenses were assigned to computers rather than users. The discrepancies arose from the way the application tracked and displayed licensed endpoints.

## Solution
The issue was resolved by upgrading the server to version 5941, which fixed the license filtering discrepancies. This upgrade ensured that the counts displayed in both sections of the application aligned correctly.

## Notes
- It is important to ensure that the Automatic Release License feature is enabled to manage licenses effectively going forward.
- Future investigations into license discrepancies should consider the version of the software being used, as updates may resolve underlying issues.
```