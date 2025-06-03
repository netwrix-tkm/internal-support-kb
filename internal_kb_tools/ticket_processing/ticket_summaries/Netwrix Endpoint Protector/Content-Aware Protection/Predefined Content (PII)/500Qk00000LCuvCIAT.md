## Ticket Metadata
- **Ticket ID:** 500Qk00000LCuvCIAT
- **Case Number:** 433949
- **Status:** Closed - Resolved
- **Account/Company:** RoundRobin Tech Services
- **Contact Name:** Nayan Rajore
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Predefined Content (PII)
- **Version:** 7.1

## Problem Description
The customer, Univest Stocking PTV LTD, reported two main issues during a Proof of Concept (POC) for the Netwrix Endpoint Protector:
1. The Netwrix EPP certificate was not installed on web browsers, which affected access to certain websites requiring biometric authentication.
2. The Optical Character Recognition (OCR) functionality for Social Security Numbers (SSN) and Tax IDs in both text and images was not functioning as expected.

## Environment Details
- The customer utilizes devices that require biometric authentication for accessing specific websites.
- The issues were encountered during a POC phase, indicating a testing environment rather than a production setup.

## Troubleshooting Steps
1. Scheduled a remote session with the customer to address the issues.
2. Investigated the installation status of the Netwrix EPP certificate on web browsers.
3. Reviewed the OCR settings and configurations to identify any discrepancies or misconfigurations.

## Root Cause
The root cause of the issues was identified as a lack of proper installation of the Netwrix EPP certificate on the web browsers, which was necessary for the biometric authentication process. Additionally, there were configuration issues affecting the OCR functionality for SSN and Tax ID recognition.

## Solution
During the remote session, the following actions were taken to resolve the issues:
1. The Netwrix EPP certificate was successfully installed on the required web browsers, enabling the necessary biometric authentication.
2. The OCR settings were adjusted and tested, resulting in successful recognition of SSN and Tax IDs in both text and images.

## Notes
- Ensure that the Netwrix EPP certificate is installed on all relevant web browsers before conducting POCs, especially when biometric authentication is required.
- Regularly verify OCR configurations and test them in the environment to prevent similar issues in the future.