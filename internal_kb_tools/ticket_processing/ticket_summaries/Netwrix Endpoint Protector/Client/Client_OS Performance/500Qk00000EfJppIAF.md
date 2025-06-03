## Ticket Metadata
- **Ticket ID:** 500Qk00000EfJppIAF
- **Case Number:** 418536
- **Status:** Closed - Resolved
- **Account/Company:** ZS
- **Contact Name:** Manpreet Singh
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** 5941

## Problem Description
The customer reported that `SSLSplit.exe` was crashing on 10% of machines in the ZS environment, specifically those running EPP client version 6.2.2.1 with Stealthy DPI enabled. This was a significant increase from the previous version (5.9.3.5), where only 1% of machines experienced crashes. The crashes occurred approximately once per week on each affected machine.

## Environment Details
- **EPP Client Version:** 6.2.2.1
- **Previous EPP Client Version:** 5.9.3.5
- **Feature Enabled:** Stealthy DPI

## Troubleshooting Steps
1. **Monitoring Review:** The monitoring team assessed the crash frequency and patterns.
2. **Version Comparison:** A comparison was made between the crash rates of EPP versions 5.9.3.5 and 6.2.2.1.
3. **Escalation:** The issue was escalated for further investigation due to its impact on a significant number of machines.
4. **Development Investigation:** Developers investigated potential causes, including thread safety issues related to the `libevent` library used by DPI.
5. **Testing:** Intensive testing was conducted to reproduce the crash and identify the root cause.

## Root Cause
The root cause of the crashes was identified as a potential race condition related to the thread safety of the `libevent` library, which was not being used in a thread-safe manner. This issue was exacerbated by the new features introduced in the 6.2.2.1 version.

## Solution
The issue was resolved by updating the EPP client to version 5941, which included improvements and fixes related to the identified thread safety issues. The customer confirmed that the update resolved the crashing problem, allowing the ticket to be closed.

## Notes
- It is important to monitor the performance of new versions closely, especially when enabling features like Stealthy DPI, as they may introduce unforeseen issues.
- Future updates should include thorough testing for thread safety in libraries used by critical components to prevent similar issues.