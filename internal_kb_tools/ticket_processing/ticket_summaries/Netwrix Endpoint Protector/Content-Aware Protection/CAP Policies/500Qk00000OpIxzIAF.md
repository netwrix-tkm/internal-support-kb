## Ticket Metadata
- **Ticket ID:** 500Qk00000OpIxzIAF
- **Case Number:** 444138
- **Status:** Closed - Resolved
- **Account/Company:** Black Sesame Technologies
- **Contact Name:** Tai Ting Tseng
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** Client: 6.2.4.2000, Server: 5.9.4.1, OS: Windows 11

## Problem Description
The customer reported that when the Content-Aware Protection (CAP) policy is enabled for AnyDesk, the newly downloaded AnyDesk executable fails to run. The customer intended to block only file transfers while allowing the application to function normally.

## Environment Details
- **Client Version:** 6.2.4.2000
- **Server Version:** 5.9.4.1
- **Operating System:** Windows 11

## Troubleshooting Steps
1. Assisted the customer in reproducing the issue while gathering logs.
2. Examined the relevant policy settings.
3. Inquired if the policy had ever functioned with AnyDesk in a test environment.
4. Suggested the customer remove the computer from the policy, which allowed AnyDesk to run.
5. Noted that AnyDesk fails to launch when the policy is reactivated.
6. Requested the customer to upload logs for further inspection.
7. Discussed the inclusion of EXE, SYS, and DLL files in the policy settings with the customer.

## Root Cause
The CAP policy was configured to block file transfers and incident reporting, which inadvertently prevented AnyDesk from launching. The policy settings included all file types, including executable files, which caused AnyDesk to be blocked.

## Solution
The issue was resolved by advising the customer to uncheck the selection box for EXE, SYS, and DLL file types in the CAP policy settings. This adjustment allowed AnyDesk to run while still blocking file transfers. The customer was also encouraged to submit a feature request if they needed to block specific file types without affecting application functionality.

## Notes
- It is important to avoid enabling all file types in the CAP policy, as this can lead to unintended blocking of essential applications.
- Customers should be informed that while blocking file types can enhance security, it may also restrict the functionality of legitimate applications like AnyDesk.
- If the customer requires specific file types to be blocked while allowing applications to run, they should consider submitting a feature request for more granular control over the CAP settings.