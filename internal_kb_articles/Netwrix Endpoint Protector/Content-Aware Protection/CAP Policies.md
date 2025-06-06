# Comprehensive Knowledge Base Guide: Content-Aware Protection (CAP) Policies in Netwrix Endpoint Protector

## Overview

Content-Aware Protection (CAP) Policies in Netwrix Endpoint Protector are designed to monitor, block, and report sensitive data transfers across various endpoints and exit points. This feature is critical for ensuring data security, compliance with regulations, and preventing data leaks. CAP Policies leverage advanced mechanisms like Deep Packet Inspection (DPI), contextual detection, and metadata analysis to enforce data security rules. This guide provides a unified reference for understanding, troubleshooting, and optimizing CAP Policies, ensuring consistent and effective support for customers.

---

## Technical Background

### Key Concepts

- **Content-Aware Protection (CAP):** A feature that scans data transfers for sensitive information based on predefined policies, such as blocking sensitive data (e.g., credit card numbers, personal identification) or specific file types.
- **Exit Points:** Channels through which data can leave the organization, such as email, USB devices, cloud storage, printers, remote desktop connections, and Zoom chat.
- **Deep Packet Inspection (DPI):** A mechanism for analyzing network traffic to identify sensitive data in real-time, including encrypted traffic.
- **Contextual Detection:** A feature that identifies sensitive data based on patterns, such as credit card numbers or specific keywords.
- **Allowlist/Denylist:** Lists used to permit or block specific file types, domains, or devices.
- **Thresholds:** Settings that define the sensitivity level for triggering CAP actions based on detected data patterns.
- **Intercept VPN:** A feature that enables monitoring of network traffic on macOS devices.
- **File Shadowing:** A feature that retains copies of blocked files for auditing purposes.
- **Reporting V2:** An advanced logging feature that captures detailed information, including destination details.

### System Context

CAP Policies are applied at the client level and enforced through the Endpoint Protector (EPP) agent. Policies are configured on the server and pushed to clients. Proper functionality depends on:
- Correct policy configuration.
- Up-to-date client and server versions.
- Adequate system permissions (e.g., Full Disk Access on macOS).

Netwrix Endpoint Protector operates across multiple platforms, including Windows, macOS, and Linux. The system integrates with third-party tools like Zscaler, CrowdStrike, and Palo Alto GlobalProtect, which may impact CAP functionality.

---

## Issue Recognition & Triage

### Symptoms of CAP Policy Issues

- CAP policies not triggering as expected (e.g., files not blocked, incorrect reports).
- False positives or negatives in sensitive data detection.
- Missing logs or incomplete data in reports.
- Problems with notifications or remediation actions.
- Application functionality disrupted by CAP policies.
- Conflicts with third-party security tools.

### Priority Assessment

- **High Priority:** Data leaks, inability to block sensitive files, or major system failures.
- **Medium Priority:** False positives/negatives or intermittent issues.
- **Low Priority:** Configuration questions or minor usability concerns.

---

## Diagnostic Methodology

### Systematic Approach

1. **Verify Policy Configuration:**
   - Ensure CAP policies are correctly set up, including thresholds, allowlists/denylists, and exit points.
   - Review CAP policy settings, including file types, contextual detection rules, and process names.

2. **Check DPI Settings:**
   - Confirm DPI is enabled and properly configured for the environment.
   - Ensure DPI certificates are trusted.

3. **Verify Environment Details:**
   - Confirm server and client versions are up to date.
   - Check operating system and platform configurations.
   - Ensure permissions (e.g., Full Disk Access on macOS) are granted.

4. **Reproduce the Issue:**
   - Attempt to replicate the reported behavior in a controlled environment.
   - Collect logs during the reproduction.

5. **Review Logs:**
   - Analyze CAP logs (`cf_log`, `cf_log_details`, `olog`) for errors, warnings, or unexpected behavior.
   - Include client logs (`eppclient.log`, `eppsslsplit.log`) and server logs.

6. **Test Adjustments:**
   - Modify policy settings incrementally to isolate the root cause.
   - Use test builds or updated versions if available.

7. **Identify Conflicts:**
   - Check for interactions with third-party tools or system settings.
   - Disable conflicting features temporarily (e.g., DPI).

8. **Escalate if Necessary:**
   - If the issue persists or involves a known bug, escalate to the development team.

---

## Common Scenarios & Solutions

### Scenario 1: CAP Policy Not Triggering
**Symptoms:** Files are not blocked or reported despite matching policy criteria.  
**Solution:**  
- Verify policy configuration and thresholds.  
- Ensure DPI is enabled and certificates are trusted.  
- Test with different file types and exit points.  
- Escalate if the issue involves unsupported formats or known bugs.

### Scenario 2: False Positives in Reports
**Symptoms:** CAP policies flag files incorrectly as sensitive.  
**Solution:**  
- Use contextual detection and regular expressions to refine policies.  
- Disable metadata scanning if unnecessary.  
- Whitelist specific file paths or domains.

### Scenario 3: Notification Issues
**Symptoms:** Users do not receive remediation pop-ups for blocked actions.  
**Solution:**  
- Check user rights and notification settings.  
- Reconfigure CAP policies to prioritize user notifications.  
- Test on a single machine before rolling out changes.

### Scenario 4: Conflicts with Third-Party Tools
**Symptoms:** CAP functionality is disrupted by tools like Zscaler or CrowdStrike.  
**Solution:**  
- Disable conflicting features temporarily (e.g., DPI).  
- Adjust denylists to exclude internal domains.  
- Work with the customer to resolve conflicts.

### Scenario 5: Missing Logs for Data Transfers
**Symptoms:** Reporting V2 not enabled.  
**Solution:** Enable Reporting V2 to capture detailed logs, including destination details.

### Scenario 6: Application Blocked by CAP Policy
**Symptoms:** Inclusion of executable files in the policy.  
**Solution:** Exclude EXE, SYS, and DLL file types from the policy.

---

## Information Collection

### Key Questions for Customers

- What specific behavior or issue are you experiencing?
- Which exit points or applications are affected?
- Are DPI and CAP policies enabled and configured?
- Are there any recent changes to the environment (e.g., updates, new policies)?
- Are there any third-party tools in use (e.g., Zscaler, CrowdStrike)?
- What is the operating system and client version in use?

### Logs and Data to Collect

- CAP logs (`cf_log`, `cf_log_details`, `olog`).
- Client logs (`eppclient.log`, `eppsslsplit.log`).
- Screenshots or videos demonstrating the issue.
- Policy configuration details (thresholds, allowlists/denylists).
- Debug logs if the issue is intermittent.

---

## Best Practices & Tips

1. **Policy Validation:** Regularly review CAP policies for accuracy and relevance.
2. **DPI Configuration:** Ensure DPI certificates are trusted and settings are optimized.
3. **Environment Maintenance:** Keep client and server versions up to date.
4. **Customer Communication:** Clearly explain system limitations and set realistic expectations.
5. **Testing:** Use controlled environments to reproduce issues before applying fixes.
6. **Documentation:** Maintain detailed records of policy configurations and troubleshooting steps.

---

## Escalation Guidelines

### Criteria for Escalation

- Issues involving known bugs or unsupported features.
- Persistent problems despite thorough troubleshooting.
- Requests for new features or enhancements.

### Escalation Procedure

1. Collect all relevant logs, screenshots, and customer details.
2. Document troubleshooting steps and findings.
3. Submit a detailed report to the development team.
4. Follow up with the customer regarding progress and updates.

---

This guide serves as a comprehensive reference for handling Content-Aware Protection (CAP) policy issues in Netwrix Endpoint Protector. By following the outlined methodologies, support engineers can effectively diagnose, resolve, and escalate problems while maintaining clear communication with customers.