# Knowledge Base Reference Guide: Troubleshooting "Device Not Recognized" Issues in Netwrix Endpoint Protector

## Overview
This guide provides a comprehensive reference for troubleshooting "Device Not Recognized" issues in Netwrix Endpoint Protector (EPP). These issues occur when devices fail to be identified, blocked, or managed as expected by the EPP platform. Understanding and resolving these problems is critical to maintaining device control, ensuring compliance with security policies, and minimizing disruptions to end users.

This document outlines key concepts, diagnostic methodologies, common scenarios, and best practices to help support engineers systematically address and resolve these issues.

---

## Technical Background
### Key Concepts
- **Device Control**: A core feature of EPP that manages access to external devices (e.g., USB drives, printers, cameras) based on predefined policies.
- **Device Recognition**: The process by which EPP identifies devices using attributes such as Vendor ID (VID), Product ID (PID), and serial numbers.
- **Global Rights**: Settings that define default permissions for device types across the organization.
- **Agent-Server Communication**: The EPP client (agent) installed on endpoints communicates with the EPP server to enforce policies and report device activity.

### Common Terminology
- **VID/PID**: Unique identifiers for devices used by EPP to recognize and manage them.
- **DLP (Data Loss Prevention)**: Features that prevent unauthorized data transfer, which can sometimes conflict with device recognition.
- **Backend Configuration**: Server-side settings that influence how devices are managed and logged.

### System Context
EPP operates in a client-server architecture where:
1. The **EPP Client** enforces policies on endpoints.
2. The **EPP Server** manages configurations, logs, and device inventories.
3. Devices are categorized and controlled based on their attributes and the applied policies.

---

## Issue Recognition & Triage
### Symptoms
- Devices appear as "Blocked" or "Offline" in the EPP console despite being connected.
- Devices fail to appear in the EPP inventory or logs.
- Specific device types (e.g., printers, cameras, docking stations) are not recognized.
- Device functionality is impaired after enabling certain features (e.g., DLP).

### Priority Assessment
- **High Priority**: Critical devices (e.g., printers, scanners) affecting business operations.
- **Medium Priority**: Peripheral devices (e.g., headsets, cameras) causing user inconvenience.
- **Low Priority**: Non-essential devices or cosmetic issues (e.g., incorrect status display).

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Environment Details**:
   - Confirm the EPP version (server and client).
   - Identify the affected device type and connection method (USB, PCIe, etc.).
   - Check for recent updates or configuration changes.

2. **Reproduce the Issue**:
   - Attempt to replicate the problem in a controlled environment.
   - Test the device on another endpoint with the same EPP configuration.

3. **Check Device Recognition**:
   - Verify if the device appears in the EPP console or logs.
   - Use VID/PID to manually search for the device.

4. **Review Logs**:
   - Collect client and server logs for errors related to device detection.
   - Look for communication issues between the agent and server.

5. **Test Configuration Changes**:
   - Adjust global rights or device-specific policies.
   - Temporarily disable conflicting features (e.g., DLP) to isolate the issue.

6. **Escalate if Necessary**:
   - Engage R&D for unresolved compatibility or backend issues.
   - Provide detailed logs and reproduction steps.

---

## Information Collection
### Questions to Ask Customers
- What is the affected device type and model?
- When did the issue first occur? Were there any recent changes (e.g., updates, migrations)?
- Is the issue isolated to specific endpoints or widespread?
- Are there any error messages or unusual behavior in the EPP console?

### Data to Collect
- **Logs**:
  - Client logs (`epp.log`) from affected endpoints.
  - Server logs for device recognition and communication errors.
- **Configuration Files**:
  - `epp.nginx.conf` for server settings.
  - `options.sh` for Linux client installations.
- **Device Details**:
  - VID, PID, and serial number of the affected device.
- **Screenshots**:
  - EPP console views showing the device status.

---

## Common Scenarios & Solutions
### Scenario 1: USB Printer Not Recognized
- **Case Reference**: [500Qk00000BOQr3IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BOQr3IAH/view)
- **Root Cause**: Default settings blocked the printer unless USB printing support was enabled.
- **Solution**: Update to Windows agents version 6.2.3.0037 or later.

### Scenario 2: Audio/Video Devices Blocked by DLP
- **Case Reference**: [500Qk00000ByhrmIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ByhrmIAB/view)
- **Root Cause**: Conflict between DLP settings and device recognition.
- **Solution**: Apply a test build with improved audio device recognition.

### Scenario 3: Domain Migration Issues
- **Case Reference**: [500Qk00000COD5FIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000COD5FIAX/view)
- **Root Cause**: Lack of synchronization between the new domain and EPP console.
- **Solution**: Synchronize the new domain into the EPP console.

### Scenario 4: Docking Stations Blocked
- **Case Reference**: [500Qk00000Od8KtIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Od8KtIAJ/view)
- **Root Cause**: Incorrect global rights configuration.
- **Solution**: Allow "USB Device" and "Unknown Device" in global rights settings.

---

## Detailed Case Studies
### Case Study: HP Laptops with MediaTek WiFi Adapter
- **Case Reference**: [500Qk00000EIj9vIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EIj9vIAD/view)
- **Symptoms**: WiFi adapter not recognized in EPP console.
- **Diagnostic Steps**:
  - Verified server and client versions.
  - Escalated to engineering for compatibility analysis.
- **Resolution**: Updated EPP server to version 5.9.4.1, which included a fix for device recognition.
- **Key Takeaways**: Always ensure compatibility with the latest hardware by keeping EPP updated.

### Case Study: Google Meet Audio Device Issues
- **Case Reference**: [500Qk00000KLsY9IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KLsY9IAL/view)
- **Symptoms**: Delays in joining Google Meet due to audio device detection.
- **Diagnostic Steps**:
  - Reviewed logs and tested device behavior.
  - Updated server and client versions.
- **Resolution**: Resolved by upgrading to the latest EPP versions.
- **Key Takeaways**: Monitor audio device compatibility after agent installations.

---

## Best Practices & Tips
1. **Maintain Up-to-Date Software**:
   - Regularly update EPP server and client versions to address known issues and improve compatibility.

2. **Test Configurations in Controlled Environments**:
   - Before deploying changes, test them on a small subset of devices to identify potential issues.

3. **Document Changes**:
   - Keep detailed records of configuration adjustments and troubleshooting steps for future reference.

4. **Communicate Known Limitations**:
   - Inform customers about product limitations (e.g., inbuilt SD Card Readers) to manage expectations.

5. **Proactive Monitoring**:
   - Use logs and reports to identify potential device recognition issues before they impact users.

---

## Escalation Guidelines
- **When to Escalate**:
  - Compatibility issues with new hardware.
  - Persistent backend configuration problems.
  - Unresolved issues after applying known fixes.

- **How to Escalate**:
  - Provide detailed logs, reproduction steps, and environment details.
  - Include VID/PID and serial numbers for affected devices.
  - Clearly document all troubleshooting steps taken.

---

This guide serves as a definitive reference for handling "Device Not Recognized" issues in Netwrix Endpoint Protector, enabling support engineers to resolve problems efficiently and consistently.