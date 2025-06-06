# Netwrix Endpoint Protector Knowledge Base: Client Upgrade Troubleshooting Guide

## Overview

The **Client Upgrade** feature in **Netwrix Endpoint Protector (EPP)** is essential for maintaining endpoint security, compatibility, and functionality. Upgrading client software ensures that endpoints remain secure, benefit from new features, and align with server requirements. This guide provides a comprehensive approach to diagnosing, resolving, and preventing issues related to client upgrades across various operating systems and environments.

---

## Technical Background

### Key Concepts
- **Netwrix Endpoint Protector (EPP):** A platform for device control, data loss prevention, and endpoint security.
- **Client Software:** Installed on endpoints to enforce policies and communicate with the EPP server.
- **Upgrade Process:** Updates client software to newer versions via the EPP console or manual installation.
- **Compatibility:** Ensures client versions align with server versions and operating system requirements.
- **Upgrade Methods:**
  - **Console-Based Upgrade:** Initiated from the EPP server dashboard.
  - **Manual Installation:** Performed using MSI packages or offline patches.
  - **Third-Party Tools:** Used for Linux deployments (e.g., Ansible, Puppet).

### Terminology
- **EPP Console:** The management interface for deploying and monitoring client upgrades.
- **Upgrade Job:** A scheduled task initiated via the console to update client software.
- **Offline Patch:** A downloadable package used to manually update clients when automatic upgrades fail.
- **Logs:** Diagnostic files generated during installation or upgrade processes, such as `eppclient.log` or MSI logs.
- **EPPSetServer Tool:** A utility for reconfiguring client-server communication settings.

---

## Issue Recognition & Triage

### Common Symptoms
- **Grayed-Out Clients:** Clients appear unselectable in the upgrade interface despite being online and licensed.
- **Upgrade Failures:** Errors during the upgrade process, such as "Upgrade Failed" or "Completed with Errors."
- **Endpoint Functionality Issues:** Problems like BSOD or unresponsive systems post-upgrade.
- **Missing Client Versions:** Desired client versions not listed in the EPP console.
- **Configuration Errors:** Clients pointing to incorrect servers or reverting to default settings.
- **Compatibility Issues:** Errors due to unsupported operating systems or outdated server versions.
- **Performance Issues:** Slow upgrade progress or limited visibility of eligible clients.

### Priority Assessment
- **High Priority:** Security vulnerabilities, widespread upgrade failures, or critical endpoint functionality issues.
- **Medium Priority:** Individual client upgrade failures or minor compatibility concerns.
- **Low Priority:** Cosmetic changes or non-critical inquiries about upgrade processes.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Environment Details:**
   - Confirm server and client versions.
   - Check operating system compatibility.
   - Review network configurations (e.g., firewall rules, Active Directory policies).

2. **Reproduce the Issue:**
   - Attempt the upgrade manually or via the console.
   - Generate logs during the process for analysis.

3. **Analyze Logs:**
   - Examine `eppclient.log`, MSI logs, or event viewer entries for error codes or warnings.

4. **Check Upgrade Jobs:**
   - Identify incomplete or failed jobs that may block new upgrades.
   - Delete old jobs if necessary.

5. **Review Configuration Settings:**
   - Verify group assignments, policies, and dependencies (e.g., certificates).

6. **Test Solutions:**
   - Apply patches, modify configurations, or use alternative deployment methods (e.g., MDM tools).

7. **Validate Resolution:**
   - Confirm that the issue is resolved across all affected endpoints.
   - Document findings and update internal knowledge bases.

---

## Information Collection

### Questions to Ask Customers
- What server and client versions are being used?
- What operating systems are affected?
- Are there any error messages or logs available?
- Has the issue occurred after a recent upgrade or configuration change?
- Are there specific endpoints or groups affected?

### Logs and Data to Collect
- **EPP Client Logs:** `eppclient.log` for upgrade-related errors.
- **MSI Logs:** Generated using `/l*v <path_to_log>` during installation.
- **Event Viewer Logs:** For system-level errors.
- **Server Logs:** Synchronization and upgrade job statuses.
- **Network Details:** Firewall rules, open ports, and proxy configurations.

---

## Common Scenarios & Solutions

### Scenario 1: Grayed-Out Clients in Upgrade Interface
- **Symptoms:** Clients appear unselectable despite being online and licensed.
- **Resolution:**
  - Delete old upgrade jobs blocking new selections.
  - Verify client licensing and synchronization status.

### Scenario 2: Upgrade Job Fails for Large Batches
- **Symptoms:** Upgrade jobs with hundreds of clients fail or become unresponsive.
- **Resolution:**
  - Split large upgrade jobs into smaller batches.
  - Monitor each batch for completion.

### Scenario 3: Missing Client Versions in Console
- **Symptoms:** Desired client version not listed in the upgrade interface.
- **Resolution:**
  - Update the EPP console to reflect the latest versions.
  - Use offline patches for manual upgrades.

### Scenario 4: BSOD During Upgrade
- **Symptoms:** Blue screen errors caused by `cssdlp20.sys`.
- **Resolution:**
  - Uninstall and reinstall the EPP client.
  - Verify driver compatibility.

### Scenario 5: Compatibility Issues with Linux Clients
- **Symptoms:** Errors during installation due to identical `.deb` package versions.
- **Resolution:**
  - Modify `.deb` package names to include OS version identifiers.

### Scenario 6: Slow Upgrade Progress
- **Symptoms:** Upgrade jobs take an unusually long time to complete.
- **Resolution:**
  - Uninstall and redeploy clients using third-party tools.
  - Wait for server updates to ensure compatibility.

---

## Detailed Case Studies

### Case Study 1: Grayed-Out Clients Blocking Upgrade
- **Symptoms:** Clients unselectable despite being online.
- **Diagnostic Steps:** Verified upgrade jobs, deleted old jobs.
- **Resolution:** Cleared old jobs; clients became selectable.
- **Key Takeaways:** Always check for incomplete jobs before initiating upgrades.

### Case Study 2: BSOD During Upgrade
- **Symptoms:** Blue screen errors caused by `cssdlp20.sys`.
- **Diagnostic Steps:** Collected logs, identified driver conflict.
- **Resolution:** Uninstalled and reinstalled EPP client.
- **Key Takeaways:** Monitor driver compatibility during upgrades.

### Case Study 3: Linux Client Compatibility Issues
- **Symptoms:** Installation errors due to identical `.deb` package versions.
- **Diagnostic Steps:** Compared archives, modified package names.
- **Resolution:** Renamed `.deb` packages to include OS version identifiers.
- **Key Takeaways:** Use distinct naming conventions for multi-OS environments.

---

## Best Practices & Tips

1. **Pre-Upgrade Checks:**
   - Verify compatibility between server and client versions.
   - Test upgrades on a small subset of endpoints.

2. **Documentation:**
   - Maintain detailed records of server migrations, patches, and configurations.
   - Update internal knowledge bases with resolved cases.

3. **Communication:**
   - Clearly inform customers about OS and version support limitations.
   - Provide step-by-step instructions for manual upgrades.

4. **Proactive Monitoring:**
   - Regularly audit server and client configurations.
   - Monitor for new patches and updates.

5. **Batch Upgrades:**
   - Split large upgrade jobs into smaller batches to avoid failures.

6. **Offline Patches:**
   - Use offline patches for manual upgrades when automatic methods fail.

---

## Escalation Guidelines

### Criteria for Escalation
- Security vulnerabilities affecting multiple endpoints.
- Persistent upgrade failures despite troubleshooting.
- Critical functionality issues post-upgrade (e.g., BSOD, unresponsive systems).

### Escalation Process
1. **Document Findings:** Include logs, error messages, and troubleshooting steps.
2. **Contact Development Team:** Escalate issues related to patches or version compatibility.
3. **Customer Communication:** Inform the customer about the escalation and expected timelines.

---

By following this guide, support engineers can systematically address client upgrade issues, ensuring efficient resolutions and maintaining customer satisfaction.