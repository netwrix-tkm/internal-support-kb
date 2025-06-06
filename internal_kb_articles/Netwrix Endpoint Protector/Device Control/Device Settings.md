# Netwrix Endpoint Protector Knowledge Base: Device Control - Device Settings

## Overview

This guide focuses on troubleshooting and resolving issues related to the **Device Control** component and **Device Settings** feature within the Netwrix Endpoint Protector (EPP) platform. Device Settings govern how endpoints interact with connected devices, ensuring compliance with organizational policies and preventing unauthorized data transfers. Understanding and resolving issues in this category is critical for maintaining endpoint security, minimizing downtime, and ensuring seamless device management.

## Technical Background

### Key Concepts
- **Device Control**: A module within EPP that manages access to devices such as USB drives, Bluetooth peripherals, and network adapters.
- **Device Settings**: Configurations that define access rights, encryption policies, and behavior for specific device types or groups.
- **Global Rights**: Organization-wide policies applied to all devices unless overridden by custom settings.
- **Custom Settings**: Device-specific or user-specific configurations that override global rights.
- **Deep Packet Inspection (DPI)**: A feature used to monitor and control data transfers, including file uploads and downloads.
- **Whitelisting**: Allowing specific devices or device types while blocking others.
- **Encryption Policies**: Rules that enforce encryption on removable devices to secure data.

### System Context
- **EPP Server**: Centralized management console for configuring policies and monitoring endpoints.
- **EPP Client**: Agent installed on endpoints to enforce policies and report activity to the server.
- **Logs**: Critical for diagnosing issues, including system logs, audit logs, and debug logs.
- **Licensing**: Ensures the functionality of the EPP platform; expired licenses can disrupt operations.

## Issue Recognition & Triage

### Common Symptoms
- Devices not functioning as expected (e.g., blocked access, failure to inherit settings).
- Errors in the management console (e.g., low disk space, duplicate entries).
- Endpoint performance issues (e.g., slowness, BSOD).
- Connectivity problems (e.g., clients showing offline).
- Policy misconfigurations (e.g., encryption not applied, settings not inherited).

### Priority Assessment
- **High Priority**: Issues causing endpoint downtime, data loss, or security vulnerabilities (e.g., BSOD, inability to block unauthorized devices).
- **Medium Priority**: Configuration issues affecting specific devices or users (e.g., whitelisting failures, inheritance problems).
- **Low Priority**: Non-critical errors or cosmetic issues (e.g., duplicate entries in the console).

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Problem**: Gather detailed information from the customer, including symptoms, affected devices, and recent changes.
2. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
3. **Analyze Logs**: Review relevant logs to identify errors or anomalies.
4. **Isolate the Cause**: Determine whether the issue is related to configuration, software bugs, or environmental factors.
5. **Apply Fixes**: Implement solutions based on the root cause.
6. **Verify Resolution**: Confirm that the issue is resolved and document the steps taken.

### Decision Points
- **Configuration Issue**: Check policy settings, inheritance rules, and device rights.
- **Software Bug**: Verify the EPP version and consult release notes for known issues.
- **Environmental Factor**: Investigate network settings, firewall rules, and hardware compatibility.

## Information Collection

### Questions to Ask Customers
- What is the specific issue or error message?
- Which devices or endpoints are affected?
- When did the issue start, and were there any recent changes (e.g., upgrades, policy updates)?
- What troubleshooting steps have already been attempted?

### Logs and Data to Collect
- **System Logs**: `/var/log/journal` for server-related issues.
- **Audit Logs**: For policy enforcement and device activity.
- **Debug Logs**: For detailed troubleshooting.
- **Configuration Snapshots**: Current policy and rights settings.
- **Screenshots or Videos**: To illustrate the issue.

## Common Scenarios & Solutions

### Scenario 1: Devices Not Recognized or Blocked
- **Symptoms**: USB devices or Bluetooth peripherals not functioning despite being whitelisted.
- **Resolution**: Verify Global Rights and custom settings. Add the device explicitly under Global Rights if necessary. (Example: [500Qk00000KaiztIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KaiztIAB/view))

### Scenario 2: Policy Inheritance Issues
- **Symptoms**: Group-level settings not applied to hosts; custom settings overriding global policies.
- **Resolution**: Reset custom settings to global and ensure group-level policies are correctly configured. (Example: [500Qk00000JQsgAIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JQsgAIAT/view))

### Scenario 3: Endpoint Performance Problems
- **Symptoms**: Slowness or BSOD after client upgrades.
- **Resolution**: Identify problematic drivers and disable or replace them. (Example: [500Qk00000C587hIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C587hIAB/view))

### Scenario 4: Logging Issues
- **Symptoms**: Excessive or missing log entries.
- **Resolution**: Adjust logging configurations and optimize server resources. (Example: [500Qk00000MXlmiIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MXlmiIAD/view))

### Scenario 5: Connectivity Problems
- **Symptoms**: Clients showing offline.
- **Resolution**: Check firewall settings and ensure licenses are applied. (Example: [500Qk00000NtjosIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NtjosIAB/view))

## Detailed Case Studies

### Case Study 1: BSOD After Client Upgrade
- **Ticket**: [500Qk00000C587hIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C587hIAB/view)
- **Symptoms**: Slowness and BSOD on multiple laptops.
- **Diagnostic Steps**: Renamed problematic driver file (`cssdlp20.sys`).
- **Resolution**: Prevented the driver from loading, resolving the BSOD.
- **Key Takeaways**: Monitor driver compatibility after upgrades.

### Case Study 2: Duplicate Device Entries
- **Ticket**: [500Qk00000NLNIwIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NLNIwIAP/view)
- **Symptoms**: Over 10,000 duplicate printer entries in the console.
- **Diagnostic Steps**: Identified "noUser" events as the cause.
- **Resolution**: Deleted duplicates and educated the customer on event logging behavior.
- **Key Takeaways**: Monitor event logging configurations to prevent clutter.

### Case Study 3: USB Encryption Configuration
- **Ticket**: [500Qk00000Osd3OIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Osd3OIAR/view)
- **Symptoms**: Automatic encryption not applied to USB devices.
- **Diagnostic Steps**: Reviewed and corrected device rules.
- **Resolution**: Enabled encryption for whitelisted devices.
- **Key Takeaways**: Ensure device rules are properly configured for encryption.

## Best Practices & Tips

1. **Regular Updates**: Keep the EPP server and client software updated to the latest versions.
2. **Proactive Monitoring**: Regularly review logs, disk space, and policy configurations.
3. **Clear Communication**: Provide customers with detailed instructions and confirm understanding.
4. **Configuration Snapshots**: Take snapshots before making significant changes to facilitate rollback if needed.
5. **Documentation**: Maintain detailed records of troubleshooting steps and resolutions for future reference.

## Escalation Guidelines

### When to Escalate
- Issues involving critical security vulnerabilities.
- Problems requiring engineering team intervention (e.g., software bugs).
- Cases where standard troubleshooting fails to resolve the issue.

### How to Escalate
1. Collect all relevant logs, screenshots, and configuration details.
2. Document the troubleshooting steps already taken.
3. Submit a detailed escalation request to the engineering team or next-level support.

By following this guide, support engineers can systematically diagnose and resolve issues related to Device Control and Device Settings, ensuring consistent and effective customer support.