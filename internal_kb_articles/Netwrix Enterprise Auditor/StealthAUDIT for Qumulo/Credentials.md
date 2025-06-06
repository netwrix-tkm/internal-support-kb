# Knowledge Base Reference Guide: Troubleshooting Credential Issues in StealthAUDIT for Qumulo

## Overview

This guide focuses on troubleshooting credential-related issues in StealthAUDIT for Qumulo within Netwrix Enterprise Auditor. Credential issues can prevent scans from functioning correctly, impacting data collection and analysis. Understanding and resolving these problems is critical to ensuring seamless integration and accurate auditing of Qumulo NAS systems.

## Technical Background

### Key Concepts
- **StealthAUDIT for Qumulo**: A component of Netwrix Enterprise Auditor designed to perform scans and collect data from Qumulo NAS systems.
- **Access Analyzer Scans**: These scans require specific permissions to access and analyze data on Qumulo NAS nodes.
- **Collection Account**: The account used by StealthAUDIT to authenticate and perform scans on target systems.
- **Data-Administrators Role**: A Qumulo-specific role that grants permissions necessary for Access Analyzer scans.

### System Context
- **Qumulo NAS**: A scalable file storage system that requires precise permission configurations for external tools like StealthAUDIT to interact with its nodes.
- **Permissions**: Proper configuration of permissions on all nodes of the Qumulo NAS is essential for successful scans. Missing permissions can lead to scan failures.

## Issue Recognition & Triage

### Symptoms
- Scans for Qumulo NAS fail while scans for other systems (e.g., NAM) function correctly.
- Error messages indicating authentication or permission issues may appear in logs.

### Priority Assessment
- **High Priority**: Credential issues that prevent scans from functioning entirely.
- **Medium Priority**: Partial scan failures or degraded performance due to insufficient permissions.

## Diagnostic Methodology

### Systematic Approach
1. **Verify Scan Configuration**: Confirm that the scan settings in StealthAUDIT are correctly configured for the Qumulo NAS target.
2. **Check Permissions**: Review the permissions assigned to the collection account on all Qumulo NAS nodes.
3. **Analyze Logs**: Examine scan logs for error messages related to authentication or access issues.
4. **Test Connectivity**: Use test credentials to verify connectivity and permissions on the Qumulo NAS.

### Decision Points
- If permissions are missing, proceed to grant the required roles.
- If permissions are correct but scans still fail, escalate for deeper investigation.

## Information Collection

### Customer Queries
- What error messages are displayed during the scan failure?
- Has the collection account been configured with the necessary permissions on all Qumulo NAS nodes?
- Are other systems experiencing similar issues, or is this isolated to Qumulo NAS?

### Logs and Data
- **Scan Logs**: Collect logs from StealthAUDIT to identify authentication or access errors.
- **Permission Details**: Request screenshots or documentation of the collection account's permissions on Qumulo NAS nodes.
- **Environment Details**: Confirm the product version, build number, and Qumulo NAS configuration.

## Common Scenarios & Solutions

### Scenario 1: Missing Permissions
- **Symptoms**: Scan fails with errors indicating insufficient permissions.
- **Resolution**: Grant "Group membership in the Data-Administrators role" to the collection account on all Qumulo NAS nodes.

### Scenario 2: Incorrect Role Assignment
- **Symptoms**: Permissions are assigned, but the collection account is not part of the correct role.
- **Resolution**: Verify and adjust the role assignment to ensure the collection account is part of the Data-Administrators role.

### Scenario 3: Node-Specific Configuration Issues
- **Symptoms**: Scans succeed on some nodes but fail on others.
- **Resolution**: Ensure permissions are consistently applied across all nodes of the Qumulo NAS.

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000OJjzkIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OJjzkIAD/view)
#### Initial Symptoms
The customer reported that scans for Qumulo NAS were failing, while scans for other systems were functioning correctly.

#### Diagnostic Steps
1. Reviewed permissions required for Access Analyzer scans.
2. Identified that the collection account lacked "Group membership in the Data-Administrators role."
3. Confirmed that permissions needed to be granted on both nodes of the Qumulo NAS.

#### Key Information Leading to Resolution
- The collection account did not have the necessary permissions on all nodes.
- The "Group membership in the Data-Administrators role" was identified as a missing requirement.

#### Resolution
Granted the required permissions to the collection account on both nodes of the Qumulo NAS. Verified that the scan was operational after the adjustment.

#### Key Takeaways
- Always verify permissions on all nodes of the Qumulo NAS.
- Reference the [Qumulo Target Requirements](https://helpcenter.netwrix.com/bundle/AccessAnalyzer_12.0/page/Content/Config/Qumulo/Overview.htm) for detailed permission guidelines.

#### Efficiency Improvements
- Create a checklist for verifying permissions during initial scan setup.
- Develop automated scripts to test connectivity and permissions across all nodes.

## Best Practices & Tips

1. **Permission Verification**: Always confirm that the collection account has the required permissions on all nodes of the Qumulo NAS.
2. **Documentation Reference**: Use the [Qumulo Target Requirements](https://helpcenter.netwrix.com/bundle/AccessAnalyzer_12.0/page/Content/Config/Qumulo/Overview.htm) as a definitive guide for permission configurations.
3. **Customer Communication**: Clearly explain the importance of permissions and provide step-by-step instructions for granting them.
4. **Proactive Monitoring**: Implement regular checks to ensure permissions remain intact and scans continue to function correctly.
5. **Efficiency Tools**: Develop scripts or tools to automate permission checks and connectivity tests.

## Escalation Guidelines

### Criteria for Escalation
- Permissions are correctly configured, but scans still fail.
- Errors indicate potential bugs or compatibility issues with the Qumulo NAS version.
- Customer environment includes complex configurations requiring advanced troubleshooting.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Collect relevant logs and configuration details.
3. Submit the case to Tier 2 or Development teams with a detailed summary of the issue and actions taken.

End of Document.