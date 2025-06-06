# Netwrix Enterprise Auditor: Troubleshooting File System Action Module Issues

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the File System Action Module in Netwrix Enterprise Auditor (NEA). The File System Action Module is a critical component used to execute actions such as copying, moving, or managing files within a monitored environment. Understanding and resolving issues in this category is essential for maintaining system functionality and ensuring customer satisfaction.

## Technical Background
The File System Action Module in NEA relies on the StealthAUDIT for Windows File Systems collector to execute configured actions. These actions are managed through applets and services that depend on proper installation paths, configuration, and prerequisites. Key components include:
- **Action Module Service**: Executes the configured actions.
- **Installation Path**: The directory where the module's executables and libraries are installed.
- **Version Compatibility**: The module expects specific versions of input tables and libraries to function correctly.
- **Prerequisites**: Proper configuration and understanding of the module's requirements are necessary for successful execution.

## Issue Recognition & Triage
### Symptoms
- Errors indicating version mismatches (e.g., "Input table is version 2, while version 1 is expected").
- Failure to execute actions such as copying or moving files.
- Customer confusion regarding prerequisites or configuration steps.

### Priority Assessment
- **High Priority**: Errors that prevent critical actions from executing, impacting business operations.
- **Medium Priority**: Configuration issues that delay action setup but do not affect existing functionality.
- **Low Priority**: General inquiries or requests for guidance on using the module.

## Diagnostic Methodology
1. **Verify Error Messages**: Review the exact error message reported by the customer to identify the issue type (e.g., version mismatch, configuration error).
2. **Check Installation Paths**: Confirm that the module's executables and libraries are installed in the correct directory.
3. **Review Service Configuration**: Examine the "Path to Execute" property of the service in the Services panel.
4. **Validate Prerequisites**: Ensure the customer has met all prerequisites for the action module.
5. **Engage Professional Services**: For complex configurations or customer training needs, involve the Professional Services Team.

## Information Collection
When troubleshooting, gather the following information:
- **Error Details**: Exact error messages and screenshots, if available.
- **Environment Details**: Platform, collector code, and NEA version.
- **Service Configuration**: "Path to Execute" property and installation directory.
- **Customer Actions**: Steps taken by the customer leading up to the issue.
- **Logs**: Relevant logs from the NEA system and the File System Action Module.

## Common Scenarios & Solutions
### Scenario 1: Version Mismatch Error
- **Symptom**: Error indicating "Input table is version 2, while version 1 is expected."
- **Root Cause**: The Action Module service is referencing an incorrect installation path.
- **Resolution**:
  1. Uninstall the File System Action Module Applet using the NEA Action Configuration or the command:
     ```bash
     sc delete StealthAUDITFSAM
     ```
  2. Re-execute the configured action in NEA to reinstall the service in the correct location.
  3. Verify the installation path and service configuration.

### Scenario 2: Difficulty Configuring Copy/Move Jobs
- **Symptom**: Customer unable to create a job for copying/moving files.
- **Root Cause**: Lack of understanding of prerequisites and configuration steps.
- **Resolution**:
  1. Refer the customer to the Professional Services Team for detailed guidance.
  2. Provide documentation and resources to help the customer understand the module's requirements.
  3. Follow up to ensure the customer has received the necessary support.

## Detailed Case Studies
### Case Study 1: Version Mismatch Error
- **Ticket ID**: [500Qk00000DlAm1IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DlAm1IAF/view)
- **Initial Symptoms**: Customer reported an error indicating a version mismatch (version 2 vs. expected version 1).
- **Diagnostic Steps**:
  1. Verified the error message and installation path.
  2. Checked the "Path to Execute" property of the service.
  3. Suggested uninstalling and reinstalling the module.
- **Resolution**:
  - Uninstalled the module using the command `sc delete StealthAUDITFSAM`.
  - Re-executed the action to reinstall the service in the correct location.
- **Key Takeaways**:
  - Always verify installation paths and service configurations.
  - Ensure customers are aware of proper installation procedures.

### Case Study 2: Difficulty Configuring Copy/Move Jobs
- **Ticket ID**: [500Qk00000N5gfhIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000N5gfhIAB/view)
- **Initial Symptoms**: Customer requested assistance with creating a copy/move job.
- **Diagnostic Steps**:
  1. Confirmed the customer's need for guidance.
  2. Referred the case to the Professional Services Team.
  3. Followed up to ensure the customer received support.
- **Resolution**:
  - Professional Services Team provided the necessary guidance.
- **Key Takeaways**:
  - Involve Professional Services early for complex configurations.
  - Ensure customers have access to documentation and training resources.

## Best Practices & Tips
- **Verify Installation Paths**: Always confirm that the module's executables and libraries are installed in the correct directory.
- **Document Prerequisites**: Provide clear documentation to customers on prerequisites for using the action module.
- **Engage Professional Services**: For complex configurations or training needs, involve the Professional Services Team promptly.
- **Follow Up**: Ensure customers receive the necessary support and follow up to confirm resolution.
- **Maintain Logs**: Encourage customers to provide detailed logs and screenshots to expedite troubleshooting.

## Escalation Guidelines
- **When to Escalate**:
  - Errors persist after verifying installation paths and service configurations.
  - Customer requires advanced guidance beyond the scope of standard support.
  - Issues involve potential bugs or require hotfixes.
- **How to Escalate**:
  1. Gather all relevant information, including logs, error messages, and environment details.
  2. Document troubleshooting steps taken and their outcomes.
  3. Escalate to the appropriate team (e.g., Professional Services, Development) with a detailed summary of the issue.

By following this guide, support engineers can systematically diagnose and resolve issues related to the File System Action Module in Netwrix Enterprise Auditor, ensuring consistent and effective support for customers.