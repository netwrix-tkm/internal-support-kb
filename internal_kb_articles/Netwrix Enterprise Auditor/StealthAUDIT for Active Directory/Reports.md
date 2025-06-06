# Comprehensive Knowledge Base Guide: Troubleshooting StealthAUDIT for Active Directory Reports

## Overview
This guide provides a systematic approach to troubleshooting issues related to the "Reports" feature in the StealthAUDIT for Active Directory component of Netwrix Enterprise Auditor. It covers common scenarios, diagnostic methodologies, and resolution strategies to ensure consistent and effective support. Understanding and resolving these issues is critical for maintaining accurate reporting, ensuring compliance, and meeting customer requirements.

---

## Technical Background
### Key Concepts
- **StealthAUDIT for Active Directory (SA):** A module within Netwrix Enterprise Auditor designed to collect, analyze, and report on Active Directory (AD) data.
- **Reports:** Predefined or custom outputs generated from collected AD data, often used for compliance, security, and operational insights.
- **SQL Views and Tables:** Many reports rely on SQL queries that pull data from specific views or tables, such as `SA_ADInventory_UsersView` or `SA_FSAC_DailyActivityView`.
- **Filtering Logic:** Reports often include filters (e.g., date ranges, group names) to refine the data presented.
- **Job Scheduling:** Data collection and report generation depend on scheduled jobs that must run in the correct sequence to ensure data accuracy.

### Terminology
- **Unresolved SIDs:** Security Identifiers (SIDs) in AD groups that no longer map to valid user accounts.
- **Sensitive Groups:** AD groups with elevated privileges, such as Domain Admins or DnsAdmins.
- **Analysis Tasks:** SQL-based tasks that process raw data into meaningful insights for reports.
- **Netwrix Activity Monitor (NAM):** A component that collects and logs activity data for reports.

---

## Issue Recognition & Triage
### Common Symptoms
- Reports fail to generate or display errors (e.g., "This site can’t be reached").
- Data discrepancies, such as stale or missing information.
- Custom reports not reflecting requested changes or attributes.
- Ambiguous SQL errors during report generation.
- Customers unable to drill down into report details.

### Priority Assessment
- **High Priority:** Reports critical for compliance or audits are failing or inaccurate.
- **Medium Priority:** Custom report requests or minor discrepancies in non-critical reports.
- **Low Priority:** General inquiries about report functionality or terminology.

---

## Diagnostic Methodology
### Systematic Approach
1. **Understand the Problem:**
   - Review the customer's description and clarify requirements.
   - Identify whether the issue is with report generation, data accuracy, or configuration.

2. **Verify the Environment:**
   - Confirm the versions of Netwrix components in use.
   - Check the configuration of relevant jobs and SQL queries.

3. **Reproduce the Issue:**
   - Attempt to replicate the problem in a test environment if possible.
   - Review logs and error messages for clues.

4. **Analyze Dependencies:**
   - Ensure that all prerequisite jobs (e.g., data collection) have run successfully.
   - Check for misconfigurations in SQL queries or filtering logic.

5. **Implement and Test Fixes:**
   - Apply changes incrementally and test after each adjustment.
   - Validate the report output with the customer.

---

## Information Collection
### Questions to Ask Customers
- What specific report or data are you trying to access?
- Are there any error messages or unexpected behaviors?
- When was the issue first noticed, and has it occurred before?
- Have there been any recent changes to the environment (e.g., updates, configuration changes)?
- What are the expected results versus the actual results?

### Logs and Data to Collect
- SQL query logs for the affected report.
- Debug logs from the Netwrix Enterprise Auditor.
- Screenshots or exported reports showing the issue.
- Output from PowerShell scripts to verify installed components and configurations.

---

## Common Scenarios & Solutions
### Scenario 1: Report Fails to Generate
- **Symptoms:** Error message "This site can’t be reached."
- **Root Cause:** Misconfigured Web Server service account.
- **Solution:** Reconfigure the Web Server service to run under an account with appropriate database access. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BRRygIAH/view)

### Scenario 2: Stale Data in Reports
- **Symptoms:** Reports show outdated information or blank data.
- **Root Cause:** Misaligned job schedules causing data to lag behind.
- **Solution:** Adjust job schedules to ensure data updates occur before report generation. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HfJhfIAF/view)

### Scenario 3: Missing Attributes in Reports
- **Symptoms:** Custom report does not include requested columns.
- **Root Cause:** SQL query does not reference the required attributes.
- **Solution:** Modify the SQL view to include the missing columns. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FoGvOIAV/view)

### Scenario 4: Ambiguous SQL Errors
- **Symptoms:** Error "Ambiguous Column Name" during report execution.
- **Root Cause:** Conflicting column names in SQL queries.
- **Solution:** Explicitly specify table names in the SQL query to resolve ambiguity. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LxkfXIAR/view)

### Scenario 5: Unresolved SIDs in AD Groups
- **Symptoms:** No built-in report for identifying unresolved SIDs.
- **Root Cause:** Lack of out-of-the-box functionality for this use case.
- **Solution:** Create a custom SQL view connecting relevant tables to identify unresolved SIDs. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BZss5IAD/view)

---

## Detailed Case Studies
### Case Study 1: Custom Group Change Report
- **Ticket:** [500Qk00000BnGmwIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BnGmwIAF/view)
- **Symptoms:** Customer needed a report for group membership changes.
- **Diagnostic Steps:**
  - Verified the environment and existing reports.
  - Created a custom SQL job to filter group membership changes.
- **Resolution:** Delivered a custom report and updated email recipients.
- **Key Takeaways:** Custom SQL jobs can address gaps in built-in reporting.

### Case Study 2: Sensitive Group Membership Discrepancies
- **Ticket:** [500Qk00000MXLYtIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MXLYtIAP/view)
- **Symptoms:** Report showed incorrect group membership data.
- **Diagnostic Steps:**
  - Reviewed job schedules and debug logs.
  - Identified timing misalignment between data updates and report generation.
- **Resolution:** Rescheduled jobs to align with report timing.
- **Key Takeaways:** Ensure job schedules are logically sequenced.

### Case Study 3: Adding Columns to Empty Groups Report
- **Ticket:** [500Qk00000FoGvOIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FoGvOIAV/view)
- **Symptoms:** Customer requested additional columns in a report.
- **Diagnostic Steps:**
  - Reviewed the existing SQL view.
  - Modified the view to include the requested attributes.
- **Resolution:** Updated the report to reflect the changes.
- **Key Takeaways:** SQL views can be customized to meet specific requirements.

---

## Best Practices & Tips
- **SQL Query Design:** Always specify table names to avoid ambiguity when referencing columns.
- **Job Scheduling:** Align data collection and report generation jobs to ensure accurate and up-to-date data.
- **Documentation:** Direct customers to relevant Help Center articles for self-service solutions.
- **Custom Reports:** Use existing reports as templates to minimize development time.
- **Customer Communication:** Clearly explain technical limitations and provide alternative solutions when necessary.

---

## Escalation Guidelines
- **Escalate to Development Team:**
  - When a feature request is required (e.g., adding drill-down capabilities).
  - For unresolved SQL errors after thorough troubleshooting.
- **Escalate to Senior Engineers:**
  - When the issue involves complex SQL modifications or advanced configurations.
  - For recurring issues that may indicate a systemic problem.
- **Provide Detailed Context:**
  - Include logs, SQL queries, and a summary of troubleshooting steps already taken.

--- 

This guide serves as a comprehensive reference for handling issues related to StealthAUDIT for Active Directory reports, ensuring consistent and effective support delivery.