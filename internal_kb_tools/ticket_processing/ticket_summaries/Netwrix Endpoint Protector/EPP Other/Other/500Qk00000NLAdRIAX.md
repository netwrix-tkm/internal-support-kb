## Ticket Metadata
- **Ticket ID:** 500Qk00000NLAdRIAX
- **Case Number:** 439986
- **Status:** Closed - Resolved
- **Account/Company:** Helo.ai
- **Contact Name:** Qazi Amir
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported that they were unable to open the WINMAN application when the Netwrix Endpoint Protector (EPP) was installed on their client machine. After removing EPP, the application worked properly, indicating a conflict with the EPP installation.

## Environment Details
- The issue was specifically noted to occur on a Windows environment.
- The Advanced Printer and MTP Scanning option was suspected to be causing the problem.

## Troubleshooting Steps
1. Confirmed that the issue occurred only when EPP was installed.
2. Suggested checking if "Advanced Printer and MTP Scanning" was enabled in the global settings.
3. Advised the customer to disable the Advanced Printer and MTP Scanning option.
4. Instructed the customer to update the policies on the EPP client and restart the computer.
5. Verified if the issue persisted after disabling the DPI option.
6. Conducted a remote connection to further investigate the issue.
7. Created an Advanced Scanning exception for the process name associated with WINMAN.

## Root Cause
The WINMAN application was not starting due to the Advanced Scanning option in the Netwrix Endpoint Protector, which was interfering with the application's normal operation.

## Solution
The issue was resolved by applying an Advanced Scanning exception for the process name associated with the WINMAN application. This allowed the application to start successfully without interference from the EPP.

## Notes
- Ensure that any applications that may conflict with EPP are added to the Advanced Scanning exceptions to prevent similar issues in the future.
- It is advisable to check for multiple process names used by applications, as the issue may persist if not all relevant process names are included in the exceptions.