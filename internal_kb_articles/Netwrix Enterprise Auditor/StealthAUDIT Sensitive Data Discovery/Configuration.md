# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT Sensitive Data Discovery Configuration Issues

## Overview

This guide focuses on troubleshooting configuration issues within the **StealthAUDIT Sensitive Data Discovery (SDD)** feature of Netwrix Enterprise Auditor. The SDD feature is critical for identifying and managing sensitive data across file systems and SharePoint environments. Proper configuration ensures accurate data discovery, minimizes false positives, and supports compliance efforts. This guide provides a systematic approach to diagnosing and resolving common issues, with insights drawn from real-world cases.

---

## Technical Background

### Key Concepts
- **Sensitive Data Discovery (SDD):** A feature that scans file systems and SharePoint environments to identify sensitive data based on predefined criteria.
- **LAT Preservation:** A setting that retains Last Access Time (LAT) metadata during scans. This requires specific write permissions and is applicable only in Windows environments.
- **False Positives:** Files incorrectly flagged as containing sensitive data. These can be excluded using filters configured in the SDD settings.
- **UNC/Share Format:** Universal Naming Convention paths (e.g., `\\server\share\path`) used to specify file locations in network environments.

### System Context
- **File System Scans:** SDD scans file servers and NAS devices to identify sensitive data. Proper permissions and configuration are essential for accurate results.
- **SharePoint Scans:** Operates independently of file system scans, with its own configuration and criteria.
- **Service Accounts:** Must have appropriate permissions to access file systems, write LAT metadata (if enabled), and execute scans.

---

## Issue Recognition & Triage

### Common Symptoms
1. Errors during bulk imports, such as "DLPEX database does not exist, there is no data to import."
2. False positives not being excluded despite configuration.
3. Uncertainty about wildcard usage in false positive filters.

### Priority Assessment
- **High Priority:** Errors preventing scans or imports (e.g., database-related errors).
- **Medium Priority:** Configuration issues affecting scan accuracy (e.g., false positives not excluded).
- **Low Priority:** General inquiries about feature capabilities (e.g., wildcard usage).

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Environment Details:**
   - Confirm product version, build number, and component.
   - Check service account permissions and access to target systems.

2. **Reproduce the Issue:**
   - Attempt to replicate the error or behavior in a controlled environment.

3. **Analyze Logs and Settings:**
   - Review error messages, logs, and configuration settings.
   - Focus on permissions, paths, and feature-specific options (e.g., LAT preservation).

4. **Test Incremental Changes:**
   - Adjust settings or permissions incrementally to isolate the root cause.

5. **Validate Resolution:**
   - Confirm that the issue is resolved and document the steps taken.

---

## Information Collection

### Questions to Ask Customers
- What is the exact error message or behavior observed?
- What type of environment is being scanned (e.g., file system, SharePoint)?
- Are there any recent changes to permissions, configurations, or software versions?
- Is LAT preservation enabled, and are write permissions configured?

### Logs and Data to Collect
- **Error Logs:** From the Netwrix Enterprise Auditor console.
- **Configuration Details:** Screenshots or exports of SDD settings.
- **Service Account Permissions:** Details on access levels for file systems or SharePoint.
- **Environment Details:** File server/NAS device type, SharePoint version, etc.

---

## Common Scenarios & Solutions

### Scenario 1: Bulk Import Error - "DLPEX database does not exist"
- **Root Cause:** LAT preservation was enabled, but the service account lacked write permissions.
- **Solution:** Disable LAT preservation in the SDD settings. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FR7cgIAD/view)

### Scenario 2: False Positives Not Excluded for File Systems
- **Root Cause:** Incorrect path format in the false positive configuration.
- **Solution:** Use the correct UNC/Share format for file paths. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NNFAnIAP/view)

### Scenario 3: Wildcard Usage in False Positive Filters
- **Root Cause:** Lack of clarity on wildcard support in exclusion filters.
- **Solution:** Confirm that wildcards (e.g., `*.txt`) are supported and configure filters before running scans. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NrOBrIAN/view)

---

## Detailed Case Studies

### Case 1: Bulk Import Error
- **Symptoms:** "DLPEX database does not exist" error during file system bulk import.
- **Diagnostic Steps:**
  1. Verified service account permissions and access to the NAS device.
  2. Cleared existing data and rescanned the file server group.
  3. Disabled LAT preservation, resolving the issue.
- **Key Takeaways:** LAT preservation requires write permissions. Disable it unless necessary. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FR7cgIAD/view)

### Case 2: False Positives Not Excluded
- **Symptoms:** Test false positive not excluded for file systems, but working for SharePoint.
- **Diagnostic Steps:**
  1. Reviewed false positive configuration paths.
  2. Identified incorrect path format (not in UNC/Share format).
  3. Corrected the path, resolving the issue.
- **Key Takeaways:** Always use UNC/Share format for file system paths. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NNFAnIAP/view)

### Case 3: Wildcard Usage Inquiry
- **Symptoms:** Customer unsure if wildcards are supported in false positive filters.
- **Diagnostic Steps:**
  1. Reviewed documentation and conducted internal testing.
  2. Confirmed wildcard support and provided configuration guidance.
- **Key Takeaways:** Configure filters before scans and consult documentation for syntax. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NrOBrIAN/view)

---

## Best Practices & Tips

1. **LAT Preservation:**
   - Disable unless required. If enabled, ensure write permissions are configured.

2. **False Positive Filters:**
   - Use UNC/Share format for file paths.
   - Configure filters before running scans to avoid unnecessary processing.

3. **Service Account Permissions:**
   - Verify read/write access to all target systems and databases.

4. **Documentation Reference:**
   - Regularly consult the Netwrix Help Center for updates and best practices:
     - [Adding False Positive Exclusion Filters](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Settings/SensitiveData/Exclusions/Add.htm)
     - [NEA v11.6 - False Positives Tab](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/EnterpriseAuditor/Admin/Settings/SensitiveData/Exclusions/Overview.htm)

---

## Escalation Guidelines

### When to Escalate
- Persistent errors after following standard troubleshooting steps.
- Issues involving unsupported configurations or environments.
- Requests for feature enhancements or customizations.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration details.
2. Document the steps already taken and their outcomes.
3. Submit the case to the appropriate escalation team with a detailed summary.

--- 

End of Document.