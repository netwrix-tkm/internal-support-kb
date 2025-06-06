## Ticket Metadata
- **Ticket ID:** 500Qk00000FhNKcIAN
- **Case Number:** 420916
- **Status:** Closed - Resolved
- **Account/Company:** Psomas
- **Contact Name:** Jonathan Ross
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Initial setup
- **Version:** 11.5

## Problem Description
The customer reported that the audit, sensitive data discovery, and activity features of the Netwrix software had become dilapidated and were no longer providing output. They requested a health check, potential updates, and assistance with various issues.

## Environment Details
- **Location:** United States (California)
- **Product Version:** 11.5
- **Age:** 11.7

## Troubleshooting Steps
1. Performed a light health check of the Netwrix Enterprise Auditor (NEA) and Netwrix Activity Monitor (NAM) applications.
2. Identified missing jobs in the Panzura Collections job group, specifically:
   - Open Access Job
   - Direct Permissions Job
   - Broken Inheritance Job
   - Content Job
   - Sensitive Data Job
3. Compared the Panzura Collections job group with the Windows Filers Collection Job group and noted the discrepancies.
4. Copied the missing jobs from the Windows Filers Collection to the Panzura Collection and updated the host lists to target the Panzura servers.
5. Ran the entire file system group to verify functionality.
6. Investigated an error with the Active Directory Integration (ADI) scan that prompted duplicate domains.
7. Resolved the duplicate domain error by configuring the ADI scan hosts list to target one domain controller per domain.
8. Identified communication issues with NAM agents over port 4498 and verified that the port was established and listening bidirectionally.
9. Discovered a bug related to NTLM authentication, which was resolved in version 7.0.3099, and created a new ticket (#00421953) for further investigation.

## Root Cause
The primary issue was that the Panzura Job Collection was not correctly configured to point to the Panzura hosts, lacking the necessary jobs that were present in the Windows file server job collection. Additionally, duplicate domains in the host management and a communication issue over port 4498 contributed to the overall malfunction.

## Solution
The issue was resolved by:
- Copying the missing jobs from the Windows Filers Collection to the Panzura Collection and updating the host lists to target the correct servers.
- Configuring the ADI scan to target one domain controller per domain to eliminate duplicate domain errors.
- Verifying and ensuring that port 4498 was properly configured for communication, while addressing the NTLM authentication bug in the latest software version.

## Notes
- Future health checks should include verifying job configurations across different collections to ensure all necessary jobs are present.
- Be aware of potential duplicate domain issues in host management, which can affect ADI scans.
- Ensure that all agents are able to communicate over the required ports, and keep software updated to avoid known bugs, such as the NTLM authentication issue.