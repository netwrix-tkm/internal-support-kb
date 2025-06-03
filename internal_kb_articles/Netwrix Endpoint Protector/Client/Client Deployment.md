# Netwrix Endpoint Protector Knowledge Base: Client Deployment

## Overview
Netwrix Endpoint Protector (EPP) is a Data Loss Prevention (DLP) solution designed to secure endpoints across various operating systems. The Client Deployment feature enables administrators to install, configure, and manage EPP clients on devices. Common issues in this category include installation failures, connectivity problems, compatibility concerns, and deployment errors using third-party tools like JAMF, Intune, and MDM solutions.

This article provides a structured approach to troubleshooting and resolving issues related to EPP client deployment, along with best practices to prevent recurring problems.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Linux setup files unavailable | Customer requested setup files for unsupported OS versions | Verify available versions and provide download links | Provide links for supported OS versions | [Linux Setup Files Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C7CGsIAN/view) |
| Debian 12 client ETA | Customer requested ETA for Debian 12 client | Confirm release dependencies and provide test build | Provide test build for POC | [Debian 12 Client ETA](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcYZfIAN/view) |
| Amazon Linux 2 installation errors | Dependency errors during installation | Verify compatibility and provide updated client | Provide compatible client version | [Amazon Linux 2 Installation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cd55qIAB/view) |
| JAMF profile misconfiguration | Errors during upgrade jobs | Verify JAMF profile setup | Correct JAMF profile configuration | [JAMF Profile Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000COhhdIAD/view) |
| Windows Server TLS issue | Clients unable to connect despite network availability | Check TLS settings | Enable TLS 1.2 | [Windows Server TLS Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CpEq3IAF/view) |
| macOS installation script for FileWave | Lack of FileWave-specific script | Adapt JAMF script for FileWave | Provide template script | [FileWave Script Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DqnI6IAJ/view) |
| macOS Sonoma proxy issue | Client fails to connect with proxy enabled | Test with proxy disabled | Install without proxy, enable post-installation | [macOS Sonoma Proxy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EzyooIAB/view) |
| Intune provisioning failure | Clients installed but not connecting | Reset installation using zap tool | Reinstall agent after zap tool reset | [Intune Provisioning Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F3yGjIAJ/view) |
| macOS Sequoia compatibility inquiry | Customer requested compatibility confirmation | Verify compatibility documentation | Confirm compatibility with recommended version | [macOS Sequoia Compatibility Inquiry](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G8XX3IAN/view) |
| Red Hat Linux compatibility inquiry | Customer requested support for older Red Hat versions | Check compatibility matrix | Confirm unsupported status | [Red Hat Linux Compatibility Inquiry](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GE4QjIAL/view) |

---

## Detailed Issues

### Linux Setup Files Unavailable
**Symptoms:** Customer requested setup files for unsupported Linux distributions (e.g., Ubuntu 24.04).  
**Troubleshooting Steps:**  
1. Verify the availability of setup files for requested OS versions.  
2. Provide download links for supported versions.  
3. Inform the customer about upcoming releases for unsupported versions.  

**Solution:**  
Provide the following links for supported distributions:  
- Ubuntu 18.04: [Download Link](https://download.endpointprotector.com/linux_agent/EPPClient_v2.4.2.1006/EPPClient_ubuntu_18.04_v2.4.2.1006_x86_64.tar.gz)  
- Ubuntu 20.04: [Download Link](https://download.endpointprotector.com/linux_agent/EPPClient_v2.4.2.1006/EPPClient_ubuntu_20.04_v2.4.2.1006_x86_64.tar.gz)  
- Ubuntu 22.04: [Download Link](https://download.endpointprotector.com/linux_agent/EPPClient_v2.4.2.1006/EPPClient_ubuntu_22.04_v2.4.2.1006_x86_64.tar.gz)  

**Source Ticket:** [Linux Setup Files Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C7CGsIAN/view)

---

### Debian 12 Client ETA
**Symptoms:** Customer requested ETA for Debian 12 client for POC.  
**Troubleshooting Steps:**  
1. Confirm release dependencies (e.g., server version 5.8.4.0).  
2. Provide test build for immediate use.  
3. Follow up on QA testing status.  

**Solution:**  
Provide test build for Debian 12 client: [Test Build Link](https://download.endpointprotector.com/linux_agent/EPPClient_v2.4.1.2001/EPPClient_debian_12_v2.4.1.2001_x86_64.tar.gz).  

**Source Ticket:** [Debian 12 Client ETA](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CcYZfIAN/view)

---

### Amazon Linux 2 Installation Errors
**Symptoms:** Dependency errors during installation on Amazon Linux 2.  
**Troubleshooting Steps:**  
1. Verify compatibility of provided client version.  
2. Provide updated client version for Amazon Linux 2.  
3. Test installation and resolve dependency issues.  

**Solution:**  
Provide compatible client version: [Download Link](https://download.endpointprotector.com/linux_agent/EPPClient_v2.4.1.2001/EPPClient_amzn_2_v2.4.1.2001_x86_64.tar.gz).  

**Source Ticket:** [Amazon Linux 2 Installation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cd55qIAB/view)

---

### JAMF Profile Misconfiguration
**Symptoms:** Errors during upgrade jobs due to JAMF profile misconfiguration.  
**Troubleshooting Steps:**  
1. Verify JAMF profile setup.  
2. Schedule a meeting to review deployment settings.  
3. Correct profile configuration and test deployment.  

**Solution:**  
Ensure JAMF profile is correctly configured before initiating upgrades.  

**Source Ticket:** [JAMF Profile Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000COhhdIAD/view)

---

### Windows Server TLS Issue
**Symptoms:** Clients unable to connect despite successful telnet tests.  
**Troubleshooting Steps:**  
1. Verify network connectivity.  
2. Check TLS settings on Windows machines.  
3. Enable TLS 1.2.  

**Solution:**  
Enable TLS 1.2 on affected Windows machines to restore connectivity.  

**Source Ticket:** [Windows Server TLS Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CpEq3IAF/view)

---

## Best Practices

1. **Verify Compatibility:** Always check the compatibility matrix for supported operating systems and versions before deployment.  
2. **Pre-Deployment Checks:** Conduct thorough pre-deployment checks, including network settings, proxy configurations, and license availability.  
3. **Regular Updates:** Ensure client agents are updated alongside operating system upgrades to avoid functionality issues.  
4. **Documentation Access:** Provide customers with links to the latest deployment guides for third-party tools like JAMF, Intune, and MDM solutions.  
5. **Error Reporting:** Encourage customers to provide detailed error messages and logs for faster troubleshooting.  

---

## Advanced Topics

### Silent Uninstallation with Password
For environments requiring silent uninstallation, use the following commands:  

**Windows:**  
```bash
msiexec.exe /x <PATH to MSI file> ADMIN_PASSWORD_0="ADD_UNINSTALL_PASSWORD_HERE" /qn REBOOT=ReallySuppress
```  

**Mac:**  
```bash
/Applications/EndpointProtectorClient.app/Contents/Applications/EppNotifier.app/Contents/MacOS/remove-epp ADD_PASSWORD_HERE
```  

Ensure uninstall passwords are securely managed and not exposed in scripts or logs.  

**Source Ticket:** [Silent Uninstallation](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O1XdeIAF/view)  

--- 

End of Article.