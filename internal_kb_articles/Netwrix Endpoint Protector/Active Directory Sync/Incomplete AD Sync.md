# Knowledge Base Reference Guide: Troubleshooting Incomplete Active Directory Sync in Netwrix Endpoint Protector

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to incomplete Active Directory (AD) synchronization in Netwrix Endpoint Protector (EPP). AD sync is a critical feature that ensures seamless integration between the Endpoint Protector appliance and an organization's Active Directory, enabling centralized user and group management. Understanding and resolving AD sync issues is essential to maintaining system functionality and user access.

## Technical Background
### Key Concepts
- **Active Directory Sync**: A process that imports users and groups from an organization's AD into the Endpoint Protector system.
- **AD Connector**: The configuration that establishes communication between the Endpoint Protector appliance and the AD server.
- **User-Group Associations**: Relationships between users and groups in AD that are mirrored in Endpoint Protector.
- **Password Policies**: Settings that determine password expiration and reset requirements for users.

### System Context
- **Netwrix Endpoint Protector**: A data security solution that relies on AD sync for user and group management.
- **Sync Behavior**: AD sync can be configured to import users, groups, and their associations. Any discrepancies in this process can lead to incomplete or incorrect data in Endpoint Protector.
- **Common Components**: Domain Controller (DC), AD connector, Endpoint Protector appliance, and synchronization logs.

## Issue Recognition & Triage
### Symptoms
- Random or incorrect user-group associations.
- Users deleted from Endpoint Protector not being re-imported during subsequent syncs.
- Password reset issues for AD-synced users.
- Groups not syncing properly, leading to incomplete policy application.
- Specific users missing from the admin list despite being part of synced groups.

### Priority Assessment
- **High Priority**: Issues affecting user authentication, admin access, or critical policy enforcement.
- **Medium Priority**: Problems with group memberships or non-critical user accounts.
- **Low Priority**: Cosmetic or non-urgent discrepancies in user-group associations.

## Diagnostic Methodology
### Systematic Approach
1. **Verify AD Connector Configuration**:
   - Confirm the connection to the Domain Controller is successful.
   - Check the AD connector settings for accuracy.
2. **Review Sync Logs**:
   - Analyze logs for errors or warnings during the sync process.
3. **Validate User-Group Data**:
   - Cross-check user and group memberships in AD and Endpoint Protector.
4. **Test Sync Behavior**:
   - Perform manual syncs and observe the results.
5. **Replicate the Issue**:
   - Attempt to reproduce the problem in a controlled environment.
6. **Consult Documentation and Previous Cases**:
   - Reference known issues and solutions for similar scenarios.

## Information Collection
### Customer Questions
- What specific issue are you experiencing with AD sync?
- Are all users/groups affected, or only specific ones?
- Have there been any recent changes to your AD configuration?
- Are you using any custom policies or settings in Endpoint Protector?

### Data to Collect
- AD connector configuration details.
- Sync logs from the Endpoint Protector appliance.
- Screenshots of affected users/groups in AD and Endpoint Protector.
- Details of any recent updates or changes to the system.

## Common Scenarios & Solutions
### Scenario 1: Random User-Group Associations
- **Symptoms**: Users appear in incorrect groups after sync.
- **Resolution**: Reconfigure the AD connector and delete existing users/groups in Endpoint Protector before re-syncing. Ensure the AD structure is correctly mapped. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dr1WLIAZ/view)

### Scenario 2: Deleted Users Not Re-Imported
- **Symptoms**: Users deleted from Endpoint Protector are not re-imported during subsequent syncs.
- **Resolution**: Restore deleted users from the backend or ensure the AD connector is configured to re-import deleted users. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Fom8rIAB/view)

### Scenario 3: Password Reset Issues for AD-Synced Users
- **Symptoms**: AD-synced users cannot reset passwords due to missing "old password."
- **Resolution**: Disable the "ignore AD authentication" setting and adjust password expiration policies to "never expire." [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GCMI8IAP/view)

### Scenario 4: Groups Not Syncing Properly
- **Symptoms**: Policies applied to groups do not include all users.
- **Resolution**: Investigate user login behavior and ensure group memberships are correctly configured in AD. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H4yv5IAB/view)

### Scenario 5: Missing Admin Users
- **Symptoms**: Specific users do not appear as admins despite being part of synced groups.
- **Resolution**: Verify group memberships and restore deleted users from the backend. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hx9FCIAZ/view)

### Scenario 6: Incomplete User Sync
- **Symptoms**: Not all users in an AD group are imported into Endpoint Protector.
- **Resolution**: Check if the missing users were previously deleted from Endpoint Protector and restore them if necessary. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NrDUvIAN/view)

## Detailed Case Studies
### Case Study 1: Random User-Group Associations
- **Ticket**: [500Qk00000Dr1WLIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dr1WLIAZ/view)
- **Symptoms**: Random user-group associations after AD sync.
- **Key Diagnostic Steps**: Verified AD connector, reconfigured sync, consulted technical expert.
- **Resolution**: Issue resolved after customer confirmed adjustments were effective.
- **Takeaways**: Validate AD structure and sync settings during initial configuration.

### Case Study 2: Deleted Users Not Re-Imported
- **Ticket**: [500Qk00000Fom8rIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Fom8rIAB/view)
- **Symptoms**: Deleted users not re-imported during sync.
- **Key Diagnostic Steps**: Reviewed sync logs, restored users from backend.
- **Resolution**: Restored deleted users and re-synced successfully.
- **Takeaways**: Ensure deleted users are handled correctly in sync settings.

### Case Study 3: Password Reset Issues
- **Ticket**: [500Qk00000GCMI8IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GCMI8IAP/view)
- **Symptoms**: AD-synced users unable to reset passwords.
- **Key Diagnostic Steps**: Reviewed password policies, adjusted settings.
- **Resolution**: Disabled "ignore AD authentication" and set passwords to "never expire."
- **Takeaways**: Align password policies with AD sync configurations.

### Case Study 4: Groups Not Syncing Properly
- **Ticket**: [500Qk00000H4yv5IAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H4yv5IAB/view)
- **Symptoms**: Incomplete group sync for Content Aware Alerts.
- **Key Diagnostic Steps**: Verified group memberships, analyzed MySQL data.
- **Resolution**: Explained behavior caused by user switching devices.
- **Takeaways**: Monitor user login behavior for potential conflicts.

### Case Study 5: Missing Admin Users
- **Ticket**: [500Qk00000Hx9FCIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Hx9FCIAZ/view)
- **Symptoms**: Specific users missing from admin list.
- **Key Diagnostic Steps**: Verified group memberships, performed manual sync.
- **Resolution**: Restored users and re-synced successfully.
- **Takeaways**: Check for deleted users when troubleshooting missing accounts.

### Case Study 6: Incomplete User Sync
- **Ticket**: [500Qk00000NrDUvIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NrDUvIAN/view)
- **Symptoms**: Not all users in AD group imported.
- **Key Diagnostic Steps**: Observed behavior during remote session, restored deleted users.
- **Resolution**: Restored users and re-synced successfully.
- **Takeaways**: Always verify if missing users were previously deleted.

## Best Practices & Tips
- **Validate Configuration**: Ensure AD connector settings are accurate and tested during initial setup.
- **Monitor Logs**: Regularly review sync logs for errors or warnings.
- **Backup Before Changes**: Create backups or snapshots before modifying the Endpoint Protector appliance.
- **Align Policies**: Ensure password and group policies in Endpoint Protector align with AD settings.
- **Communicate Clearly**: Maintain open communication with customers to gather all relevant details.

## Escalation Guidelines
- **Escalate to Tier 2/3**:
  - If the issue persists after following standard troubleshooting steps.
  - If the root cause involves complex backend configurations or database issues.
- **Provide Detailed Documentation**:
  - Include logs, screenshots, and a summary of steps already taken.
- **Engage Development Team**:
  - For issues related to product bugs or feature limitations.