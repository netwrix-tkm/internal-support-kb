# Knowledge Base Reference Guide: Troubleshooting Sensitive Data Discovery (SDD) Issues in Custom Reports

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the Sensitive Data Discovery (SDD) feature in Netwrix Enterprise Auditor, specifically within the context of Custom Reports. SDD is a critical component for identifying and reporting sensitive data across monitored environments. Understanding and resolving issues in this category ensures accurate reporting, compliance, and customer satisfaction.

## Technical Background

### Key Concepts
- **Sensitive Data Discovery (SDD):** A feature in Netwrix Enterprise Auditor that scans files and folders to identify sensitive data based on predefined or custom criteria.
- **Custom Reports:** Reports tailored to specific customer requirements, often used to display sensitive data findings or skipped files during scans.
- **Password-Protected Files:** Files, such as ZIP archives, that require a password to access their contents. These files may pose challenges for automated scanning tools.

### System Context
- **Netwrix Enterprise Auditor Version:** Issues discussed here pertain to version 11.6.
- **StealthAUDIT Integration:** SDD is integrated with StealthAUDIT to enhance data discovery and reporting capabilities.
- **Common Use Cases:** Monitoring sensitive data in specific directories, generating reports for compliance, and identifying skipped files during scans.

## Issue Recognition & Triage

### Symptoms
- SDD skips password-protected ZIP files without notifying the user.
- Difficulty in configuring new servers or folders for SDD scans and reports.
- Discrepancies in sensitive data reporting due to incomplete scans.

### Priority Assessment
- **High Priority:** Issues that result in incomplete scans or missing sensitive data in reports.
- **Medium Priority:** Configuration challenges for new servers or folders.
- **Low Priority:** Feature requests or enhancements, such as additional reporting capabilities.

## Diagnostic Methodology

1. **Confirm the Issue:**
   - Verify the reported behavior (e.g., skipped files, incomplete scans, or configuration challenges).
   - Reproduce the issue in a test environment if possible.

2. **Engage Relevant Teams:**
   - For product defects, involve the R&D team to investigate and develop a fix.
   - For configuration issues, provide step-by-step guidance to the customer.

3. **Test Resolutions:**
   - Validate any fixes or configurations in a controlled environment before deploying them to the customer.

4. **Communicate Updates:**
   - Keep the customer informed about progress, expected timelines, and resolution steps.

## Information Collection

### Questions to Ask Customers
- What version of Netwrix Enterprise Auditor are you using?
- Are there specific files, folders, or servers where the issue occurs?
- Have you noticed any patterns (e.g., file types, locations) in the skipped files?
- What are the criteria for your Custom Reports?

### Logs and Data to Collect
- SDD scan logs to identify skipped files or errors.
- Configuration details for the affected servers or folders.
- Screenshots or exported reports showing discrepancies.

## Common Scenarios & Solutions

### Scenario 1: SDD Skips Password-Protected ZIP Files
- **Symptoms:** Files are skipped without notification during scans.
- **Root Cause:** Product defect in handling password-protected ZIP files.
- **Resolution:** Apply the hotfix developed for version 11.6, which restores functionality for handling password-protected ZIP files created with WinRAR and introduces notifications for skipped files.
- **Reference Case:** [500Qk00000KZGZXIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KZGZXIA5/view)

### Scenario 2: Configuring SDD for a New Server and Folder
- **Symptoms:** Difficulty in adding a new server and setting up a daily report for a specific folder.
- **Root Cause:** Lack of prior configuration for the new server and folder.
- **Resolution:** Provide instructions for adding the server, validate scans for the specified folder, and create a Custom Report based on the customer's criteria.
- **Reference Case:** [500Qk00000PT5NlIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PT5NlIAL/view)

## Detailed Case Studies

### Case Study 1: Skipped Password-Protected ZIP Files
- **Ticket ID:** [500Qk00000KZGZXIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KZGZXIA5/view)
- **Initial Symptoms:** Customer reported that SDD skipped password-protected ZIP files without notification.
- **Diagnostic Steps:**
  1. Verified the issue by reviewing scan logs.
  2. Engaged the R&D team to investigate and develop a hotfix.
  3. Tested the hotfix to ensure it resolved the issue.
- **Resolution:** Released a hotfix that restored functionality and added notifications for skipped files.
- **Key Takeaways:** Always verify scan logs for skipped files and communicate hotfix timelines clearly to customers.

### Case Study 2: Adding a New Server and Folder
- **Ticket ID:** [500Qk00000PT5NlIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PT5NlIAL/view)
- **Initial Symptoms:** Customer needed assistance configuring SDD for a new server and folder.
- **Diagnostic Steps:**
  1. Reviewed the customer's existing configuration.
  2. Provided step-by-step instructions for adding the new server.
  3. Validated that scans were running correctly for the specified folder.
  4. Created a Custom Report to meet the customer's requirements.
- **Resolution:** Successfully configured the new server and folder, ensuring accurate reporting.
- **Key Takeaways:** Validate scans before generating reports to avoid discrepancies.

## Best Practices & Tips

1. **Proactive Communication:**
   - Keep customers informed about progress and timelines for fixes or configurations.
   - Provide clear instructions and follow up to ensure successful implementation.

2. **Thorough Validation:**
   - Always test fixes and configurations in a controlled environment before deployment.
   - Validate scans and reports to ensure accuracy.

3. **Documentation:**
   - Maintain detailed records of customer configurations and resolutions for future reference.
   - Log feature requests and enhancement ideas for product improvement.

4. **Efficiency Improvements:**
   - Use templates for common configuration tasks to streamline the setup process.
   - Develop automated scripts for validating scans and generating reports.

## Escalation Guidelines

### When to Escalate
- Issues involving product defects or unresolvable technical challenges.
- Requests for new features or significant enhancements.
- Cases where customer expectations cannot be met with existing functionality.

### How to Escalate
1. Collect all relevant information, including logs, screenshots, and customer requirements.
2. Document the issue clearly, including steps to reproduce and any attempted resolutions.
3. Submit the case to the R&D or Product Management team with a detailed summary.
4. Communicate the escalation status and expected timelines to the customer.