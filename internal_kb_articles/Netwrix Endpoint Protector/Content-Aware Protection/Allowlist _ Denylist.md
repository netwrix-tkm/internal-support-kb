# Netwrix Endpoint Protector Knowledge Base: Content-Aware Protection - Allowlist/Denylist

## Overview
Netwrix Endpoint Protector's Content-Aware Protection (CAP) module enables organizations to enforce data security policies by using allowlists and denylists to control file transfers, application usage, email domains, and URL access. The Allowlist/Denylist feature is a critical component of CAP, allowing administrators to define rules for permitted and restricted content. This article provides a comprehensive guide to troubleshooting common issues, understanding root causes, and implementing solutions related to Allowlist/Denylist functionality.

---

## Common Issues and Solutions

### 1. CAP Policy Blocking Files Without Sensitive Data
**Symptoms:** Files without sensitive data (e.g., credit card information) are blocked due to incorrect CAP policy settings.  
**Troubleshooting Steps:**  
1. Verify CAP policy configuration in the Content-Aware Protection settings.  
2. Check if all file types are selected for scanning.  
3. Deselect unnecessary file types to ensure only files with sensitive data are blocked.  

**Root Cause:** CAP policy was configured to scan all file types, causing false positives.  
**Solution:**  
- Adjust the CAP policy to block only files containing sensitive data.  
- Use valid sensitive data formats for testing.  

---

### 2. WhatsApp Uploads Blocked Despite No Policies
**Symptoms:** WhatsApp uploads fail for users; uninstalling Endpoint Protector temporarily resolves the issue.  
**Troubleshooting Steps:**  
1. Verify that no CAP policies are blocking WhatsApp uploads.  
2. Check for other security tools installed on affected machines.  
3. Disable conflicting tools (e.g., Netskope One Client) and test functionality.  

**Root Cause:** Conflict between Endpoint Protector and Netskope One Client.  
**Solution:**  
- Disable Netskope One Client to resolve the conflict.  

---

### 3. Allowlist Editing Interface Closes Unexpectedly
**Symptoms:** Policy interface closes unexpectedly when selecting usernames during allowlist editing.  
**Troubleshooting Steps:**  
1. Investigate for interference from other programs running on the system.  
2. Disable or adjust settings of conflicting programs.  

**Root Cause:** Conflict with another program interfering with the Endpoint Protector interface.  
**Solution:**  
- Identify and disable the conflicting program.  

---

### 4. Blocked .dwg Files Despite Domain Allowlist
**Symptoms:** .dwg files are blocked even though the domain is added to the allowlist.  
**Troubleshooting Steps:**  
1. Verify the allowlist configuration for the domain.  
2. Check denylist settings for file extensions.  
3. Add the .dwg file extension to the allowlist.  

**Root Cause:** .dwg file extension was included in the denylist, overriding the domain allowlist.  
**Solution:**  
- Add the .dwg file extension to the allowlist and ensure the domain is correctly configured.  

---

### 5. Policies Not Applying to New Devices
**Symptoms:** Devices moved to an allowed policy remain blocked, impacting user workflows.  
**Troubleshooting Steps:**  
1. Verify device recognition in the Endpoint Protector system.  
2. Check CAP policy settings for compatibility with new devices.  
3. Amend the CAP policy and confirm changes are applied.  

**Root Cause:** Potential issue with device recognition or CAP policy application.  
**Solution:**  
- Amend the CAP policy and ensure devices are correctly recognized.  

---

### 6. Internal Emails Blocked Despite Allowlist
**Symptoms:** Internal emails are flagged as external and blocked, despite domains being added to the allowlist.  
**Troubleshooting Steps:**  
1. Verify email domain allowlist entries.  
2. Check DPI settings under "Device Control" > "Global Settings."  
3. Remove "@" symbol from allowlist entries.  

**Root Cause:** CAP policy does not recognize domains formatted with the "@" symbol.  
**Solution:**  
- Remove "@" symbol from allowlist entries (e.g., use `domain.com` instead of `@domain.com`).  

---

### 7. DPI Allowlist Entries Not Visible in CAP Policy
**Symptoms:** DPI allowlist entries disappear after saving, causing confusion about their application.  
**Troubleshooting Steps:**  
1. Confirm backend functionality of the allowlist entries.  
2. Upgrade to version 5.9.4.1 to fix UI bug.  

**Root Cause:** UI bug in version 5.9.4.0 prevents allowlist entries from displaying correctly.  
**Solution:**  
- Upgrade to version 5.9.4.1 to resolve the UI issue.  

---

### 8. Blocking Specific URL Paths Unsupported
**Symptoms:** Unable to block `dropbox.com/login` while allowing `dropbox.com`.  
**Troubleshooting Steps:**  
1. Verify product limitations regarding URL path blocking.  
2. Submit feature request for granular URL blocking capabilities.  

**Root Cause:** Current product functionality only supports domain-level blocking.  
**Solution:**  
- Inform customer of limitations and submit feature request for URL path blocking.  

---

### 9. File Blocking Not Working for Specific File Types
**Symptoms:** Excel (.xlsx) and Word (.docx) files were not blocked in WhatsApp, while executable (.exe) files were successfully blocked.  
**Troubleshooting Steps:**  
1. Verify CAP policy settings to ensure .xlsx and .docx file types are included in the blocklist.  
2. Confirm WhatsApp exit points are selected in the policy settings.  
3. Check entity selection to ensure the policy is applied to the correct computer.  
4. Test file blocking functionality.  
5. Verify if MTP scanning is enabled.  

**Root Cause:** MTP scanning was disabled, preventing the blocking of specified file types.  
**Solution:** Enable MTP scanning in the CAP policy settings.  

---

### 10. Excessive "Content Threat Blocked" Logs
**Symptoms:** Logs for Facebook.com were generated despite users not visiting the site.  
**Troubleshooting Steps:**  
1. Conduct a remote session to attempt to reproduce the issue.  
2. Generate EPP client logs using the following commands on Mac:  
   ```bash
   sudo /bin/launchctl unload /Library/LaunchDaemons/com.cososys.eppclient.launchdaemon.plist
   sudo touch /private/var/log/eppclient.log
   sudo touch /private/var/log/eppsslsplit.log
   sudo /bin/launchctl load /Library/LaunchDaemons/com.cososys.eppclient.launchdaemon.plist
   ```  
3. Analyze logs to identify background calls.  

**Root Cause:** Background calls from third-party websites triggered content threat alerts.  
**Solution:** Confirm alerts were due to background calls and educate the customer.  

---

### 11. Blocking Email Attachments to Free Services
**Symptoms:** Unable to block attachments to Gmail while allowing specific users.  
**Troubleshooting Steps:**  
1. Navigate to CAP > DPI > DPI Ports & Settings.  
2. Select "Gmail" in the "Select Parser" dropdown.  
3. Add allowed business domains under "Allowed Domains for Google Business Accounts."  
4. Save changes and test configuration.  

**Root Cause:** Limitation in Denylists feature for domain-specific configurations.  
**Solution:** Restrict Gmail access to approved business domains using DPI settings.  

---

### 12. Allowlist for Email Uploads
**Symptoms:** Unable to configure email uploads for specific domains.  
**Troubleshooting Steps:**  
1. Navigate to CAP > DPI settings.  
2. Add business domains to "Allowed business accounts."  
3. Test configuration to ensure non-business domains are blocked.  

**Root Cause:** Lack of proper configuration in CAP settings.  
**Solution:** Add business domains to Allowed Accounts in DPI settings.  

---

## Best Practices
- **Enable MTP Scanning:** Ensure MTP scanning is enabled for file blocking policies involving applications like WhatsApp.  
- **Verify Allowlist/Denylist Configurations:** Regularly review configurations to prevent conflicts between Allowlist and Denylist rules.  
- **Keep Lists Concise:** Maintain concise Allow/Deny lists to optimize system performance.  
- **Test Policies in Controlled Environments:** Test configurations before deploying them widely to avoid unexpected issues.  
- **Educate Users:** Provide clear guidance on interpreting notifications and configuring policies effectively.  

---

## Advanced Topics

### Handling Background Calls in Content Threat Logs
Background calls from third-party websites can trigger false positives in content threat logs. Use log analysis tools to identify the source of these calls and educate users about their implications.

### Feature Requests for Missing Functionality
For missing features like URL blocking or differentiating personal/corporate applications, guide customers to submit formal feature requests through the appropriate channels. Monitor updates from the product team to keep customers informed.

---

End of Article.