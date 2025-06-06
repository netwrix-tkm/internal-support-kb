# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## **Overview**  
This guide focuses on troubleshooting and resolving issues related to the **Device Control** component of **Netwrix Endpoint Protector (EPP)**, specifically within the **Custom Classes** feature. Device Control is critical for managing access to devices and enforcing security policies across endpoints. Understanding this category is essential for ensuring proper functionality, minimizing downtime, and maintaining compliance with organizational security standards.

---

## **Technical Background**  
### **Key Concepts**  
- **Device Control**: A feature within EPP that allows administrators to manage and restrict access to devices connected to endpoints.  
- **Custom Classes**: A sub-feature that enables the creation of tailored device groups based on specific attributes such as Vendor ID (VID), Product ID (PID), or serial numbers.  
- **Effective Rights Report**: A report that displays devices and their associated permissions for endpoints.  
- **Offline Temporary Passwords (OTP)**: Time-limited passwords used to grant temporary access to devices.  
- **Bulk Enrollment**: A method for adding multiple devices to the Allowed Specific Devices list using .xls files.  

### **System Context**  
- **EPP Server**: The central management system responsible for policy enforcement and device monitoring.  
- **EPP Client**: Installed on endpoints to enforce policies and communicate with the server.  
- **Logs**: Critical for diagnosing issues, including server logs, client logs, and device-specific logs.  
- **Licensing**: Ensures proper functionality and communication between the server and clients.  

---

## **Issue Recognition & Triage**  
### **Symptoms**  
- Discrepancies in reports (e.g., missing devices in Effective Rights).  
- Incorrect or missing VID/PID data for devices.  
- Licensing or connectivity issues between EPP clients and the server.  
- Bulk enrollment errors when adding devices.  
- Unexpected behavior of OTPs or device access restrictions.  

### **Priority Assessment**  
- **High Priority**: Issues affecting security policies (e.g., unrestricted device access).  
- **Medium Priority**: Errors in reporting or bulk enrollment that do not compromise security.  
- **Low Priority**: General inquiries or requests for documentation.  

---

## **Diagnostic Methodology**  
### **Systematic Approach**  
1. **Verify the Problem**: Confirm the reported issue by replicating the behavior or reviewing logs/screenshots provided by the customer.  
2. **Categorize the Issue**: Determine whether the problem is related to configuration, system limitations, or external factors (e.g., file encoding).  
3. **Investigate Logs**: Analyze server and client logs for errors or anomalies.  
4. **Test Scenarios**: Recreate the issue in a controlled environment to identify root causes.  
5. **Consult Documentation**: Refer to product manuals and known limitations for clarification.  
6. **Escalate if Necessary**: If the issue cannot be resolved, escalate to engineering with detailed findings.  

---

## **Information Collection**  
### **Customer Queries**  
- What is the specific behavior observed?  
- Are there screenshots or logs available?  
- What version of EPP is being used?  
- Are the devices physical or virtual?  
- Have any recent changes been made to the system or policies?  

### **Logs/Data to Collect**  
- **Server Logs**: For policy updates and device communication.  
- **Client Logs**: For device detection and enforcement issues.  
- **Screenshots**: Effective Rights reports, Device Manager, or error messages.  
- **Configuration Files**: Bulk enrollment .xls files or policy settings.  

---

## **Common Scenarios & Solutions**  
### **Scenario 1: Missing Devices in Effective Rights Report**  
- **Symptoms**: Report displays fewer devices than expected.  
- **Root Cause**: System limitation—only devices with configurable rights are displayed.  
- **Solution**: Confirm expected behavior with the customer and provide documentation.  
- **Reference Case**: [500Qk00000GHkoRIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GHkoRIAT/view)  

### **Scenario 2: Incorrect VID/PID for Printers**  
- **Symptoms**: Missing VID/PID or unusual serial numbers for printers.  
- **Root Cause**: Virtual printers or devices lacking serial numbers.  
- **Solution**: Verify physical devices and clarify system limitations.  
- **Reference Case**: [500Qk00000Hi3LWIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hi3LWIAZ/view)  

### **Scenario 3: Bulk Enrollment Errors**  
- **Symptoms**: Incorrect VID/PID assignment during bulk enrollment.  
- **Root Cause**: File encoding changes by third-party software (e.g., Libre Office).  
- **Solution**: Use Microsoft Excel to save .xls files and ensure proper encoding.  
- **Reference Case**: [500Qk00000NLFreIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NLFreIAH/view)  

### **Scenario 4: OTP Validity Issues**  
- **Symptoms**: OTP grants access beyond the intended time limit.  
- **Root Cause**: Potential system clock discrepancies or OTP mechanism failure.  
- **Solution**: Verify system clock and test OTP functionality.  
- **Reference Case**: [500Qk00000HT487IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HT487IAD/view)  

### **Scenario 5: Licensing and Connectivity Problems**  
- **Symptoms**: EPP client fails to receive policies despite successful connection tests.  
- **Root Cause**: Licensing issues affecting client-server communication.  
- **Solution**: Confirm licensing status and monitor connectivity.  
- **Reference Case**: [500Qk00000HZcevIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HZcevIAD/view)  

---

## **Detailed Case Studies**  
### **Case Study 1: Bulk Enrollment Encoding Issue**  
- **Ticket ID**: [500Qk00000NLFreIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NLFreIAH/view)  
- **Symptoms**: Incorrect VID/PID assignment during bulk enrollment.  
- **Diagnostic Steps**:  
  - Recreated the issue using the customer’s .xls file.  
  - Tested with a fresh sample file saved using Microsoft Excel.  
- **Resolution**: Advised the customer to avoid using Libre Office for editing .xls files.  
- **Key Takeaways**: Ensure compatibility of file formats for bulk uploads.  

### **Case Study 2: OTP Validity Issue**  
- **Ticket ID**: [500Qk00000HT487IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HT487IAD/view)  
- **Symptoms**: OTP grants access beyond the intended time limit.  
- **Diagnostic Steps**:  
  - Tested OTP functionality in a controlled environment.  
  - Verified system clock settings.  
- **Resolution**: No documented resolution; customer closed the case independently.  
- **Key Takeaways**: Always verify time-sensitive mechanisms and system clock accuracy.  

---

## **Best Practices & Tips**  
1. **Documentation**: Provide clear explanations of system limitations to customers upfront.  
2. **Testing**: Recreate issues in a controlled environment to identify root causes.  
3. **File Compatibility**: Use recommended software (e.g., Microsoft Excel) for bulk uploads.  
4. **Logs**: Collect comprehensive logs for faster diagnosis.  
5. **Licensing**: Regularly verify licensing status to prevent communication issues.  
6. **Customer Communication**: Set realistic expectations and provide actionable recommendations.  

---

## **Escalation Guidelines**  
### **Criteria for Escalation**  
- Issues involving system bugs or limitations requiring engineering intervention.  
- Problems that cannot be resolved after thorough troubleshooting.  
- High-priority cases affecting security or compliance.  

### **Escalation Process**  
1. Document all findings, including logs, screenshots, and test results.  
2. Submit a detailed report to the engineering team via the internal escalation system.  
3. Follow up with the customer to provide updates and manage expectations.  

---  
End of Document.  