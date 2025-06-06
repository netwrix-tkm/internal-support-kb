```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000JbfcMIAR
- **Case Number:** 430098
- **Status:** Closed - Resolved
- **Account/Company:** Molina Healthcare, Inc.
- **Contact Name:** Chris Kennedy
- **Product:** Netwrix Enterprise Auditor
- **Component:** Action Module
- **Feature:** Survey
- **Version:** 11.6.0.74

## Problem Description
The internal vulnerability team identified a critical vulnerability (CVE-2024-53677) in Apache Struts affecting the Stealthbits/Enterprise Auditor installation. The customer was unsure how to resolve the issue since the vulnerable component was part of the software installation.

## Environment Details
- The vulnerable file identified was located at:
  ```
  C:\Program Files (x86)\STEALTHbits\StealthAUDIT\Actions\SurveyWebServlet\WEB-INF\lib\struts2-core-6.3.0.2.jar
  ```
- The customer was not using the NEA Survey action module, which is the only component that utilizes the Apache Struts binary.

## Troubleshooting Steps
1. Confirmed the presence of the vulnerable Apache Struts file in the installation.
2. Verified that the customer was not using the NEA Survey action module.
3. Advised the customer to remove the offending Apache Struts file to mitigate the vulnerability.
4. Notified the customer about the upcoming patch in NEA version 11.6.0.132+, which would upgrade to Apache Struts 6.7.0.

## Root Cause
The vulnerability was due to the inclusion of an outdated version of Apache Struts (6.3.0.2) in the Stealthbits/Enterprise Auditor installation, which was identified as having a critical security flaw allowing remote code execution.

## Solution
The issue was resolved by:
- Removing the vulnerable Apache Struts file from the customer's environment since they were not using the Survey action module.
- Informing the customer about the availability of a patch in NEA version 11.6.0.132+, which upgrades to a secure version of Apache Struts (6.7.0). The customer was offered assistance with the upgrade.

## Notes
- The vulnerability has been patched, and the patch will be available in the next scheduled cumulative update (CU) on 01/31/2025.
- It is important for customers to regularly check for updates and patches to mitigate vulnerabilities in third-party libraries.
- If the customer decides to use the Survey action module in the future, they should ensure that they are using the updated version of the software to avoid similar vulnerabilities.
```