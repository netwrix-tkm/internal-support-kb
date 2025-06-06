## Ticket Metadata
- **Ticket ID:** 500Qk00000CJJuVIAX
- **Case Number:** 413051
- **Status:** Closed - Resolved
- **Account/Company:** Geislinger GmbH
- **Contact Name:** Panagiotis Dragatis
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** 5.9.4.1 (fix included in this version)

## Problem Description
The customer reported that their policy to remediate the upload of CAD files, specifically PRT files from Siemens NX, was not functioning as expected. PRT files were being uploaded without remediation, as they were recognized as "unidentified" in the EPP logs instead of being blocked.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **File Type:** PRT files from Siemens NX

## Troubleshooting Steps
1. The support engineer replicated the issue using a test file provided by the customer.
2. The customer was asked to test with a larger PRT file (365 KB) to see if it would be recognized differently.
3. A log was generated by the customer to assist in diagnosing the issue.
4. A test build of the client was prepared and provided to the customer for installation on 1-2 computers.

## Root Cause
The issue was identified as a bug in the previous versions of the Netwrix Endpoint Protector, which caused PRT files to be incorrectly classified as "unidentified" rather than being recognized and blocked as intended.

## Solution
The problem was resolved by installing a test build (version 6.2.3.0044) provided by the support team. This build correctly recognized PRT files and enforced the remediation policy as expected. The fix was confirmed to be included in the upcoming version 5.9.4.1.

## Notes
- Ensure that customers experiencing similar issues are advised to test with larger files if the initial tests do not yield expected results.
- Always check for the latest version of the software that may contain critical fixes for known issues.
- Document any specific file types or scenarios that lead to misclassification for future reference.