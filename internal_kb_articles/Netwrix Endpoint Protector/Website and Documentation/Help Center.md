# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## Overview  
This guide focuses on troubleshooting and resolving issues related to the Netwrix Endpoint Protector (EPP) platform, specifically within the scope of website and documentation features accessed via the Help Center. These issues often involve disk space management, device control configurations, and upgrade inquiries. Understanding this category is critical for ensuring system stability, maintaining compatibility, and providing accurate guidance to customers.

## Technical Background  
Netwrix Endpoint Protector is a comprehensive solution for endpoint security, offering features such as device control, content inspection, and data protection. Key components include:  
- **EPP Server**: Manages policies, logs, and system configurations.  
- **EPP Client**: Installed on endpoints to enforce policies.  
- **Help Center**: Provides documentation and troubleshooting resources.  

### Key Concepts  
- **Disk Space Management**: Logs and cached files can accumulate over time, consuming disk space and potentially causing system warnings or failures.  
- **Device Control**: Policies regulate access to external devices based on identifiers like Vendor ID (VID) and Product ID (PID).  
- **Upgrade Compatibility**: Ensuring compatibility with newer operating systems and offline environments is essential for long-term system viability.  

## Issue Recognition & Triage  
### Symptoms  
- **Disk Space Issues**: Low disk space warnings, system performance degradation.  
- **Device Control Problems**: Inability to locate VID/PID or configure external device access.  
- **Upgrade Inquiries**: Questions about compatibility with newer OS versions or offline operation.  

### Priority Assessment  
- **Critical**: Disk space issues affecting system functionality.  
- **High**: Device control misconfigurations preventing policy enforcement.  
- **Medium**: Upgrade inquiries requiring detailed compatibility analysis.  

## Diagnostic Methodology  
### Step-by-Step Approach  
1. **Identify the Issue**: Review customer reports and symptoms.  
2. **Gather Environment Details**: Confirm platform, version, and operating system.  
3. **Examine Logs**: Check system/service logs for errors or excessive growth.  
4. **Reproduce the Problem**: If applicable, replicate the issue in a test environment.  
5. **Apply Targeted Solutions**: Use proven resolution strategies based on the issue type.  

## Information Collection  
### Customer Questions  
- What symptoms are you experiencing?  
- What version of EPP are you using?  
- What operating system is in use?  
- Are there any recent changes to the system or policies?  

### Logs/Data to Collect  
- System logs (e.g., journal logs, PHP-FPM logs).  
- Device control policy configurations.  
- VID/PID details for external devices.  
- Upgrade compatibility requirements (e.g., OS version, offline operation).  

## Common Scenarios & Solutions  
### Scenario 1: Disk Space Issues  
#### Symptoms  
Low disk space warnings on the EPP server.  

#### Resolution  
1. Clear excessive logs using commands:  
   ```bash  
   journalctl --vacuum-size=100M  
   echo '' > /usr/local/logs/php-fpm.log  
   ```  
2. Adjust filesystem reserved blocks:  
   ```bash  
   tune2fs -m 1 /dev/nvme0n1p4  
   ```  
3. Remove cached files:  
   ```bash  
   rm -rf /run/shm/mcache/*  
   ```  
4. Implement log rotation or size limits to prevent recurrence.  

### Scenario 2: Device Control VID/PID Retrieval  
#### Symptoms  
Customer unable to locate VID/PID for external storage devices.  

#### Resolution  
1. Guide the customer to access Device Manager on Windows:  
   - Navigate to **Device Manager**.  
   - Locate the external device under **Universal Serial Bus controllers**.  
   - Right-click the device, select **Properties**, and view the **Details** tab.  
   - Select **Hardware IDs** to find VID/PID.  
2. Alternatively, use command-line tools like `wmic` or PowerShell to retrieve identifiers.  

### Scenario 3: Upgrade Compatibility  
#### Symptoms  
Customer inquiries about upgrading EPP in an offline environment and compatibility with newer Linux distributions.  

#### Resolution  
1. Confirm current EPP versions and operating system.  
2. Provide compatibility details for CentOS 8, Rocky Linux 8, and Alma Linux 8.  
3. Recommend upgrade paths based on offline operation requirements.  

## Detailed Case Studies  
### Case Study 1: Disk Space Issue  
- **Ticket ID:** [500Qk00000C6DlHIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C6DlHIAV/view)  
#### Initial Symptoms  
Low disk space warnings on the EPP server.  

#### Diagnostic Steps  
- Reviewed system logs and identified excessive growth.  
- Executed commands to clear logs and cached files.  

#### Key Information  
Large journal logs and PHP-FPM logs were consuming disk space.  

#### Resolution  
Cleared logs, adjusted reserved blocks, and removed cached files.  

#### Key Takeaways  
Regular log monitoring and rotation are essential to prevent disk space issues.  

---

### Case Study 2: VID/PID Retrieval  
- **Ticket ID:** [500Qk00000CqY3aIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CqY3aIAF/view)  
#### Initial Symptoms  
Customer unable to locate VID/PID for external storage devices.  

#### Diagnostic Steps  
- Scheduled a remote session to guide the customer.  
- Demonstrated VID/PID retrieval via Device Manager.  

#### Key Information  
The issue was due to a lack of familiarity with Windows tools.  

#### Resolution  
Provided step-by-step guidance to locate VID/PID.  

#### Key Takeaways  
Educating customers on OS-specific tools can resolve similar issues efficiently.  

---

### Case Study 3: Upgrade Compatibility Inquiry  
- **Ticket ID:** [500Qk00000EflPYIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EflPYIAZ/view)  
#### Initial Symptoms  
Customer inquired about upgrading EPP in an offline environment.  

#### Diagnostic Steps  
- Reviewed current EPP versions and OS compatibility.  
- Investigated support for newer Linux distributions.  

#### Key Information  
Customer was using CentOS 7 in an offline environment.  

#### Resolution  
Provided upgrade recommendations and compatibility details for CentOS 8, Rocky Linux 8, and Alma Linux 8.  

#### Key Takeaways  
Offline environments require careful planning for upgrades and compatibility.  

## Best Practices & Tips  
- **Disk Space Management**: Implement log rotation and size limits to prevent excessive growth.  
- **Device Control**: Provide clear documentation on VID/PID retrieval for various operating systems.  
- **Upgrade Planning**: Regularly review compatibility with newer OS versions and plan upgrades proactively.  
- **Customer Communication**: Use remote sessions and clear instructions to resolve issues efficiently.  

## Escalation Guidelines  
### Criteria for Escalation  
- Issues affecting critical system functionality (e.g., disk space warnings causing downtime).  
- Compatibility inquiries requiring development team input.  
- Complex device control configurations requiring advanced troubleshooting.  

### Escalation Procedure  
1. Document all troubleshooting steps and collected data.  
2. Provide a detailed summary of the issue and attempted resolutions.  
3. Escalate to the appropriate team with relevant logs and environment details.  