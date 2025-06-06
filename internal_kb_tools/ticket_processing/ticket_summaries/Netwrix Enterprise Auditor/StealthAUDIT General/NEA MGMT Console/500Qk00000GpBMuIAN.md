## Ticket Metadata
- **Ticket ID:** 500Qk00000GpBMuIAN
- **Case Number:** 423404
- **Status:** Closed - Resolved
- **Account/Company:** Oak Hill Advisors
- **Contact Name:** Douglas Kupcha
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA MGMT Console
- **Version:** 11.6

## Problem Description
The customer reported that SQL permission jobs on-premises were timing out and not finishing properly.

## Environment Details
- The issue occurred in a Netwrix Enterprise Auditor environment, specifically using version 11.6.
- The SQL jobs were running on-premises.

## Troubleshooting Steps
1. Reviewed SQL permission scan logs which indicated that jobs were running for extended periods (e.g., 1 hour and 1 minute).
2. Confirmed that permissions appeared to be correctly configured.
3. Engaged development team to analyze timeout issues and gather evidence from previous occurrences.
4. Discussed potential overlaps in job scheduling that could be causing conflicts.
5. Explored the need for capturing successful logins in addition to failures to better understand job performance.

## Root Cause
The root cause of the issue was identified as the need for an upgrade to utilize a hotfix for SQL Data Collector (DC). The existing configuration was insufficient to handle the job loads effectively, leading to timeouts.

## Solution
The issue was resolved by upgrading the system to implement the necessary hotfix for SQL DC. This upgrade improved the performance of the SQL permission jobs, allowing them to complete successfully without timing out.

## Notes
- It is important to monitor job scheduling to prevent overlaps that may hide underlying issues.
- Future implementations should consider capturing both successful and failed logins to provide a more comprehensive view of job performance.
- Ensure that the system is kept up to date with the latest patches and hotfixes to avoid similar issues in the future.