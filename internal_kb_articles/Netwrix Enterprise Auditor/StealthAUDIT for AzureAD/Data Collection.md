# Netwrix Enterprise Auditor: StealthAUDIT for AzureAD - Data Collection Troubleshooting Guide

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the **Data Collection** feature in the **StealthAUDIT for AzureAD** component of **Netwrix Enterprise Auditor**. It is designed to help support engineers systematically diagnose, resolve, and prevent common problems encountered during data collection processes. Understanding this category is critical for ensuring accurate and reliable data collection from cloud-based applications and on-premises databases, which are essential for auditing and compliance.

---

## Technical Background

### Key Concepts
- **StealthAUDIT for AzureAD**: A component of Netwrix Enterprise Auditor designed to collect and analyze data from Azure Active Directory (Azure AD) environments.
- **Data Collection**: The process of gathering information from cloud-based applications and on-premises databases for auditing purposes.
- **Collections**: Predefined or custom configurations that specify the scope and parameters of data collection tasks.
- **EntraIDInventory**: A specific process within StealthAUDIT for AzureAD responsible for inventorying Azure AD objects and attributes.

### Terminology
- **ExecuteScalar**: A method in database operations used to execute a query and return a single value. Errors related to this method often indicate database connection issues.
- **Resource Contention**: A situation where multiple processes compete for the same system resources, leading to performance degradation or failures.
- **Licensing Requirements**: Specific licenses needed to enable certain features or collections within Netwrix Enterprise Auditor.

### System Context
- Supported database types include **MS SQL**, **AzureSQL**, **MongoDB**, **RedShift**, **PostgresSQL**, **Oracle**, **Db2**, and **MySQL**.
- Licensing is required for specific collections, and customers must ensure they have the appropriate licenses to access desired features.

---

## Issue Recognition & Triage

### Symptoms
- **Licensing Issues**: Customers inquire about unavailable features or collections.
- **Connection Errors**: Errors such as "ExecuteScalar requires an open and available Connection. The connection's current state is closed."
- **Performance Degradation**: Scans fail or take longer than expected due to resource contention.

### Priority Assessment
- **High Priority**: Connection errors causing repeated scan failures.
- **Medium Priority**: Licensing inquiries that block feature access.
- **Low Priority**: General questions about out-of-the-box solutions or configuration.

---

## Diagnostic Methodology

1. **Understand the Problem**: Review the customer's description and clarify the issue.
2. **Check Licensing**: Verify if the customer has the necessary licenses for the requested features.
3. **Review Logs**: Analyze logs for errors, timestamps, and patterns.
4. **Assess Resource Usage**: Identify potential conflicts with other processes (e.g., backups).
5. **Test Changes**: Implement adjustments (e.g., scheduling changes) and monitor results.

---

## Information Collection

### Questions to Ask Customers
- What specific collections or features are you trying to use?
- Have you recently made changes to your environment or schedule?
- Are there any concurrent processes (e.g., backups) running during scans?

### Logs and Data to Collect
- **Scan Logs**: Review logs for errors and timestamps.
- **System Resource Metrics**: Check CPU, memory, and disk usage during scans.
- **Licensing Details**: Confirm the customer's licensing status.

---

## Common Scenarios & Solutions

### Scenario 1: Licensing Inquiry
- **Symptom**: Customer requests information about unavailable collections.
- **Root Cause**: Lack of appropriate licensing.
- **Solution**: Provide documentation on licensing requirements and refer the customer to the sales team for assistance.
- **Example Case**: [500Qk00000KvsZgIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KvsZgIAJ/view)

### Scenario 2: Connection Error During Scan
- **Symptom**: "ExecuteScalar requires an open and available Connection" error.
- **Root Cause**: Resource contention with concurrent backup processes.
- **Solution**: Reschedule the scan to avoid conflicts and monitor for recurrence.
- **Example Case**: [500Qk00000LJtW9IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LJtW9IAL/view)

---

## Detailed Case Studies

### Case Study 1: Licensing Inquiry
- **Ticket ID**: [500Qk00000KvsZgIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KvsZgIAJ/view)
- **Initial Symptoms**: Customer requested information on creating collections for cloud-based applications and on-premises databases.
- **Diagnostic Steps**:
  1. Reviewed the customer's request and provided relevant documentation.
  2. Identified that the requested collections required additional licensing.
- **Key Information**: Licensing requirements were not met.
- **Resolution**: Provided documentation and referred the customer to the sales team.
- **Key Takeaways**:
  - Always verify licensing status early in the troubleshooting process.
  - Provide clear documentation to address customer inquiries.

### Case Study 2: Connection Error During Scan
- **Ticket ID**: [500Qk00000LJtW9IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LJtW9IAL/view)
- **Initial Symptoms**: EntraIDInventory process failed with a connection error after a successful run.
- **Diagnostic Steps**:
  1. Reviewed logs and identified a UNIQUE key constraint error prior to the connection issue.
  2. Investigated resource contention with concurrent backup operations.
  3. Rescheduled the scan to avoid conflicts.
- **Key Information**: Resource contention caused the connection error.
- **Resolution**: Adjusted the scan schedule, resolving the issue.
- **Key Takeaways**:
  - Monitor resource usage during scans to identify potential conflicts.
  - Test changes to ensure stability after adjustments.

---

## Best Practices & Tips

1. **Verify Licensing Early**: Always confirm the customer's licensing status when they inquire about specific features or collections.
2. **Monitor Resource Usage**: Use system monitoring tools to identify and address resource contention.
3. **Schedule Scans Strategically**: Avoid running scans during peak resource usage periods or concurrent processes like backups.
4. **Provide Clear Documentation**: Share relevant links and resources to empower customers with self-service options.
5. **Implement Alerts**: Set up alerts for connection errors to proactively address issues.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following standard troubleshooting steps.
- Logs indicate a deeper system-level problem (e.g., database corruption).
- Licensing or feature access requires intervention from the sales or product teams.

### How to Escalate
1. Document all troubleshooting steps and findings.
2. Include relevant logs, screenshots, and customer communications.
3. Escalate to the appropriate team (e.g., engineering, sales) with a clear summary of the issue and actions taken.

--- 

This guide serves as a definitive reference for handling issues related to the **Data Collection** feature in **StealthAUDIT for AzureAD**, enabling support engineers to resolve problems efficiently and consistently.