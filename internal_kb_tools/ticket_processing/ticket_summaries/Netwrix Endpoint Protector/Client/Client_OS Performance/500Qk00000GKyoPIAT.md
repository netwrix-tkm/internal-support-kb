```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GKyoPIAT
- **Case Number:** 422308
- **Status:** Closed - Resolved
- **Account/Company:** AmSafe Bridport
- **Contact Name:** Pabasara Ratnayake
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** Not specified

## Problem Description
The performance of endpoint devices dropped severely when the Endpoint Protector client was installed during a proof of concept (POC). This issue was observed across all devices used for testing.

## Environment Details
- The issue affected multiple projects, with specific performance degradation noted when using Microsoft Visual Studio.

## Troubleshooting Steps
1. Initial reports indicated that the Endpoint Protector client was causing performance issues.
2. A meeting was scheduled with the customer to discuss the problem and gather logs.
3. Specific processes were added to the exception list to mitigate the performance impact.
4. Testing was conducted on the customer's PC, where it was confirmed that Visual Studio was functioning correctly after adjustments.
5. Further testing was requested on additional computers to ensure the solution was effective across different environments.

## Root Cause
The performance drops were caused by the Endpoint Protector client interfering with system processes, particularly affecting applications like Microsoft Visual Studio. The client required specific processes to be whitelisted to function optimally without degrading system performance.

## Solution
The issue was resolved by adding necessary processes to the exception list of the Endpoint Protector client. This adjustment allowed Visual Studio and other applications to operate without performance degradation. The customer confirmed that the solution worked for one specific project, but further testing was needed for other projects.

## Notes
- It is important to identify and add any additional processes that may be affected by the Endpoint Protector client in future cases.
- Continuous monitoring and testing across different projects are recommended to ensure that performance issues do not reoccur.
- A follow-up meeting was suggested to address any remaining issues related to other projects.
```