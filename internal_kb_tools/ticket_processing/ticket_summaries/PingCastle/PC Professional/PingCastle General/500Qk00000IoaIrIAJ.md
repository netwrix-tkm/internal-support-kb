```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000IoaIrIAJ
- **Case Number:** 428175
- **Status:** Closed - Resolved
- **Account/Company:** Exide Technologies SAS
- **Contact Name:** Rhondel Herrera
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer inquired about how PingCastle detects obsolete versions of Windows and whether there is a database or official Microsoft documentation that the tool references for this information.

## Environment Details
- The customer was using PingCastle version 3.2.0.1.

## Troubleshooting Steps
1. Confirmed that PingCastle uses Microsoft documentation to determine End of Support (EoS) dates for Windows versions.
2. Provided links to relevant Microsoft documentation for Windows 10 and Windows 11.
3. Explained the specific code in PingCastle that checks for obsolete Windows versions.
4. Clarified that the detection of obsolete OS is based on the date the report was run, which explains why certain versions were not flagged in previous reports.

## Root Cause
The confusion arose from the timing of the report generation and the EoS dates set in the PingCastle rules. The customer noted that Windows 11 21H2 was not detected in a September review because its EoS was not until October.

## Solution
The issue was resolved by explaining that:
- PingCastle checks for obsolete versions based on the EoS dates documented by Microsoft.
- The specific code responsible for this check was shared with the customer for transparency.
- A bug was identified regarding the EoS date for Windows 10, which will be updated in the next release of PingCastle.

## Notes
- It is important for users to understand that the detection of obsolete OS versions is time-sensitive and based on the report generation date.
- Customers should be encouraged to refer to the official Microsoft documentation for the most accurate EoS information.
- A bug regarding the EoS date for Windows 10 was logged and will be addressed in future updates.
```