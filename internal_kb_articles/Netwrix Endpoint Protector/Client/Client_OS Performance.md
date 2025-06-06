# Comprehensive Knowledge Base Guide: Troubleshooting Client/OS Performance Issues in Netwrix Endpoint Protector

## Overview

This guide provides a systematic approach to diagnosing and resolving Client/OS Performance issues in Netwrix Endpoint Protector (EPP). These issues often involve performance degradation, application conflicts, connectivity problems, or unexpected behavior caused by EPP components. Understanding and addressing these problems is critical to maintaining system stability, user productivity, and data protection.

### Scope
- **Platform:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Common Symptoms:** Performance degradation, application crashes, connectivity issues, unexpected blocking, and policy enforcement failures.

---

## Technical Background

### Key Concepts
1. **Endpoint Protector Client:** A software agent installed on endpoints to enforce data protection policies, monitor activity, and control device access.
2. **Content Aware Protection (CAP):** A feature that inspects content for sensitive data and enforces policies such as blocking or logging.
3. **Device Control:** Manages access to peripheral devices like USB drives, Bluetooth devices, and printers.
4. **Data Protection Inspection (DPI):** Monitors and controls data transfers, including network traffic and file uploads.
5. **Intercept VPN Traffic:** A feature that ensures VPN traffic is monitored and controlled by EPP.
6. **Advanced Scanning:** A feature that scans applications and processes for sensitive data interactions.

### System Context
- **Client-Server Architecture:** EPP clients communicate with the EPP server to enforce policies and log activities.
- **Operating Systems:** EPP supports Windows, macOS, and Linux environments, with specific features and limitations for each OS.
- **Third-Party Interactions:** EPP often interacts with other security tools (e.g., Zscaler, CrowdStrike) and applications (e.g., Outlook, Visual Studio), which can lead to conflicts.

---

## Issue Recognition & Triage

### Common Symptoms
- **Performance Issues:** High CPU or memory usage, slow file transfers, or application lag.
- **Connectivity Problems:** Inability to access websites, applications, or network resources.
- **Application Crashes:** Unexpected shutdowns of applications like Outlook or Visual Studio.
- **Policy Enforcement Failures:** CAP or Device Control policies not applying as expected.
- **Unexpected Prompts:** Pop-ups for permissions (e.g., Bluetooth access) during installation or upgrades.

### Priority Assessment
- **High Priority:** Issues causing data loss, widespread performance degradation, or critical application failures.
- **Medium Priority:** Problems affecting specific users or non-critical applications.
- **Low Priority:** Cosmetic issues or minor inconveniences without functional impact.

---

## Diagnostic Methodology

### Systematic Approach
1. **Initial Assessment:**
   - Confirm the symptoms and affected environment.
   - Verify the EPP version and operating system details.
2. **Reproduce the Issue:**
   - Attempt to replicate the problem in a controlled environment.
   - Use logs and screenshots to document behavior.
3. **Isolate Variables:**
   - Test with EPP features (e.g., DPI, CAP) enabled and disabled.
   - Check for conflicts with third-party applications or security tools.
4. **Analyze Logs:**
   - Review client and server logs for errors or anomalies.
   - Focus on specific modules (e.g., CAP, Device Control) based on the issue.
5. **Apply Fixes:**
   - Implement temporary workarounds (e.g., whitelisting, disabling features).
   - Test permanent solutions (e.g., updates, configuration changes).

---

## Information Collection

### Key Questions for Customers
- What are the symptoms, and when did they start?
- What is the operating system and EPP version in use?
- Are there any recent changes (e.g., upgrades, new policies)?
- What applications or websites are affected?
- Are there any third-party security tools installed?

### Logs to Collect
- **Client Logs:**
  - `/private/var/log/eppclient.log`
  - `/private/var/log/eppclient_append.log`
- **Configuration Files:**
  - `/etc/epp/reprovision.db`
  - `/etc/epp/rights.s3db`
  - `/etc/epp/netdlp/netdlp_settings.json`
- **Screenshots:** Document error messages or unusual behavior.

---

## Common Scenarios & Solutions

### Scenario 1: High Memory Usage
- **Symptoms:** Excessive memory consumption (e.g., 1-50GB) by EPP agents.
- **Root Cause:** Excessive logging or file tracing on heavily utilized drives.
- **Solution:** Add affected drives to the allowlist and optimize tracing settings. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C3YhRIAV/view)

### Scenario 2: Application Crashes
- **Symptoms:** Outlook or Visual Studio crashes after EPP installation.
- **Root Cause:** Advanced Scanning feature interfering with application processes.
- **Solution:** Add affected applications to the Advanced Scanning exception list. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JkQhJIAV/view)

### Scenario 3: Connectivity Issues
- **Symptoms:** Inability to access websites or application tabs.
- **Root Cause:** EPP blocking necessary resources or conflicting with other tools.
- **Solution:** Whitelist affected URLs or reset application settings. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000L2IWGIA3/view)

### Scenario 4: Policy Enforcement Failures
- **Symptoms:** CAP policies not blocking sensitive data as expected.
- **Root Cause:** Compatibility issues with unsupported OS versions or DPI settings.
- **Solution:** Use supported OS versions and update EPP to the latest version. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NFb3gIAD/view)

---

## Detailed Case Studies

### Case Study 1: Bluetooth Devices Greyed Out After Upgrade
- **Ticket ID:** [500Qk00000BOHBJIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BOHBJIA5/view)
- **Symptoms:** Previously connected Bluetooth devices became non-functional.
- **Diagnostic Steps:** Verified Device Control settings, analyzed logs, and provided a test build.
- **Resolution:** Test build resolved the issue; fix included in the next release.
- **Key Takeaways:** Monitor known issues in release notes and provide test builds cautiously.

### Case Study 2: File Transfer Speed Decrease
- **Ticket ID:** [500Qk00000DXoMjIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DXoMjIAL/view)
- **Symptoms:** Slow file transfers after reaching daily transfer limits.
- **Diagnostic Steps:** Reviewed transfer settings and analyzed logs.
- **Resolution:** Disabled file transfer threshold settings.
- **Key Takeaways:** Regularly review and adjust transfer limits for high-volume users.

### Case Study 3: AWS Workspace Instability
- **Ticket ID:** [500Qk00000O46fLIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O46fLIAR/view)
- **Symptoms:** Users unable to log in; temporary profiles created.
- **Diagnostic Steps:** Verified license import, modified CAP policies, and upgraded EPP.
- **Resolution:** Upgraded EPP server and client versions.
- **Key Takeaways:** Test upgrades on a single instance before full deployment.

---

## Best Practices & Tips

1. **Proactive Monitoring:**
   - Regularly review logs and performance metrics.
   - Test new EPP versions in controlled environments before deployment.

2. **Effective Communication:**
   - Clearly explain temporary workarounds and long-term solutions to customers.
   - Provide regular updates during complex investigations.

3. **Configuration Management:**
   - Maintain updated allowlists and exception lists for critical applications.
   - Use supported OS versions and configurations to ensure compatibility.

4. **Escalation Readiness:**
   - Escalate promptly for unresolved issues or when development team input is required.
   - Provide detailed logs and reproduction steps to expedite resolution.

---

## Escalation Guidelines

### Criteria for Escalation
- Issues affecting multiple users or critical systems.
- Problems requiring development team investigation (e.g., suspected bugs).
- Cases unresolved after applying standard troubleshooting steps.

### Escalation Process
1. Gather all relevant logs, screenshots, and customer details.
2. Document reproduction steps and temporary workarounds.
3. Submit a detailed escalation request to the appropriate team.

--- 

End of Document.