# Netwrix Enterprise Auditor: StealthAUDIT for Active Directory - Activity Feature Troubleshooting Guide

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the **Activity** feature in the **StealthAUDIT for Active Directory** component of **Netwrix Enterprise Auditor (NEA)**. The Activity feature is critical for monitoring and reporting on Active Directory (AD) events, such as user account activity, lockouts, and authentication events. Understanding and resolving issues in this category ensures accurate auditing and compliance reporting, while minimizing disruptions to Active Directory monitoring.

## Technical Background
### Key Concepts
- **StealthAUDIT for Active Directory (AD):** A component of NEA designed to collect and analyze AD data, including user activity, authentication events, and account lockouts.
- **Activity Feature:** Focuses on monitoring and reporting AD events, such as user logins, account lockouts, and changes.
- **Job Groups:** Predefined workflows in NEA that collect and process specific types of data. For example, the "AD Activity" job group collects activity-related data.
- **Licensing:** Certain features, such as AD Activity, require specific licenses. Attempting to use unlicensed features can result in errors.
- **NAM Agents:** Network Activity Monitoring agents deployed on Domain Controllers (DCs) to collect AD activity data.

### Terminology
- **AD Activity Job Group:** A collection of jobs designed to monitor and report on AD events.
- **Lockout Analyzer:** A tool for investigating account lockouts by identifying the source of lockout events.
- **NTP (Network Traffic Processing):** A feature used to process and forward AD activity data to NAM agents.
- **API Connectivity:** Communication between NEA components and external systems for data collection and processing.

## Issue Recognition & Triage
### Common Symptoms
- Errors when running AD Activity reports (e.g., "Invalid object name 'dbo.SA_ADActivity_EventsView'").
- Missing or incomplete data in AD Activity reports.
- Inability to locate specific reports, such as account lockout reports.
- AD Activity jobs failing to run or collect data.
- Frequent account lockouts without clear sources.

### Priority Assessment
- **High Priority:** Issues affecting compliance reporting or critical AD monitoring (e.g., missing authentication data, frequent account lockouts).
- **Medium Priority:** Errors related to unlicensed features or misconfigured jobs.
- **Low Priority:** Requests for guidance on using specific features or reports.

## Diagnostic Methodology
1. **Verify Licensing:** Confirm that the customer is licensed for the AD Activity feature.
2. **Check Job Configuration:** Ensure the relevant job group (e.g., AD Activity) is configured correctly and has run successfully.
3. **Review Logs:** Analyze job logs for errors or warnings.
4. **Inspect Database:** Query the database to verify the presence of expected data.
5. **Validate Environment:** Confirm that all necessary components (e.g., NAM agents, API connectivity) are properly configured.
6. **Upgrade Software:** Check if the customer is using the latest version of NEA, as updates often resolve known issues.

## Information Collection
### Questions to Ask the Customer
- What specific error messages or symptoms are you encountering?
- Have you recently upgraded NEA or migrated to a new environment?
- Are you licensed for the AD Activity feature?
- When was the last time the relevant job group ran successfully?
- Are there any environmental changes (e.g., new DCs, network changes) that could impact data collection?

### Data to Collect
- Job logs from the NEA console server.
- Database query results for the relevant tables (e.g., `SA_ADActivity_EventsView`).
- Screenshots of job configurations and error messages.
- Version and build information for NEA and its components.
- Details about the customer's environment (e.g., number of DCs, NAM agent deployment).

## Common Scenarios & Solutions
### Scenario 1: Error Running AD Activity Reports
- **Symptoms:** Error message: "Invalid object name 'dbo.SA_ADActivity_EventsView'."
- **Root Cause:** Customer not licensed for the AD Activity feature.
- **Solution:** Disable the AD Activity job group and guide the customer to use alternative jobs, such as AD Inventory > 2-AD_Changes. [Case Reference: [500Qk00000Comk5IAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Comk5IAB/view)]

### Scenario 2: Missing Lockout Reports
- **Symptoms:** Customer unable to find a report for recently locked-out accounts.
- **Root Cause:** Deprecation of the previous Lockout job and lack of awareness of the new job location.
- **Solution:** Direct the customer to the Active Directory > 6. Activity job group, which includes lockout reporting. Provide updated documentation. [Case Reference: [500Qk00000CRkr7IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CRkr7IAD/view)]

### Scenario 3: AD Authentication Data Missing
- **Symptoms:** Monthly AD authentication monitoring job captures only one day's data.
- **Root Cause:** Suspected bug in the software version.
- **Solution:** Upgrade NEA to the latest version. [Case Reference: [500Qk00000F3dPEIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F3dPEIAZ/view)]

### Scenario 4: Configuration Issues After Migration
- **Symptoms:** AD Activity collection not functioning after migration to a new environment.
- **Root Cause:** AD Activity job group not configured, and NAM agents not deployed on DCs.
- **Solution:** Configure AD Activity collection, deploy NAM agents, and resolve API connectivity issues. [Case Reference: [500Qk00000MHRLmIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MHRLmIAP/view)]

### Scenario 5: Frequent Account Lockouts
- **Symptoms:** Account lockouts occurring every five minutes; customer unable to identify the source.
- **Root Cause:** Lack of detailed analysis tools and reliance on auto-unlock scripts.
- **Solution:** Recommend using the Lockout Analyzer tool for deeper insights into lockout sources. [Case Reference: [500Qk00000OiOooIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OiOooIAF/view)]

## Detailed Case Studies
### Case Study 1: Licensing Issue with AD Activity Reports
- **Symptoms:** Error message when running reports.
- **Diagnostic Steps:** Verified licensing, reviewed job logs, and checked database.
- **Resolution:** Disabled unlicensed job group and provided alternative solutions.
- **Key Takeaways:** Always verify licensing before troubleshooting feature-specific issues.

### Case Study 2: Missing Lockout Reports
- **Symptoms:** Customer unable to locate lockout reports.
- **Diagnostic Steps:** Reviewed job groups and documentation.
- **Resolution:** Directed customer to the correct job group and provided updated documentation.
- **Key Takeaways:** Keep documentation updated to reflect feature changes.

### Case Study 3: Authentication Data Missing
- **Symptoms:** Monthly job captures only one day's data.
- **Diagnostic Steps:** Verified job configuration, reviewed logs, and upgraded software.
- **Resolution:** Upgraded NEA to the latest version.
- **Key Takeaways:** Regularly update software to avoid known bugs.

### Case Study 4: Post-Migration Configuration Issues
- **Symptoms:** AD Activity collection not functioning.
- **Diagnostic Steps:** Verified job configuration, deployed NAM agents, and resolved API issues.
- **Resolution:** Configured AD Activity collection and restored functionality.
- **Key Takeaways:** Use a post-migration checklist to ensure all components are configured.

### Case Study 5: Frequent Account Lockouts
- **Symptoms:** Lockouts occurring every five minutes.
- **Diagnostic Steps:** Reviewed existing reports and recommended specialized tools.
- **Resolution:** Referred customer to the Lockout Analyzer tool.
- **Key Takeaways:** Specialized tools provide deeper insights into complex issues.

## Best Practices & Tips
- **Verify Licensing Early:** Confirm the customer's licensing status before troubleshooting feature-specific issues.
- **Keep Documentation Updated:** Ensure that all feature changes and deprecations are reflected in the documentation.
- **Use Specialized Tools:** Recommend tools like the Lockout Analyzer for complex issues such as frequent account lockouts.
- **Monitor After Upgrades:** Regularly check job results and logs after software upgrades to ensure functionality.
- **Post-Migration Checklist:** Use a checklist to confirm that all job groups and agents are properly configured after migrations.

## Escalation Guidelines
- **When to Escalate:**
  - Persistent issues after following standard troubleshooting steps.
  - Suspected software bugs that require development team involvement.
  - Complex environmental issues, such as API connectivity failures.
- **How to Escalate:**
  - Collect all relevant logs, screenshots, and configuration details.
  - Document all troubleshooting steps taken and their outcomes.
  - Submit a detailed escalation request to the appropriate internal team or vendor support.