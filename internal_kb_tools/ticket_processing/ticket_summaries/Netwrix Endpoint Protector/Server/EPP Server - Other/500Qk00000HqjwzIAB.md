## Ticket Metadata
- **Ticket ID:** 500Qk00000HqjwzIAB
- **Case Number:** 425886
- **Status:** Closed - Resolved
- **Account/Company:** Gameskraft
- **Contact Name:** Vikash Singh
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer reported that an external source indicated a public URL was exposing sensitive encryption keys and configuration data. They sought to understand the criticality and severity of this exposure and its hosting details.

## Environment Details
- The URL in question: [https://dlp.gameskraft.com/easylock/generatedData/metadata.txt](https://dlp.gameskraft.com/easylock/generatedData/metadata.txt)
- Data displayed included encryption keys (ivMp, saltMp, mpPub, encMpPrivByMp), unique identifiers (elId), and various configuration settings (pingInterval, passwordRules).

## Troubleshooting Steps
1. Scheduled a call with the customer to discuss the issue in detail.
2. Reviewed the contents of the exposed URL to assess the sensitivity of the data.
3. Consulted with a developer regarding the security implications of the exposed data.
4. Confirmed that sensitive data in the file is encrypted and does not pose a security risk.
5. Discussed potential measures to restrict access to the URL.

## Root Cause
The URL was publicly accessible, allowing anyone to view the data it contained. However, the data was determined to be encrypted and not directly sensitive, as it relied on a master password stored securely on the EPP server.

## Solution
During the call with the customer, it was confirmed that the data exposed does not pose a security risk due to its encryption. The customer was advised that the sensitive information is protected and that the URL could remain public for the time being. The support team will discuss internally whether to restrict access to the URL in the future.

## Notes
- It is important to verify the encryption status of any sensitive data before taking action on exposed URLs.
- Future assessments should consider both the nature of the data and the security measures in place to protect it.
- The customer was advised to monitor the situation and report any further concerns regarding the URL's accessibility.