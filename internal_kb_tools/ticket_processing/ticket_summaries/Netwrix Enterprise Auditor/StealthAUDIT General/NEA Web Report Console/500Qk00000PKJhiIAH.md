## Ticket Metadata
- **Ticket ID:** 500Qk00000PKJhiIAH
- **Case Number:** 445568
- **Status:** Closed - Resolved
- **Account/Company:** Wellington Management Company LLP
- **Contact Name:** Matt Frazier
- **Product:** Netwrix Enterprise Auditor
- **Component:** Web Report Console
- **Feature:** NEA Web Report Console
- **Version:** 11.6

## Problem Description
The customer reported that after updating the server certificates, the WebUI of the Netwrix Enterprise Auditor was not responding. They were unable to find a relevant knowledge base article to assist with the issue.

## Environment Details
- **Platform:** Unsupported platform noted during troubleshooting.
- **Product Version:** 11.6

## Troubleshooting Steps
1. Confirmed the issue with the WebUI not responding after the server certificate update.
2. Identified that the platform was unsupported.
3. Reviewed documentation related to securing the Web Console for potential configuration issues.
4. Suggested reviewing the following knowledge base article: [Securing the Web Console](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Install/Application/Reports/Secure.htm).

## Root Cause
The issue was determined to be related to an incorrect configuration following the update of the server certificates, compounded by the use of an unsupported platform.

## Solution
The issue was resolved by following the guidelines provided in the knowledge base article on securing the Web Console. The customer was directed to ensure that the server certificates were correctly configured according to the documentation.

## Notes
- Ensure that the platform is supported before performing updates to server certificates.
- Always refer to the relevant knowledge base articles when encountering issues after configuration changes.
- Future updates should be tested in a controlled environment to prevent similar issues from affecting production systems.