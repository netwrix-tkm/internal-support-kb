# Knowledge Base Reference Guide: Troubleshooting File Shadow Issues in Netwrix Endpoint Protector

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the file shadow feature in Netwrix Endpoint Protector, specifically when certain file types (e.g., `.doc`, `.docx`) cannot be created. Understanding and resolving these issues is critical to maintaining the integrity of file monitoring and ensuring seamless operation of the Allowlist/Denylist functionality.

### Purpose
- To equip support engineers with a systematic approach to diagnose and resolve file shadow issues.
- To ensure consistent handling of customer cases involving file creation restrictions.

### Scope
This guide focuses on the Allowlist/Denylist functionality within the Reports & Analysis / Logs component of Netwrix Endpoint Protector.

---

## Technical Background

### Key Concepts
- **File Shadowing**: A feature that creates copies of files for monitoring and auditing purposes.
- **Allowlist/Denylist**: Configuration settings that control which file types or operations are permitted or restricted.
- **File Repository Settings**: The backend configuration that governs file storage and access rules.

### System Context
- The file shadow feature relies on the Allowlist/Denylist to determine permissible file types.
- Misconfigurations in the Allowlist/Denylist or file repository settings can lead to unexpected behavior, such as the inability to create specific file types.

---

## Issue Recognition & Triage

### Symptoms
- Customers report that specific file types (e.g., `.doc`, `.docx`) cannot be created or shadowed.
- Logs may show errors or warnings related to file creation.

### Priority Assessment
- **High Priority**: If the issue affects critical business operations or compliance requirements.
- **Medium Priority**: If the issue is isolated to non-critical file types or environments.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Configuration**: Check the Allowlist/Denylist settings for the affected file types.
2. **Review Logs**: Analyze logs for errors or warnings related to file creation.
3. **Test File Creation**: Attempt to create files with various extensions to isolate the issue.
4. **Inspect Repository Settings**: Examine the file repository configuration for restrictions.

### Decision Points
- If the Allowlist/Denylist is misconfigured, proceed to update the settings.
- If the repository settings are restrictive, adjust them to allow the affected file types.

---

## Information Collection

### Customer Queries
- What file types are affected?
- When did the issue first occur?
- Have there been recent changes to the Allowlist/Denylist or repository settings?

### Data to Collect
- Allowlist/Denylist configuration files.
- Logs from the Reports & Analysis / Logs component.
- Screenshots or error messages related to the issue.

---

## Common Scenarios & Solutions

### Scenario 1: Misconfigured Allowlist/Denylist
- **Symptoms**: Specific file types are blocked.
- **Resolution**: Update the Allowlist to include the affected file types and ensure no conflicting Denylist entries exist.

### Scenario 2: Restrictive Repository Settings
- **Symptoms**: File creation fails despite correct Allowlist/Denylist settings.
- **Resolution**: Adjust the repository settings to permit the creation of the affected file types.

---

## Detailed Case Studies

### Case Study: File Shadow Issue with `.doc` and `.docx` Files
- **Ticket ID**: [500Qk00000FV63hIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FV63hIAD/view)
- **Initial Symptoms**: Customer reported that `.doc` and `.docx` files could not be created using the file shadow feature.
- **Diagnostic Steps**:
  1. Verified Allowlist/Denylist settings.
  2. Reviewed logs for errors related to `.doc` and `.docx` files.
  3. Tested file creation with other extensions to confirm the issue was isolated.
  4. Inspected repository settings for restrictions.
- **Key Information**: The repository settings were found to restrict `.doc` and `.docx` file creation.
- **Resolution**:
  - Updated the repository settings to allow `.doc` and `.docx` files.
  - Verified that the Allowlist included these extensions and no conflicting Denylist entries were present.
- **Key Takeaways**:
  - Repository settings can override Allowlist/Denylist configurations.
  - Regular reviews of repository settings are essential to prevent similar issues.
- **Efficiency Improvements**:
  - Develop a checklist for repository settings to streamline diagnostics.

---

## Best Practices & Tips

1. **Regular Configuration Reviews**: Periodically review Allowlist/Denylist and repository settings to prevent misconfigurations.
2. **Log Analysis**: Use logs as the primary diagnostic tool to identify root causes quickly.
3. **Customer Communication**: Clearly explain the resolution steps to customers and provide guidance on preventing similar issues.
4. **Documentation**: Maintain detailed records of configuration changes for future reference.

---

## Escalation Guidelines

### Criteria for Escalation
- The issue persists despite following the diagnostic methodology.
- Logs indicate a deeper system-level problem beyond configuration.
- The customer requires a resolution within a critical timeframe.

### Escalation Procedure
1. Document all diagnostic steps and findings.
2. Collect relevant logs and configuration files.
3. Escalate to the Tier 2 or Development team with a detailed summary of the issue.

--- 

This guide serves as a definitive reference for handling file shadow issues related to the Allowlist/Denylist functionality in Netwrix Endpoint Protector.