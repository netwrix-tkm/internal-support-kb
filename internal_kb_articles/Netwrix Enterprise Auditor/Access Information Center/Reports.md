# Netwrix Enterprise Auditor Knowledge Base: Access Information Center Reports

## Overview
The Access Information Center (AIC) in Netwrix Enterprise Auditor is a critical component for generating and managing reports related to permissions, activity, and audit data. This guide provides a comprehensive reference for troubleshooting issues related to AIC reports, ensuring support engineers can diagnose and resolve problems efficiently. Understanding this category is essential for maintaining customer satisfaction and ensuring the functionality of reporting features.

## Technical Background
### Key Concepts
- **Access Information Center (AIC):** A web-based interface for accessing audit data and generating reports.
- **Reports:** Include permissions, activity, attribute changes, and other audit-related data.
- **Dependencies:** AIC relies on system scans, bulk imports, and database views for report generation.
- **Limitations:** AIC is a 32-bit process with memory constraints, impacting large report generation.

### Terminology
- **SPAA_PermissionsView:** A database view required for permissions reports.
- **FSAC/FSAA Jobs:** File System Activity Collector and Analyzer jobs responsible for gathering file system activity data.
- **MaxRowCount:** Configuration parameter controlling the maximum rows in reports.
- **UNC Paths:** Universal Naming Convention paths used for file system activity reporting.

### System Context
- **Versioning:** Issues often stem from outdated versions of AIC or Netwrix Enterprise Auditor.
- **Configuration Files:** Key settings are stored in `AccessInformationCenter.service.exe.config`, `webservice.config`, and `web.config`.
- **Dependencies:** Features like SharePointSPAA and StealthAUDIT impact report functionality.

## Issue Recognition & Triage
### Symptoms
- Errors such as "STATUS 500" or "Page can't be displayed."
- Missing or incomplete report data.
- Long query times or timeouts.
- Reports exceeding row limits or memory constraints.
- Compatibility issues with file formats or email templates.

### Priority Assessment
- **High Priority:** Errors preventing report generation or access to critical audit data.
- **Medium Priority:** Performance issues or missing data in non-critical reports.
- **Low Priority:** Cosmetic issues or inquiries about unsupported features.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Environment Details:** Confirm product version, build number, and dependencies.
2. **Replicate the Issue:** Attempt to reproduce the problem in a lab environment.
3. **Review Logs:** Examine application logs, event viewer entries, and scan summaries.
4. **Check Configuration:** Validate settings in configuration files and IIS bindings.
5. **Test Upgrades:** Upgrade to the latest supported version to rule out known bugs.
6. **Engage Development Team:** For unresolved issues, consult the development team for insights.

### Decision Points
- **Upgrade Required:** If the issue is linked to an outdated version.
- **Configuration Issue:** If logs indicate misconfigured settings.
- **Known Bug:** If the error matches documented defects in specific builds.

## Information Collection
### Customer Queries
- What version of Netwrix Enterprise Auditor and AIC are you using?
- What specific report or feature is affected?
- Are there any error messages or codes displayed?
- Have there been recent changes to the environment (e.g., upgrades, configuration changes)?

### Logs and Data
- Application logs from AIC.
- Event viewer entries from the application server.
- Scan summaries and histories.
- Configuration files (`AccessInformationCenter.service.exe.config`, `web.config`).
- Screenshots or error messages provided by the customer.

## Common Scenarios & Solutions
### Scenario 1: "STATUS 500" Error in Permissions Report
- **Root Cause:** Missing SPAA_PermissionsView due to inactive SharePointSPAA processes.
- **Solution:** Upgrade AIC to the latest version and ensure SharePointSPAA processes are configured and running.
- **Reference Case:** [500Qk00000E59H8IAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E59H8IAJ/view)

### Scenario 2: Large Report Export Fails
- **Root Cause:** Memory limitations in the 32-bit AIC process.
- **Solution:** Export reports in CSV format and filter data to reduce row count.
- **Reference Case:** [500Qk00000EBPO4IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EBPO4IAP/view)

### Scenario 3: "No Records Found" in Attribute Changes Report
- **Root Cause:** Selected object and time frame contain no change events.
- **Solution:** Verify object and time frame settings; demonstrate functionality with other objects.
- **Reference Case:** [500Qk00000G1LfXIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G1LfXIAV/view)

### Scenario 4: Unsupported File Format for User Imports
- **Root Cause:** Attempting to import Excel files instead of CSV.
- **Solution:** Convert Excel files to CSV format before importing.
- **Reference Case:** [500Qk00000GcuT0IAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GcuT0IAJ/view)

### Scenario 5: Long Query Times for Folder Activity
- **Root Cause:** Lack of indexing in outdated versions.
- **Solution:** Upgrade to the latest version with improved indexing.
- **Reference Case:** [500Qk00000GEJMYIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GEJMYIA5/view)

## Detailed Case Studies
### Case Study 1: Permissions Report Error
- **Symptoms:** "STATUS 500" error when accessing permissions report.
- **Diagnostic Steps:** Verified version, upgraded AIC, reviewed logs.
- **Resolution:** Upgraded to version 11.6.0.21; confirmed missing view due to inactive processes.
- **Takeaways:** Ensure required processes are configured and running.
- **Reference Case:** [500Qk00000E59H8IAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E59H8IAJ/view)

### Case Study 2: Exporting Large Reports
- **Symptoms:** Unable to export large reports; memory errors.
- **Diagnostic Steps:** Tested export formats, increased MaxRowCount, reviewed logs.
- **Resolution:** Recommended CSV format for large reports; advised filtering data.
- **Takeaways:** Understand limitations of 32-bit processes and row limits.
- **Reference Case:** [500Qk00000EBPO4IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EBPO4IAP/view)

### Case Study 3: Nasuni Activity Display Issue
- **Symptoms:** Activity displayed in C: paths instead of UNC paths.
- **Diagnostic Steps:** Reviewed FSAC/FSAA job configurations, modified host lists.
- **Resolution:** Reconfigured scans to target all Nasuni hosts; verified UNC path display.
- **Takeaways:** Proper host mapping is critical for accurate data representation.
- **Reference Case:** [500Qk00000LnWqjIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LnWqjIAF/view)

## Best Practices & Tips
- **Upgrade Regularly:** Ensure customers use supported versions to avoid known bugs and limitations.
- **Verify Configurations:** Check settings in configuration files and IIS bindings during troubleshooting.
- **Educate Customers:** Provide clear instructions for supported formats and features.
- **Monitor Scans:** Regularly review scan statuses and logs to catch issues early.
- **Document Errors:** Maintain a repository of common error messages and resolutions for quick reference.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist after following standard troubleshooting steps.
- Errors linked to product defects requiring development team intervention.
- Customer dissatisfaction due to unresolved problems.

### Escalation Procedure
1. Gather all relevant logs, screenshots, and configuration files.
2. Document troubleshooting steps taken and results.
3. Submit a detailed escalation request to the development team.
4. Communicate escalation status and expected timelines to the customer.