# Netwrix Endpoint Protector: Device Control - Custom Classes Knowledge Base

## Overview

The **Device Control** component of **Netwrix Endpoint Protector (EPP)** allows organizations to manage and restrict access to devices connected to endpoints. The **Custom Classes** feature enables administrators to define specific device types or groups for granular control. This article addresses common issues encountered with this feature, provides troubleshooting steps, explains root causes, and outlines tested solutions.

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Effective Rights Report Discrepancy | Report shows fewer devices than expected | Verify report settings and system behavior | Confirm expected behavior and educate users | [Effective Rights Report Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GHkoRIAT/view) |
| Offline Installer Request | Customer requested the latest offline installer | Verify version and prepare installer | Provide the requested offline installer | [Offline Installer Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GYMzUIAX/view) |
| Missing Printer VID/PID | EPP client does not collect VID/PID for some printers | Check device type and logs | Clarify limitations and recommend physical printers | [Printer VID/PID Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hi3LWIAZ/view) |
| OTP Validity Issue | OTP valid for 15 minutes allowed access for 20 days | Test OTP functionality and time restrictions | Investigate OTP mechanism and system clock | [OTP Validity Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HT487IAD/view) |
| EPP Client Not Receiving Policies | Client not receiving policies despite successful connection | Verify client-server connection and licensing | Confirm licensing and monitor connectivity | [Client Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HZcevIAD/view) |
| License Release Delay | License release request not reflected immediately | Check release settings and refresh interface | Inform user of 30-day delay for license release | [License Release Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M6b8LIAR/view) |
| Bulk USB Enrollment Error | Bulk enrollment assigns incorrect VID/PID | Test with fresh XLS file and verify encoding | Avoid Libre Office and use compatible tools | [Bulk USB Enrollment Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NLFreIAH/view) |
| Virtual Appliance Migration | Inquiry about moving EPP appliance from Nutanix to VMware | Recommend backup and restore method | Deploy new appliance and restore from backup | [Virtual Appliance Migration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OpkSnIAJ/view) |

---

## Detailed Issues

### 1. Effective Rights Report Discrepancy
**Symptoms:**  
The Effective Rights report displayed only 15 devices instead of the expected 41.

**Troubleshooting Steps:**  
1. Confirm the issue is related to the Effective Rights report.  
2. Investigate the discrepancy in the number of devices displayed.  
3. Review the report generation process and settings.  
4. Escalate to engineering if necessary.

**Root Cause:**  
The report was functioning as designed, listing only devices for which rights could be set on Linux machines.

**Solution:**  
- Confirm the report's behavior is expected.  
- Educate users on how the report works to prevent confusion.  

**Source Ticket:** [Effective Rights Report Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GHkoRIAT/view)

---

### 2. Offline Installer Request
**Symptoms:**  
Customer requested the latest offline installer for version 5.9.4.0.

**Troubleshooting Steps:**  
1. Verify the version requested by the customer.  
2. Confirm the availability of the offline installer.  
3. Prepare and send the installer to the customer.

**Root Cause:**  
The customer required the latest version to maintain functionality and security.

**Solution:**  
Provide the offline installer for version 5.9.4.0.

**Source Ticket:** [Offline Installer Request](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GYMzUIAX/view)

---

### 3. Missing Printer VID/PID
**Symptoms:**  
- EPP client does not collect VID/PID for some printers.  
- Some printers display unusual serial numbers.

**Troubleshooting Steps:**  
1. Review EPP client configuration and device detection settings.  
2. Investigate missing VID/PID cases.  
3. Analyze serial number anomalies.  
4. Request logs and screenshots from the customer.

**Root Cause:**  
- Virtual printers (e.g., "Print to PDF") do not have VID/PID.  
- Some physical devices lack serial numbers.

**Solution:**  
- Clarify limitations of the EPP client.  
- Recommend using physical printers for accurate detection.

**Source Ticket:** [Printer VID/PID Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hi3LWIAZ/view)

---

### 4. OTP Validity Issue
**Symptoms:**  
An OTP valid for 15 minutes allowed access for 20 days.

**Troubleshooting Steps:**  
1. Block the device in question.  
2. Create and apply a 15-minute OTP.  
3. Wait 20 minutes and confirm if the device is still accessible.

**Root Cause:**  
Potential issue with the OTP mechanism or system clock discrepancies.

**Solution:**  
Investigate OTP functionality and ensure time-based restrictions are enforced.

**Source Ticket:** [OTP Validity Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HT487IAD/view)

---

### 5. EPP Client Not Receiving Policies
**Symptoms:**  
Client not receiving policies despite successful connection tests.

**Troubleshooting Steps:**  
1. Verify client-server connection.  
2. Check server logs for policy updates.  
3. Investigate potential licensing issues.

**Root Cause:**  
Temporary licensing issue affecting client-server communication.

**Solution:**  
- Confirm licensing is up to date.  
- Monitor client-server connectivity.

**Source Ticket:** [Client Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HZcevIAD/view)

---

### 6. License Release Delay
**Symptoms:**  
License release request did not reflect immediately.

**Troubleshooting Steps:**  
1. Verify the license release request was submitted successfully.  
2. Check if the release was scheduled for a future date.  
3. Refresh the interface to confirm changes.

**Root Cause:**  
License release was scheduled for 30 days instead of immediate execution.

**Solution:**  
Inform the user of the 30-day delay and ensure clarity on release settings.

**Source Ticket:** [License Release Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M6b8LIAR/view)

---

### 7. Bulk USB Enrollment Error
**Symptoms:**  
Bulk enrollment XLS file assigned incorrect VID/PID values.

**Troubleshooting Steps:**  
1. Test with a fresh XLS file.  
2. Verify encoding of the file used for bulk enrollment.  
3. Recreate the issue in a support environment.

**Root Cause:**  
Encoding changes made by Libre Office caused the server to misinterpret VID/PID data.

**Solution:**  
- Avoid using Libre Office for editing XLS files.  
- Use Microsoft Excel or other compatible tools.

**Source Ticket:** [Bulk USB Enrollment Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NLFreIAH/view)

---

### 8. Virtual Appliance Migration
**Symptoms:**  
Customer requested guidance on moving EPP appliance from Nutanix to VMware.

**Troubleshooting Steps:**  
1. Advise against direct migration via SSH.  
2. Recommend deploying a new appliance on VMware.  
3. Use System Backup V2 and Audit Log Backup for migration.

**Root Cause:**  
Misunderstanding of the migration process between virtualization platforms.

**Solution:**  
Deploy a new appliance and restore data using backup tools.

**Source Ticket:** [Virtual Appliance Migration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OpkSnIAJ/view)

---

## Best Practices

- **Effective Rights Reports:** Educate users on expected behavior to avoid confusion.  
- **Offline Installers:** Maintain an updated repository of available versions for quick access.  
- **Device Detection:** Ensure physical devices are used for accurate VID/PID reporting.  
- **OTP Management:** Regularly verify system clocks and OTP functionality.  
- **Licensing:** Keep licenses up to date to prevent communication issues.  
- **Bulk Enrollment:** Use compatible tools like Microsoft Excel to avoid encoding issues.  
- **Virtual Appliance Migration:** Follow recommended backup and restore procedures for seamless transitions.

---

## Advanced Topics

### High Resource Usage During Bulk Enrollment
- Monitor server performance during bulk operations.  
- Optimize policies and limit file shadowing to necessary scenarios.  
- Plan migrations to new instances to address performance bottlenecks.  

--- 

End of Article.