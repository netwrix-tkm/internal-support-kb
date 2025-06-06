## Ticket Metadata
- **Ticket ID:** 500Qk00000OvsAjIAJ
- **Case Number:** 444514
- **Status:** Closed - Resolved
- **Account/Company:** Octapharma
- **Contact Name:** Brian Hill
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported an error during the installation of PingCastle, specifically encountering error code 26201 when attempting to install via MSI without the necessary prerequisites.

## Environment Details
- **Installation Method:** MSI installer
- **Prerequisites:** Not installed prior to the attempt

## Troubleshooting Steps
1. Verified the installation method was correct (MSI).
2. Attempted to install PingCastle without any prerequisites.
3. Reviewed error code 26201 for potential causes.
4. Confirmed that no prior installations or dependencies were present.

## Root Cause
The installation error (code 26201) was caused by the absence of SQL Server Management Studio (SSMS), which is a prerequisite for running the MSI installer for PingCastle Enterprise.

## Solution
The issue was resolved by installing SQL Server Management Studio (SSMS) on the system. After the installation of SSMS, the PingCastle installation proceeded successfully without any errors.

## Notes
- Ensure that all prerequisites, including SSMS, are installed before attempting to install PingCastle to avoid similar issues in the future.
- It may be beneficial to include a checklist of prerequisites in the installation documentation for PingCastle to assist users in avoiding installation errors.