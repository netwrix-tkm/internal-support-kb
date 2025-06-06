# Knowledge Base Reference Guide: Troubleshooting Data Collection Issues in StealthAUDIT for EMC

## Overview
This guide provides a comprehensive reference for diagnosing and resolving data collection issues in the StealthAUDIT for EMC component of Netwrix Enterprise Auditor (NEA). These issues often involve challenges with permissions, configuration mismatches, or environmental factors that impact the ability to collect and report data accurately. Understanding and addressing these issues is critical to ensuring the integrity and completeness of audit data.

## Technical Background
StealthAUDIT for EMC is a component of NEA designed to collect and analyze data from EMC storage systems, including Isilon OneFS and Celerra NAS environments. Key concepts include:

- **File System Auditing Agent (FSAA):** Responsible for scanning file systems and collecting permissions and activity data.
- **Proxy as a Service:** A configuration option for data collection that uses a proxy server to facilitate communication with EMC systems.
- **CEE Agent:** A component that forwards events from EMC systems to NEA for processing.
- **System.Data.SQLite.dll:** A critical library used by NEA for database operations during data collection.

### Common Terminology
- **FSAC Job:** File System Activity Collection job, responsible for gathering activity data.
- **Seek Job:** A job type that scans file systems for specific data.
- **BackupAdmin Role:** A role in EMC systems that grants necessary permissions for data collection.
- **Registry Access:** Required for certain operations, such as reading configuration data from the Windows registry.

## Issue Recognition & Triage
### Symptoms
- Missing users or groups in permission reports.
- Inability to locate activity log files post-patching.
- Errors during scans, such as COM object casting issues or assembly loading errors.
- Scans failing at specific progress percentages.

### Priority Assessment
- **High Priority:** Issues that prevent data collection entirely or result in incomplete reports.
- **Medium Priority:** Errors that occur intermittently or affect non-critical data.
- **Low Priority:** Minor configuration mismatches that do not impact functionality.

## Diagnostic Methodology
1. **Verify Environment Details:**
   - Confirm NEA version and hotfixes applied.
   - Identify the EMC system type (e.g., Isilon OneFS, Celerra NAS).
   - Check service account permissions and roles.

2. **Reproduce the Issue:**
   - Run the affected job (e.g., FSAC or Seek) and capture error messages.
   - Perform a 0-depth scan to isolate the problem.

3. **Analyze Logs and Configuration:**
   - Review NEA logs for detailed error messages.
   - Check FSAA and Proxy configurations.
   - Verify registry access and environmental variables.

4. **Identify Root Cause:**
   - Look for mismatched DLL versions, incorrect permissions, or configuration errors.

## Information Collection
### Questions to Ask Customers
- What version of NEA and hotfixes are installed?
- What type of EMC system is being audited?
- Have there been recent changes to the environment (e.g., patches, configuration updates)?
- Are there specific error messages or logs available?

### Logs and Data to Collect
- NEA job logs (e.g., FSAC, Seek).
- Windows Event Logs from the NEA server.
- Screenshots of configuration settings.
- Output of PowerShell commands for DLL version checks.

## Common Scenarios & Solutions
### Scenario 1: Missing Users/Groups in Reports
- **Symptoms:** Built-in Administrators group not appearing in permission reports.
- **Root Cause:** Incorrect FSAA scan configuration for EMC Isilon OneFS.
- **Resolution:**
  1. Update FSAA scan configuration to include necessary scoping options.
  2. Add the service account to the BackupAdmin Role.
  3. Conduct a new scan to verify results.
- **Reference Case:** [413806](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CaMG1IAN/view)

### Scenario 2: Missing Activity Logs Post-Patching
- **Symptoms:** No activity logs found after a patch was applied.
- **Root Cause:** Incorrect Proxy configuration and registry access issues.
- **Resolution:**
  1. Correct Proxy settings and add the Proxy install path to environmental variables.
  2. Ensure registry access permissions are properly configured.
  3. Perform a bulk import for the EMC host.
- **Reference Case:** [421694](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G3RYjIAN/view)

### Scenario 3: Assembly Loading Errors
- **Symptoms:** Seek jobs fail with a `System.Data.SQLite` assembly error.
- **Root Cause:** Outdated `System.Data.SQLite.dll` file in the installation directory.
- **Resolution:**
  1. Identify the outdated DLL version using PowerShell.
  2. Replace the outdated DLL with the correct version.
  3. Perform a 0-depth scan to confirm functionality.
- **Reference Case:** [428321](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ir5qRIAR/view)

### Scenario 4: Scan Errors After Hotfix Application
- **Symptoms:** Scans fail at 22% with COM object casting errors.
- **Root Cause:** Registry access issues caused by residual configurations after hotfix application.
- **Resolution:**
  1. Uninstall NEA and SDD components.
  2. Reboot the NEA server.
  3. Install the latest versions of NEA and SDD.
  4. Run the 0-CreateSchema job and initiate the scan.
- **Reference Case:** [431273](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KHi5xIAD/view)

## Detailed Case Studies
### Case Study 1: Missing Built-in Administrators Group ([413806](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CaMG1IAN/view))
- **Symptoms:** Missing users/groups in reports.
- **Diagnostic Steps:** Verified FSAA configuration, adjusted scoping options, and added service account to BackupAdmin Role.
- **Resolution:** Updated configuration and conducted a new scan.
- **Key Takeaways:** Always verify the correct device type is selected during configuration.

### Case Study 2: Missing Activity Logs ([421694](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G3RYjIAN/view))
- **Symptoms:** No logs post-patching.
- **Diagnostic Steps:** Verified Proxy settings, corrected registry access, and performed a bulk import.
- **Resolution:** Adjusted configuration and re-ran the FSAC job.
- **Key Takeaways:** Monitor Proxy settings and environmental variables after patches.

### Case Study 3: Assembly Loading Error ([428321](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ir5qRIAR/view))
- **Symptoms:** Seek jobs fail with DLL errors.
- **Diagnostic Steps:** Identified outdated DLL version and replaced it.
- **Resolution:** Replaced DLL and confirmed functionality with a 0-depth scan.
- **Key Takeaways:** Ensure all binaries are updated during patches.

### Case Study 4: Scan Errors After Hotfix ([431273](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KHi5xIAD/view))
- **Symptoms:** Scans fail at 22%.
- **Diagnostic Steps:** Uninstalled and reinstalled NEA and SDD components.
- **Resolution:** Clean installation resolved the issue.
- **Key Takeaways:** Always reboot the server after uninstalling components to clear residual configurations.

## Best Practices & Tips
- **Configuration Validation:** Always verify device type, Proxy settings, and environmental variables during setup.
- **Permission Management:** Regularly review and update service account roles and permissions.
- **Patch Testing:** Test patches in a staging environment to identify potential issues before deployment.
- **DLL Version Checks:** Use PowerShell to verify DLL versions after updates.
- **Documentation:** Follow the latest NEA documentation for configuration and troubleshooting.

## Escalation Guidelines
- **When to Escalate:**
  - Issues persist after following documented resolution steps.
  - Errors involve unsupported configurations or third-party components.
  - Critical data collection is blocked, impacting business operations.

- **How to Escalate:**
  1. Gather all relevant logs, screenshots, and configuration details.
  2. Document steps already taken and their outcomes.
  3. Submit a detailed escalation request to the Netwrix development or professional services team.