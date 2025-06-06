## Ticket Metadata
- **Ticket ID:** 500Qk00000IHTxkIAH
- **Case Number:** 427002
- **Status:** Closed - Resolved
- **Account/Company:** City National Bank (CNB)
- **Contact Name:** Kim Holmes
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Custom Reports
- **Version:** 11.6

## Problem Description
The customer reported that a customized report in StealthAUDIT was failing due to a specialized table not being created after migrating scanning from an Azure server to two new on-premises servers.

## Environment Details
- The software version in use was Netwrix Enterprise Auditor (NEA) version 11.6.0.11.
- The issue arose after a fresh installation and migration of the scanning environment.

## Troubleshooting Steps
1. The customer confirmed that the necessary attribute 'extensionAttribute9' was not being collected by the Active Directory Inventory (ADI) job.
2. The support team requested additional information regarding the impact of the issue, affected users, and previous troubleshooting steps taken.
3. The customer provided the requested logs and outputs from PowerShell scripts to assist in diagnosing the issue.
4. A web meeting was scheduled to further investigate the problem and confirm the current software setup.

## Root Cause
The root cause of the issue was identified as the 'extensionAttribute9' attribute not being collected by the Active Directory Inventory (1-AD_Scan) job, which is essential for the customized report to function correctly.

## Solution
The support team corrected the attribute collection settings to ensure that 'extensionAttribute9' was included in the ADI job. After making this adjustment, the team initiated a mock schedule scan and staged jobs for JOB_AD_WeakPasswords and JOB_AD_WeakPasswords_Custom, which needed to run after the completion of the 1-AD_Scan job.

## Notes
- The customer confirmed that the issue was resolved successfully, and the report generation was functioning as expected after the changes were implemented.
- It is important to ensure that all necessary attributes are configured correctly during migration to prevent similar issues in the future.
- The ticket was closed with a reminder that it can be reopened within 30 days if any related issues arise.