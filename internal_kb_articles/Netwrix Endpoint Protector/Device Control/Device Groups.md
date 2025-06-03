# Netwrix Endpoint Protector: Device Control - Device Groups Knowledge Base

## Overview

The **Device Groups** feature in **Netwrix Endpoint Protector** allows administrators to manage and enforce policies for specific sets of devices. This functionality is critical for ensuring compliance with organizational security requirements, such as restricting device usage, managing group priorities, and generating reports. However, common issues can arise due to misconfigurations, user misunderstandings, or environmental factors like server migrations.

This article provides a detailed guide to troubleshooting and resolving common issues related to Device Groups, including step-by-step procedures, root cause analysis, and tested solutions. It also includes best practices to prevent recurring problems.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Blocking Bluetooth Data Transfer | Bluetooth data transfer remains enabled despite policy settings | Verify Device Control settings and update policies | Correct misconfigured policies to block Bluetooth | [Blocking Bluetooth Data Transfer](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FDkXSIA1/view) |
| Managing Device Groups | Unable to add or delete computers in a group | Review group management process with the customer | Guide customer on correct group management steps | [Managing Device Groups](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FPTKjIAP/view) |
| File Tracing Report Issues | Unable to fetch File Tracing reports by group | Verify group-wise settings and provide instructions | Guide customer on fetching reports correctly | [File Tracing Report Issues](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GdTsBIAV/view) |
| Uninstalling Endpoint Protector Agents | Need to uninstall agents from multiple machines | Provide uninstallation script and SCCM deployment guidance | Deploy custom script via SCCM | [Uninstalling Endpoint Protector Agents](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JScozIAD/view) |
| Creating Custom Device Groups | Need to whitelist devices by PID, VID, and serial numbers | Explain custom group creation process | Guide customer on creating and managing custom groups | [Creating Custom Device Groups](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MtmU2IAJ/view) |
| Server Migration and User Import Issues | Users and computers not imported after server migration | Verify Azure AD and EPP server settings | Adjust Azure AD settings and re-sync | [Server Migration and User Import Issues](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NmYjlIAF/view) |
| Changing Device Group Priorities | Unable to reorder device groups | Explain drag-and-drop functionality for group priorities | Use drag-and-drop to reorder groups | [Changing Device Group Priorities](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O1QM2IAN/view) |

---

## Detailed Issues

### Blocking Bluetooth Data Transfer

**Symptoms:**  
Bluetooth data transfer remains enabled on devices despite applying policies to block it.

**Troubleshooting Steps:**  
1. Review the Device Control settings in Netwrix Endpoint Protector.
2. Verify the policies applied to the relevant Device Groups.
3. Update the policy settings to explicitly block Bluetooth data transfer.
4. Test the changes on a sample device to confirm the restrictions are effective.

**Root Cause:**  
Misconfiguration in the Device Control settings allowed Bluetooth data transfer.

**Solution:**  
- Update the policy settings for the relevant Device Group to explicitly disable Bluetooth data transfer.
- Apply and test the changes to ensure the functionality is blocked.

**Warnings:**  
- Regularly review Device Control policies to ensure compliance with security requirements.

**Source Ticket:** [Blocking Bluetooth Data Transfer](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FDkXSIA1/view)

---

### Managing Device Groups

**Symptoms:**  
Unable to add new computers to a group or delete existing ones.

**Troubleshooting Steps:**  
1. Conduct a meeting with the customer to understand the issue.
2. Review the process for managing device groups.
3. Provide guidance on the correct steps to add or delete computers.

**Root Cause:**  
User misunderstanding of the group management process.

**Solution:**  
- Guide the customer on the correct procedure for managing device groups.

**Warnings:**  
- Ensure users are familiar with group management features to prevent similar issues.

**Source Ticket:** [Managing Device Groups](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FPTKjIAP/view)

---

### File Tracing Report Issues

**Symptoms:**  
Unable to fetch File Tracing reports based on group-wise settings.

**Troubleshooting Steps:**  
1. Confirm the issue with the customer and gather details.
2. Provide instructions on how to fetch the File Tracing report.
3. Follow up to ensure the issue is resolved.

**Root Cause:**  
Configuration or usage issue with group-wise settings.

**Solution:**  
- Guide the customer on the correct steps to fetch the File Tracing report.

**Source Ticket:** [File Tracing Report Issues](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GdTsBIAV/view)

---

### Uninstalling Endpoint Protector Agents

**Symptoms:**  
Need to uninstall Endpoint Protector agents from multiple client machines.

**Troubleshooting Steps:**  
1. Review the customer's request for uninstallation methods.
2. Check for existing scripts or executables for uninstallation.
3. Provide guidance on deploying the script via SCCM.

**Root Cause:**  
No automated solution readily available for mass uninstallation.

**Solution:**  
- Provide a custom uninstallation script.
- Guide the customer on deploying the script via SCCM.

**Warnings:**  
- Test uninstallation scripts in a controlled environment before deployment.
- Maintain a backup of configurations before performing mass uninstalls.

**Source Ticket:** [Uninstalling Endpoint Protector Agents](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JScozIAD/view)

---

### Creating Custom Device Groups

**Symptoms:**  
Need to whitelist devices by PID, VID, and serial numbers.

**Troubleshooting Steps:**  
1. Understand the customer’s requirements.
2. Provide detailed instructions on creating custom device groups.
3. Guide the customer on adding devices in bulk.

**Root Cause:**  
Customer required a method to manage and whitelist devices efficiently.

**Solution:**  
- Explain the process of creating custom device groups.
- Guide the customer on managing devices by specific identifiers.

**Source Ticket:** [Creating Custom Device Groups](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MtmU2IAJ/view)

---

### Server Migration and User Import Issues

**Symptoms:**  
Users and computers not imported after server migration.

**Troubleshooting Steps:**  
1. Verify EPP server settings.
2. Check Azure AD configuration.
3. Provide relevant documentation for Azure settings.
4. Re-sync after adjustments.

**Root Cause:**  
Incorrect Azure AD configuration for user mapping.

**Solution:**  
- Adjust Azure AD settings and re-sync.
- Use groups for departmental separation.

**Warnings:**  
- Ensure Azure AD settings are correctly configured to prevent synchronization issues.

**Source Ticket:** [Server Migration and User Import Issues](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NmYjlIAF/view)

---

### Changing Device Group Priorities

**Symptoms:**  
Unable to reorder device groups.

**Troubleshooting Steps:**  
1. Explain the drag-and-drop functionality for group priorities.
2. Demonstrate how to reorder groups.

**Root Cause:**  
Customer unaware of drag-and-drop functionality.

**Solution:**  
- Use drag-and-drop to reorder device groups.

**Source Ticket:** [Changing Device Group Priorities](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O1QM2IAN/view)

---

## Best Practices

- Regularly review and update Device Control policies to ensure compliance with security requirements.
- Provide training sessions or documentation for users unfamiliar with group management features.
- Test any custom scripts or configurations in a controlled environment before deployment.
- Maintain backups of configurations before performing significant changes, such as mass uninstalls or server migrations.
- Ensure Azure AD settings are correctly configured to avoid synchronization issues.

---

## Advanced Topics

### Hybrid Environments and Azure AD Synchronization
- When using hybrid environments, ensure the "Map on-premises users" feature in Azure AD is configured appropriately to prevent duplicate usernames.
- Refer to the [EPP Directory Services Overview](https://helpcenter.netwrix.com/bundle/EndpointProtector_5.9.4/page/Content/EndpointProtector/Admin/DirectoryServices/Overview.htm) and [API Permission Configuration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis) for detailed guidance.

---