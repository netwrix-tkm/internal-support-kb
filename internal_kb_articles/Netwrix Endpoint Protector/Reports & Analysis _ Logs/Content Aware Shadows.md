# Knowledge Base Reference Guide: Troubleshooting File Shadowing and User Activity Monitoring in Netwrix Endpoint Protector

## Overview

This guide focuses on troubleshooting issues related to enabling file shadowing and monitoring user activity on the internet within the Netwrix Endpoint Protector platform. File shadowing is a critical feature that allows organizations to maintain visibility into file operations, ensuring compliance and security. Understanding and resolving issues in this category is essential for maintaining system functionality and meeting organizational monitoring requirements.

---

## Technical Background

### Key Concepts
- **File Shadowing**: A feature that captures and stores copies of files accessed, modified, or transferred by users. This is essential for auditing and compliance purposes.
- **Content Aware Shadows**: A specific implementation of file shadowing that focuses on capturing content based on predefined policies.
- **User Activity Monitoring**: The process of tracking user actions, such as internet browsing and file operations, to ensure adherence to organizational policies.

### System Context
- **Netwrix Endpoint Protector**: A data loss prevention (DLP) solution designed to monitor and control sensitive data across endpoints.
- **Configuration Levels**: Settings can be applied at the global, group, or computer level. Misconfigurations at any level can lead to feature malfunctions.

---

## Issue Recognition & Triage

### Symptoms
- File shadowing is not functioning as expected.
- User activity logs do not reflect internet activity or file operations.
- Errors or inconsistencies in the application interface when enabling shadowing.

### Priority Assessment
- **High Priority**: If the issue impacts compliance or critical monitoring requirements.
- **Medium Priority**: If the issue is isolated to a specific endpoint or user.
- **Low Priority**: If the issue is non-critical and does not affect core operations.

---

## Diagnostic Methodology

1. **Verify Configuration Settings**:
   - Check global, group, and computer-level settings for file shadowing.
   - Ensure policies are correctly applied and not overridden.

2. **Test Feature Functionality**:
   - Attempt to enable file shadowing through the application interface.
   - Perform test operations (e.g., file transfers) to verify shadowing.

3. **Review Logs**:
   - Examine user activity logs for discrepancies.
   - Look for error messages or missing entries related to file shadowing.

4. **Isolate the Issue**:
   - Determine if the problem is specific to a user, endpoint, or policy.

5. **Apply Configuration Changes**:
   - Adjust settings at the computer level if necessary.
   - Re-test functionality after changes.

---

## Information Collection

### Questions to Ask Customers
- What specific issues are you experiencing with file shadowing or user activity monitoring?
- Have there been any recent changes to policies or configurations?
- Is the issue affecting all users or specific endpoints?

### Data to Collect
- Screenshots of the configuration settings.
- Logs from the Netwrix Endpoint Protector platform.
- Details of recent changes to the environment (e.g., software updates, policy changes).

---

## Common Scenarios & Solutions

### Scenario 1: File Shadowing Not Enabled
- **Cause**: Misconfiguration at the computer level.
- **Solution**: Review and correct the computer-level settings. Ensure policies are applied correctly.

### Scenario 2: Missing User Activity Logs
- **Cause**: Incomplete or incorrect policy definitions.
- **Solution**: Update policies to include the desired user activity parameters. Verify logs after changes.

### Scenario 3: Errors in Application Interface
- **Cause**: Software bug or corrupted configuration.
- **Solution**: Restart the application, reapply configurations, and check for updates or patches.

---

## Detailed Case Studies

### Case Study 1: File Shadowing Configuration Issue
- **Ticket ID**: [500Qk00000F6PfrIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F6PfrIAF/view)
- **Initial Symptoms**: Customer reported that file shadowing could not be enabled, and user activity logs were incomplete.
- **Diagnostic Steps**:
  1. Reviewed configuration settings at all levels.
  2. Attempted to enable file shadowing through the interface.
  3. Checked user activity logs for discrepancies.
  4. Identified incorrect settings at the computer level.
- **Resolution**:
  - Corrected the computer-level configuration settings.
  - Verified that file shadowing was successfully enabled.
  - Confirmed that user activity logs reflected the expected data.
- **Key Takeaways**:
  - Always verify computer-level settings when troubleshooting file shadowing.
  - Ensure that policies are not overridden by local configurations.
- **Efficiency Improvements**:
  - Develop a checklist for verifying configuration settings to streamline diagnostics.

---

## Best Practices & Tips

1. **Standardize Configuration Settings**:
   - Use templates or predefined policies to minimize configuration errors.

2. **Regularly Audit Logs**:
   - Periodically review user activity and file shadowing logs to ensure functionality.

3. **Document Changes**:
   - Maintain a record of configuration changes to facilitate troubleshooting.

4. **Proactive Monitoring**:
   - Use automated alerts to detect issues with file shadowing or user activity monitoring.

5. **Customer Communication**:
   - Clearly explain the steps being taken to resolve the issue.
   - Provide guidance on preventing similar issues in the future.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following standard troubleshooting steps.
- The problem affects multiple users or endpoints.
- The root cause is suspected to be a software bug or system limitation.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration details.
2. Document the troubleshooting steps already taken.
3. Submit the case to the appropriate escalation team with a detailed summary.

--- 

This guide serves as a comprehensive reference for troubleshooting file shadowing and user activity monitoring issues in Netwrix Endpoint Protector. By following the outlined methodologies and best practices, support engineers can resolve these issues efficiently and consistently.