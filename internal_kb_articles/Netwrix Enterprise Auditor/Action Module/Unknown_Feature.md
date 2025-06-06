# Knowledge Base Reference Guide: Troubleshooting File System Copy Action Issues in Netwrix Enterprise Auditor

## Overview

The File System Copy Action in Netwrix Enterprise Auditor's Action Module is a critical feature that automates the copying of files from a source location to a destination. Proper configuration and execution of this feature are essential for ensuring data integrity and operational efficiency. This guide provides a systematic approach to diagnosing and resolving issues related to the File System Copy Action, with a focus on common problems, troubleshooting methodologies, and best practices.

---

## Technical Background

### Key Concepts
- **File System Copy Action**: A feature in the Action Module that facilitates automated file transfers between source and destination paths.
- **Temporary Folder (`fsam.tmp`)**: A staging area where files are temporarily created before being transferred to the destination.
- **UNC Paths**: Universal Naming Convention paths (e.g., `\\ServerName\ShareName`) used to specify network locations.
- **Source Table**: A configuration element that defines the files and folder structure to be copied.

### System Context
- The File System Copy Action relies on accurate path definitions and folder structures to execute successfully.
- Temporary files are created in the `fsam.tmp` folder during the copy process. If the process encounters errors, these files may be deleted without reaching the destination.

---

## Issue Recognition & Triage

### Symptoms
- Files are created in the `fsam.tmp` folder but are not transferred to the destination.
- Temporary files are deleted every 1-2 minutes without any files appearing in the destination folder.
- The issue persists regardless of configuration options such as overwrite, terminate, retry, and batching.

### Categorization
- **Severity**: Medium to High (depending on the criticality of the file transfer operation).
- **Priority**: High for production environments where file transfers are time-sensitive.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Configuration**:
   - Confirm that both source and destination paths are specified as full UNC paths.
   - Check the source table for completeness, including folder structure definitions.

2. **Reproduce the Issue**:
   - Attempt to replicate the problem in a controlled environment using the same configuration.

3. **Analyze Logs**:
   - Review logs for errors or warnings related to file creation, deletion, or path resolution.

4. **Isolate Variables**:
   - Test with different source and destination paths to rule out environmental factors.

5. **Escalate if Necessary**:
   - If the issue cannot be resolved through configuration adjustments, escalate to the development team with detailed logs and environment information.

---

## Information Collection

### Questions to Ask the Customer
- Are the source and destination paths specified as full UNC paths?
- Does the source table include the folder structure, or is it expected to be reconstructed?
- Have there been any recent changes to the network environment or permissions?

### Logs and Data to Collect
- Action Module logs from the affected system.
- Screenshots or exports of the File System Copy Action configuration.
- Details of the source and destination folder structures.

---

## Common Scenarios & Solutions

### Scenario 1: Incorrect Path Specification
- **Symptoms**: Files are created in `fsam.tmp` but not transferred.
- **Root Cause**: Source and destination paths are not specified as full UNC paths.
- **Resolution**: Update the configuration to use full UNC paths for both source and destination.

### Scenario 2: Missing Folder Structure in Source Table
- **Symptoms**: Files are copied, but the folder structure is not preserved.
- **Root Cause**: The source table does not include the folder structure.
- **Resolution**: Modify the source table to include the folder structure or reconstruct it during the copy process.

---

## Detailed Case Studies

### Case Study: Ticket [500Qk00000IlVUFIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IlVUFIA3/view)
- **Initial Symptoms**: Files were being created in the `fsam.tmp` folder but were not reaching the destination. Temporary files were deleted every 1-2 minutes.
- **Diagnostic Steps**:
  1. Verified that the issue persisted regardless of configuration options (overwrite, terminate, retry, batching).
  2. Reviewed the process flow and confirmed the temporary file creation and deletion behavior.
  3. Attempted to replicate the issue in a controlled environment.
  4. Escalated the issue to the development team for further investigation.
- **Key Information**: The source and destination paths were not specified as full UNC paths, and the source table did not include the folder structure.
- **Resolution**: Updated the configuration to use full UNC paths for both source and destination. This resolved the issue for file transfers but did not preserve the folder structure.
- **Key Takeaways**:
  - Always specify full UNC paths for source and destination.
  - Ensure the source table includes the folder structure or plan to reconstruct it.
- **Efficiency Improvements**: Develop a pre-deployment checklist to verify path specifications and source table completeness.

---

## Best Practices & Tips

1. **Use Full UNC Paths**:
   - Always specify full UNC paths for both source and destination to avoid path resolution errors.

2. **Validate Source Table**:
   - Ensure the source table includes the folder structure or plan to reconstruct it during the copy process.

3. **Test in a Controlled Environment**:
   - Replicate the configuration in a test environment to identify potential issues before deployment.

4. **Monitor Logs**:
   - Regularly review Action Module logs for warnings or errors that may indicate configuration issues.

5. **Document Configuration Changes**:
   - Maintain detailed records of configuration changes to facilitate troubleshooting and rollback if needed.

---

## Escalation Guidelines

### Criteria for Escalation
- The issue persists after verifying path specifications and source table completeness.
- Logs indicate errors that cannot be resolved through configuration adjustments.
- The problem affects critical operations or multiple environments.

### Escalation Procedure
1. Collect all relevant logs, screenshots, and configuration details.
2. Document the steps taken to reproduce the issue.
3. Submit the case to the development team with a detailed description of the problem and findings.

--- 

This guide serves as a comprehensive reference for troubleshooting File System Copy Action issues in Netwrix Enterprise Auditor. By following the outlined methodologies and best practices, support engineers can efficiently diagnose and resolve these problems while minimizing impact on customer operations.