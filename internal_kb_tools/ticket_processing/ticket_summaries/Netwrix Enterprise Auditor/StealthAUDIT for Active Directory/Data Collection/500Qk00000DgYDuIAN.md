## Ticket Metadata
- **Ticket ID:** 500Qk00000DgYDuIAN
- **Case Number:** 416341
- **Status:** Closed - Resolved
- **Account/Company:** Fair Isaac Corporation (FICO)
- **Contact Name:** Prashanth Varma Sammeta
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Active Directory
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported errors occurring in nine specific jobs related to Active Directory data collection. The jobs affected were:
1. AD_Scan
2. AD_ChangeTracking
3. AD_DCSummary
4. AD_DomainControllers
5. AD_DomainInfo
6. AD_DSRM
7. AD_ExtraDomainAttributes
8. AD_Lockouts
9. AD_TimeSync

The customer provided log files for these jobs for further analysis.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Issue Type:** Incorrect configuration: target server software

## Troubleshooting Steps
1. Reviewed the log files provided by the customer for the nine jobs.
2. Attempted to rerun the AD_Scan job to check if the issue persisted.
3. Investigated host accessibility and permissions for the remaining jobs that were dependent on the AD_Scan results.

## Root Cause
The primary issue was identified as incorrect configuration related to the target server software. The AD_Scan job had issues that were resolved by rerunning it, while the other jobs encountered problems due to dependencies on the AD_Scan results and issues with host accessibility and permissions.

## Solution
The issue with the AD_Scan job was resolved by simply rerunning the scan. Once the AD_Scan job completed successfully, the remaining jobs were able to function correctly as they were dependent on the results of the AD_Scan. It was also necessary to ensure that the host accessibility and permissions were correctly configured for the other jobs to avoid similar issues in the future.

## Notes
- Ensure that all jobs dependent on the AD_Scan are monitored closely after any changes to configuration or permissions.
- Regularly verify host accessibility and permissions to prevent similar issues from arising in the future.
- Document any changes made to configurations to aid in troubleshooting if similar issues occur.