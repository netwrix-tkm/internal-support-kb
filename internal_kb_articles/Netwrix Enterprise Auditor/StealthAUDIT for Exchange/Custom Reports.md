# Knowledge Base Reference Guide: Troubleshooting Custom Reports in StealthAUDIT for Exchange

## Overview
This guide focuses on troubleshooting issues related to custom reports in the StealthAUDIT for Exchange component of Netwrix Enterprise Auditor. Custom reports are a critical feature that allows organizations to generate tailored insights from their Exchange environments. Understanding how to diagnose and resolve issues in this area ensures accurate reporting and enhances customer satisfaction.

## Technical Background
### Key Concepts
- **StealthAUDIT for Exchange**: A component of Netwrix Enterprise Auditor designed to collect, analyze, and report on Exchange-related data.
- **Custom Reports**: User-defined reports created by configuring analysis tasks and SQL scripts to extract specific data.
- **Analysis Tasks**: Configurable jobs that collect and process data, often serving as the foundation for custom reports.
- **SQL Scripts**: Queries used to manipulate and retrieve data for reporting purposes.

### System Context
- **Database Tables**: Custom reports often rely on specific database tables (e.g., `MailEnabledGroupListingWithManager`) to store and query data.
- **Execution Order**: Analysis tasks must be executed in the correct sequence to ensure dependent tables are populated before subsequent tasks run.
- **Schema Changes**: Missing or altered database columns can lead to report failures or incorrect outputs.

## Issue Recognition & Triage
### Symptoms
- Reports returning incorrect or incomplete data (e.g., zero counts for all groups).
- Errors or failures when attempting to create or execute custom reports.
- Customer confusion regarding the report creation process.

### Priority Assessment
- **High Priority**: Reports critical to business operations are failing or producing inaccurate data.
- **Medium Priority**: Issues with non-critical reports or delays caused by process misunderstandings.
- **Low Priority**: General inquiries or requests for guidance on report creation.

## Diagnostic Methodology
1. **Understand the Problem**: Review the customer's description of the issue and clarify any ambiguities.
2. **Reproduce the Issue**: Attempt to replicate the problem in a test environment using the customer's configuration.
3. **Analyze Dependencies**: Check for missing or incorrect database columns, unexecuted tasks, or script errors.
4. **Validate SQL Scripts**: Review the SQL queries for syntax errors, incorrect table references, or logical flaws.
5. **Test Solutions**: Implement and test potential fixes in a controlled environment before applying them to the customer's system.

## Information Collection
### Questions to Ask the Customer
- What specific issue are you experiencing with the custom report?
- Can you provide the SQL script or configuration details for the report?
- Have all prerequisite analysis tasks been executed?
- Are there any recent changes to your environment (e.g., schema updates, software upgrades)?

### Logs and Data to Collect
- SQL scripts used for the report.
- Output logs from analysis tasks.
- Screenshots or error messages related to the issue.
- Database schema details, if applicable.

## Common Scenarios & Solutions
### Scenario 1: Incorrect Report Output
**Symptoms**: Report displays zero counts for all groups.  
**Root Cause**: Missing database column (`managedbyprincipalid`) in the referenced table.  
**Solution**: Update the SQL script to reference the correct tables and columns. [Example Case: [500Qk00000D56YNIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D56YNIAZ/view)]  
**Resolution Steps**:
1. Review the SQL script for missing or incorrect references.
2. Modify the script to include the correct columns and logic.
3. Test the updated script to ensure accurate output.

### Scenario 2: Report Creation Process Missteps
**Symptoms**: Unable to create a custom report due to task dependency issues.  
**Root Cause**: The customer did not execute the first analysis task before configuring the second task.  
**Solution**: Guide the customer to execute tasks in the correct order. [Example Case: [500Qk00000FtVgsIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FtVgsIAF/view)]  
**Resolution Steps**:
1. Identify the sequence of tasks required for the report.
2. Ensure the first task is executed to populate the necessary table.
3. Configure and execute the second task to query the populated table.

## Detailed Case Studies
### Case Study 1: Incorrect Report Output
- **Ticket ID**: [500Qk00000D56YNIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D56YNIAZ/view)  
- **Initial Symptoms**: Report "SA_GroupInfo_MailGroupManagerCount" displayed zero counts for all groups.  
- **Diagnostic Steps**:
  1. Exported and reviewed the SQL script.
  2. Identified the missing `managedbyprincipalid` column in the `MailEnabledGroupListingWithManager` table.
  3. Corrected the SQL script to reference the appropriate columns and tables.
- **Resolution**: Updated SQL script resolved the issue, and the report displayed accurate counts.  
- **Key Takeaways**:
  - Always validate SQL scripts for accuracy before deployment.
  - Missing database columns can lead to incorrect report outputs.

### Case Study 2: Report Creation Process Missteps
- **Ticket ID**: [500Qk00000FtVgsIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FtVgsIAF/view)  
- **Initial Symptoms**: Customer unable to create a custom report due to task dependency issues.  
- **Diagnostic Steps**:
  1. Reviewed the customer's process and identified the missing execution step.
  2. Walked the customer through the correct sequence of task execution.
- **Resolution**: Customer successfully created and executed the report after following the correct process.  
- **Key Takeaways**:
  - Emphasize the importance of task execution order in documentation.
  - Provide clear, step-by-step instructions for complex processes.

## Best Practices & Tips
- **SQL Script Validation**: Always test SQL scripts in a development environment before deploying them to production.
- **Documentation**: Provide customers with detailed, step-by-step guides for creating custom reports.
- **Task Execution Order**: Highlight the importance of executing analysis tasks in the correct sequence.
- **Proactive Communication**: Follow up promptly on missed meetings to avoid delays in issue resolution.
- **Checklist Approach**: Offer customers a checklist to ensure all prerequisites are met before report creation.

## Escalation Guidelines
- **When to Escalate**:
  - The issue involves complex database schema changes or requires development team intervention.
  - The customer is dissatisfied with the resolution timeline or quality.
  - The issue impacts multiple customers or is identified as a recurring problem.
- **How to Escalate**:
  1. Document all troubleshooting steps and findings.
  2. Provide detailed logs, scripts, and error messages.
  3. Notify the escalation team with a clear summary of the issue and its business impact.