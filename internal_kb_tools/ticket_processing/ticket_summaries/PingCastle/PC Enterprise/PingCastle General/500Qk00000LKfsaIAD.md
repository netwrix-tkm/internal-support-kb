# Ticket Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000LKfsaIAD
- **Case Number:** 434352
- **Status:** Closed - Resolved
- **Account/Company:** HP INC
- **Contact Name:** Christopher Keil
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3.0.11

## Problem Description
The customer reported that PingCastle was not collecting Azure data during scans, resulting in no Azure data being populated in the reports when using a standard license RTU key.

## Environment Details
- PingCastle version: 3.3.0.11
- License type: Standard RTU key
- Required permissions: Global Admin privileges for the scan account

## Troubleshooting Steps
1. Installed PingCastle version 3.3.0.11.
2. Configured the scan using an enterprise license key.
3. Ran the Azure AD scan using the command-line version (pingcastle.exe).
4. Ensured the scan account had Global Admin privileges.
5. Reviewed the scan results to verify if Azure data populated correctly.

## Root Cause
The issue was caused by insufficient privileges for the scan account. PingCastle requires Global Admin privileges to successfully collect Azure data and populate indicators in the report. Tests confirmed that accounts with lower privileges resulted in incomplete or zero-score reports.

## Solution
The customer confirmed that using an account with Global Admin privileges resolved the issue. After switching to a Global Admin account, the scan was able to collect Azure data and populate indicators as expected. The ticket was closed after verifying that the resolution was effective and no further issues were reported.

## Notes
- Ensure that the scan account has Global Admin privileges when running Azure scans with PingCastle.
- The problem was not related to the PingCastle version or license type, as the same behavior was observed across multiple builds and configurations.
- Future users should be aware that insufficient permissions can lead to incomplete scan results.