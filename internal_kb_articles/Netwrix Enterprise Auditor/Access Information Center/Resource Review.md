# Netwrix Enterprise Auditor: Access Information Center - Resource Review Troubleshooting Guide

## Overview
The **Access Information Center (AIC)** within Netwrix Enterprise Auditor is a critical component for managing and reviewing access permissions across various resources. The **Resource Review** feature enables organizations to audit and validate access rights, ensuring compliance with security policies and regulatory requirements. This guide provides a comprehensive reference for troubleshooting issues related to the Resource Review feature, equipping support engineers with the tools and methodologies needed to resolve problems efficiently and consistently.

---

## Technical Background
### Key Concepts
- **Access Information Center (AIC):** A portal within Netwrix Enterprise Auditor that provides visibility into access permissions for resources such as file shares, Active Directory, SharePoint, and cloud services.
- **Resource Review:** A feature that allows administrators to review and validate permissions for specific resources, ensuring that access aligns with organizational policies.
- **Least Privilege Principle:** A security model where users are granted the minimum level of access necessary to perform their roles.
- **DFS (Distributed File System):** A Microsoft technology that enables the grouping of shared folders located on different servers into a single namespace.

### System Context
- **Version:** All cases referenced in this guide pertain to **Netwrix Enterprise Auditor 11.6**.
- **Components:** Resource Review functionality interacts with various subsystems, including SQL databases, scanning engines, and user/group permission models.
- **Common Issues:** Errors may arise from database misconfigurations, permission conflicts, or limitations in the product's design.

---

## Issue Recognition & Triage
### Symptoms
- **HTTP 500 Errors:** Users encounter server errors when accessing specific features in the AIC portal.
- **Missing Resources:** Certain resources, such as DFS shares, are not displayed in the Resource Review.
- **Access Discrepancies:** Users report unexpected access limitations or visibility into resources.
- **Configuration Requests:** Customers request changes to default behavior, such as excluding specific groups or expanding access for certain roles.

### Priority Assessment
- **High Priority:** Issues that block critical audits or compliance reviews (e.g., missing DFS shares).
- **Medium Priority:** Errors that affect usability but have workarounds (e.g., HTTP 500 errors with specific features).
- **Low Priority:** Requests for configuration changes or clarifications on system behavior.

---

## Diagnostic Methodology
### Systematic Approach
1. **Reproduce the Issue:**
   - Attempt to replicate the reported behavior in a controlled environment.
   - Use customer-provided data, such as screenshots or logs, to guide testing.

2. **Analyze Logs:**
   - Review application and system logs for error messages or anomalies.
   - Focus on SQL queries, permission checks, and scan results.

3. **Engage Development Team:**
   - For complex issues, consult with the development team to analyze error messages or confirm expected behavior.

4. **Validate Configuration:**
   - Check system settings, such as scan schedules, group permissions, and resource scoping.

5. **Test Solutions:**
   - Apply potential fixes in a test environment before implementing them in production.

---

## Information Collection
### Customer Questions
- What specific error or behavior are you experiencing?
- When did the issue first occur, and has it happened before?
- Have there been any recent changes, such as updates or configuration modifications?
- What resources or users are affected?

### Data to Collect
- **Logs:** Application logs, SQL query results, and error messages.
- **Screenshots:** Visual evidence of the issue.
- **Environment Details:** Product version, build number, and configuration settings.
- **Reproduction Steps:** Detailed steps to replicate the issue.

---

## Common Scenarios & Solutions
### Scenario 1: HTTP 500 Error in Permissions Review
- **Symptoms:** Users encounter an HTTP 500 error when accessing the Permissions Review.
- **Root Cause:** Bug in the AIC portal related to null value handling in the database.
- **Solution:** Apply the cumulative update released on **August 16, 2024**. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DuwwIIAR/view)

### Scenario 2: Limited Access for Users in Multiple Groups
- **Symptoms:** Users in multiple groups can only see resources associated with the first group.
- **Root Cause:** System behavior aligned with the least privilege principle.
- **Solution:** Confirm expected behavior and review group permissions to ensure alignment with user roles. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FFxS9IAL/view)

### Scenario 3: Excluding Domain Admins from Resource Audit
- **Symptoms:** Customers request to exclude the "domain admins" group from resource audit reports.
- **Root Cause:** Product design limitation; resource owners have full visibility into their resources.
- **Solution:** Clarify system behavior and explain that exclusions are not supported. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JgBIfIAN/view)

### Scenario 4: Expanding Reader Role Access
- **Symptoms:** Reader Role cannot access Azure RBAC, Office 365, or SQL Server.
- **Root Cause:** Default configuration limits Reader Role access to certain resources.
- **Solution:** Specify tenant names in the configuration to grant access to additional cloud resources. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000K9jCAIAZ/view)

### Scenario 5: Missing DFS Shares in Resource Review
- **Symptoms:** DFS shares are not displayed in the Resource Review.
- **Root Cause:** DFS scans were disabled, preventing shares from being populated in the database.
- **Solution:** Enable DFS jobs, run scans, and validate that shares are displayed. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PbN2VIAV/view)

---

## Detailed Case Studies
### Case Study 1: HTTP 500 Error in Permissions Review
- **Symptoms:** HTTP 500 error when accessing Permissions Review.
- **Diagnostic Steps:** Reviewed logs, identified `System.InvalidOperationException`, and consulted development team.
- **Resolution:** Applied cumulative update to fix null value handling.
- **Key Takeaways:** Test updates for null value handling issues. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DuwwIIAR/view)

### Case Study 2: Limited Access for Users in Multiple Groups
- **Symptoms:** Users in multiple groups see limited resources.
- **Diagnostic Steps:** Reviewed group permissions and replicated issue.
- **Resolution:** Confirmed behavior as intended; no changes required.
- **Key Takeaways:** Document least privilege principle to avoid confusion. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FFxS9IAL/view)

### Case Study 3: Missing DFS Shares
- **Symptoms:** DFS shares missing from Resource Review.
- **Diagnostic Steps:** Checked DFS job status, enabled jobs, and ran scans.
- **Resolution:** Enabled DFS jobs and validated share visibility.
- **Key Takeaways:** Regularly verify scan configurations. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PbN2VIAV/view)

---

## Best Practices & Tips
- **Regular Updates:** Ensure the AIC portal is updated with the latest cumulative updates to address known bugs.
- **Proactive Monitoring:** Regularly check scan configurations and job statuses to prevent missing data.
- **Documentation:** Maintain clear documentation on system behavior, such as the least privilege principle and resource owner visibility.
- **Customer Communication:** Clearly explain product limitations and provide alternative solutions when possible.
- **Testing Environment:** Use a controlled environment to replicate and test issues before applying fixes in production.

---

## Escalation Guidelines
- **When to Escalate:**
  - Issues involving unresolvable bugs or product limitations.
  - Requests for new features or significant configuration changes.
  - Problems requiring development team input for root cause analysis.
- **How to Escalate:**
  - Provide detailed logs, screenshots, and reproduction steps.
  - Summarize troubleshooting steps already taken.
  - Clearly state the impact on the customer’s operations.

--- 

End of Document.