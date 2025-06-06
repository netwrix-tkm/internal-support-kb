# Netwrix Endpoint Protector: Comprehensive Guide to Troubleshooting eDiscovery Policy Issues

## Overview

This guide provides a systematic approach to understanding, diagnosing, and resolving issues related to eDiscovery (eD) Policies in Netwrix Endpoint Protector (EPP). eDiscovery policies are critical for identifying and managing sensitive data at rest and in transit, ensuring compliance with organizational and regulatory requirements. This document serves as a definitive reference for support engineers, enabling consistent and effective troubleshooting of eDiscovery-related issues.

---

## Technical Background

### Key Concepts
- **eDiscovery Policies**: Configurations within EPP designed to scan and identify sensitive data based on predefined or custom rules.
- **Data at Rest vs. Data in Transit**: eDiscovery policies can target data stored on devices (at rest) or data being transferred (in transit).
- **Content Aware Protection (CAP)**: A related feature that works in tandem with eDiscovery to monitor and control sensitive data.
- **Location Lists**: Specific directories or paths configured for eDiscovery scans.
- **MIME Type Allowlist/Denylist**: Global settings that determine which file types are included or excluded from scans.
- **Regex Patterns**: Custom expressions used to define specific search criteria for sensitive data.

### System Context
- eDiscovery policies rely on proper configuration of scanning rules, file type filters, and location lists.
- Global settings, such as MIME Type allowlists, apply across all policies and can impact both eDiscovery and CAP functionalities.
- Misconfigurations or misunderstandings of policy behavior can lead to incomplete scans, false positives, or missed detections.

---

## Issue Recognition & Triage

### Common Symptoms
- Policies not detecting specific file types or sensitive data (e.g., [500Qk00000CPiDRIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CPiDRIA1/view)).
- Scans returning no results or incomplete results (e.g., [500Qk00000H39ueIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H39ueIAB/view)).
- Reports not generated after scans (e.g., [500Qk00000KDUb3IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KDUb3IAH/view)).
- Misunderstanding of policy behavior, such as file deletion tracking or partitioning systems (e.g., [500Qk00000KTnBWIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KTnBWIA1/view)).

### Triage Steps
1. **Categorize the Issue**:
   - Detection failure (specific file types or sensitive data).
   - Configuration misunderstanding (e.g., allowlists, regex, partitions).
   - Reporting or alerting issues.
2. **Assess Priority**:
   - High: Data compliance risks or critical business impact.
   - Medium: Non-critical detection or reporting issues.
   - Low: General inquiries or feature clarifications.

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Customer's Environment**:
   - Identify the operating systems, file types, and sensitive data involved.
   - Confirm the version of EPP and any recent changes or updates.
2. **Verify Policy Configuration**:
   - Check eDiscovery settings, including location lists, file type filters, and regex patterns.
   - Review global MIME Type allowlist/denylist settings.
3. **Test Functionality**:
   - Conduct test scans to replicate the issue.
   - Compare results with expected behavior.
4. **Analyze Logs**:
   - Collect and review logs to identify errors or misconfigurations.
5. **Communicate Findings**:
   - Provide clear explanations and next steps to the customer.

---

## Information Collection

### Key Questions to Ask
- What specific data or file types are you trying to detect?
- Are you scanning data at rest, in transit, or both?
- Have there been any recent changes to your EPP configuration or environment?
- Are you using custom regex patterns or predefined rules?
- Have you configured location lists or global MIME Type settings?

### Logs and Data to Collect
- eDiscovery policy configuration files.
- Scan logs and error messages.
- Screenshots of policy settings.
- Details of the customer's environment (OS, file paths, etc.).

---

## Common Scenarios & Solutions

### Scenario 1: Detection Failure for Specific File Types
- **Example**: SQL files not detected on MacOS ([500Qk00000H39ueIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H39ueIAB/view)).
- **Solution**:
  - Verify file type filters in the eDiscovery policy.
  - Adjust MIME Type allowlist settings to include the desired file types.
  - Test the policy after making changes.

### Scenario 2: No Results Returned for Scans
- **Example**: Linux devices not returning any scan results ([500Qk00000H39ueIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H39ueIAB/view)).
- **Solution**:
  - Confirm that location lists are properly configured.
  - Check for misconfigurations in the eDiscovery policy.
  - Conduct test scans to validate functionality.

### Scenario 3: Misunderstanding of Partitioning System
- **Example**: Reports not generated due to incorrect partition selection ([500Qk00000KDUb3IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KDUb3IAH/view)).
- **Solution**:
  - Educate the customer on time-labeled partitions and their impact on scan results.
  - Recommend backing up Audit Logs before initiating new scans.

### Scenario 4: Clarification on Logging Capabilities
- **Example**: Customer inquiring about file deletion tracking ([500Qk00000KTnBWIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KTnBWIA1/view)).
- **Solution**:
  - Explain the scenarios in which EPP logs "delete file" events.
  - Provide documentation for further reference.

---

## Detailed Case Studies

### Case Study 1: Custom Policy Creation ([500Qk00000BhNaxIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BhNaxIAF/view))
- **Symptoms**: Customer needed to create a custom policy for detecting credit card and bank routing numbers.
- **Diagnostic Steps**:
  - Scheduled a remote session to understand requirements.
  - Reviewed previous POC setup and guided the customer through policy creation.
- **Resolution**:
  - Assisted in configuring eDiscovery for specific folders and paths.
  - Demonstrated alert-only policy setup.
- **Key Takeaways**:
  - Document POC setups to avoid loss of information.
  - Renew licenses promptly to maintain access to configurations.

### Case Study 2: Transition from Forcepoint to EPP ([500Qk00000KzQF1IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KzQF1IAN/view))
- **Symptoms**: Customer needed to replicate departing employee reports.
- **Diagnostic Steps**:
  - Conducted a remote session to address questions.
  - Provided guidance on CAP features and contextual detection.
- **Resolution**:
  - Suggested feature requests and provided documentation for further assistance.
- **Key Takeaways**:
  - Transitioning customers may require additional support to adapt to new systems.
  - Contextual Detection can be a viable alternative to REGEX rules.

---

## Best Practices & Tips

1. **Thoroughly Test Policies**:
   - Always test eDiscovery policies after configuration to ensure expected behavior.
2. **Document Configurations**:
   - Encourage customers to maintain detailed records of their setups for future reference.
3. **Educate Customers**:
   - Provide clear explanations of global settings, partitioning systems, and logging capabilities.
4. **Use Regex Sparingly**:
   - Avoid excessive use of regex patterns to prevent performance degradation.
5. **Backup Audit Logs**:
   - Remind customers to back up logs before initiating new scans to avoid data loss.

---

## Escalation Guidelines

### When to Escalate
- Complex issues requiring development team involvement (e.g., suspected bugs).
- Persistent detection failures despite correct configurations.
- Performance issues impacting multiple customers.

### How to Escalate
- Collect all relevant logs, screenshots, and configuration details.
- Provide a detailed summary of troubleshooting steps taken.
- Submit the case to the appropriate escalation queue with clear documentation.