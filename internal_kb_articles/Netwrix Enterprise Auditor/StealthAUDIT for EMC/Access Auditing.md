# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## StealthAUDIT for EMC: Access Auditing  

### **Overview**  
Access auditing within the StealthAUDIT for EMC component of Netwrix Enterprise Auditor is a critical feature for organizations seeking to monitor and manage file system access across their environments. This category of issues typically involves challenges with bulk imports, scan configurations, and permissions, which can impact the accuracy and reliability of access auditing. Understanding these issues and their resolution is essential for maintaining operational integrity and ensuring compliance with security policies.

---

### **Technical Background**  
#### **Key Concepts**  
- **Filesystem Access Auditing Agent (FSAA):** A module within StealthAUDIT for EMC responsible for collecting access data from file systems.  
- **Tier 1 and Tier 2 Databases:** Hierarchical database structures used to store and process access data. Mismatches between these tiers can disrupt data imports.  
- **Host Lists:** Configuration files that define the servers or shares targeted for auditing. Incorrect host lists can lead to scan failures.  
- **NTFS Permissions:** File system permissions that govern access to shares. Misconfigured permissions can block scanning processes.  

#### **System Context**  
- **Netwrix Enterprise Auditor Version:** Issues in this category are commonly reported in versions 11.5 and 11.6.  
- **Target Environments:** Includes Dell Powerstore, Dell Isilon, and other NAS devices.  

---

### **Issue Recognition & Triage**  
#### **Symptoms**  
- Bulk import failures with error messages referencing database mismatches.  
- "Access denied" errors during scan configuration or execution.  
- Scans pointing to outdated or invalid host lists.  

#### **Priority Assessment**  
- **High Priority:** Issues that prevent access auditing entirely or impact critical compliance reporting.  
- **Medium Priority:** Errors that affect specific shares or configurations but do not disrupt overall auditing.  

---

### **Diagnostic Methodology**  
#### **Systematic Approach**  
1. **Verify Error Messages:** Review logs and error details to identify the root cause (e.g., database mismatch, permissions issue).  
2. **Check Configuration Settings:** Validate host lists, scan depth, and target shares.  
3. **Test Permissions:** Ensure the service account has the necessary NTFS permissions for the target shares.  
4. **Engage External Support:** If the issue involves third-party storage systems (e.g., Dell Isilon), consult vendor documentation or support.  

#### **Decision Points**  
- **Database Mismatch:** Proceed with resetting access data.  
- **Permissions Issue:** Escalate to SQL DBAs or storage administrators for resolution.  
- **Host List Errors:** Correct the host list and reconfigure scans.  

---

### **Information Collection**  
#### **Customer Questions**  
- What error messages are being displayed?  
- What version of Netwrix Enterprise Auditor is in use?  
- What storage system or NAS device is being targeted?  
- Has the service account been granted appropriate permissions?  

#### **Logs and Data to Collect**  
- FSAA logs from the Netwrix Enterprise Auditor platform.  
- SQL error logs if database-related issues are suspected.  
- Host list configurations and scan settings.  
- NTFS permission settings for the target shares.  

---

### **Common Scenarios & Solutions**  
#### **Scenario 1: Bulk Import Failure Due to Database Mismatch**  
- **Symptoms:** Error message indicating Tier 1 and Tier 2 database mismatch.  
- **Solution:** Reset access data by setting `AccessGUID` to 'RESET' in the `SA_FSAA_Hosts` table.  

#### **Scenario 2: Permissions Issue During Bulk Import**  
- **Symptoms:** "User does not have permission to perform this action" error.  
- **Solution:** Grant necessary permissions to the service account used for the bulk import.  

#### **Scenario 3: Invalid Host List Configuration**  
- **Symptoms:** FSAA scans fail due to outdated or decommissioned servers in the host list.  
- **Solution:** Update the host list to include valid servers and reconfigure the scan settings.  

#### **Scenario 4: NTFS Permissions Blocking Access**  
- **Symptoms:** "Access denied" error when scanning Dell Isilon shares.  
- **Solution:** Adjust NTFS permissions to allow the scan account access to the target share.  

---

### **Detailed Case Studies**  
#### **Case Study 1: Bulk Import Failure Due to Database Mismatch**  
- **Ticket ID:** [500Qk00000CL4BNIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CL4BNIA1/view)  
- **Initial Symptoms:** Bulk import failed with error indicating Tier 1 and Tier 2 database mismatch.  
- **Diagnostic Steps:** Reset access data by modifying the `SA_FSAA_Hosts` table.  
- **Resolution:** Permissions issue was identified and resolved by granting access to the service account.  
- **Key Takeaways:** Always verify database integrity and service account permissions before initiating bulk imports.  

#### **Case Study 2: Invalid Host List Configuration**  
- **Ticket ID:** [500Qk00000N4spNIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000N4spNIAR/view)  
- **Initial Symptoms:** FSAA scans failed due to outdated host list configurations.  
- **Diagnostic Steps:** Created a new host list and corrected scan settings.  
- **Resolution:** Updated host list and verified data reporting in the Access Information Center (AIC).  
- **Key Takeaways:** Regularly review and update host lists to ensure they reflect current server configurations.  

#### **Case Study 3: NTFS Permissions Blocking Access**  
- **Ticket ID:** [500Qk00000OigkAIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OigkAIAR/view)  
- **Initial Symptoms:** "Access denied" error when scanning Dell Isilon shares.  
- **Diagnostic Steps:** Reviewed NTFS permissions and engaged Dell support for guidance.  
- **Resolution:** Adjusted NTFS permissions to grant access to the scan account.  
- **Key Takeaways:** Ensure NTFS permissions are correctly configured for nested shares.  

---

### **Best Practices & Tips**  
- **Pre-Scan Validation:** Always verify host lists, scan settings, and permissions before initiating scans.  
- **Service Account Permissions:** Ensure the service account has full access to the target shares and databases.  
- **Documentation Updates:** Maintain detailed records of configuration changes and permissions adjustments.  
- **Vendor Collaboration:** Engage with storage system vendors for guidance on specific configurations.  
- **Regular Audits:** Periodically review scan settings and host lists to prevent misconfigurations.  

---

### **Escalation Guidelines**  
#### **Criteria for Escalation**  
- Issues involving third-party storage systems that require vendor support.  
- Persistent errors despite following documented troubleshooting steps.  
- Database corruption or integrity issues impacting multiple components.  

#### **Escalation Procedures**  
1. Collect all relevant logs, error messages, and configuration details.  
2. Document troubleshooting steps already performed.  
3. Escalate to Tier 2 or Tier 3 support with a detailed summary of the issue.  
4. If vendor support is required, provide all necessary context and engage directly with the vendor.  

---  
End of Document.  