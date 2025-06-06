# Netwrix Enterprise Auditor Knowledge Base: StealthAUDIT for AzureAD Configuration Issues

## Overview
This guide focuses on troubleshooting and resolving configuration issues related to StealthAUDIT for AzureAD within Netwrix Enterprise Auditor. These issues typically involve problems with inventory jobs, group membership visibility, or auditing configurations for Microsoft Entra ID. Understanding and addressing these issues is critical for ensuring accurate data collection, reporting, and compliance.

## Technical Background
StealthAUDIT for AzureAD is a component of Netwrix Enterprise Auditor designed to collect and analyze data from Azure Active Directory (Azure AD). Key features include inventory jobs for group memberships, user data, and auditing configurations for Microsoft Entra ID. Proper configuration of inventory jobs and auditing connections is essential for accurate data retrieval and reporting.

### Key Concepts
- **Azure AD Inventory Job**: A scheduled task that collects data from Azure AD, including group memberships and user information.
- **Active Inventory Console (AIC)**: A dashboard that displays collected inventory data.
- **ADInventory_GroupView**: A database view that lists groups retrieved from Azure AD.
- **AzureADInventory_GroupMembersView**: A database view that lists group membership details.
- **Microsoft Entra ID Auditing**: A feature that enables auditing of Azure AD activities, requiring specific configuration steps.

## Issue Recognition & Triage
### Symptoms
- Missing groups or group memberships in inventory views (e.g., ADInventory_GroupView).
- Discrepancies between data displayed in the Active Inventory Console and database views.
- Customer confusion regarding configuration steps for Microsoft Entra ID Auditing.

### Priority Assessment
- **High Priority**: Issues affecting critical reporting or compliance data.
- **Medium Priority**: Configuration-related queries that do not impact immediate functionality.
- **Low Priority**: General guidance requests or minor discrepancies.

## Diagnostic Methodology
1. **Verify Symptoms**: Confirm the issue reported by the customer (e.g., missing groups or unclear configuration steps).
2. **Check Configuration**: Review the setup of Azure AD Inventory jobs or auditing connections.
3. **Run Tests**: Execute full inventory scans or test auditing connections to identify discrepancies.
4. **Analyze Logs**: Examine relevant database views and logs for errors or missing data.
5. **Confirm Resolution**: Ensure the issue is resolved and data is accurately reflected.

## Information Collection
### Questions to Ask Customers
- What specific data or groups are missing?
- Have any recent changes been made to Azure AD or inventory job configurations?
- Are there any error messages or logs available?

### Logs and Data to Collect
- **Inventory Job Logs**: Logs from Azure AD Inventory jobs.
- **Database Views**: Data from ADInventory_GroupView and AzureADInventory_GroupMembersView.
- **Configuration Details**: Screenshots or descriptions of current auditing or inventory job settings.

## Common Scenarios & Solutions
### Scenario 1: Missing Groups in Inventory Views
#### Symptoms
Groups appear in the Active Inventory Console but are missing from ADInventory_GroupView.

#### Resolution Steps
1. Verify the presence of groups in Azure AD.
2. Check the configuration of the Azure AD Inventory job.
3. Assign the correct host to the inventory job.
4. Run a full Azure AD Inventory scan.
5. Confirm group membership data in AzureADInventory_GroupMembersView.

### Scenario 2: Microsoft Entra ID Auditing Configuration Guidance
#### Symptoms
Customer requests assistance with configuring auditing for Microsoft Entra ID.

#### Resolution Steps
1. Review the official documentation: [Microsoft Entra ID Auditing Configuration](https://helpcenter.netwrix.com/bundle/EnterpriseAuditor_11.6/page/Content/Config/EntraID/Access.htm).
2. Ensure prerequisites are met (e.g., permissions, API access).
3. Guide the customer through each configuration step.
4. Test the connection to confirm successful setup.

## Detailed Case Studies
### Case Study 1: Missing Groups in Inventory Views
#### Ticket Reference: [500Qk00000H9QT3IAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H9QT3IAN/view)
- **Initial Symptoms**: Groups visible in the Active Inventory Console were missing from ADInventory_GroupView.
- **Diagnostic Steps**:
  1. Verified group presence in Azure AD.
  2. Checked Azure AD Inventory job configuration.
  3. Assigned the host to the inventory job and ran a full scan.
- **Key Information**: The Azure AD Inventory job was not set up correctly.
- **Resolution**: Configured the inventory job properly and executed a full scan.
- **Takeaways**: Always verify inventory job configuration and run full scans to ensure data accuracy.

### Case Study 2: Microsoft Entra ID Auditing Configuration Guidance
#### Ticket Reference: [500Qk00000IgyNDIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IgyNDIAZ/view)
- **Initial Symptoms**: Customer requested guidance on auditing configuration.
- **Diagnostic Steps**:
  1. Reviewed documentation and prerequisites.
  2. Walked the customer through configuration steps.
- **Key Information**: Lack of clarity on configuration steps was the root cause.
- **Resolution**: Provided detailed guidance and ensured successful setup.
- **Takeaways**: Familiarize customers with documentation and prerequisites before starting configuration.

## Best Practices & Tips
- **Inventory Job Configuration**: Regularly review and test inventory job settings to ensure accurate data collection.
- **Documentation Familiarity**: Encourage customers to consult official documentation for configuration guidance.
- **Proactive Communication**: Schedule follow-ups to confirm issue resolution and address any lingering concerns.
- **Log Analysis**: Use database views and logs to pinpoint discrepancies and validate solutions.
- **Training**: Provide training resources to customers for self-service troubleshooting and configuration.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist despite following resolution steps.
- Errors indicate potential bugs or system limitations.
- Customer requires advanced configuration assistance beyond standard documentation.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Collect relevant logs and configuration details.
3. Submit a detailed escalation request to the appropriate team.
4. Communicate escalation status and expected timelines to the customer.