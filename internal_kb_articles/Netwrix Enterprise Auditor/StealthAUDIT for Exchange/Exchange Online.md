# Netwrix Enterprise Auditor: Troubleshooting Exchange Online Integration Issues

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to Exchange Online integration within Netwrix Enterprise Auditor (NEA), specifically focusing on the StealthAUDIT for Exchange component. Exchange Online integration is critical for organizations leveraging NEA to audit and monitor their cloud-based Exchange environments. Proper configuration ensures accurate data collection, reporting, and compliance adherence. This document outlines systematic approaches, common scenarios, and best practices to resolve issues efficiently.

---

## Technical Background

### Key Concepts
- **Exchange Online Integration**: The process of connecting NEA to Microsoft Exchange Online to collect audit data, generate reports, and monitor activity.
- **StealthAUDIT for Exchange**: A collector module in NEA designed to gather data from Exchange environments, including Exchange Online.
- **Public Folders**: Shared folders in Exchange used for collaboration, which may require special handling during migrations or reporting.
- **Termed Users**: Disabled or inactive user accounts in Exchange Online that can cause errors during data collection if not properly excluded.

### System Context
- **Connection Profiles**: Define how NEA connects to Exchange Online, including authentication and host settings.
- **Host List**: Specifies the servers or endpoints NEA interacts with for data collection.
- **Job Groups**: Logical groupings of data collection jobs, such as Exchange Online or Public Folders jobs.
- **Permissions**: Exchange Online requires specific permissions for NEA to access data, including MAPI-based permissions for certain reports.

---

## Issue Recognition & Triage

### Symptoms
- Errors during Exchange Online job processing.
- Blank or incomplete reports.
- Jobs failing to complete or populate necessary data tables.
- Issues arising after migrations from Exchange On-Prem to Exchange Online.

### Categorization
1. **Configuration Issues**: Problems with connection profiles, host lists, or job group assignments.
2. **Data Collection Errors**: Failures caused by termed users, missing permissions, or incorrect settings.
3. **Migration-Related Issues**: Misconfigurations following a transition from Exchange On-Prem to Exchange Online.

### Priority Assessment
- **High Priority**: Jobs failing to run or critical reports not generating.
- **Medium Priority**: Errors related to specific users or folders but not affecting overall functionality.
- **Low Priority**: Minor configuration adjustments or optimization requests.

---

## Diagnostic Methodology

1. **Verify Requirements**:
   - Confirm Exchange Online permissions and prerequisites are met.
   - Check that necessary dependencies are installed on the NEA server.

2. **Review Configuration**:
   - Inspect connection profiles and host lists.
   - Ensure job groups are correctly assigned (e.g., Public Folders Job in the Exchange Online group).

3. **Analyze Logs**:
   - Collect and review job logs for error messages or warnings.
   - Look for patterns indicating specific issues (e.g., termed users causing errors).

4. **Test Adjustments**:
   - Apply configuration changes incrementally and test after each adjustment.
   - Run jobs manually to verify functionality.

5. **Validate Results**:
   - Confirm that jobs complete successfully and reports are populated with accurate data.

---

## Information Collection

### Questions to Ask Customers
- Have there been any recent migrations or changes to the Exchange environment?
- Are there specific jobs or reports that are failing?
- Have any permissions or configurations been modified recently?

### Data to Collect
- Job logs and error messages.
- Screenshots of connection profile and host list configurations.
- Details of the Exchange Online environment, including termed users and public folder settings.

---

## Common Scenarios & Solutions

### Scenario 1: Errors Caused by Termed Users
- **Symptoms**: Errors during job processing due to disabled accounts.
- **Solution**: Configure the Exchange Online job to exclude termed users. Regularly review and update filters to prevent similar issues.
- **Reference Case**: [500Qk00000IgxPWIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IgxPWIAZ/view)

### Scenario 2: Public Folder Report Not Working Post-Migration
- **Symptoms**: Reports configured for Exchange On-Prem fail after migration to Exchange Online.
- **Solution**: Relocate the Public Folders Job to the Exchange Online group and verify MAPI-based permissions.
- **Reference Case**: [500Qk00000LBb8EIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LBb8EIAT/view)

### Scenario 3: PF_FolderScans Job Not Completing
- **Symptoms**: Blank reports due to incomplete data collection.
- **Solution**: Correct connection profile, host list, and query settings. Enable "Use Office 365 – Connect to Office 365" in the query settings.
- **Reference Case**: [500Qk00000P896AIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000P896AIAR/view)

---

## Detailed Case Studies

### Case Study 1: Termed Users Causing Errors
- **Initial Symptoms**: Errors during Exchange Online job processing.
- **Diagnostic Steps**: Reviewed job logs, identified termed users as the cause.
- **Resolution**: Configured the job to exclude termed users.
- **Key Takeaways**: Regularly update filters to exclude disabled accounts.

### Case Study 2: Public Folder Report Post-Migration
- **Initial Symptoms**: Report failed to pull data after migration.
- **Diagnostic Steps**: Verified job group assignment and permissions.
- **Resolution**: Relocated the job to the Exchange Online group.
- **Key Takeaways**: Always review job configurations after migrations.

### Case Study 3: PF_FolderScans Job Failure
- **Initial Symptoms**: Blank custom report due to incomplete job.
- **Diagnostic Steps**: Checked connection profile, host list, and query settings.
- **Resolution**: Corrected settings and enabled Office 365 connection.
- **Key Takeaways**: Validate configuration settings after updates.

---

## Best Practices & Tips

1. **Regular Configuration Reviews**:
   - Periodically review job settings, filters, and permissions to ensure alignment with the current environment.

2. **Proactive Migration Planning**:
   - Before migrating from Exchange On-Prem to Exchange Online, plan and test job configurations to avoid disruptions.

3. **Log Analysis**:
   - Use job logs as the primary diagnostic tool to identify root causes quickly.

4. **Customer Communication**:
   - Clearly explain the steps being taken and provide guidance on preventing similar issues in the future.

5. **Documentation Updates**:
   - Keep internal and customer-facing documentation up to date with the latest best practices and configuration guidelines.

---

## Escalation Guidelines

### When to Escalate
- Issues persist after following standard troubleshooting steps.
- Errors indicate potential bugs or require development intervention.
- Customer requests enhancements or features beyond current product capabilities.

### How to Escalate
- Collect all relevant logs, screenshots, and configuration details.
- Document the steps already taken and their outcomes.
- Submit a detailed escalation request to the appropriate internal team.

--- 

This guide serves as a definitive reference for handling Exchange Online integration issues in Netwrix Enterprise Auditor, enabling support engineers to resolve problems efficiently and consistently.