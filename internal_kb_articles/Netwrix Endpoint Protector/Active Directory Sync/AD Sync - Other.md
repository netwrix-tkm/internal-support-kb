# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## Active Directory Sync - Other  

### **Overview**  
Active Directory (AD) Sync is a critical feature of Netwrix Endpoint Protector (EPP) that enables seamless integration with Active Directory environments, including Azure AD and on-premise AD. This functionality allows administrators to synchronize user accounts, groups, and devices, ensuring accurate policy enforcement and streamlined management. Understanding and troubleshooting issues in this category is essential for maintaining system integrity, minimizing downtime, and ensuring compliance with organizational policies.  

### **Technical Background**  
#### **Key Concepts**  
- **Active Directory Sync**: A feature that connects EPP to AD environments to import users, groups, and devices for policy application and reporting.  
- **Synchronization Frequency**: Sync intervals can vary, with Azure AD sync often configured to occur every 15 minutes.  
- **Primary Groups**: Microsoft restricts syncing users from primary groups like "Domain Users."  
- **Multi-Tenant Platform (MTP)**: A setting that enables AD authentication in multi-tenant environments.  

#### **Terminology**  
- **Distinguished Name (DN)**: The unique identifier for objects in AD, e.g., `CN=GroupName,DC=Domain,DC=com`.  
- **LDAP/LDAPS Ports**: Common ports for AD communication (389 for LDAP, 636 for LDAPS).  
- **sf_guard_user Table**: A database table in EPP that stores user account information.  

#### **System Context**  
Netwrix Endpoint Protector integrates with AD environments to enforce policies based on group memberships, synchronize devices, and manage administrative roles. Proper configuration of AD Sync settings is crucial for ensuring accurate data synchronization and avoiding stale or missing entries.  

---

### **Issue Recognition & Triage**  
#### **Symptoms**  
- Stale devices reappearing in the EPP console after deletion.  
- Failed AD binding due to invalid credentials or misconfigured settings.  
- Missing users or groups in the EPP interface after synchronization.  
- Errors related to group filters or incorrect domain name formats.  
- Authentication failures despite successful sync tests.  

#### **Priority Assessment**  
- **High Priority**: Issues affecting authentication, admin access, or policy enforcement.  
- **Medium Priority**: Problems with stale data or missing groups that do not immediately impact functionality.  
- **Low Priority**: Configuration inquiries or requests for clarification on system capabilities.  

---

### **Diagnostic Methodology**  
#### **Systematic Approach**  
1. **Verify Sync Settings**: Check synchronization frequency, connection ports, and authentication settings.  
2. **Test Connectivity**: Use the "Test" button in the AD Sync interface to confirm successful connection.  
3. **Review Logs**: Examine system logs for error messages related to synchronization or authentication.  
4. **Database Inspection**: Query the `sf_guard_user` table for deleted or inactive entries.  
5. **Replicate the Issue**: Attempt to reproduce the problem in a controlled environment.  
6. **Check Permissions**: Ensure the AD account used for synchronization has sufficient privileges.  

#### **Decision Points**  
- If sync tests fail, focus on credentials and connection settings.  
- If users or groups are missing, inspect database flags and group configurations.  
- If stale data persists, verify server version and apply updates or hotfixes.  

---

### **Information Collection**  
#### **Customer Questions**  
- What version of Netwrix Endpoint Protector are you using?  
- Are you using Azure AD or on-premise AD?  
- Have there been any recent changes to your AD environment or EPP configuration?  
- What error messages are you seeing?  

#### **Logs and Data to Collect**  
- **Sync Logs**: Export logs from the AD Sync interface.  
- **Database Queries**: Run SQL commands to inspect the `sf_guard_user` table.  
- **Screenshots**: Capture configuration settings and error messages.  
- **Network Details**: Confirm ports and protocols used for AD communication.  

---

### **Common Scenarios & Solutions**  
#### **Scenario 1: Stale Devices Reappearing**  
- **Symptoms**: Deleted devices reappear in the EPP console after sync events.  
- **Solution**: Upgrade the EPP server to the latest version and apply hotfixes. Ensure EPP agents are uninstalled from removed devices.  
- **Reference Case**: [500Qk00000Ctc8zIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ctc8zIAB/view)  

#### **Scenario 2: Failed AD Binding**  
- **Symptoms**: Binding fails with "invalid credentials" error.  
- **Solution**: Verify credentials, connection ports, and domain name format. Update to the latest server version if necessary.  
- **Reference Case**: [500Qk00000CUFltIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CUFltIAH/view)  

#### **Scenario 3: Missing Groups or Users**  
- **Symptoms**: Groups or users do not appear in the EPP interface after sync.  
- **Solution**: Correct domain name format and ensure group names are accurately defined. Check for duplicate database entries.  
- **Reference Case**: [500Qk00000DElduIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DElduIAD/view)  

#### **Scenario 4: Authentication Failures**  
- **Symptoms**: AD accounts fail to authenticate despite successful sync tests.  
- **Solution**: Disable enforced password change policies in the appliance settings.  
- **Reference Case**: [500Qk00000HfBvPIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HfBvPIAV/view)  

---

### **Detailed Case Studies**  
#### **Case Study 1: Stale Devices Reappearing**  
- **Ticket ID**: [500Qk00000Ctc8zIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ctc8zIAB/view)  
- **Symptoms**: Stale devices reappeared in the EPP console after deletion.  
- **Diagnostic Steps**: Verified sync settings, server version, and agent uninstallation status.  
- **Resolution**: Upgraded the server and applied hotfixes.  
- **Key Takeaways**: Regular updates prevent stale data issues.  

#### **Case Study 2: Failed AD Binding**  
- **Ticket ID**: [500Qk00000CUFltIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CUFltIAH/view)  
- **Symptoms**: Binding failed due to invalid credentials.  
- **Diagnostic Steps**: Tested connection ports and credentials.  
- **Resolution**: Corrected credentials and updated server version.  
- **Key Takeaways**: Always verify credentials and domain name formats.  

#### **Case Study 3: Missing Groups**  
- **Ticket ID**: [500Qk00000DElduIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DElduIAD/view)  
- **Symptoms**: Groups failed to sync due to incorrect domain name format.  
- **Diagnostic Steps**: Tested various group name formats.  
- **Resolution**: Corrected domain name format in AD settings.  
- **Key Takeaways**: Proper syntax is critical for successful synchronization.  

---

### **Best Practices & Tips**  
1. **Regular Updates**: Keep the EPP server updated to the latest version to benefit from bug fixes and improvements.  
2. **Database Maintenance**: Periodically check for deleted or inactive entries in the `sf_guard_user` table.  
3. **Documentation**: Provide customers with clear instructions on configuration settings and syntax requirements.  
4. **Testing**: Always test sync configurations after making changes to ensure proper functionality.  
5. **Customer Communication**: Use screenshots and logs to clarify issues and solutions during troubleshooting.  

---

### **Escalation Guidelines**  
#### **Criteria for Escalation**  
- Persistent issues after applying standard troubleshooting steps.  
- Errors related to server-side limitations or bugs requiring R&D intervention.  
- Requests for new features or enhancements.  

#### **Escalation Procedure**  
1. Document all troubleshooting steps and findings.  
2. Attach relevant logs, screenshots, and database queries.  
3. Submit a detailed escalation ticket to the R&D team with priority status.  
4. Communicate escalation status to the customer and provide updates as available.  

---  
End of Document.  