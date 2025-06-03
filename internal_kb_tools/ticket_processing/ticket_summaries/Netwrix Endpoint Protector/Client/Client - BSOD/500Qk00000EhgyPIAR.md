```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000EhgyPIAR
- **Case Number:** 418640
- **Status:** Closed - Resolved
- **Account/Company:** Canada Guaranty
- **Contact Name:** Parinkumar Patel
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client - BSOD
- **Version:** Windows 11

## Problem Description
The customer reported experiencing Blue Screen of Death (BSOD) errors on Windows 11 endpoints after installing the Data Loss Prevention (DLP) agent during a pilot program for upgrading their endpoints.

## Environment Details
- Operating System: Windows 11
- Software: Netwrix Endpoint Protector DLP agent
- Affected Endpoints: Multiple endpoints in a pilot program

## Troubleshooting Steps
1. Customer provided mini dump files and logs from affected machines for analysis.
2. Technical support requested the latest client version to be tested on one of the affected computers.
3. Engineering analyzed the crash dump and identified a potential conflict with Fortinet's driver, specifically "AV_FortiEDRWinDriver."
4. Customer was advised to reach out to Fortinet for further assistance regarding the identified driver issue.

## Root Cause
The BSOD was determined to be caused by a conflict with Fortinet's driver, which was installed on the endpoints alongside the DLP agent.

## Solution
The customer resolved the issue by contacting Fortinet regarding the problematic driver. It was suggested that they either update or remove the Fortinet software to prevent further BSOD occurrences.

## Notes
- Ensure that any third-party security software is compatible with the Netwrix Endpoint Protector before installation.
- Advise customers to monitor for BSOD issues after installing new software, especially security-related applications.
- Encourage customers to provide detailed logs and dump files for quicker diagnosis in future cases.
```