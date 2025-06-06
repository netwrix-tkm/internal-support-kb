# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## Overview  
This guide focuses on troubleshooting and resolving issues related to the "Additional Tools" feature of Netwrix Endpoint Protector (EPP). These issues often involve deployment tools, update management, patch installations, and integration challenges. Understanding this category is critical for ensuring smooth operations, minimizing downtime, and maintaining customer satisfaction.  

## Technical Background  
Netwrix Endpoint Protector is a data security solution designed to prevent data loss and enforce endpoint protection policies. The "Additional Tools" feature encompasses scripts, patches, deployment utilities, and integration configurations that enhance the functionality of the EPP system. Key concepts include:  
- **Update Management**: Ensuring updates and patches are applied correctly.  
- **Deployment Tools**: Automating the installation and configuration of EPP clients across various platforms.  
- **Integration**: Configuring EPP to interact with other Netwrix products or third-party solutions.  
- **Platform Compatibility**: Supporting diverse operating systems such as Windows, Mac, and Linux.  

## Issue Recognition & Triage  
### Common Symptoms  
- Persistent update notifications despite successful installation.  
- Deployment options deactivated during client updates.  
- Requests for scripts or installation files.  
- Certificate conflicts with third-party solutions.  
- Integration inquiries with other Netwrix products.  

### Priority Assessment  
- **High Priority**: Issues affecting security patches, deployment failures, or certificate conflicts.  
- **Medium Priority**: Requests for scripts, installation files, or guidance on integration.  
- **Low Priority**: Persistent notifications or minor usability concerns.  

## Diagnostic Methodology  
1. **Initial Assessment**: Review the customer’s problem description and environment details.  
2. **Reproduce the Issue**: If possible, replicate the issue in a test environment.  
3. **Analyze Logs and Data**: Examine relevant logs, deployment settings, and update history.  
4. **Identify Root Cause**: Determine whether the issue stems from configuration, compatibility, or known bugs.  
5. **Apply Resolution**: Implement the appropriate solution based on the identified root cause.  

## Information Collection  
### Questions to Ask Customers  
- What version of Netwrix Endpoint Protector are you using?  
- What operating systems are affected?  
- Have you attempted any troubleshooting steps?  
- Are there specific error messages or logs available?  
- Is this issue affecting multiple endpoints or a single machine?  

### Logs and Data to Collect  
- Update history and deployment logs.  
- Configuration files for deployment tools.  
- Screenshots or error messages.  
- Relevant scripts or patch files.  

## Common Scenarios & Solutions  
### Scenario 1: Persistent Update Notifications  
**Symptoms**: Security updates appear repeatedly in the update list despite successful installation.  
**Solution**: Advise the customer to disregard the notification if the update has been applied successfully. Monitor for future server updates to address the bug.  
**Reference Case**: [500Qk00000CpNV7IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CpNV7IAN/view)  

### Scenario 2: Deployment Options Deactivated  
**Symptoms**: Deployment options are unavailable during client updates, but manual installation works.  
**Solution**: Verify deployment settings and permissions. Assist the customer in configuring the deployment tool correctly.  
**Reference Case**: [500Qk00000CyUHGIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CyUHGIA3/view)  

### Scenario 3: Patch Deployment Across Platforms  
**Symptoms**: Customer requests guidance for deploying a patch across Mac, Ubuntu, and Windows platforms.  
**Solution**: Provide detailed instructions for patch deployment on each platform. Ensure the customer understands the urgency and steps involved.  
**Reference Case**: [500Qk00000DkFz3IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DkFz3IAF/view)  

### Scenario 4: Script Requests for Deployment  
**Symptoms**: Customer requests specific scripts to assist with deployment processes.  
**Solution**: Provide the requested script and confirm its functionality. Follow up to ensure customer satisfaction.  
**Reference Case**: [500Qk00000HyaurIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HyaurIAB/view)  

### Scenario 5: Integration with Netwrix Data Classification  
**Symptoms**: Customer seeks guidance on integrating Endpoint Protector with Netwrix Data Classification.  
**Solution**: Inform the customer that direct integration is not available but metadata scanning is supported. Recommend creating custom dictionaries for enhanced functionality.  
**Reference Case**: [500Qk00000IKIHlIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IKIHlIAP/view)  

### Scenario 6: Certificate Conflicts  
**Symptoms**: DPI feature experiences operational issues due to certificate conflicts with third-party solutions.  
**Solution**: Investigate the certificate conflict and provide guidance on obtaining intermediate certificates. Escalate if necessary.  
**Reference Case**: [500Qk00000KpWVNIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KpWVNIA3/view)  

### Scenario 7: Offline Patch Requests  
**Symptoms**: Customer requests an offline patch for a specific version.  
**Solution**: Check patch availability and communicate the timeline for release if unavailable.  
**Reference Case**: [500Qk00000LQxDFIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LQxDFIA1/view)  

### Scenario 8: Installation File Requests  
**Symptoms**: Customer requests installation files for specific operating systems.  
**Solution**: Locate and share the requested installation file promptly.  
**Reference Case**: [500Qk00000NlKfcIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NlKfcIAF/view)  

## Detailed Case Studies  
### Case Study 1: Persistent Update Notifications  
**Ticket ID**: [500Qk00000CpNV7IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CpNV7IAN/view)  
**Symptoms**: Repeated appearance of a security update despite successful installation.  
**Diagnostic Steps**: Verified update history and confirmed successful installation. Identified a known bug causing the issue.  
**Resolution**: Advised the customer to disregard the notification.  
**Key Takeaways**: Known bugs should be communicated clearly to customers, along with expected resolution timelines.  

### Case Study 2: Deployment Options Deactivated  
**Ticket ID**: [500Qk00000CyUHGIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CyUHGIA3/view)  
**Symptoms**: Deployment options unavailable during updates.  
**Diagnostic Steps**: Reviewed deployment settings and permissions. Conducted a remote session to assist the customer.  
**Resolution**: Adjusted deployment settings to enable updates.  
**Key Takeaways**: Permissions and configurations are critical for deployment tools.  

### Case Study 3: Certificate Conflicts  
**Ticket ID**: [500Qk00000KpWVNIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KpWVNIA3/view)  
**Symptoms**: DPI feature conflicts with third-party certificates.  
**Diagnostic Steps**: Investigated certificate requirements and escalated the issue.  
**Resolution**: Provided guidance on obtaining intermediate certificates.  
**Key Takeaways**: Certificate conflicts require careful handling and escalation when necessary.  

## Best Practices & Tips  
- **Documentation**: Maintain detailed records of scripts, patches, and deployment tools for quick access.  
- **Customer Communication**: Provide clear and concise instructions, ensuring customers understand the resolution steps.  
- **Proactive Monitoring**: Stay updated on known bugs and upcoming patches to anticipate customer needs.  
- **Escalation Protocols**: Establish clear criteria for escalating complex issues to senior engineers or development teams.  
- **Efficiency Improvements**: Automate repetitive tasks, such as sharing installation files or scripts, to save time.  

## Escalation Guidelines  
- Escalate issues involving certificate conflicts, unresolved bugs, or urgent security patches.  
- Provide detailed documentation of troubleshooting steps and findings when escalating.  
- Ensure timely follow-up with customers after escalation to maintain trust and satisfaction.  