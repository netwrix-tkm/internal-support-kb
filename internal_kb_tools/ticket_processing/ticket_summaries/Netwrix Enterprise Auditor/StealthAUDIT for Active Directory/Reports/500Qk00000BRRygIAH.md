```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000BRRygIAH
- **Case Number:** 410977
- **Status:** Closed - Resolved
- **Account/Company:** Logix
- **Contact Name:** Ahmed Shaban
- **Product:** Netwrix Enterprise Auditor
- **Component:** Reports
- **Feature:** Published Reports
- **Version:** 11.6

## Problem Description
The customer reported that after installing the Netwrix Enterprise Auditor in their lab and scanning Active Directory, the published reports were not functioning. The error message displayed was "This site can’t be reached."

## Environment Details
- **Collector Code:** StealthAUDIT for Active Directory
- **Installation Path:** C:\Program Files (x86)\STEALTHbits\StealthAUDIT
- **Installed Versions:**
  - Netwrix Access Information Center: 11.6.0.14
  - Netwrix Enterprise Auditor: 11.6.0.69
  - StealthINTERCEPT Server: 7.3.9.160
  - StealthINTERCEPT Windows Agent: 7.3.9.150

## Troubleshooting Steps
1. The support team requested the output of a PowerShell script to gather information about installed components.
2. The customer provided the requested output confirming the installation of relevant software.
3. The support team advised the customer to secure the published reports by following a specific article on the Netwrix help center.
4. The customer attempted to implement the suggested changes but continued to experience the same issue.
5. A session was scheduled to further investigate the problem.

## Root Cause
The issue was identified as a misconfiguration of the Netwrix Enterprise Auditor Web Server service, which was not running under an account with database access. This prevented the service from connecting to the database to retrieve and display the reports.

## Solution
During a support session, the Web Server service was reconfigured to run as a user account that had the necessary database access. This change allowed the service to authenticate users based on their roles and successfully display the published reports.

## Notes
- Ensure that the Web Server service is always configured to run under an account with appropriate database access to avoid similar issues in the future.
- Refer to the following knowledge base article for further details on service configuration: [Netwrix KB Article](https://helpcenter.netwrix.com/bundle/z-kb-articles-salesforce/page/kA0Qk0000000Qs9KAE.html).
```