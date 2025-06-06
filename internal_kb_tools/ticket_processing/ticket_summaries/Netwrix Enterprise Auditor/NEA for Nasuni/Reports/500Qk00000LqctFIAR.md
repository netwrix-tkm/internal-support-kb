## Ticket Metadata
- **Ticket ID:** 500Qk00000LqctFIAR
- **Case Number:** 435774
- **Status:** Closed - Resolved
- **Account/Company:** Crestron Electronics
- **Contact Name:** Dean Bardowell
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA for Nasuni
- **Feature:** Reports
- **Version:** 11.5.0.269

## Problem Description
The customer reported an error during the 'Resolve links' analysis task on the FSAA System Scans job, specifically receiving the message: "Invalid length parameter passed to the LEFT or SUBSTRING function. This statement has been terminated." This issue arose after successfully running the '3. Nasuni analysis task' on the FSAA Bulk Import job.

## Environment Details
- The SA_FSDFS_Links table contained entries from Nasuni filers and DFS namespaces.
- The error occurred after running the '0-FSDFS System Scans' job for the first time.

## Troubleshooting Steps
1. Verified the entries in the SA_FSDFS_Links table for both Nasuni and non-Nasuni entries.
2. Attempted to reproduce the error by running the following jobs in sequence:
   - "0-FSDFS System Scans"
   - "3. Nasuni analysis task"
   - "1. Resolve links analysis task"
3. Observed the error message during the execution of the 'Resolve links' task.
4. Investigated permissions for the scan account on the identified DFS hosts.

## Root Cause
The root cause of the issue was identified as a defect in the product related to how the Nasuni entries were being processed during the 'Resolve links' analysis task. The error was triggered by invalid parameters being passed to SQL functions due to the structure of the data in the SA_FSDFS_Links table.

## Solution
A hotfix was released (Update 11.6.0.139) that addressed the issue with the 'Resolve links' analysis task. After applying the hotfix, the error message was no longer observed during the execution of the task.

## Notes
- After the hotfix was applied, other unrelated FSAA errors were still present, such as "Path not found scanning" and "Error getting Security descriptor for share."
- It is important to ensure that permissions for the scan account are correctly set up to avoid similar issues in the future.
- Continuous monitoring of the system after applying updates is recommended to catch any residual or new issues.