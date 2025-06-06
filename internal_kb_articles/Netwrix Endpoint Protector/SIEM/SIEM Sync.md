# Netwrix Endpoint Protector SIEM Sync Troubleshooting Guide

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the **SIEM Sync** feature in **Netwrix Endpoint Protector (EPP)**. SIEM Sync enables the integration of EPP with Security Information and Event Management (SIEM) systems, allowing organizations to centralize and analyze security logs. Proper functionality of this feature is critical for maintaining visibility into security events and ensuring compliance with organizational policies.

This document is designed to help support engineers systematically diagnose, resolve, and prevent issues related to SIEM Sync. It includes technical background, diagnostic methodologies, common scenarios, and real-world case studies to ensure consistent and effective problem resolution.

---

## Technical Background

### Key Concepts
- **SIEM Integration**: The process of forwarding logs from EPP to a SIEM system for centralized analysis.
- **Syslog Protocol**: A standard protocol used for log forwarding. EPP supports both `syslog-ng` and `rsyslog` formats.
- **TLS Encryption**: Ensures secure transmission of logs between EPP and the SIEM server.
- **Log Forwarding Ports**: Common ports include `514` (UDP/TCP), `6514` (TLS), and `1516` (custom configurations).
- **Configuration Settings**: Includes SIEM server IP, port, protocol, and log format.

### System Context
- **EPP Server**: Acts as the source of logs, configured to forward events to the SIEM.
- **SIEM Server**: Receives and processes logs for analysis.
- **Network Configuration**: Firewalls, routing, and DNS settings must allow communication between the EPP and SIEM servers.

---

## Issue Recognition & Triage

### Common Symptoms
- Logs not appearing in the SIEM server.
- Connection errors between EPP and SIEM.
- Logs being sent in an unsupported format.
- Issues after system upgrades, migrations, or reconfigurations.

### Priority Assessment
- **High Priority**: No logs are being received, impacting security monitoring.
- **Medium Priority**: Logs are delayed or incomplete.
- **Low Priority**: Configuration inquiries or feature requests.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Verify Configuration**:
   - Check SIEM integration settings in the EPP UI.
   - Confirm the SIEM server IP, port, protocol, and log format.
2. **Test Connectivity**:
   - Use `ping`, `telnet`, or `tcpdump` to verify communication between the EPP and SIEM servers.
   - Check firewall rules and ensure required ports are open.
3. **Review Logs**:
   - Examine EPP logs for errors related to SIEM integration.
   - Check SIEM server logs for incoming traffic.
4. **Validate Compatibility**:
   - Ensure the SIEM server supports the configured log format (e.g., `syslog-ng` vs. `rsyslog`).
   - Verify TLS version compatibility if encryption is enabled.
5. **Reproduce the Issue**:
   - Attempt to resend logs or reconfigure the SIEM integration to isolate the problem.

---

## Information Collection

### Questions to Ask Customers
- What SIEM solution are you using?
- What is the configured log format (e.g., `syslog-ng`, `rsyslog`)?
- Are there any recent changes to the environment (e.g., upgrades, migrations)?
- What ports are configured for log forwarding?
- Are there any error messages in the SIEM or EPP logs?

### Data to Collect
- Screenshots of the SIEM integration settings in EPP.
- Logs from the EPP server (`/var/log/syslog` or `/var/log/syslog-ng/`).
- SIEM server logs showing incoming traffic.
- Network configuration details (firewall rules, routing settings).

---

## Common Scenarios & Solutions

### Scenario 1: Logs Not Received by SIEM
- **Root Cause**: Firewall blocking the log forwarding port.
- **Solution**: Open the required port (e.g., `514`, `6514`) in the firewall.

### Scenario 2: Unsupported Log Format
- **Root Cause**: EPP configured to send `syslog-ng` logs, but SIEM expects `rsyslog`.
- **Solution**: Update the SIEM server to accept `syslog-ng` logs or reconfigure EPP to use `rsyslog`.

### Scenario 3: TLS Encryption Issues
- **Root Cause**: Mismatch in TLS versions between EPP and SIEM.
- **Solution**: Verify and update the TLS configuration on both servers.

### Scenario 4: Post-Migration Issues
- **Root Cause**: Syslog service not enabled on the new server.
- **Solution**: Enable `syslog-ng` in the database (`support_syslogng=1`).

### Scenario 5: Configuration Errors
- **Root Cause**: Duplicate SIEM configurations causing conflicts.
- **Solution**: Remove duplicate configurations and test log forwarding.

---

## Detailed Case Studies

### Case 1: Missing Key Pair Preventing Access
- **Ticket**: [500Qk00000BrLT3IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BrLT3IAN/view)
- **Symptoms**: Unable to access EPP server on AWS EC2 due to missing SSH key pair.
- **Diagnostic Steps**:
  - Confirmed absence of the key pair.
  - Scheduled a remote session to access the backend.
- **Resolution**: Gained backend access and re-established log forwarding.
- **Key Takeaway**: Ensure key pairs are properly assigned during deployment.

### Case 2: Logs Not Received After Upgrade
- **Ticket**: [500Qk00000H6Sr3IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H6Sr3IAF/view)
- **Symptoms**: Logs stopped after upgrading to Ubuntu 22.04.
- **Diagnostic Steps**:
  - Verified firewall settings and SIEM configuration.
  - Re-saved the SIEM configuration in EPP.
- **Resolution**: Re-saving the configuration restored log forwarding.
- **Key Takeaway**: Always validate settings after system upgrades.

### Case 3: TLS Encryption Blocking Logs
- **Ticket**: [500Qk00000NVfPqIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NVfPqIAL/view)
- **Symptoms**: Logs stopped after enabling TLS encryption.
- **Diagnostic Steps**:
  - Verified TLS settings on both servers.
  - Identified a blockage on the SIEM server side.
- **Resolution**: Demonstrated that logs were being sent; customer resolved the SIEM-side issue.
- **Key Takeaway**: Ensure TLS version compatibility between systems.

---

## Best Practices & Tips

1. **Validate Configuration**:
   - Double-check SIEM integration settings after any changes to the environment.
   - Use the correct log format (`syslog-ng` or `rsyslog`) based on SIEM compatibility.

2. **Test Connectivity**:
   - Use tools like `tcpdump` and `telnet` to verify communication between servers.
   - Ensure required ports are open in the firewall.

3. **Document Changes**:
   - Maintain detailed records of configuration changes for future reference.
   - Create snapshots before making backend changes.

4. **Proactive Monitoring**:
   - Regularly review logs to identify potential issues early.
   - Test log forwarding after upgrades or migrations.

5. **Customer Communication**:
   - Provide clear instructions and set expectations for resolution timelines.
   - Share relevant documentation and troubleshooting steps.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following standard troubleshooting steps.
- Backend changes (e.g., database updates) are required.
- The root cause is suspected to be a product defect.

### How to Escalate
- Collect all relevant logs and configuration details.
- Document the troubleshooting steps taken and their outcomes.
- Submit the case to the engineering team with a detailed summary.

--- 

This guide serves as a definitive reference for handling SIEM Sync issues in Netwrix Endpoint Protector, ensuring consistent and effective problem resolution.