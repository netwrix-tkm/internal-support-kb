# Netwrix Enterprise Auditor: StealthAUDIT for Windows - Data Collection Troubleshooting Guide

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the **Data Collection** feature of **StealthAUDIT for Windows** within **Netwrix Enterprise Auditor (NEA)**. Data collection is a critical component for gathering actionable insights from Windows environments, and ensuring its reliability is essential for maintaining audit accuracy and compliance. This document outlines systematic approaches, common scenarios, and best practices to help support engineers diagnose and resolve issues effectively.

---

## Technical Background
### Key Concepts
- **StealthAUDIT for Windows**: A component of NEA designed to collect data from Windows environments, including file shares, group memberships, and privileged accounts.
- **Data Collection Jobs**: Predefined or custom tasks that gather specific information from target systems.
- **INI Files**: Configuration files (e.g., `SBTFileMon.ini`) used by StealthAUDIT agents to define scanning parameters.
- **Proxy Server Configuration**: A setup where the SA server acts as an intermediary for scanning remote systems.
- **RPC (Remote Procedure Call)**: A protocol used for communication between the SA server and target hosts during data collection.

### Terminology
- **FSAC Scan**: File System Access Control scan, used to audit file share permissions.
- **SG_LocalAdmins**: A predefined job for identifying local administrator group memberships.
- **NAM (Network Access Management)**: A system for managing network paths and access configurations.

### System Context
StealthAUDIT relies on accurate configuration of network paths, INI files, and job parameters to perform data collection. Misconfigurations or environmental issues (e.g., network connectivity, permissions) can disrupt the process, leading to incomplete or failed scans.

---

## Issue Recognition & Triage
### Symptoms
- **FSAC Scan Failures**: Errors indicating inability to locate INI files or access network paths.
- **Incomplete Data Collection**: Missing data in result tables (e.g., `SA_SG_LocalAdmins_Details`) after a scan.
- **Intermittent RPC Errors**: Scans failing on specific hosts due to communication issues.

### Priority Assessment
- **High Priority**: Scans failing across multiple hosts or critical data missing.
- **Medium Priority**: Intermittent issues affecting non-critical hosts.
- **Low Priority**: Configuration questions or minor data discrepancies.

---

## Diagnostic Methodology
1. **Error Analysis**: Review error messages and logs for specific failure points (e.g., missing INI files, RPC errors).
2. **Configuration Validation**: Verify network paths, proxy server settings, and job parameters.
3. **Environment Testing**: Test connectivity and permissions for affected hosts.
4. **Historical Review**: Check for similar issues in the support database or customer history.
5. **Reproduction**: Attempt to replicate the issue in a controlled environment.

---

## Information Collection
### Questions to Ask Customers
- What specific error messages are you encountering?
- Are all hosts affected, or only specific ones?
- Have there been recent changes to the network or server configurations?
- What version and build of NEA are you using?

### Logs and Data to Collect
- **SA Console Logs**: For detailed error messages and job execution details.
- **INI File Locations**: Verify the presence and accessibility of configuration files.
- **Network Path Accessibility**: Test access to shared paths from the SA server.
- **Job Configuration Details**: Export job settings for review.

---

## Common Scenarios & Solutions
### Scenario 1: FSAC Scan Fails Due to Missing INI File
- **Symptoms**: Error indicating inability to retrieve the INI file path from the registry.
- **Root Cause**: Misconfigured proxy server or missing INI file.
- **Solution**: Configure the SA server as a proxy server and ensure the `SBTFileMon.ini` file is correctly placed and accessible. [Case Reference: [500Qk00000GAf0fIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GAf0fIAD/view)]

### Scenario 2: Customer Unaware of Existing Job Functionality
- **Symptoms**: Customer requests assistance for a task already supported by a predefined job.
- **Root Cause**: Lack of familiarity with NEA's capabilities.
- **Solution**: Guide the customer to use the relevant predefined job (e.g., `SG_LocalAdmins`) and explain its functionality. [Case Reference: [500Qk00000KNGv0IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KNGv0IAH/view)]

### Scenario 3: Intermittent RPC Errors During Scans
- **Symptoms**: Data for some hosts missing due to RPC errors.
- **Root Cause**: Analysis task does not retain data for previously successful hosts when failures occur.
- **Solution**: Implement a custom job to retain previous results and recommend upgrading to NEA v11.6.0.133 or later. [Case Reference: [500Qk00000M5542IAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M5542IAB/view)]

---

## Detailed Case Studies
### Case 1: FSAC Scan Failure
- **Initial Symptoms**: FSAC scan failed with an error about missing INI file paths.
- **Diagnostic Steps**: Verified network path accessibility, reviewed configuration settings, and checked for INI file presence.
- **Key Information**: Proxy server was not configured correctly.
- **Resolution**: Configured the SA server as a proxy server and ensured the `SBTFileMon.ini` file was accessible.
- **Takeaways**: Always validate proxy server configurations and INI file placement during setup.

### Case 2: SG_LocalAdmins Job Usage
- **Initial Symptoms**: Customer requested help identifying group memberships for local administrators.
- **Diagnostic Steps**: Confirmed licensing and guided the customer to the predefined `SG_LocalAdmins` job.
- **Key Information**: Customer was unaware of existing functionality.
- **Resolution**: Provided instructions to run the job and retrieve results.
- **Takeaways**: Educate customers on leveraging predefined jobs to maximize NEA's value.

### Case 3: RPC Errors During Scans
- **Initial Symptoms**: Intermittent RPC errors caused data loss for some hosts.
- **Diagnostic Steps**: Ran the `SG_LocalAdmins` task, analyzed logs, and identified missing functionality in the analysis task.
- **Key Information**: Task did not retain data for previously successful hosts.
- **Resolution**: Delivered a custom job and recommended upgrading to NEA v11.6.0.133.
- **Takeaways**: Ensure tasks are designed to handle intermittent failures gracefully.

---

## Best Practices & Tips
- **Validate Configurations**: Regularly verify proxy server settings, INI file placements, and network path accessibility.
- **Leverage Predefined Jobs**: Familiarize customers with existing job functionality to reduce unnecessary support requests.
- **Monitor Task Performance**: Use logs and results to identify patterns of intermittent failures.
- **Upgrade Regularly**: Encourage customers to stay on the latest NEA version to benefit from bug fixes and enhancements.
- **Document Resolutions**: Maintain detailed records of resolved cases to build a robust knowledge base.

---

## Escalation Guidelines
- **When to Escalate**:
  - Issues persist despite following standard troubleshooting steps.
  - Errors indicate potential bugs or missing functionality.
  - Customer requires a custom solution beyond existing capabilities.
- **How to Escalate**:
  - Provide a detailed summary of the issue, including logs, configuration details, and steps already taken.
  - Submit the case to the development or product team for further analysis.
  - Communicate escalation status and expected timelines to the customer.

--- 

This guide serves as a definitive reference for handling data collection issues in StealthAUDIT for Windows, ensuring consistent and effective support for Netwrix Enterprise Auditor users.