## Ticket Metadata
- **Ticket ID:** 500Qk00000KHPcnIAH
- **Case Number:** 431262
- **Status:** Closed - Resolved
- **Account/Company:** Arity
- **Contact Name:** James Ceart
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** 6.2.4.1006

## Problem Description
The customer reported discrepancies in the blocking of data transfers, particularly with CCN and PDFs, across various testing methods. They noted that certain sensitive data was not being blocked as expected, leading to potential data leakage.

## Environment Details
- Agent version: 6.1.0.600 (upgraded to 6.2.4.1006 during troubleshooting)
- Testing methods included Clipboard, HTTPS Post, HTTPS File Upload, HTTP Post, HTTP File Upload, FTP File Upload, and file sharing via OneDrive and Google Drive.

## Troubleshooting Steps
1. Conducted tests across multiple data transfer methods to identify discrepancies in blocking.
2. Enabled Stealthy DPI and Meta Data Scanning.
3. Created and tested a new policy to block sensitive data uploads.
4. Checked the file Allow List and ensured Network Share was enabled.
5. Collected logs using the support tool.
6. Held multiple Microsoft Teams meetings with the customer to gather information and perform live tests.
7. Reviewed and adjusted policy settings to ensure proper blocking of sensitive data.

## Root Cause
The issue stemmed from the configuration of the policies. Initially, the policies did not include OneDrive as an exit point, which allowed uploads to proceed without being blocked. Additionally, previously uploaded files may have been cached by OneDrive, leading to confusion about whether the blocking was functioning correctly.

## Solution
The customer successfully created a new policy that effectively blocked uploads of certain modified PDFs to OneDrive. This policy was prioritized and set to include OneDrive as an exit point. After testing, the uploads of sensitive data were successfully blocked as intended.

## Notes
- Ensure that policies are correctly configured to include all relevant exit points to prevent similar issues.
- Advise customers to test with new files that have not been previously uploaded to avoid cache-related issues.
- Regularly review and update policies to adapt to changes in data transfer methods and security requirements.