```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000NMEvCIAX
- **Case Number:** 440079
- **Status:** Closed - Resolved
- **Account/Company:** Oak Hill Advisors
- **Contact Name:** Giri Kowalke
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Windows File Systems
- **Feature:** Data Collection
- **Version:** 11.6

## Problem Description
The customer reported that their FSAA and FS_SEEK collection jobs were crashing ungracefully, leaving behind a `running.lck` file and causing a .NET crash on their NEA server. This issue had been occurring since the start of the project but was only identified after a deep dive into the collected data.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Product Version:** 11.6
- **Build Number:** 11.6.0.66
- The issue was not reproducible in the support technician's lab environment, indicating it was specific to the client's setup.

## Troubleshooting Steps
1. Reviewed logs and screenshots of the .NET error provided by the client.
2. Attempted to recreate the issue in a lab environment but did not experience the same crashes.
3. Verified that Crowdstrike was not blocking any processes related to the collection jobs.
4. Upgraded to the latest versions of NEA and SDD, but the .NET error persisted.

## Root Cause
The root cause of the issue was identified as a bug in the software that was addressed in a hotfix released on March 20, 2025. The specific conditions under which the FSAA and FS_SEEK jobs crashed were not replicated in the support lab, indicating an environment-specific issue.

## Solution
The issue was resolved by applying the hotfix that was published on March 20, 2025. The customer was advised to deploy this hotfix, which corrected the underlying problem causing the .NET crashes during the collection jobs.

## Notes
- Ensure that all clients are informed about the importance of applying hotfixes promptly to avoid similar issues.
- Monitor the performance of FSAA and FS_SEEK collection jobs after applying updates to ensure stability.
- Document any environment-specific configurations that may contribute to issues for future reference.
```