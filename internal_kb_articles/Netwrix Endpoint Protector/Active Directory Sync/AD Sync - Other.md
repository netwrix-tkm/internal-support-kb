# Netwrix Endpoint Protector: Active Directory Sync - Troubleshooting Guide

## Overview
The Active Directory (AD) Sync feature in Netwrix Endpoint Protector (EPP) enables seamless integration with on-premise or cloud-based Active Directory environments, allowing for user and group synchronization. This feature is critical for managing user access, applying policies, and maintaining accurate device and user data. However, various issues can arise during configuration, synchronization, or operation, leading to challenges such as stale data, failed syncs, or misconfigured settings.

This guide provides a comprehensive overview of common issues, troubleshooting steps, root causes, and tested solutions for resolving problems related to the AD Sync feature.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Stale devices reappearing in EPP | Deleted devices reappear after sync | Verify server version and sync settings | Upgrade server and apply hotfixes | [Stale Devices Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ctc8zIAB/view) |
| AD binding fails due to invalid credentials | "Bind to Active Directory failed" error | Verify credentials and connection ports | Correct credentials and retry | [AD Binding Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CUFltIAH/view) |
| AD group not found during sync | "Group not found or no users present in group!" error | Verify domain name format and group syntax | Correct domain name format | [Group Not Found](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DElduIAD/view) |
| Unable to apply group filter | All groups are synced instead of filtered ones | Verify filter syntax and documentation | Use correct filter syntax | [Group Filter Syntax Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E79xmIAB/view) |
| Azure AD sync stops granting access | Security group members lose access | Check MTP settings and AD authentication | Re-enable MTP and reconfigure settings | [Azure AD Sync Access Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EjEtBIAV/view) |
| "Domain Users" group not syncing | Group not visible in user list | Verify group type and sync settings | Use custom classes for access | [Domain Users Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EqcAoIAJ/view) |
| AD connection fails for admin import | Connection works for machines but not admins | Verify group name and connection syntax | Correct group name in settings | [Admin Import Connection Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FPPiXIAX/view) |
| AD authentication fails | Users cannot authenticate | Verify AD location and group names | Correct location and group settings | [AD Authentication Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FPTMNIA5/view) |
| Deleted users cannot be re-added | Sync fails for previously deleted users | Check database for deleted user entries | Clear deleted entries from database | [Deleted Users Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G9IhIIAV/view) |
| SSL certificate setup confusion | No CSR option in DLP server | Confirm SSL certificate limitations | Generate CSR externally and import | [SSL Certificate Setup](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GaDqLIAV/view) |
| Manual policy application inefficiency | Policies not applied automatically | Review Azure AD sync configuration | Configure auto-policy application | [Policy Automation Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GAqvPIAT/view) |
| AD Admin Group sync fails | Admin group not syncing correctly | Verify group name and configuration | Correct configuration and retry | [Admin Group Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GBKOpIAP/view) |
| SaaS integration with on-prem AD | Customer unsure about integration | Confirm connector requirement | Use on-prem connector for sync | [SaaS Integration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HBzJLIA1/view) |
| Password expired error during login | Users cannot log in despite valid passwords | Check appliance password policy | Disable enforced password change | [Password Expired Error](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HfBvPIAV/view) |
| Unable to add new EPP admin via AD Sync | Error adding new admin to AD group | Verify sync settings and permissions | Correct configuration and retry | [Add New Admin Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JdzDZIAZ/view) |
| Missing user in admin panel | User not visible after sync | Check database flags for user | Update database flags to active | [Missing User Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MIcyHIAT/view) |
| New AD group not syncing | Group not appearing in Device Control | Recreate AD sync configuration | Delete and recreate sync settings | [New Group Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O35VFIAZ/view) |
| New AD admins not appearing | New admins not visible after sync | Check for duplicate database entries | Remove duplicates and retry sync | [New Admins Sync Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O8l0kIAB/view) |

---

## Detailed Issues

### Stale Devices Reappearing in EPP
**Symptoms:** Deleted devices reappear in the EPP console after synchronization.  
**Troubleshooting Steps:**
1. Verify if the EPP agent was uninstalled from the deleted devices.
2. Check the "Last seen" column in the Device Control -> Computers section.
3. Confirm synchronization settings with Azure AD.
4. Investigate server version and applied hotfixes.  
**Root Cause:** Outdated server version caused improper handling of device removal.  
**Solution:** Upgrade the EPP server to the latest version and apply hotfixes.  
**Source Ticket:** [Stale Devices Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ctc8zIAB/view)

---

### AD Binding Fails Due to Invalid Credentials
**Symptoms:** Error message: "Bind to Active Directory failed. Check the login credentials and/or server details."  
**Troubleshooting Steps:**
1. Verify credentials used for AD binding.
2. Test connection using ports 389 (LDAP) and 636 (LDAPS).
3. Confirm AD settings and retry binding.  
**Root Cause:** Incorrect login credentials or misconfigured settings.  
**Solution:** Correct the credentials and ensure proper configuration.  
**Source Ticket:** [AD Binding Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CUFltIAH/view)

---

### AD Group Not Found During Sync
**Symptoms:** Error message: "Group not found or no users present in group!"  
**Troubleshooting Steps:**
1. Verify group name syntax (pure name, Canonical Name, Distinguished Name).
2. Check domain name format in AD authentication settings.  
**Root Cause:** Incorrect domain name format in AD settings.  
**Solution:** Update domain name format to "DC=domain,DC=com".  
**Source Ticket:** [Group Not Found](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DElduIAD/view)

---

### Unable to Apply Group Filter
**Symptoms:** All groups are synced instead of filtered ones.  
**Troubleshooting Steps:**
1. Verify filter syntax in Directory Services settings.
2. Consult documentation for correct syntax examples.  
**Root Cause:** Incorrect or unclear filter syntax.  
**Solution:** Use the correct syntax for group filtering.  
**Source Ticket:** [Group Filter Syntax Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E79xmIAB/view)

---

## Best Practices
- **Regular Updates:** Keep the EPP server updated to the latest version to benefit from bug fixes and improvements.
- **Verify Settings:** Double-check all AD sync configurations, including credentials, group names, and domain formats.
- **Monitor Sync Logs:** Regularly review synchronization logs for errors or warnings.
- **Database Maintenance:** Periodically clean up deleted entries in the database to prevent conflicts.
- **Documentation:** Refer to official documentation for syntax examples and configuration guidelines.

---

## Advanced Topics
### Handling Duplicate Database Entries
If duplicate entries in the database prevent synchronization:
1. Query the database for duplicates:
   ```sql
   SELECT * FROM sf_guard_user WHERE deleted = 1;
   DELETE FROM sf_guard_user WHERE deleted = 1;
   ```
2. Restart the MySQL service and retry synchronization.

### Integrating SaaS with On-Prem AD
For cloud-hosted EPP integration with on-prem AD:
- Deploy an on-prem connector to facilitate synchronization.
- Follow the provided documentation for setup and configuration.

