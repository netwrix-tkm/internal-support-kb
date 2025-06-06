## Ticket Metadata
- **Ticket ID:** 500Qk00000HcpCiIAJ
- **Case Number:** 425418
- **Status:** Closed - Resolved
- **Account/Company:** Marsh & McLennan Companies
- **Contact Name:** Kay Groth
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Database
- **Version:** 11.6

## Problem Description
The customer reported an exception (EOleException) indicating an "Invalid object name 'SA_1-AD_Scan_DEFAULT'" after upgrading from version 11.5 to 11.6 while attempting to run the ADI Scan.

## Environment Details
- **Table Name:** SPEgine
- The issue arose post-upgrade to version 11.6 of the Netwrix Enterprise Auditor.

## Troubleshooting Steps
1. The customer confirmed that the table 'SA_1-AD_Scan_DEFAULT' existed prior to the upgrade.
2. The customer deleted the table 'SA_1-AD_Scan_DEFAULT' in an attempt to resolve the issue.
3. The job was rerun multiple times to verify if the issue persisted.

## Root Cause
The root cause of the issue was not explicitly identified; however, it was noted that the table 'SA_1-AD_Scan_DEFAULT' was present before the upgrade and became invalid post-upgrade, leading to the exception being thrown.

## Solution
The issue was resolved after the customer deleted the problematic table and reran the job. The job began to behave normally again, indicating that the deletion of the table resolved the exception.

## Notes
- It is important to ensure that all necessary tables are backed up before performing upgrades to avoid data loss.
- Future upgrades should be tested in a staging environment to identify potential issues before applying them to production systems.
- Monitor the system closely after upgrades for any unexpected behavior related to database objects.