# Knowledge Base Reference Guide: Troubleshooting Custom Reports in StealthAUDIT for Windows File Systems

## Overview
Custom Reports in StealthAUDIT for Windows File Systems are a critical feature of Netwrix Enterprise Auditor, enabling users to generate tailored insights into file system activity, permissions, and configurations. These reports are essential for compliance, security audits, and operational efficiency. Understanding how to troubleshoot issues in this category ensures timely resolution, minimizes downtime, and enhances customer satisfaction.

## Technical Background
### Key Concepts
- **Custom Reports**: User-defined reports that extract specific data from file system scans and database tables.
- **StealthAUDIT Collector**: The module responsible for gathering data from Windows File Systems.
- **SQL Views**: Custom SQL queries used to filter and manipulate data for reporting purposes.
- **Scan Depth**: The level of folder hierarchy analyzed during data collection.
- **Database Tables**: Core tables such as `SA_FS_DLPResults_ShareDetails` and `FSAC_ActivityEvents` store scanned data for reporting.

### System Context
- **Netwrix Enterprise Auditor (NEA)**: A platform for auditing and reporting on IT infrastructure.
- **StealthAUDIT**: A collector within NEA that focuses on file system data.
- **Custom Report Configuration**: Involves defining filters, columns, and data sources to meet specific reporting needs.

## Issue Recognition & Triage
### Symptoms
- Errors during report generation (e.g., "Invalid object name").
- Missing columns or data in reports after upgrades.
- Connectivity issues preventing discovery jobs.
- Reports failing to meet specific customer requirements.

### Priority Assessment
- **High Priority**: Errors preventing critical scans or compliance reporting.
- **Medium Priority**: Missing data or columns impacting report usability.
- **Low Priority**: Requests for new report configurations or enhancements.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Environment Details**: Confirm product version, collector configuration, and database connectivity.
2. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
3. **Analyze Logs and Data**: Review relevant logs, database tables, and report configurations.
4. **Identify Root Cause**: Determine whether the issue stems from misconfiguration, data limitations, or software bugs.
5. **Implement Resolution**: Apply fixes or adjustments based on findings.

### Decision Points
- **Configuration Issue**: Adjust report settings or SQL filters.
- **Database Issue**: Verify table existence and data integrity.
- **Software Bug**: Recommend upgrading to a newer version or applying patches.

## Information Collection
### Customer Queries
- What version of Netwrix Enterprise Auditor is installed?
- Are there any recent upgrades or changes to the environment?
- What specific error messages or symptoms are observed?
- What are the desired report parameters (columns, filters, etc.)?

### Logs and Data to Collect
- Screenshots of error messages or report configurations.
- SQL queries used in custom reports.
- Database table structure and sample data.
- Network connectivity logs (if applicable).

## Common Scenarios & Solutions
### Scenario 1: Invalid Object Name Error
- **Symptoms**: Error message "Invalid object name 'dbo.SA_FS_DLPResults_EnterpriseSummary'" during report generation.
- **Resolution**: Adjust custom report configuration to reference existing database objects. Verify table existence and data integrity. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BQ75yIAD/view)

### Scenario 2: Discovery Job Fails Due to Connectivity Issues
- **Symptoms**: NEA console unable to perform PING checks, preventing discovery jobs.
- **Resolution**: Customize job settings to bypass PING status checks. Ensure network configurations allow PING if required. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E0d6AIAR/view)

### Scenario 3: Missing Columns After Upgrade
- **Symptoms**: "Last Modified" column missing in custom report after upgrading to version 11.6.
- **Resolution**: Create a new SQL view to join relevant tables and restore missing columns. Back up custom configurations before upgrades. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EReNtIAL/view)

### Scenario 4: Permission Change Tracking for Top-Level Folders
- **Symptoms**: Customer unable to track permission changes for top-level folders.
- **Resolution**: Implement a SQLView job with filters for folder-level changes and path length conditions. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EJHoHIAX/view)

### Scenario 5: Custom Report for Specific File Types
- **Symptoms**: Existing file type report does not include required columns.
- **Resolution**: Guide customer on creating custom reports using NEA's reporting tools. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GU3sQIAT/view)

### Scenario 6: CIFS Open Access Report Customization
- **Symptoms**: Customer needs a new report with specific filters and email notifications.
- **Resolution**: Copy and modify the existing report to meet new requirements. Provide annotated screenshots for guidance. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IL3BsIAL/view)

### Scenario 7: Permission Groups Report Customization
- **Symptoms**: Customer requests filtering out users and displaying share paths instead of folder paths.
- **Resolution**: Modify report filters to exclude users. Suggest SQL View Creation for advanced customization. [Ticket Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MncqhIAB/view)

## Detailed Case Studies
### Case Study 1: Invalid Object Name Error
- **Symptoms**: Error during permission scan bulk import.
- **Diagnostic Steps**: Verified database table existence and report configuration.
- **Key Information**: Misconfiguration in report charts referencing non-existent objects.
- **Resolution**: Adjusted report configuration during a remote session.
- **Takeaways**: Always verify database configurations before initiating bulk imports.

### Case Study 2: Discovery Job Connectivity Issues
- **Symptoms**: Discovery job failed due to PING check failures.
- **Diagnostic Steps**: Reviewed job settings and network configurations.
- **Key Information**: NEA console unable to reach servers via PING.
- **Resolution**: Customized job settings to bypass PING checks.
- **Takeaways**: Ensure network configurations align with job requirements.

### Case Study 3: Missing Columns After Upgrade
- **Symptoms**: "Last Modified" column missing post-upgrade.
- **Diagnostic Steps**: Verified SQL views and table structure.
- **Key Information**: Upgrade process did not retain custom configurations.
- **Resolution**: Created new SQL view to restore missing column.
- **Takeaways**: Back up custom configurations before upgrades.

### Case Study 4: Permission Change Tracking
- **Symptoms**: Customer unable to track permission changes for top-level folders.
- **Diagnostic Steps**: Analyzed FSAC_ActivityEvents table and created SQL filters.
- **Key Information**: Path length condition used to limit results to top-level folders.
- **Resolution**: Implemented SQLView job with specific filters.
- **Takeaways**: SQL filtering is effective for granular reporting needs.

### Case Study 5: CIFS Open Access Report Customization
- **Symptoms**: Customer requested a new report with specific filters and email notifications.
- **Diagnostic Steps**: Reviewed existing report settings and demonstrated report creation process.
- **Key Information**: Separate reports required for different scan depths and hostnames.
- **Resolution**: Created new report and provided annotated screenshots.
- **Takeaways**: Clear documentation simplifies report creation for customers.

## Best Practices & Tips
- **Backup Configurations**: Always back up custom reports and settings before upgrades.
- **SQL View Creation**: Use SQL views for advanced filtering and data manipulation.
- **Documentation**: Provide clear, annotated guides for report creation and customization.
- **Customer Communication**: Clarify requirements and provide step-by-step instructions.
- **Testing**: Test upgrades and new configurations in staging environments.

## Escalation Guidelines
### Criteria for Escalation
- Issues involving software bugs or limitations requiring development intervention.
- Complex report configurations beyond standard support capabilities.
- Persistent errors despite following troubleshooting steps.

### Escalation Procedure
1. Gather all relevant logs, screenshots, and customer requirements.
2. Document troubleshooting steps and findings.
3. Submit a detailed escalation request to the appropriate team (e.g., Development or ProServ).
4. Communicate escalation status and expected timelines to the customer.