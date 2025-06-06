## Ticket Metadata
- **Ticket ID:** 500Qk00000GqfqkIAB
- **Case Number:** 423489
- **Status:** Closed - Resolved
- **Account/Company:** Idaho State Controllers Office
- **Contact Name:** Phil Cook
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that most of their reports within the Netwrix system were not displaying current data. Specific issues included outdated activity logs for File System, Exchange, and Active Directory reports.

## Environment Details
- **Netwrix Access Information Center (AIC)** was being used for data collection.
- The system was transitioning from StealthDefend to StealthIntercept agents.

## Troubleshooting Steps
1. Verified the last activity dates in various reports:
   - File Folder Deletions: Last activity on 6/27/24
   - Permission Changes: Last activity on 5/26/23
   - Exchange Mailbox Logons: No reports in the last week
   - AD Activity reports: Last activity from 1/2023
2. Investigated the FileSystem Activity (FSAC) data not being updated.
3. Checked for access denied errors in the Network share path for NAM archives.
4. Reviewed logs in the expected directory but found them missing.
5. Noted that a bulk import was needed for FSAA System Scans.
6. Identified an error in the Main FileSystem SEEK scan due to file path length exceeding Windows limits.

## Root Cause
- The primary issue was an access denied error for the Network share path for NAM archives, which prevented the FSAC data from being updated. Additionally, the Main FileSystem SEEK scan failed due to a file path length exceeding the Windows maximum of 254 characters.

## Solution
1. Corrected the service account details within NAM and granted the necessary access to the Share and NTFs path on the NAM/NEA host.
2. Disabled the Proxy option for jobs to ensure archived events would be pushed to the NEA host.
3. Queued the necessary bulk import for FSAA System Scans.
4. Enabled long path support in the Windows Registry:
   ```plaintext
   HKLM\SYSTEM\CurrentControlSet\Control\FileSystem
   - Name: LongPathsEnabled
   - Value: 1
   ```
5. Limited the host PageFile to the largest drive (D:) to prevent OS mishandling of system-controlled expansion.
6. Informed the customer that a reboot of the NEA host was required for the changes to take effect.

## Notes
- Ensure that the NEA host is rebooted after making registry changes for long path support to take effect.
- Monitor the system after the next scheduled scan to confirm that the settings changes have resolved the data update issues.
- For future cases, verify service account permissions and access to network shares as a first step in troubleshooting similar issues.