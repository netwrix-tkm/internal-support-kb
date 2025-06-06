# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## StealthAUDIT for Windows File Systems: Reports  

### Overview  
This guide focuses on troubleshooting and resolving issues related to the **Reports** feature in the **StealthAUDIT for Windows File Systems** component of **Netwrix Enterprise Auditor**. Reports are critical for providing insights into file system activity, permissions, stale content, sensitive data, and other operational metrics. Understanding how to diagnose and resolve issues in this category ensures accurate reporting and optimal system performance.  

### Technical Background  
#### Key Concepts  
- **StealthAUDIT for Windows File Systems**: A module within Netwrix Enterprise Auditor designed to collect, analyze, and report on file system data.  
- **Reports**: Outputs generated from collected data, providing actionable insights into file system activity, permissions, stale content, sensitive data, and more.  
- **Jobs**: Configurations within StealthAUDIT that define the scope and parameters for data collection and analysis.  
- **SQL Server**: The backend database used to store collected data and generate reports.  

#### Terminology  
- **FSAA**: File System Assessment and Analysis.  
- **AIC**: Access Information Center, used for monitoring activity data.  
- **TempDB**: Temporary database in SQL Server used for intermediate data storage during job execution.  
- **Report.xml**: Configuration file defining report parameters.  

### Issue Recognition & Triage  
#### Symptoms  
- Reports fail to generate or display incorrect data.  
- Errors such as "Sequence contains more than one matching element" or "Data at root level is invalid."  
- Missing or incomplete data in reports.  
- Performance degradation during job execution.  

#### Priority Assessment  
- **High Priority**: Errors preventing critical reports from generating (e.g., permission changes, sensitive data).  
- **Medium Priority**: Reports displaying incomplete or incorrect data.  
- **Low Priority**: Cosmetic issues or minor discrepancies in report formatting.  

### Diagnostic Methodology  
#### Systematic Approach  
1. **Verify Symptoms**: Confirm the error message or issue reported by the customer.  
2. **Reproduce the Issue**: Attempt to replicate the problem in a lab environment.  
3. **Analyze Logs**: Review DEBUG-level logs and SQL Server logs for errors.  
4. **Check Configuration**: Inspect job settings, report.xml files, and SQL scripts.  
5. **Test Adjustments**: Apply changes incrementally and test for resolution.  

#### Decision Points  
- If the issue is related to SQL errors, focus on database configuration and scripts.  
- If the report fails due to duplicate entries, inspect the report.xml file.  
- If data is missing, verify job execution and data collection settings.  

### Information Collection  
#### Customer Questions  
- What is the exact error message or issue observed?  
- Which report or job is affected?  
- Are there any recent changes to the environment (e.g., decommissioned servers, new hosts)?  
- What version of Netwrix Enterprise Auditor is being used?  

#### Logs and Data  
- DEBUG-level logs from Netwrix Enterprise Auditor.  
- SQL Server logs and tempdb statistics.  
- Screenshots of error messages.  
- Configuration files (e.g., report.xml).  

### Common Scenarios & Solutions  
#### Scenario 1: Report Fails with "Sequence contains more than one matching element"  
**Resolution**: Remove duplicate entries in the `<Reports>` section of the report.xml file.  
**Reference Case**: [500Qk00000HsLowIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HsLowIAF/view)  

#### Scenario 2: Missing Data in Sensitive Data Report  
**Resolution**: Ensure the report targets the correct SQL view (e.g., `FSDLP_MatchesView`).  
**Reference Case**: [500Qk00000Kh5aPIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kh5aPIAR/view)  

#### Scenario 3: Stale Content Report Displays Incorrect Data  
**Resolution**: Adjust SQL scripts in the `SA_FS_StaleContent_ShareSummary` analysis task.  
**Reference Case**: [500Qk00000IU958IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IU958IAD/view)  

#### Scenario 4: Open Shares Report Shows No Data  
**Resolution**: Rerun the FSAA workflow and verify exceptions.  
**Reference Case**: [500Qk00000ElbAXIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ElbAXIAZ/view)  

#### Scenario 5: Permission Change Scan Job Fails  
**Resolution**: Change the display type from chart to grid in the report configuration.  
**Reference Case**: [500Qk00000EftIFIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EftIFIAZ/view)  

### Detailed Case Studies  
#### Case Study 1: Broken Inheritance Analysis Job Timeout  
**Symptoms**: Job execution time increased from 2.5 hours to over 40 hours.  
**Diagnostic Steps**:  
- Increased timeout period.  
- Scoped analysis tasks to file server only.  
- Reviewed SQL Server tempdb configuration.  

**Resolution**: Limited scope using a WHERE clause in the SQL script.  
**Key Takeaways**: Monitor tempdb size and avoid excessive workload configurations.  
**Reference Case**: [500Qk00000BxEyHIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BxEyHIAV/view)  

#### Case Study 2: Sensitive Data Report Missing Results  
**Symptoms**: Report generated with no data despite configured SEEK jobs.  
**Diagnostic Steps**:  
- Reviewed SEEK system scan reports.  
- Verified report targeting the correct SQL view.  

**Resolution**: Created a new report targeting `FSDLP_MatchesView`.  
**Key Takeaways**: Ensure reports target the correct views and verify SEEK job configurations.  
**Reference Case**: [500Qk00000Kh5aPIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Kh5aPIAR/view)  

#### Case Study 3: Open Shares Report Shows No Data  
**Symptoms**: Report indicated no open shares despite evidence of existing open shares.  
**Diagnostic Steps**:  
- Verified Open Access job success.  
- Checked FSAA exceptions.  

**Resolution**: Rerun FSAA workflow and exceptions.  
**Key Takeaways**: Monitor FSAA exceptions and ensure workflows are executed correctly.  
**Reference Case**: [500Qk00000ElbAXIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ElbAXIAZ/view)  

### Best Practices & Tips  
1. **Regular Configuration Reviews**: Periodically review job settings, report.xml files, and SQL scripts to ensure accuracy.  
2. **Monitor SQL Server Resources**: Ensure tempdb and other SQL resources are adequately sized for large jobs.  
3. **Document Changes**: Maintain detailed records of configuration changes and troubleshooting steps for future reference.  
4. **Customer Communication**: Clearly explain technical limitations and resolutions to manage expectations effectively.  
5. **Proactive Maintenance**: Regularly clean up decommissioned servers and outdated data to prevent reporting issues.  

### Escalation Guidelines  
#### Criteria for Escalation  
- Critical reports fail to generate despite troubleshooting efforts.  
- SQL Server errors persist after adjustments.  
- Issues involve product defects requiring development intervention.  

#### Escalation Procedure  
1. Gather all relevant logs, screenshots, and configuration files.  
2. Document troubleshooting steps and findings.  
3. Submit an internal escalation ticket with detailed analysis and supporting data.  
4. Follow up with the development team for resolution timelines.  

This guide serves as a comprehensive reference for handling issues related to the **Reports** feature in **StealthAUDIT for Windows File Systems**. By following the outlined methodologies, support engineers can effectively diagnose, resolve, and prevent recurring issues.