## Ticket Metadata
- **Ticket ID:** 500Qk00000LbGbFIAV
- **Case Number:** 435056
- **Status:** Closed - Resolved
- **Account/Company:** Provable Labs
- **Contact Name:** Ruben de Vries
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** DPI - Other
- **Version:** 5.1

## Problem Description
The customer reported performance issues with the Netwrix Endpoint Protector (EPP) Client, specifically that the EppClient process was consuming excessive CPU resources (100-150%) during standard disk operations, such as using version control (git) and code editors (VsCode/IntelliJ). This high CPU usage was causing noticeable slowdowns in workstation performance.

## Environment Details
- The majority of the staff are software engineers.
- The issue was observed during standard operations that are not typically disk-intensive.

## Troubleshooting Steps
1. Analyzed client logs to identify the cause of high CPU usage.
2. Recommended the customer to deselect the "Github Client" from the CAP policy under Exit Point.
3. Suggested selecting "Git" under the Policy Denylist > Source Code > Restricted Apps.
4. Proposed adding specific file paths to the Allowlist > File Location to potentially improve performance.
5. Awaited confirmation from the customer regarding the resolution of the issue.

## Root Cause
The root cause of the performance issue was identified as the EppClient scanning a large number of git files, which led to excessive CPU usage during routine operations.

## Solution
The issue was resolved by:
- Deselecting the "Github Client" from the CAP policy.
- Selecting "Git" under the Policy Denylist.
- Optionally adding specific file paths to the Allowlist to reduce the number of files being scanned by the EppClient.

These adjustments significantly reduced the CPU usage and improved overall workstation performance.

## Notes
- It is important to monitor the performance after making configuration changes to ensure that the desired improvements are achieved.
- Future users experiencing similar issues should consider reviewing the CAP policy settings and the files being scanned by the EppClient to optimize performance.