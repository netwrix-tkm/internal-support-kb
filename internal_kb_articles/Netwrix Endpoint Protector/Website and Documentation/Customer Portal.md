# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## Overview  
This guide focuses on troubleshooting issues related to the **Customer Portal** feature of the Netwrix Endpoint Protector (EPP). The Customer Portal is a critical component for managing product visibility, licenses, and system configurations. Understanding and resolving issues in this category ensures uninterrupted access to essential functionalities, enhances customer satisfaction, and maintains system reliability.  

## Technical Background  
The Netwrix Endpoint Protector is a data security solution designed to protect sensitive information across endpoints. The Customer Portal serves as the interface for administrators to manage their accounts, licenses, and system configurations. Common issues in this category often involve connectivity, visibility, resource allocation, and system updates. Key concepts include:  
- **Server Certificate Stack**: Ensures secure communication between endpoints and the server.  
- **Deep Packet Inspection (DPI)**: Monitors and filters network traffic for specific policies.  
- **Content Aware Protection (CAP)**: Tracks and logs file transfers and uploads.  
- **Hotfix Deployment**: Updates applied to address vulnerabilities or improve system functionality.  

## Issue Recognition & Triage  
### Symptoms to Identify  
- Inability to log into the Customer Portal.  
- Missing product visibility or license information.  
- Logs not being received or processed.  
- System unresponsiveness or resource exhaustion.  
- Errors related to disk space or server certificates.  

### Priority Assessment  
- **Critical**: Issues affecting system availability or security (e.g., disk space errors, certificate failures).  
- **High**: Problems preventing log capture or visibility into licenses.  
- **Medium**: Configuration issues or missing features for new administrators.  
- **Low**: General inquiries or minor unexpected behaviors.  

## Diagnostic Methodology  
### Systematic Approach  
1. **Initial Assessment**: Gather details about the issue, including error messages, affected features, and recent changes.  
2. **Environment Verification**: Confirm server configurations, resource allocations, and network settings.  
3. **Log Analysis**: Collect and review relevant logs (e.g., DPI logs, CAP logs, server logs).  
4. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.  
5. **Root Cause Identification**: Narrow down potential causes based on observed behavior and collected data.  
6. **Resolution Implementation**: Apply fixes, monitor results, and confirm resolution with the customer.  

## Information Collection  
### Questions to Ask Customers  
- What error messages are displayed?  
- Have there been any recent changes to the system (e.g., updates, resource adjustments)?  
- Are specific features or functionalities affected?  
- What browsers, operating systems, or endpoints are being used?  
- Are proxies or firewalls configured in the environment?  

### Logs/Data to Collect  
- DPI logs and CAP logs.  
- Server performance metrics (CPU, RAM, disk space).  
- Event Viewer crash reports (e.g., related to sslsplit).  
- Network traffic data for affected endpoints.  

## Common Scenarios & Solutions  
### Scenario 1: Server Certificate Stack Failure  
- **Symptoms**: Unable to log into EPP; no events received.  
- **Solution**: Regenerate the Server Certificate Stack to restore communication.  
- **Reference Case**: [500Qk00000BiNLyIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BiNLyIAN/view)  

### Scenario 2: DPI Allowlist Misconfiguration  
- **Symptoms**: CAP logs not captured for file uploads; "Server responded with 0 code" error.  
- **Solution**: Add proxy port (8077) to the DPI allowlist.  
- **Reference Case**: [500Qk00000BWJqpIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BWJqpIAH/view)  

### Scenario 3: Hotfix Bug Impacting CAP Logs  
- **Symptoms**: CAP logs not sent to the server after hotfix deployment.  
- **Solution**: Deploy a replacement hotfix (adv-2024-002).  
- **Reference Case**: [500Qk00000Cd80UIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cd80UIAR/view)  

### Scenario 4: Resource Exhaustion on Server  
- **Symptoms**: Unresponsive server; out of memory errors; SQL processes fail to stop.  
- **Solution**: Increase server resources (CPU and RAM) and optimize performance.  
- **Reference Case**: [500Qk00000CGUHpIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CGUHpIAP/view)  

### Scenario 5: Disk Space Full on Hosted Appliance  
- **Symptoms**: Appliance down; "No space left on device" error.  
- **Solution**: Clean the journal in the root partition and recommend software upgrades.  
- **Reference Case**: [500Qk00000CsUILIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CsUILIA3/view)  

### Scenario 6: Missing Product Visibility for New Admin  
- **Symptoms**: New admin unable to view products/licenses in the portal.  
- **Solution**: Create a Salesforce account for the admin and verify configurations.  
- **Reference Case**: [500Qk00000L2vFrIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000L2vFrIAJ/view)  

## Detailed Case Studies  
### Case Study 1: Server Certificate Stack Failure  
- **Ticket ID**: [500Qk00000BiNLyIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BiNLyIAN/view)  
- **Symptoms**: Login failure; no events received after disk space increase.  
- **Diagnostic Steps**: Remote session, log generation, certificate analysis.  
- **Resolution**: Regenerated Server Certificate Stack.  
- **Key Takeaways**: Always verify server certificates after configuration changes.  

### Case Study 2: DPI Allowlist Misconfiguration  
- **Ticket ID**: [500Qk00000BWJqpIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BWJqpIAH/view)  
- **Symptoms**: CAP logs missing for file uploads; proxy-related errors.  
- **Diagnostic Steps**: Policy verification, DPI log analysis, proxy configuration check.  
- **Resolution**: Added proxy port to DPI allowlist.  
- **Key Takeaways**: Proxy settings are critical for DPI functionality.  

### Case Study 3: Resource Exhaustion on Server  
- **Ticket ID**: [500Qk00000CGUHpIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CGUHpIAP/view)  
- **Symptoms**: Server unresponsive; memory exhaustion.  
- **Diagnostic Steps**: Resource analysis, performance monitoring, remote session.  
- **Resolution**: Increased CPU and RAM; optimized server performance.  
- **Key Takeaways**: Proactively monitor server resources for high-load environments.  

## Best Practices & Tips  
- **Certificate Management**: Regularly verify server and client certificates after system changes.  
- **Resource Allocation**: Ensure adequate CPU and RAM for high-load environments.  
- **DPI Configuration**: Include all relevant proxies and ports in the DPI allowlist.  
- **Hotfix Testing**: Test updates in staging environments before deployment.  
- **Customer Communication**: Provide clear instructions and follow up to confirm resolution.  

## Escalation Guidelines  
### Criteria for Escalation  
- Issues involving critical system failures or security vulnerabilities.  
- Problems requiring development team intervention (e.g., hotfix bugs).  
- Cases unresolved after initial troubleshooting steps.  

### Escalation Procedure  
1. Document all troubleshooting steps and collected data.  
2. Notify the customer of the escalation and expected timelines.  
3. Forward the case to the appropriate team (e.g., DevOps, R&D).  
4. Follow up regularly to ensure progress and resolution.  