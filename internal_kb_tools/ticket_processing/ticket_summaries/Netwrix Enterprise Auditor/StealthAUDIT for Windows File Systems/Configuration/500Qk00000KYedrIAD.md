## Ticket Metadata
- **Ticket ID:** 500Qk00000KYedrIAD
- **Case Number:** 431913
- **Status:** Closed - Resolved
- **Account/Company:** American Express
- **Contact Name:** Alex Parsa
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Configuration
- **Version:** 11.5

## Problem Description
The customer inquired whether the Netwrix Enterprise Auditor encrypts data stored or transmitted, seeking confirmation on the encryption capabilities of the software.

## Environment Details
- **Product Version:** 11.5
- **Platform:** Netwrix Enterprise Auditor

## Troubleshooting Steps
1. Reviewed the customer's inquiry regarding encryption of data in transit and at rest.
2. Provided links to relevant documentation regarding HTTPS encryption:
   - [FSAA Applet Certificate Management Overview](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/DataCollector/FSAA/CertificateManagement.htm)
   - [FSAA: Scan Settings](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/DataCollector/FSAA/ScanSettings.htm)
3. Confirmed that communication between the FSAA proxy server and the target host may be encrypted.
4. Clarified that encryption is supported from the FSAA proxy server to the NEA Application server.

## Root Cause
The initial confusion stemmed from a lack of clarity regarding the encryption capabilities of the Netwrix Enterprise Auditor, specifically concerning data in transit and stored data.

## Solution
The issue was resolved by providing the customer with documentation that confirmed the presence of HTTPS encryption for data in transit between the FSAA proxy server and the NEA Application server. The customer was informed that while data at rest is not explicitly mentioned, the encryption during transmission is supported.

## Notes
- It is important to clarify to customers that while data in transit can be encrypted, they should verify the encryption status of data at rest based on their specific configurations and requirements.
- Future inquiries regarding encryption should reference the provided documentation links for accurate information.