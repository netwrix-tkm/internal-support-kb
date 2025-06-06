## Ticket Metadata
- **Ticket ID:** 500Qk00000FcpSIIAZ
- **Case Number:** 420699
- **Status:** Closed - Resolved
- **Account/Company:** Horizon Media
- **Contact Name:** Angelo DiPietro
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Custom Reports
- **Version:** 11.5

## Problem Description
The customer reported receiving an error while attempting to run a file share report to locate folders and files named "HERSHEY." The error message indicated that the filename, directory name, or volume label syntax was incorrect.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT General
- **Product Version:** 11.5

## Troubleshooting Steps
1. The customer attempted to scan multiple folder shares but encountered thousands of error messages.
2. A comment suggested checking if the service account had local admin rights on the target machine.
3. The host management table was reviewed to ensure the OS type was set correctly.
4. The configuration of the job was expanded to check the UNC path settings.

## Root Cause
The issue was caused by the use of a drive letter instead of a UNC path for the share in the job configuration, which led to incorrect syntax errors when attempting to traverse directories.

## Solution
To resolve the issue, the following steps were taken:
1. The job configuration was accessed, and the Query Properties were expanded.
2. The UNC path was set instead of a drive letter for the share.
3. The connection was verified by clicking the three dots next to the UNC path.
4. The specific share in question was selected, and the path was added successfully.

## Notes
- Ensure that the service account has the necessary permissions on the target machine to avoid similar issues in the future.
- Always use UNC paths for network shares in job configurations to prevent syntax errors.
- Regularly verify the OS type in the host management table to ensure compatibility.