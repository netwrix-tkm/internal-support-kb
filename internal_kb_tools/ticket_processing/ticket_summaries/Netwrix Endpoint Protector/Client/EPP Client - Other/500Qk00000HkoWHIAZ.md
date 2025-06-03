## Ticket Metadata
- **Ticket ID:** 500Qk00000HkoWHIAZ
- **Case Number:** 425760
- **Status:** Closed - Resolved
- **Account/Company:** Casio India Co Pvt Ltd
- **Contact Name:** Praveen Praveen Sinha
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** EPP Client - Other
- **Version:** NONE

## Problem Description
The customer reported that the internet connection stopped working on a server where the Netwrix Endpoint Protector (EPP) client was installed. After removing the EPP client, the internet connectivity was restored. The customer requested an explanation for why the EPP client caused the internet access issue, especially since their policies were set to "report only."

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Build Number:** 5941

## Troubleshooting Steps
1. The customer initially reported the issue via email, indicating that the EPP client was causing internet connectivity problems.
2. The support team requested a call to troubleshoot the issue in real-time.
3. The customer confirmed that removing the EPP client resolved the internet connectivity issue.

## Root Cause
The root cause of the internet connectivity issue was identified as a conflict or misconfiguration related to the EPP client. Although the customer's policies were set to "report only," it appears that the EPP client still interfered with network access on the server.

## Solution
The issue was resolved by removing the EPP client from the affected server, which restored internet connectivity. The customer was advised to monitor the situation and consider re-evaluating the EPP client settings or configurations if they wish to reinstall it in the future.

## Notes
- It is important to ensure that the EPP client is properly configured to avoid conflicts with network access.
- Customers should be informed that even with "report only" policies, the EPP client may still impact network functionality.
- Future installations of the EPP client should be tested in a controlled environment to identify potential issues before deployment in production.