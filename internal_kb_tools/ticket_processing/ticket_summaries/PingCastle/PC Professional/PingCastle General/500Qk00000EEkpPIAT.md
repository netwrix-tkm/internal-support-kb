## Ticket Metadata
- **Ticket ID:** 500Qk00000EEkpPIAT
- **Case Number:** 417712
- **Status:** Closed - Resolved
- **Account/Company:** TowneBank
- **Contact Name:** Joe Johann
- **Product:** PingCastle
- **Component:** PC Professional
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer reported receiving an error message when running the scanner/zerologon test within Ping Castle. The specific error noted was "Error 2: c0000022".

## Environment Details
- **Platform:** PingCastle
- **Product Version:** 3.2.0.1

## Troubleshooting Steps
1. The customer was informed that the error code corresponds to STATUS_ACCESS_DENIED.
2. Clarification was provided regarding the lack of automation for the connection to AzureAD, which affects the scheduler.
3. Instructions were given to upload JSON reports using the command line with the following command:
   ```bash
   PingCastle.exe --api-flags to be set --upload-all-reports
   ```

## Root Cause
The error code "c0000022" indicates that the mitigation against the Zero Logon vulnerability is active, resulting in access being denied.

## Solution
The issue was resolved by confirming that the error was due to the active mitigation against Zero Logon, which is a security feature. No further action was required from the customer as the error was expected behavior under the current security settings.

## Notes
- The customer should be aware that the error is not indicative of a malfunction but rather a protective measure.
- Future users running similar tests should ensure they understand the implications of security mitigations that may affect test results.