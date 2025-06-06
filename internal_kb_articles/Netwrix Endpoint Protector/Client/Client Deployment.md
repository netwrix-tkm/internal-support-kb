# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## **Overview**  
This guide focuses on troubleshooting and resolving issues related to the deployment of the Netwrix Endpoint Protector (EPP) client across various operating systems and environments. Client deployment is a critical aspect of ensuring endpoint protection functionality, and understanding common challenges and solutions is essential for maintaining customer satisfaction and system reliability.  

## **Technical Background**  
### **Key Concepts**  
- **Netwrix Endpoint Protector (EPP):** A data loss prevention (DLP) solution designed to secure endpoints across diverse operating systems.  
- **Client Deployment:** The process of installing and configuring the EPP client on endpoint devices to enable communication with the management server.  
- **Deployment Methods:** Includes manual installation, Mobile Device Management (MDM) tools (e.g., JAMF, Intune, Kandji), Group Policy Objects (GPO), and custom scripts.  
- **Compatibility:** EPP clients are tailored for specific operating systems and versions. Compatibility issues often arise when deploying clients on unsupported platforms or outdated OS versions.  

### **Terminology**  
- **MDM:** Mobile Device Management tools used for automated deployment and management of endpoint software.  
- **TLS:** Transport Layer Security protocol required for secure communication between clients and servers.  
- **PPPC Profile:** Privacy Preferences Policy Control profiles used in macOS environments to manage permissions.  
- **Uninstall Password:** A security feature requiring a password for uninstalling the EPP client.  

## **Issue Recognition & Triage**  
### **Symptoms**  
- Clients fail to connect to the server after installation.  
- Errors during installation due to missing dependencies or unsupported OS versions.  
- Deployment tools (e.g., JAMF, Intune) fail to push clients to endpoints.  
- Incorrect server IP or department codes configured during deployment.  
- Permission prompts or connectivity issues related to proxy settings.  

### **Priority Assessment**  
- **High Priority:** Issues affecting production environments, such as clients failing to connect or policies not being applied.  
- **Medium Priority:** Deployment errors or compatibility concerns that do not immediately impact production.  
- **Low Priority:** Cosmetic issues, such as incorrect OS version reporting in the Device Manager.  

## **Diagnostic Methodology**  
### **Systematic Approach**  
1. **Verify Environment Details:** Confirm OS version, deployment method, and server configuration.  
2. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment.  
3. **Check Compatibility:** Ensure the client version matches the OS version and deployment tool requirements.  
4. **Review Logs:** Collect installation, communication, and error logs for analysis.  
5. **Test Workarounds:** Apply known solutions, such as disabling proxy settings or using alternative deployment scripts.  
6. **Escalate:** If the issue persists, escalate to engineering or product teams for further investigation.  

## **Information Collection**  
### **Customer Queries**  
- What operating system and version are you deploying the client on?  
- Are you using an MDM tool or manual installation?  
- Have you configured proxy settings or custom scripts during deployment?  
- Are there any error messages or logs available?  

### **Logs to Collect**  
- Installation logs from the endpoint.  
- Communication logs between the client and server.  
- Deployment tool logs (e.g., JAMF, Intune).  
- Screenshots of error messages or prompts.  

## **Common Scenarios & Solutions**  
### **Scenario 1: Proxy Configuration Issues**  
- **Symptoms:** Clients fail to connect to the server when proxy settings are enabled during installation.  
- **Solution:** Install the client without proxy settings enabled, then configure the proxy post-installation. Alternatively, remove proxy configurations from `/etc/epp/options.ini` and associated certificate files.  
- **Reference Case:** [500Qk00000JIhbTIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JIhbTIAT/view)  

### **Scenario 2: Unsupported OS Versions**  
- **Symptoms:** Installation errors due to outdated or unsupported operating systems (e.g., Ubuntu 19.04, Arch Linux).  
- **Solution:** Inform customers of unsupported OS versions and provide links to compatible client packages for supported platforms.  
- **Reference Case:** [500Qk00000O3pJaIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O3pJaIAJ/view)  

### **Scenario 3: Deployment Tool Failures**  
- **Symptoms:** Clients do not appear in the console after deployment via MDM tools like JAMF or Intune.  
- **Solution:** Verify deployment tool configurations, use zap tools to reset installations, and re-register clients with the server.  
- **Reference Case:** [500Qk00000F3yGjIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F3yGjIAJ/view)  

### **Scenario 4: Licensing Conflicts**  
- **Symptoms:** Devices exceed license limits, causing deployment failures or connectivity issues.  
- **Solution:** Increase license counts, enable automatic license release, and monitor usage.  
- **Reference Case:** [500Qk00000LoUJmIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LoUJmIAN/view)  

### **Scenario 5: Permission Prompts on macOS**  
- **Symptoms:** Users receive Bluetooth permission prompts on macOS during login.  
- **Solution:** Enable full disk access for the EPP agent and deploy test builds to suppress prompts.  
- **Reference Case:** [500Qk00000NYOU6IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NYOU6IAP/view)  

## **Detailed Case Studies**  
### **Case Study 1: Proxy Configuration Issue**  
- **Ticket ID:** [500Qk00000JIhbTIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JIhbTIAT/view)  
- **Symptoms:** Two MacBooks failed to connect to the server when proxy settings were enabled during installation.  
- **Diagnostic Steps:** Verified installation logs, tested disabling proxy settings, and applied workarounds.  
- **Resolution:** Installed the client without proxy settings, then enabled the proxy post-installation.  
- **Key Takeaways:** Proxy settings can interfere with client-server communication during installation.  

### **Case Study 2: Unsupported OS Version**  
- **Ticket ID:** [500Qk00000O3pJaIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O3pJaIAJ/view)  
- **Symptoms:** Customer requested support for Ubuntu 19.04, which is no longer supported.  
- **Diagnostic Steps:** Reviewed compatibility documentation and provided links to supported client packages.  
- **Resolution:** Clarified that Ubuntu 19.04 is unsupported and directed the customer to use Ubuntu 20.04 or later.  
- **Key Takeaways:** Always verify OS support status before proceeding with deployment requests.  

### **Case Study 3: Licensing Conflict**  
- **Ticket ID:** [500Qk00000LoUJmIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LoUJmIAN/view)  
- **Symptoms:** Devices exceeded license limits, causing deployment issues.  
- **Diagnostic Steps:** Reviewed license allocation and increased license counts.  
- **Resolution:** Enabled automatic license release and confirmed successful deployment.  
- **Key Takeaways:** Monitor license usage and configure automatic release to manage fluctuating device counts.  

## **Best Practices & Tips**  
1. **Verify Compatibility:** Always confirm OS and client version compatibility before deployment.  
2. **Use Standardized Scripts:** Provide customers with tested deployment scripts to minimize errors.  
3. **Monitor Licenses:** Enable automatic license release to avoid conflicts in environments with dynamic device counts.  
4. **Test Builds:** Deploy test builds on a limited number of devices before wider rollout.  
5. **Document Changes:** Maintain updated documentation for deployment tools and OS compatibility.  

## **Escalation Guidelines**  
### **Criteria for Escalation**  
- Issues persist after applying known solutions and workarounds.  
- Compatibility concerns with new OS versions or deployment tools.  
- Requests for unsupported platforms or features.  

### **Escalation Procedure**  
1. Collect detailed logs and error messages.  
2. Document all troubleshooting steps taken.  
3. Escalate to engineering or product teams with a clear summary of the issue and customer impact.  
4. Follow up regularly to ensure timely resolution.  

This guide serves as a comprehensive reference for handling client deployment issues in Netwrix Endpoint Protector, enabling support engineers to resolve cases efficiently and consistently.