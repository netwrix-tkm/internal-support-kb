# Netwrix Endpoint Protector: Client Install/Uninstall Knowledge Base Guide

## Overview

This guide provides a comprehensive reference for troubleshooting and resolving issues related to the installation and uninstallation of the Netwrix Endpoint Protector (EPP) client. The EPP client is a critical component of the Endpoint Protector platform, enabling endpoint-level data protection, policy enforcement, and secure communication with the Endpoint Protector server. Proper handling of installation and uninstallation processes ensures seamless deployment, functionality, and compliance with organizational security policies.

This document is designed to equip support engineers with the knowledge and tools necessary to diagnose, resolve, and prevent issues, ensuring consistent and efficient support delivery.

---

## Technical Background

### Key Concepts
- **Endpoint Protector Client (EPP):** A software agent installed on endpoint devices to enforce data protection policies, monitor activity, and communicate with the Endpoint Protector server.
- **Client-Server Communication:** The client relies on a secure connection to the Endpoint Protector server for policy updates, reporting, and license validation.
- **Installation/Uninstallation Methods:** Clients can be installed or removed manually, via scripts, or through Mobile Device Management (MDM) solutions like Intune, Jamf, or JumpCloud.
- **Uninstallation Protection:** The EPP client often includes password protection or server-side controls to prevent unauthorized removal.
- **Zap Tool:** A specialized utility provided by Netwrix to forcibly remove the EPP client when standard uninstallation methods fail.

### Terminology
- **Silent Installation/Uninstallation:** A process that runs without user interaction, typically used for bulk deployments or removals.
- **Transparent Proxy:** A feature that intercepts and inspects network traffic for data loss prevention (DLP) purposes.
- **Configuration Profiles:** Files used to automate client settings during installation, often required for MDM deployments.
- **Compatibility Matrix:** A reference for supported operating systems and versions for the EPP client.
- **CAP (Content-Aware Protection):** Policies that monitor and control data transfers based on content.
- **DPI (Deep Packet Inspection):** A feature requiring specific configurations for secure communication.

### Supported Platforms
- **Operating Systems:** Windows, macOS, Linux (Ubuntu, RHEL).
- **Deployment Methods:** Manual installation, MDM deployment, or script-based installation.

---

## Issue Recognition & Triage

### Common Symptoms
- **Installation Errors:** Missing dependencies, blocked by security software, or insufficient privileges.
- **Uninstallation Failures:** Password prompts, remnants left behind, or missing uninstallation files.
- **Client-Server Connectivity Issues:** Clients not appearing in the server console, incorrect IP configuration, or firewall interference.
- **Compatibility Problems:** Issues with specific operating systems or outdated client/server versions.
- **Functional Issues Post-Installation:** Features not working, certificates not trusted, or policies not applied.

### Priority Assessment
- **High Priority:** Issues affecting multiple endpoints, critical business operations, or security compliance (e.g., inability to uninstall due to expired licenses, widespread connectivity failures).
- **Medium Priority:** Issues affecting individual endpoints or non-critical features (e.g., installation errors on a single device).
- **Low Priority:** Requests for guidance, documentation, or clarification (e.g., how to configure installation scripts).

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Environment Details:**
   - Operating system version.
   - EPP client version.
   - Deployment method (manual, script, MDM).
   - Server version and configuration.
   - Network configuration (e.g., static vs. dynamic IP, firewall settings).

2. **Reproduce the Issue:**
   - Attempt the installation/uninstallation process in a controlled environment.
   - Review logs for error messages or warnings.

3. **Check Compatibility:**
   - Confirm the client version is compatible with the server version.
   - Verify supported operating systems using the compatibility matrix.

4. **Analyze Logs:**
   - Installation logs (e.g., MSIExec logs for Windows, system logs for Linux/macOS).
   - Server logs for client registration or communication errors.

5. **Test Workarounds:**
   - Use alternative installation/uninstallation methods (e.g., Zap Tool, manual commands).
   - Adjust configuration files or scripts as needed.

6. **Validate the Solution:**
   - Confirm successful installation/uninstallation.
   - Verify client-server communication and policy enforcement.

7. **Escalate if Necessary:**
   - If the issue persists after standard troubleshooting, escalate to the R&D team with detailed logs and findings.

---

## Information Collection

### Questions to Ask Customers
- What operating system and version are you using?
- What version of the EPP client are you trying to install/uninstall?
- Are you using an MDM solution? If so, which one?
- What error messages are you encountering?
- Have you attempted any troubleshooting steps? If so, what were the results?

### Logs and Data to Collect
- Installation/uninstallation logs (e.g., MSI logs for Windows, `/var/log` for Linux).
- System logs (e.g., Event Viewer on Windows).
- Screenshots or error messages.
- Network connectivity tests (e.g., ping, traceroute).
- Configuration files (e.g., `options.sh`, `epp_install_parameters.txt`).

---

## Common Scenarios & Solutions

### Scenario 1: Installation Errors
- **Symptoms:** Installation fails with dependency or permission errors.
- **Resolution:**
  1. Verify that all prerequisites are met (e.g., required libraries, permissions).
  2. Use the latest version of the client compatible with the operating system.
  3. Temporarily disable security software if it blocks the installation.

### Scenario 2: Uninstallation Failures
- **Symptoms:** Uninstallation prompts for a password or leaves remnants behind.
- **Resolution:**
  1. Use the Zap Tool for forced removal.
  2. Include the uninstall password in the command if required:
     ```bash
     MsiExec /X {ProductCode} PASSWORD={password}
     ```
  3. Reboot the system after uninstallation to ensure all components are removed.

### Scenario 3: Client-Server Connectivity Issues
- **Symptoms:** Clients do not appear in the server console.
- **Resolution:**
  1. Verify network connectivity and firewall settings.
  2. Check the client configuration file for correct server details.
  3. Restart client and server services.

### Scenario 4: Compatibility Problems
- **Symptoms:** Client fails to install or function on a specific OS version.
- **Resolution:**
  1. Confirm compatibility using the Netwrix compatibility matrix.
  2. Update to the latest client version.
  3. Use alternative deployment methods if MDM solutions are unsupported.

### Scenario 5: Proxy Interference
- **Symptoms:** Client fails to connect during installation.
- **Resolution:**
  1. Temporarily disable the proxy or use the "SetServerIP" tool.
  2. Verify proxy exceptions for EPP communication.

---

## Detailed Case Studies

### Case Study 1: Uninstallation Failure Due to Missing MSI File
- **Symptoms:** Customer could not uninstall the client due to a missing MSI file.
- **Resolution:** Provided the Zap Tool for manual removal.
- **Key Takeaways:** Always maintain access to installation files for uninstallation purposes.

### Case Study 2: Installation Blocked by Security Software
- **Symptoms:** SentinelOne flagged the installation as suspicious.
- **Resolution:** Disabled SentinelOne temporarily and used the Zap Tool for a clean installation.
- **Key Takeaways:** Coordinate with security teams to whitelist EPP client installers.

### Case Study 3: Proxy Interference on macOS
- **Symptoms:** Client failed to connect during installation with a system-wide proxy enabled.
- **Resolution:** Advised disabling the proxy during installation. Connection succeeded.
- **Key Takeaways:** Document proxy-related workarounds for environments with strict network policies.

---

## Best Practices & Tips

1. **Pre-Installation Checks:**
   - Verify system requirements and dependencies.
   - Ensure administrative privileges.

2. **Use Deployment Tools:**
   - For large-scale deployments, use GPO or MDM tools like Intune or Jamf.

3. **Leverage Cleanup Tools:**
   - Use the Zap Tool to remove remnants of old installations before reinstalling.

4. **Document Configuration Settings:**
   - Maintain records of server IPs, ports, and certificates for troubleshooting.

5. **Proactive Communication:**
   - Inform customers about potential issues (e.g., VPN interference, expired licenses) and provide preventive guidance.

---

## Escalation Guidelines

### When to Escalate
- Persistent issues after following standard troubleshooting steps.
- Logs indicate a potential bug or compatibility issue.
- Requests for unsupported operating systems or custom configurations.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration files.
2. Document the troubleshooting steps already performed.
3. Submit a detailed escalation request to the R&D team via the internal ticketing system.

---

This guide serves as a definitive reference for handling client installation and uninstallation issues in Netwrix Endpoint Protector, enabling support engineers to resolve cases efficiently and consistently.