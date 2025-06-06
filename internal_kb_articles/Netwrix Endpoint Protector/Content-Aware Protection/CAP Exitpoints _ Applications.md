# Netwrix Endpoint Protector: Content-Aware Protection (CAP) Exitpoints / Applications Reference Guide

## Overview

This guide provides a comprehensive reference for troubleshooting and resolving issues related to the Content-Aware Protection (CAP) Exitpoints / Applications feature in Netwrix Endpoint Protector (EPP). CAP Exitpoints are critical for monitoring and controlling data transfers across various applications and endpoints, ensuring compliance with organizational policies and data protection regulations. This document outlines systematic approaches, common scenarios, and best practices to help support engineers address issues effectively and consistently.

---

## Technical Background

### Key Concepts
- **Content-Aware Protection (CAP):** A feature that monitors and controls data transfers based on content inspection and predefined policies.
- **Exitpoints:** Applications or channels through which data can leave an endpoint, such as email clients, cloud storage, or messaging apps.
- **Policies:** Rules configured to allow, block, or remediate data transfers based on content type, file type, or destination.
- **Deep Packet Inspection (DPI):** A mechanism used to analyze data packets for content classification and policy enforcement.

### System Context
- **Supported Platforms:** Windows, macOS, Linux (with limitations in non-GUI environments).
- **Policy Types:** Allowlist, Denylist, and Content-Aware rules.
- **Common Applications Monitored:** Email clients (Outlook), cloud storage (OneDrive, Google Drive), browsers, messaging apps (WhatsApp, Teams), and custom applications.

---

## Issue Recognition & Triage

### Identifying Issues
- **Symptoms:** Data transfers blocked unexpectedly, applications crashing, policies not enforced, or performance degradation.
- **Common Indicators:**
  - Alerts in the CAP report.
  - Application-specific errors (e.g., "The application was unable to start correctly").
  - Logs showing blocked actions despite configured allowlists.

### Assessing Priority
- **High Priority:** Issues affecting critical business applications (e.g., Outlook, OneDrive).
- **Medium Priority:** Policy enforcement inconsistencies (e.g., specific file types not blocked).
- **Low Priority:** Performance issues or minor application conflicts.

---

## Diagnostic Methodology

### Systematic Approach
1. **Reproduce the Issue:**
   - Attempt to replicate the problem in a controlled environment.
   - Verify if the issue is specific to certain endpoints, applications, or configurations.

2. **Policy Verification:**
   - Review CAP policies applied to the affected endpoints.
   - Check for conflicting rules or misconfigurations.

3. **Log Analysis:**
   - Collect logs using the EPPSupportTool.
   - Analyze CAP reports for blocked actions, errors, or anomalies.

4. **Environment Check:**
   - Confirm software versions (EPP client, application, OS).
   - Identify recent changes (e.g., updates, new policies).

5. **Testing Adjustments:**
   - Modify policies (e.g., add exceptions, use wildcards).
   - Test with updated configurations or test builds.

6. **Resolution Validation:**
   - Confirm the issue is resolved and policies are functioning as intended.
   - Monitor for recurrence over a defined period.

---

## Information Collection

### Customer Queries
- What is the affected application and its version?
- What specific actions or data transfers are being blocked or failing?
- Are there any recent changes to the environment (e.g., updates, new policies)?
- Is the issue reproducible on other endpoints?

### Data to Collect
- **Logs:** CAP reports, debug logs from EPPSupportTool.
- **Configuration Details:** Policy settings, allowlist/denylist entries.
- **Environment Details:** OS version, EPP client version, application version.
- **Screenshots/Recordings:** Evidence of the issue (e.g., error messages, blocked actions).

---

## Common Scenarios & Solutions

### Scenario 1: Policy Not Enforced
- **Example:** Blocking rules for Brave and Tor not functioning ([Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DRkX8IAL)).
- **Solution:** Verify policy settings, ensure correct user groups/endpoints are targeted, and test in a controlled environment.

### Scenario 2: Application Crashes
- **Example:** Adobe Acrobat Reader crashes with error 0xc000007b ([Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H5zh2IAB)).
- **Solution:** Add an Advanced Scanning Exception for the application.

### Scenario 3: Misclassification of Applications
- **Example:** OneDrive for Business classified as OneDrive Personal ([Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DubtVIAR)).
- **Solution:** Enable DPI and update to the latest EPP version.

### Scenario 4: Blocking Specific File Types
- **Example:** PNG email signatures blocked despite allowlist entry ([Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JvGEpIAN)).
- **Solution:** Review and adjust CAP policy to ensure proper recognition of allowed file types.

### Scenario 5: Compatibility Issues
- **Example:** CiscoVPN disconnects intermittently ([Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PSLMYIA5)).
- **Solution:** Add the CiscoVPN process to the exception list.

---

## Detailed Case Studies

### Case Study 1: Blocking File Transfers in Linux (WSL)
- **Ticket:** [500Qk00000ItTmzIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ItTmzIAF)
- **Symptoms:** File transfers blocked in WSL terminal; no user notifications.
- **Diagnostic Steps:** Verified CAP functionality in non-GUI environments, clarified limitations.
- **Resolution:** Confirmed actions logged on the EPP server; advised on feature request for Bluetooth granularity.
- **Key Takeaways:** Inform customers about limitations in non-GUI environments.

### Case Study 2: Outlook Hyperlink Slowness
- **Ticket:** [500Qk00000KdqEcIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KdqEcIAJ)
- **Symptoms:** Hyperlinks in Outlook slow to open or redirect incorrectly.
- **Diagnostic Steps:** Collected logs, excluded .ost/.pst files from scanning.
- **Resolution:** Adjusted CAP policy to resolve performance issues.
- **Key Takeaways:** Exclude large archive files from scanning to improve performance.

### Case Study 3: Regex Compatibility in Old Outlook
- **Ticket:** [500Qk00000NOq1rIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NOq1rIAD)
- **Symptoms:** Regex patterns for Brazilian PII not working in old Outlook.
- **Diagnostic Steps:** Tested policies, confirmed issue resolved in newer EPP version.
- **Resolution:** Upgraded to version 5.9.4.1.
- **Key Takeaways:** Ensure compatibility with older applications when using advanced regex.

---

## Best Practices & Tips

1. **Policy Testing:** Always test new policies in a controlled environment before deployment.
2. **Regular Updates:** Keep the EPP client and server updated to the latest versions.
3. **Log Monitoring:** Regularly review CAP reports for anomalies or misconfigurations.
4. **Clear Communication:** Provide customers with detailed instructions for log collection and testing.
5. **Documentation:** Maintain detailed records of policy changes and troubleshooting steps for future reference.

---

## Escalation Guidelines

### When to Escalate
- Issues persist despite following standard troubleshooting steps.
- Root cause cannot be identified after log analysis.
- Problems involve potential product defects or require development team input.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration details.
2. Document all troubleshooting steps taken and their outcomes.
3. Submit a detailed escalation request to the appropriate internal team, including customer impact and urgency.

--- 

This guide serves as a definitive reference for handling CAP Exitpoints / Applications issues, ensuring consistent and effective resolution.