# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT Sensitive Data Discovery (SDD) Data Collection Issues

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the **StealthAUDIT Sensitive Data Discovery (SDD)** feature within the **Netwrix Enterprise Auditor (NEA)** platform. The SDD component is critical for identifying sensitive data across an organization, ensuring compliance, and mitigating risks. Understanding and resolving issues in this category is essential for maintaining the integrity and reliability of sensitive data scans.

## Technical Background

### Key Concepts
- **Sensitive Data Discovery (SDD):** A feature of StealthAUDIT that scans target systems for sensitive data, such as personally identifiable information (PII) or financial records.
- **Differential Scans:** Scans that identify changes since the last scan, focusing on newly modified or added files.
- **SQL Jobs:** Scheduled or manual tasks executed by the SQL Server to perform data collection and processing.
- **Service Accounts:** Accounts used by StealthAUDIT to access target systems and execute scans.
- **Add-ons:** Additional components, such as the Sensitive Data add-on, required for specific functionalities.

### System Context
- **StealthAUDIT Components:** Includes modules like Sensitive Data Discovery (SDD), Activity Monitor (SAM), and Access Information Center (AIC).
- **Environment Dependencies:** Proper configuration of service accounts, SQL Server, and target hosts is critical for successful scans.
- **Common Challenges:** Issues often arise from misconfigurations, environmental constraints, or product defects.

## Issue Recognition & Triage

### Symptoms
- SQL jobs failing to execute or timing out.
- Scans not identifying expected files or data.
- Missing or incomplete logs for skipped files.
- Portal access issues, such as disabled sign-in buttons.

### Priority Assessment
- **High Priority:** Scans failing entirely, sensitive data not being detected, or critical errors in logs.
- **Medium Priority:** Partial scan failures or performance issues.
- **Low Priority:** Cosmetic issues, such as incorrect log paths for skipped files.

## Diagnostic Methodology

### Systematic Approach
1. **Verify Symptoms:** Confirm the reported issue by reviewing logs, SQL job statuses, and scan results.
2. **Check Environment:** Validate the configuration of service accounts, add-ons, and target hosts.
3. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment.
4. **Analyze Logs:** Look for error messages, timeouts, or skipped file entries.
5. **Engage Development:** If the issue appears to be a product defect, escalate with detailed findings.

### Decision Points
- **Access Issues:** Investigate service account permissions and connectivity.
- **Scan Failures:** Check for missing add-ons or configuration errors.
- **Timeouts:** Adjust SQL job settings or optimize scan schedules.

## Information Collection

### Customer Questions
- What version of StealthAUDIT and its components are being used?
- Are there any recent changes to the environment (e.g., server migrations, updates)?
- What specific error messages or symptoms are being observed?
- Are there any logs or screenshots available?

### Logs to Collect
- SQL job logs and execution history.
- StealthAUDIT debug logs.
- Windows Event Viewer logs for related errors.
- Screenshots of the issue (e.g., disabled buttons, incomplete scans).

## Common Scenarios & Solutions

### Scenario 1: SQL Jobs Not Executing
- **Symptoms:** SQL jobs fail to run, either manually or on schedule.
- **Root Cause:** Missing Sensitive Data add-on or service account access issues.
- **Solution:** 
  - Install the Sensitive Data add-on on all target hosts.
  - Verify and update service account permissions.
  - Adjust SQL job timeout settings if necessary.

### Scenario 2: Scans Timing Out
- **Symptoms:** Scans fail due to timeouts, and the portal sign-in button is disabled.
- **Root Cause:** Long file paths exceeding 300 characters or StealthAUDIT Web Server not running.
- **Solution:** 
  - Enable the `LongPathsEnabled` registry key and reboot the server.
  - Restart the StealthAUDIT Web Server to restore portal access.

### Scenario 3: Differential Scans Missing Files
- **Symptoms:** Files older than the last scan date are not detected.
- **Root Cause:** Product defect in differential scanning logic.
- **Solution:** Apply the latest update to the SDD component to fix the scanning logic.

### Scenario 4: Skipped Password-Protected Files
- **Symptoms:** Password-protected files are skipped without warnings in logs.
- **Root Cause:** Defect in logging mechanism for skipped files.
- **Solution:** Apply hotfixes to improve logging and ensure skipped files are reported with original file paths.

## Detailed Case Studies

### Case Study 1: SQL Jobs Not Executing ([Ticket ID: 500Qk00000BwzBLIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BwzBLIAZ/view))
- **Symptoms:** SQL jobs for sensitive data scans were not running.
- **Diagnostic Steps:** Verified service account access, reviewed logs, and identified missing add-ons.
- **Resolution:** Installed the Sensitive Data add-on, adjusted SQL job timeouts, and migrated to a new host.
- **Key Takeaways:** Always verify add-on installation and service account permissions before troubleshooting further.

### Case Study 2: Scans Timing Out ([Ticket ID: 500Qk00000D0NYLIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D0NYLIA3/view))
- **Symptoms:** Sensitive data scans timed out, and the portal sign-in button was disabled.
- **Diagnostic Steps:** Investigated long file path errors and checked the status of the StealthAUDIT Web Server.
- **Resolution:** Enabled `LongPathsEnabled` registry key, rebooted the server, and restarted the web server.
- **Key Takeaways:** Ensure registry settings and web server status are checked for timeout-related issues.

### Case Study 3: Differential Scans Missing Files ([Ticket ID: 500Qk00000D5ideIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000D5ideIAB/view))
- **Symptoms:** Files older than the last scan date were not detected.
- **Diagnostic Steps:** Reproduced the issue in a lab environment and engaged development for analysis.
- **Resolution:** Applied an update to fix the differential scanning logic.
- **Key Takeaways:** Differential scans rely on accurate file metadata; ensure updates are applied promptly.

### Case Study 4: Skipped Password-Protected Files ([Ticket ID: 500Qk00000HVKyLIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HVKyLIAX/view))
- **Symptoms:** Password-protected files were skipped without warnings.
- **Diagnostic Steps:** Reviewed logs, escalated to development, and applied hotfixes.
- **Resolution:** Improved logging to include skipped files with original file paths.
- **Key Takeaways:** Logging accuracy is critical for customer trust; ensure thorough QA testing.

## Best Practices & Tips

- **Pre-Scan Checklist:** Verify add-on installation, service account permissions, and SQL job configurations before initiating scans.
- **Log Review:** Regularly review logs for errors or skipped files to identify potential issues early.
- **Environment Monitoring:** Monitor server performance and connectivity to prevent timeouts or access issues.
- **Customer Communication:** Clearly explain root causes and resolutions to customers, emphasizing preventive measures.
- **Proactive Updates:** Apply product updates and hotfixes promptly to address known defects.

## Escalation Guidelines

- **When to Escalate:**
  - Issues involving product defects or unresolvable environmental constraints.
  - Persistent failures despite following standard troubleshooting steps.
  - Customer dissatisfaction or high-impact scenarios.

- **How to Escalate:**
  - Collect all relevant logs, screenshots, and environment details.
  - Document troubleshooting steps and findings in detail.
  - Submit a comprehensive escalation request to the development team or senior support engineers.

