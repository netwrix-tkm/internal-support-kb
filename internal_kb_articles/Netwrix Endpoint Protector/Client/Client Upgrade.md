# Netwrix Endpoint Protector: Client Upgrade Troubleshooting Guide

## Overview

The **Client Upgrade** feature in Netwrix Endpoint Protector (EPP) enables administrators to update endpoint agents to the latest versions, ensuring compatibility, security, and access to new features. While the upgrade process is designed to be seamless, various issues can arise, including compatibility problems, configuration errors, and environmental limitations. This guide consolidates troubleshooting steps, solutions, and best practices to address common client upgrade challenges.

---

## Common Issues and Solutions

### Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution |
|-------|----------|---------------------------|----------|
| **Clients greyed out in upgrade interface** | Unable to select clients for upgrade | Check for old upgrade jobs and delete them | Delete old upgrade jobs |
| **Upgrade job fails for large batches** | Upgrade job does not complete | Split upgrade job into smaller batches | Create smaller upgrade jobs |
| **Missing client version in Console** | Desired version not listed for upgrade | Verify version availability in Console | Update Console to include version |
| **Blue screen errors (BSOD)** | Systems crash with `cssdlp20.sys` error | Generate logs using EPP Support Tool | Reinstall EPP client |
| **Unresponsive systems during upgrade** | Systems hang and require reboot | Check installation path and logs | Use VBS script for installation |
| **Ubuntu agent not checking in** | Agent fails to communicate with server | Check `options.sh` configuration | Correct `options.sh` file |
| **Fedora client installer request** | Missing installers for Fedora versions | Verify availability of installers | Provide updated installers |
| **Printing blocked in Outlook** | Users unable to print emails | Configure Advanced Scanning Exceptions | Whitelist Outlook in exceptions |
| **Temporary access codes not recognized** | Temporary access codes fail after upgrade | Verify version, check configuration | Apply patch for version 5.9.4.1 |
| **Unable to upgrade system agents** | Certain systems cannot be selected for upgrade | Check permissions, logs, and dashboard settings | Adjust permissions and retry |
| **Slow client upgrade progress** | Upgrade job progresses slowly | Verify server version, suggest redeployment | Redeploy via Intune, wait for server patch |
| **Mac agents pointing to unknown server** | Misconfigured agents | Reconfigure agents to correct server | Update agent settings |
| **Windows Server 2016 incompatibility** | Client fails to report after upgrade | Check OS compatibility, revert version | Use older client version |
| **Linux upgrades not supported via EPP server** | Linux upgrades not supported | Suggest third-party tools | Use tools like Ansible or Puppet |

---

## Detailed Troubleshooting Steps

### 1. Clients Greyed Out in Upgrade Interface
**Symptoms:**  
Clients appear greyed out in the upgrade interface, preventing selection for upgrades.

**Troubleshooting Steps:**  
1. Check for existing upgrade jobs in the system.
2. Delete any failed or incomplete upgrade jobs.
3. Refresh the upgrade interface and attempt to select clients again.

**Root Cause:**  
Old upgrade jobs block the selection of clients for new upgrades.

**Solution:**  
Delete all old upgrade jobs and retry the upgrade process.

---

### 2. Upgrade Job Fails for Large Batches
**Symptoms:**  
Upgrade jobs containing a large number of clients fail to complete.

**Troubleshooting Steps:**  
1. Review the size of the upgrade job.
2. Split the job into smaller batches of 50-100 clients.
3. Monitor the progress of each smaller job.

**Root Cause:**  
Large batch sizes overwhelm the upgrade process, causing failures.

**Solution:**  
Create multiple smaller upgrade jobs to ensure successful completion.

---

### 3. Missing Client Version in Console
**Symptoms:**  
The desired client version is not listed in the EPP Console for upgrade.

**Troubleshooting Steps:**  
1. Verify the version availability in the Console.
2. Check for updates to the Console that include the desired version.
3. Contact support if the version is not available.

**Root Cause:**  
The EPP Console does not list all available client versions due to version availability settings.

**Solution:**  
Update the Console to include the desired client version.

---

### 4. Blue Screen Errors (BSOD)
**Symptoms:**  
Systems crash with a blue screen error, citing `cssdlp20.sys`.

**Troubleshooting Steps:**  
1. Generate logs using the EPP Support Tool.
2. Identify the driver causing the issue (`cssdlp20.sys`).
3. Uninstall the EPP client and reinstall it.

**Root Cause:**  
A conflict with the `cssdlp20.sys` driver causes the blue screen error.

**Solution:**  
Reinstall the EPP client to resolve the driver conflict.

---

### 5. Unresponsive Systems During Upgrade
**Symptoms:**  
Systems become unresponsive during the upgrade process and require a reboot.

**Troubleshooting Steps:**  
1. Check the installation path in the upgrade command.
2. Append `/l*v <path_to_log>` to the `msiexec` command to generate logs.
3. Use a VBS script to automate the installation process.

**Root Cause:**  
The installation command does not correctly point to the installer path.

**Solution:**  
Use a VBS script to ensure the installer is located and executed properly.

---

### 6. Ubuntu Agent Not Checking In
**Symptoms:**  
The Ubuntu agent fails to communicate with the EPP server.

**Troubleshooting Steps:**  
1. Check the `options.sh` file for configuration errors.
2. Correct any misconfigurations in the file.
3. Restart the agent and verify connectivity.

**Root Cause:**  
Misconfiguration in the `options.sh` file prevents communication with the server.

**Solution:**  
Edit the `options.sh` file to correct the configuration settings.

---

### 7. Fedora Client Installer Request
**Symptoms:**  
Customer requests updated client installers for Fedora versions 38, 39, and 40.

**Troubleshooting Steps:**  
1. Verify the availability of client installers for the requested Fedora versions.
2. Provide download links for the updated installers.

**Root Cause:**  
The customer did not have access to updated client installers for the specified Fedora versions.

**Solution:**  
Provide the updated client installers to the customer.

---

### 8. Printing Blocked in Outlook
**Symptoms:**  
Users are unable to print email memos in Microsoft Outlook.

**Troubleshooting Steps:**  
1. Navigate to `System Parameters >> Advanced Scanning Exceptions`.
2. Add `outlook.exe` or `olk.exe` to the Application Process Name field.
3. Whitelist Outlook in the exceptions and update policies.

**Root Cause:**  
The EPP client blocks printing in Outlook due to security settings.

**Solution:**  
Whitelist Outlook in the Advanced Scanning Exceptions.

---

## Best Practices

1. **Regularly Clean Up Old Upgrade Jobs:** Ensure that no failed or incomplete jobs remain in the system before initiating new upgrades.
2. **Split Large Upgrade Jobs:** For environments with many clients, divide upgrade jobs into smaller batches to prevent failures.
3. **Verify Configuration Settings:** Check all relevant settings, such as `options.sh` for Linux agents, before initiating upgrades.
4. **Generate Logs for Troubleshooting:** Use detailed logging options (e.g., `/l*v <path_to_log>`) to capture errors during upgrades.
5. **Communicate Changes to Users:** Inform users about any visible changes, such as new icons or features, to avoid confusion.

---

## Advanced Topics

### Handling Driver Conflicts
If blue screen errors occur due to driver conflicts (e.g., `cssdlp20.sys`), uninstall the EPP client and reinstall it using the latest version. Ensure that all drivers are compatible with the operating system.

### Linux Batch Upgrades
Linux upgrades are not supported directly via the EPP server. Use third-party tools like Ansible, Puppet, or Chef for mass deployments. Ensure compatibility with the target Linux distributions before proceeding.

### Automating Upgrades with Scripts
Use VBS or PowerShell scripts to automate client installations and upgrades, ensuring that all paths and commands are correctly configured.

---

## Conclusion

The Client Upgrade feature in Netwrix Endpoint Protector is a powerful tool for maintaining up-to-date endpoint agents. By following the troubleshooting steps and best practices outlined in this guide, administrators can resolve common issues and ensure a smooth upgrade process. For unresolved issues, contact Netwrix Support for further assistance.