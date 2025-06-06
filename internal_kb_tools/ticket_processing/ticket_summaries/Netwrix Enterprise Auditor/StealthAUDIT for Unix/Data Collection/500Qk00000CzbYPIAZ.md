```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000CzbYPIAZ
- **Case Number:** 414868
- **Status:** Closed - Resolved
- **Account/Company:** FCCI Services, Inc. (formerly FCCI Insurance Group)
- **Contact Name:** Curt McDonald
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Unix
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that aliases for their HOCohesity were not being captured, which hindered their ability to determine permissions across their filer system.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Unix
- **Build Number:** 76
- **Age:** 10.3

## Troubleshooting Steps
1. The support team requested the output from a PowerShell script to gather information about the installed Netwrix and Stealth applications.
2. The customer provided the requested PowerShell output, confirming that there were no errors in the job, but the information was not being collected.
3. A web meeting was scheduled to further investigate the issue with the customer and their network security admin.
4. During the call, it was confirmed that the Cohesity platform was not officially supported, which could be a contributing factor to the issue.

## Root Cause
The permissions were being set at the wrong level within the Cohesity platform, leading to missing details in the Netwrix Enterprise Auditor (NEA) and Access Information Center (AIC) reporting.

## Solution
The issue was resolved by adjusting the permissions settings within the Cohesity platform to ensure they were correctly configured. This allowed the NEA/AIC to capture the necessary alias information for permission determination.

## Notes
- Cohesity is not officially supported by Netwrix, which may limit functionality and data collection capabilities.
- Future users should ensure that permissions are set correctly within the Cohesity platform to avoid similar issues.
- It is recommended to utilize the Netwrix Support Portal for communication to prevent oversight in case handling.
```