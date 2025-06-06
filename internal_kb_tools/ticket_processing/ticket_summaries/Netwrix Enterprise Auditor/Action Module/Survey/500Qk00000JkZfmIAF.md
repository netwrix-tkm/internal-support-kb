## Ticket Metadata
- **Ticket ID:** 500Qk00000JkZfmIAF
- **Case Number:** 430461
- **Status:** Closed - Resolved
- **Account/Company:** Point32Health Services, Inc.
- **Contact Name:** Peter Sterianos
- **Product:** Netwrix Enterprise Auditor
- **Component:** Action Module
- **Feature:** Survey
- **Version:** 11.6

## Problem Description
A vulnerability (CVE-2024-53677) was identified on the Stealthbits server, prompting the customer to inquire about available patches or upgrades to mitigate the issue.

## Environment Details
- The customer is based in the US.
- The vulnerability was found on the NEA server.
- The offending file was related to Apache Struts, specifically `struts2-core-6.3.0.2.jar`, which is utilized in the Survey Action Module.

## Troubleshooting Steps
1. Confirmed the vulnerability with the SWAT team to determine if it was a known issue.
2. Advised the customer to remove the offending Apache Struts file since they were not using the Survey Action Module.
3. Engaged with the development team to investigate the vulnerability and potential patches.
4. Notified the customer about the patch availability in NEA version 11.6.0.132+, which uses Apache Struts 6.7.0.

## Root Cause
The issue was caused by the use of an outdated version of Apache Struts (6.3.0.2) that contained a known vulnerability (CVE-2024-53677). The customer was not using the Survey Action Module, allowing for the safe removal of the offending file.

## Solution
The vulnerability was resolved by:
- Removing the offending Apache Struts file from the customer's environment.
- Implementing a patch in NEA version 11.6.0.132+, which upgraded to Apache Struts version 6.7.0. The customer was informed of the patch and offered assistance for the upgrade.

## Notes
- Ensure that customers are aware of the importance of keeping third-party libraries up to date to avoid vulnerabilities.
- For customers not using specific modules, confirm whether it is safe to remove related files to mitigate risks.
- Future patches addressing vulnerabilities should be communicated promptly to affected customers.