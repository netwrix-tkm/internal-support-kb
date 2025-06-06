# Knowledge Base Reference Guide: Troubleshooting NEA for Nasuni Reports Issues

## Overview

This guide focuses on troubleshooting issues related to the **Reports** feature in **Netwrix Enterprise Auditor (NEA) for Nasuni**. These issues often arise during analysis tasks, such as the 'Resolve links' task, and can impact the accuracy and functionality of reports generated from Nasuni filers and DFS namespaces. Understanding and resolving these problems is critical for ensuring the integrity of audit data and maintaining customer satisfaction.

## Technical Background

### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, including file servers, DFS namespaces, and Nasuni filers.
- **Nasuni:** A cloud-based file storage solution that integrates with NEA for auditing purposes.
- **FSAA System Scans Job:** A foundational job that scans file systems and DFS namespaces to collect audit data.
- **SA_FSDFS_Links Table:** A database table that stores links between file system objects and DFS namespaces, including Nasuni entries.
- **Resolve Links Analysis Task:** A job that processes data in the SA_FSDFS_Links table to resolve relationships between file system objects and DFS namespaces.

### Common Error
- **"Invalid length parameter passed to the LEFT or SUBSTRING function":** This SQL error typically indicates malformed or unexpected data in the SA_FSDFS_Links table, which prevents proper processing during the 'Resolve links' task.

## Issue Recognition & Triage

### Symptoms
- Error message: "Invalid length parameter passed to the LEFT or SUBSTRING function. This statement has been terminated."
- Occurs during the 'Resolve links' analysis task after running the FSAA System Scans job.
- May follow successful execution of other tasks, such as the 'Nasuni analysis task.'

### Priority Assessment
- **High Priority:** If the error prevents critical audit data from being processed or impacts reporting functionality.
- **Medium Priority:** If the error is isolated to specific entries and does not affect overall system performance.

## Diagnostic Methodology

### Systematic Approach
1. **Reproduce the Issue:**
   - Run the FSAA System Scans job followed by the Nasuni analysis task and the Resolve links analysis task.
   - Confirm whether the error occurs consistently.

2. **Examine the SA_FSDFS_Links Table:**
   - Check for malformed or unexpected entries, particularly those related to Nasuni filers and DFS namespaces.

3. **Verify Permissions:**
   - Ensure the scan account has appropriate permissions on DFS hosts and Nasuni filers.

4. **Review Logs:**
   - Analyze job execution logs for additional context or related errors.

5. **Check Product Version:**
   - Confirm the NEA version and check for available updates or hotfixes.

## Information Collection

### Customer Questions
- What version of NEA is currently installed?
- Have there been any recent changes to the DFS namespaces or Nasuni filers?
- Are there other errors or issues observed during job execution?

### Logs and Data to Collect
- Execution logs for the FSAA System Scans, Nasuni analysis task, and Resolve links analysis task.
- Entries from the SA_FSDFS_Links table, particularly those related to Nasuni filers.
- Permissions configuration for the scan account on DFS hosts and Nasuni filers.

## Common Scenarios & Solutions

### Scenario 1: SQL Error During 'Resolve Links' Task
- **Symptoms:** "Invalid length parameter passed to the LEFT or SUBSTRING function."
- **Root Cause:** Malformed data in the SA_FSDFS_Links table.
- **Resolution:**
  - Apply the hotfix (Update 11.6.0.139) to address the defect in the 'Resolve links' task.
  - Verify the integrity of the SA_FSDFS_Links table after applying the update.

### Scenario 2: Permissions Issues
- **Symptoms:** Errors such as "Path not found scanning" or "Error getting Security descriptor for share."
- **Root Cause:** Insufficient permissions for the scan account.
- **Resolution:**
  - Ensure the scan account has full read access to DFS namespaces and Nasuni filers.
  - Test access manually to confirm permissions.

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000LqctFIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LqctFIAR/view)
- **Initial Symptoms:** Customer reported an error during the 'Resolve links' analysis task: "Invalid length parameter passed to the LEFT or SUBSTRING function."
- **Diagnostic Steps:**
  1. Verified entries in the SA_FSDFS_Links table for Nasuni and non-Nasuni data.
  2. Reproduced the error by running the FSAA System Scans, Nasuni analysis task, and Resolve links analysis task.
  3. Investigated permissions for the scan account on DFS hosts.
- **Key Information:** The error was linked to malformed data in the SA_FSDFS_Links table.
- **Resolution:** Applied hotfix (Update 11.6.0.139), which resolved the issue.
- **Key Takeaways:**
  - Always check for product updates when encountering SQL errors.
  - Validate table data integrity during troubleshooting.
- **Efficiency Improvements:** Automate validation of SA_FSDFS_Links table entries during job execution.

## Best Practices & Tips

1. **Regular Updates:** Ensure NEA is updated to the latest version to benefit from bug fixes and performance improvements.
2. **Permissions Validation:** Periodically verify scan account permissions on DFS namespaces and Nasuni filers.
3. **Proactive Monitoring:** Implement monitoring for job execution logs to detect errors early.
4. **Customer Communication:** Clearly explain the root cause and resolution steps to customers, emphasizing the importance of updates and permissions.
5. **Documentation:** Maintain detailed records of troubleshooting steps and resolutions for future reference.

## Escalation Guidelines

### Criteria for Escalation
- The issue persists after applying the latest hotfix or update.
- The error impacts critical audit functionality or customer operations.
- Additional defects or errors are identified during troubleshooting.

### Escalation Procedure
1. Collect all relevant logs, data, and customer environment details.
2. Document the troubleshooting steps taken and their outcomes.
3. Submit the case to the development team with a detailed analysis and request for further investigation.
4. Communicate escalation status and expected timelines to the customer.

End of document.