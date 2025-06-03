## Ticket Metadata
- **Ticket ID:** 500Qk00000CHGSwIAP
- **Case Number:** 412970
- **Status:** Closed - Resolved
- **Account/Company:** Secure Gate (@securegate.com.br)
- **Contact Name:** Tiago Guerra
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Client - Other
- **Feature:** Brazilian PII Detection
- **Version:** 6.2.4.0046

## Problem Description
The customer reported an issue with the Netwrix Endpoint Protector where Brazilian Personally Identifiable Information (PII) was generating numerous false positives. The customer was unable to use the solution effectively for six months, leading to concerns about an upcoming audit.

## Environment Details
- The customer operates in a SaaS environment.
- Testing was also conducted in an on-premises environment by the project owner, Tiago Guerra.
- The customer reported that text and CSV files containing PII were blocked, while Excel, DOC, and XML files with PII were not blocked.

## Troubleshooting Steps
1. **Initial Assessment**: Gathered information from the customer regarding the false positives and the specific file types affected.
2. **Test Build Installation**: A test build (EppClient_v6.2.4.0022) was provided to the customer for installation to address the metadata scanning issue.
3. **Log Collection**: Collected logs from the customer's environment to analyze the behavior of the EPP Client.
4. **Remote Session**: Scheduled remote sessions to further investigate the issue and gather additional logs.
5. **Contextual Detection Rules**: Suggested using contextual detection rules to improve detection accuracy for Brazilian PII.
6. **Further Testing**: Conducted tests with various file types and configurations to replicate the issue.

## Root Cause
The root cause of the false positives was identified as a lack of sufficient checksums for Brazilian PII in the EPP Client, leading to incorrect detections. Additionally, the configuration of allowlists for XML files on the cloud server contributed to the discrepancies in detection behavior between different environments.

## Solution
The issue was resolved by:
- Removing allowlists for XML files, which allowed the EPP Client to scan and block files correctly based on their metadata.
- Testing the updated configurations with user remediation on various platforms (Jira, Gmail, and standard browser uploads) to confirm that the changes worked as intended.
- The final resolution involved deploying a new test build (EppClient_v6.2.4.0046) that included improvements for Brazilian PII detection.

## Notes
- It is crucial to ensure that allowlists are consistently configured across different environments to avoid discrepancies in detection behavior.
- Future updates related to Brazilian PII detection improvements are scheduled for version 5.9.5.0, which should further enhance the accuracy of the EPP Client.
- Customers should be advised to test new builds in a controlled manner to prevent disruptions in their operations.