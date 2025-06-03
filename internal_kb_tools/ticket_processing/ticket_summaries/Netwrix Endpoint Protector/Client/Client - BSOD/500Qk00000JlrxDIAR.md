```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000JlrxDIAR
- **Case Number:** 430521
- **Status:** Closed - Resolved
- **Account/Company:** Motorola Solutions
- **Contact Name:** Daniel Harris
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client - BSOD
- **Version:** EPPClient_ubuntu_18.04_v2.4.4.1004

## Problem Description
Linux clients running the latest version of the EPP-client were experiencing kernel panics when users attempted to sync files from a repository directory on their machines.

## Environment Details
- Affected clients were using the newest version of the EPP-client on Linux.

## Troubleshooting Steps
1. Collected initial reports from users experiencing crashes during sync operations.
2. Noted that one user found success by enabling trace logging and throttling the sync process.
3. Disabling parallelization was also reported as a workaround.
4. Engaged R&D for a potential fix and raised the priority of the issue.
5. Requested logs from the customer for further analysis.
6. Followed up with R&D and raised an ADO (Azure DevOps) ticket for tracking.
7. Requested a test client from R&D to validate the fix.
8. Provided a test build for the customer to evaluate.

## Root Cause
The issue was identified as a bug in the EPP-client that caused kernel panics during file sync operations under certain conditions, particularly when parallelization was enabled.

## Solution
The issue was resolved by providing the customer with a new client version:
- **Download Link:** [EPPClient_ubuntu_18.04_v2.4.4.1004](https://download.endpointprotector.com/linux_agent/EPPLinux_v2.4.4.1004/EPPClient_ubuntu_18.04_v2.4.4.1004_x86_64.tar.gz)

The customer confirmed that this version resolved the crashing issue.

## Notes
- Users experiencing similar issues should consider disabling parallelization or enabling trace logging as temporary workarounds until the updated client can be deployed.
- Ensure to keep track of any kernel panic logs for further analysis if similar issues arise in the future.
```