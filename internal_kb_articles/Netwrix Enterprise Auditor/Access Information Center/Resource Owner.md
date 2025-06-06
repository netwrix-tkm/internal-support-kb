# Knowledge Base Reference Guide: Troubleshooting Access Information Center (AIC) Issues in Netwrix Enterprise Auditor

## Overview
This guide focuses on troubleshooting issues related to the **Access Information Center (AIC)** in **Netwrix Enterprise Auditor**, specifically within the **Resource Owner** feature. The AIC is a critical component that enables administrators to manage access permissions and assign resource ownership effectively. Understanding and resolving issues in this category is essential to maintaining seamless access management and ensuring compliance with organizational policies.

## Technical Background
The **Access Information Center (AIC)** is a feature within Netwrix Enterprise Auditor that provides visibility into access permissions and ownership of resources. It integrates with Active Directory (AD) to allow administrators to assign resource owners, manage permissions, and audit access-related activities. Key components include:

- **Resource Owner Feature**: Enables assigning ownership of resources (e.g., folders, files) to specific users or groups.
- **Active Directory Integration**: Facilitates user and group lookups for assigning ownership.
- **AIC Service**: A backend service that handles communication between the AIC console and the underlying database/AD.

### Key Terminology
- **AIC Console**: The user interface for managing access and ownership.
- **Resource Owner**: A user or group assigned as the owner of a specific resource.
- **Active Directory (AD)**: A directory service used for user and group management.
- **Build Number**: The specific version of the Netwrix Enterprise Auditor software.

## Issue Recognition & Triage
### Common Symptoms
- Errors when assigning a group or user to a folder.
- Intermittent error messages such as "There are no domains available to search."
- Temporary resolution by restarting the AIC service.

### Priority Assessment
- **High Priority**: Issues that prevent critical access management tasks, such as assigning resource owners.
- **Medium Priority**: Intermittent issues that disrupt workflows but have temporary workarounds.
- **Low Priority**: Non-blocking errors or cosmetic issues.

## Diagnostic Methodology
### Systematic Troubleshooting Approach
1. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
2. **Review Logs**: Analyze AIC logs for error messages or anomalies.
3. **Verify Permissions**: Ensure the user has the necessary permissions to perform the action.
4. **Check Configuration**: Review AIC and folder settings for recent changes.
5. **Test Connectivity**: Confirm communication between the AIC console, AD, and the database.
6. **Engage SWAT Team**: For complex or irreproducible issues, escalate to the SWAT team for deeper analysis.

## Information Collection
### Key Questions to Ask Customers
- What specific action were you performing when the issue occurred?
- Is the issue reproducible? If so, what are the exact steps?
- Have there been any recent changes to the AIC configuration or AD environment?
- Does restarting the AIC service resolve the issue temporarily?

### Logs and Data to Collect
- AIC logs from the affected system.
- Screenshots of the error messages.
- Details of the affected resource (e.g., folder path, user/group being assigned).
- AD connectivity logs, if applicable.

## Common Scenarios & Solutions
### Scenario 1: Error When Assigning a Group to a Folder
- **Symptoms**: Error occurs when attempting to assign a group to a folder in the AIC.
- **Resolution**: Ensure the user has the appropriate permissions. Monitor for similar cases to identify patterns. [Case Reference: [500Qk00000E73dpIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E73dpIAB/view)]

### Scenario 2: "No Domains Available to Search" Error
- **Symptoms**: Intermittent error message when searching for users/groups in AD.
- **Resolution**: Restarting the AIC service temporarily resolves the issue. Monitor logs for patterns or triggers. Escalate to SWAT team if the issue persists. [Case Reference: [500Qk00000KaPFjIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KaPFjIAN/view)]

## Detailed Case Studies
### Case Study 1: Error When Assigning a Group to a Folder
- **Ticket ID**: [500Qk00000E73dpIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E73dpIAB/view)
- **Initial Symptoms**: Customer reported an error in the AIC when assigning a group to a folder.
- **Diagnostic Steps**:
  1. Reviewed error logs for relevant messages.
  2. Verified user permissions.
  3. Checked for recent configuration changes.
  4. Attempted to replicate the issue in a test environment.
- **Resolution**: The customer resolved the issue independently. Specific steps were not documented.
- **Key Takeaways**: Ensure users have appropriate permissions. Monitor similar cases for patterns.

### Case Study 2: "No Domains Available to Search" Error
- **Ticket ID**: [500Qk00000KaPFjIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KaPFjIAN/view)
- **Initial Symptoms**: Intermittent error message in the AIC console when searching for users/groups.
- **Diagnostic Steps**:
  1. Collected logs and screenshots during the error occurrence.
  2. Attempted to reproduce the issue.
  3. Engaged SWAT team for further analysis.
  4. Monitored the AIC console for recurrence.
- **Resolution**: The issue did not reappear during the monitoring period. The case was closed with customer agreement.
- **Key Takeaways**: Intermittent issues require thorough log analysis and monitoring. Temporary fixes (e.g., restarting the AIC service) may not address the root cause.

## Best Practices & Tips
- **Proactive Monitoring**: Regularly monitor AIC logs for anomalies to identify potential issues early.
- **Customer Communication**: Keep customers informed about progress, especially for intermittent or unresolved issues.
- **Documentation**: Encourage customers to document steps taken to resolve issues independently.
- **Pattern Recognition**: Track similar cases to identify recurring issues and potential root causes.
- **Service Restarts**: While restarting the AIC service can provide temporary relief, focus on identifying long-term solutions.

## Escalation Guidelines
- **When to Escalate**:
  - The issue is irreproducible and cannot be resolved with standard troubleshooting.
  - Logs indicate a potential bug or system limitation.
  - The customer reports significant business impact.
- **How to Escalate**:
  1. Gather all relevant logs, screenshots, and customer-provided details.
  2. Document all troubleshooting steps taken.
  3. Submit the case to the SWAT team or development team with a detailed summary.
  4. Keep the customer informed about the escalation status and expected timelines.