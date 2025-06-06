## Ticket Metadata
- **Ticket ID:** 500Qk00000HrPHrIAN
- **Case Number:** 425917
- **Status:** Closed - Resolved
- **Account/Company:** Metropolitan State University of Denver
- **Contact Name:** Latonya Frank
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.6

## Problem Description
The customer reported that DLP scans in StealthAUDIT were returning no data, despite the presence of files containing PII on their servers. Previously, they had successfully located PII using these scans.

## Environment Details
- **Software Installed:** 
  - StealthAUDIT V11.5
  - Stealthbits Activity Monitor V6.0.1111
- **Operating System:** Not specified, but PowerShell commands were used for troubleshooting.

## Troubleshooting Steps
1. The support technician requested information on any error messages from the DLP job.
2. The customer was asked to provide a list of installed software using the following PowerShell command:
   ```powershell
   Get-CimInstance -Class Win32_Product | Where-Object {($_.Name -Like "Stealth*" -or $_.Name -like "Netwrix*" -or $_.Name -like "Postg*" -or $_.Name -like "Python*")} -ErrorAction SilentlyContinue
   ```
3. A meeting was scheduled to discuss the issue further.
4. During the meeting, it was identified that the "Sensitive Data" component was not installed, which was necessary for the DLP scans to function correctly.

## Root Cause
The root cause of the issue was determined to be the absence of the "Sensitive Data" component in the StealthAUDIT installation, which is required for the DLP scans to identify and report PII.

## Solution
The support technician downloaded and installed the "Sensitive Data" component. After installation, the customer was instructed to run the SEK System Scan and the Bulk Import before executing the DLP scans again. Following these steps, the DLP scans successfully returned the expected data.

## Notes
- Ensure that the "Sensitive Data" component is installed as part of the initial setup for DLP scans in StealthAUDIT.
- Always verify the installation of necessary components when troubleshooting similar issues to avoid delays in resolution.