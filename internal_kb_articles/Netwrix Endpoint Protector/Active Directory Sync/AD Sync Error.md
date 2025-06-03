# Netwrix Endpoint Protector Knowledge Base: Active Directory Sync Errors

## Overview
Active Directory (AD) synchronization is a critical feature of Netwrix Endpoint Protector (EPP) that enables seamless integration with AD for user authentication, group management, and single sign-on (SSO). However, various issues can arise during setup, migration, or routine operations, leading to synchronization failures, authentication errors, or misconfigured settings. This article provides a comprehensive guide to troubleshooting and resolving common AD sync errors.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| AD sync failure after server migration | Unable to connect to AD after migrating from Ubuntu 18 to Ubuntu 22 | Verify port usage and DNS resolution | Use port 389 and connect via IP address | [AD Sync Error - Ubuntu Migration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EW8iMIAT/view) |
| Misconfigured AD connection settings | Server access error during AD sync | Validate connection settings and permissions | Correct AD connection settings and verify permissions | [AD Connection Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GElAlIAL/view) |
| Incorrect user type after AD sync | Admin users appear as EPP type instead of AD type | Delete problematic users and resync | SSH into server, delete users, reboot, and resync | [User Type Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ir7c7IAB/view) |
| Expired Azure AD client secret | Unable to update expired client secret in sync settings | Recreate synchronization configuration | Delete and recreate sync configuration with new secret | [Azure AD Client Secret Expiration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ItadCIAR/view) |
| Password sync failure for AD-linked accounts | Passwords do not sync after changes in AD | Explore SSO alternatives | Configure OKTA SSO for seamless authentication | [Password Sync Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LaG5QIAV/view) |
| Missing user in Azure AD sync | Third user not synced into EPP group | Check sync logs and remove deleted groups | Remove deleted group from sync configuration | [Azure AD Group Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LeKtgIAF/view) |
| AD sync setup error | Error during local AD setup for SSO | Review configuration and test login functionality | Correct AD settings and verify login functionality | [Local AD Setup Error](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MLpkRIAT/view) |
| Incorrect AD sync input fields | Admin login fails due to misconfigured fields | Update User field and Admin Group name | Use username only (no domain) and correct group name | [Incorrect Input Fields](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OJQYtIAP/view) |
| AD sync failure in Azure VNET | Unable to sync AD after moving DLP VM to Azure VNET | Verify connectivity and permissions | Correct OU format and enable permissions | [Azure VNET Sync Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OOoaYIAT/view) |

---

## Detailed Issues

### 1. AD Sync Failure After Server Migration
**Symptoms:** After migrating from Ubuntu 18 to Ubuntu 22, the new server fails to connect to AD, while the old server works correctly.  
**Troubleshooting Steps:**  
1. Verify that the old server can connect to AD without issues.  
2. Check system logs on the new server for error messages.  
3. Test connection using both FQDN and IP address.  
4. Confirm port usage for LDAP connections.  

**Root Cause:** Incorrect port usage and DNS resolution issues when using FQDN.  
**Solution:**  
- Use port `389` for LDAP connections.  
- Connect to AD using the IP address instead of the FQDN.  

**Source Ticket:** [AD Sync Error - Ubuntu Migration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EW8iMIAT/view)  

---

### 2. Misconfigured AD Connection Settings
**Symptoms:** Server access error during AD sync, replicated in test environments.  
**Troubleshooting Steps:**  
1. Review error messages and connection settings.  
2. Verify network connectivity and permissions for the AD service account.  
3. Conduct remote session to diagnose settings.  

**Root Cause:** Misconfiguration in AD connection settings preventing authentication.  
**Solution:**  
- Correct AD connection settings.  
- Ensure the service account has necessary permissions.  
- Test connection post-correction.  

**Source Ticket:** [AD Connection Misconfiguration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GElAlIAL/view)  

---

### 3. Incorrect User Type After AD Sync
**Symptoms:** Admin users synced from AD appear as EPP type instead of AD type, preventing login with AD passwords.  
**Troubleshooting Steps:**  
1. Toggle "ignore AD Authentication" setting.  
2. SSH into server, delete problematic users, and resync.  

**Root Cause:** Users created as EPP type prior to AD sync do not automatically change to AD type.  
**Solution:**  
- SSH into the server.  
- Delete problematic users from the database.  
- Reboot the server and perform AD sync again.  

**Source Ticket:** [User Type Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ir7c7IAB/view)  

---

### 4. Expired Azure AD Client Secret
**Symptoms:** Expired client secret prevents synchronization, and no option exists to update it.  
**Troubleshooting Steps:**  
1. Confirm expiration of client secret.  
2. Delete current sync configuration and recreate it.  

**Root Cause:** Expired client secret with no system alert prior to expiration.  
**Solution:**  
- Delete existing sync configuration.  
- Recreate sync configuration using the new client secret.  

**Source Ticket:** [Azure AD Client Secret Expiration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ItadCIAR/view)  

---

### 5. Password Sync Failure for AD-Linked Accounts
**Symptoms:** Passwords for AD-linked admin accounts do not sync after changes in AD.  
**Troubleshooting Steps:**  
1. Review password sync settings.  
2. Explore SSO alternatives like Azure or OKTA.  

**Root Cause:** Failure in synchronization process for password updates.  
**Solution:**  
- Configure OKTA SSO for seamless authentication.  

**Source Ticket:** [Password Sync Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LaG5QIAV/view)  

---

### 6. Missing User in Azure AD Sync
**Symptoms:** Third user added to Azure AD group does not sync into EPP group.  
**Troubleshooting Steps:**  
1. Check sync logs and Azure AD group membership.  
2. Remove deleted groups from sync configuration.  

**Root Cause:** Deleted group in Azure AD not removed from EPP sync configuration.  
**Solution:**  
- Remove deleted group from EPP sync configuration.  

**Source Ticket:** [Azure AD Group Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LeKtgIAF/view)  

---

### 7. AD Sync Setup Error
**Symptoms:** Error during local AD setup for SSO functionality.  
**Troubleshooting Steps:**  
1. Review error message and configuration settings.  
2. Test login functionality after adjustments.  

**Root Cause:** Incorrect or incomplete AD configuration settings.  
**Solution:**  
- Correct AD settings and verify login functionality.  

**Source Ticket:** [Local AD Setup Error](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MLpkRIAT/view)  

---

### 8. Incorrect AD Sync Input Fields
**Symptoms:** Admin login fails due to incorrect User field and Admin Group name.  
**Troubleshooting Steps:**  
1. Replace User field with username only (no domain).  
2. Update Admin Group name with correct group name from AD.  

**Root Cause:** Misconfigured input fields in AD sync settings.  
**Solution:**  
- Use username only in User field.  
- Correct Admin Group name in sync settings.  

**Source Ticket:** [Incorrect Input Fields](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OJQYtIAP/view)  

---

### 9. AD Sync Failure in Azure VNET
**Symptoms:** Unable to sync AD after moving DLP VM to Azure VNET.  
**Troubleshooting Steps:**  
1. Verify connectivity using SSH and telnet.  
2. Check firewall settings and port permissions.  
3. Correct OU format and enable permissions.  

**Root Cause:** Incorrect configuration settings and permission issues.  
**Solution:**  
- Correct OU format (`DC=rstacksolutions,DC=com,OU=RSTACK-USERS`).  
- Ensure permissions are enabled for synchronization tasks.  

**Source Ticket:** [Azure VNET Sync Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OOoaYIAT/view)  

---

## Best Practices
1. **Validate Configuration Settings:** Always review AD sync settings thoroughly before testing connections.  
2. **Monitor Credentials:** Regularly check the status of client secrets and other credentials to prevent expiration-related issues.  
3. **Use IP Address for Troubleshooting:** If DNS resolution fails, use the IP address for AD connections.  
4. **Document Changes:** Maintain detailed records of configuration changes for future reference.  
5. **Enable Alerts:** Implement alerts for synchronization failures and credential expirations.  
6. **Test After Changes:** Conduct thorough testing after any configuration updates to ensure functionality.  

---

## Advanced Topics
### Handling Large-Scale Synchronization Failures
For environments with complex AD structures or large user bases, synchronization failures may require advanced troubleshooting, such as querying logs, analyzing database entries, or implementing custom scripts to validate configurations. Contact Netwrix support for assistance with such scenarios.  

---  
End of Article.