# Knowledge Base Reference Guide: Troubleshooting Domain Issues in StealthAUDIT for Active Directory

## Overview
This guide focuses on troubleshooting domain-related issues in the StealthAUDIT for Active Directory component of Netwrix Enterprise Auditor. These issues typically involve problems with domain configuration, trust relationships, authentication, and data collection across multiple domains. Understanding and resolving these issues is critical for ensuring accurate reporting and seamless functionality in environments with complex Active Directory setups.

## Technical Background
### Key Concepts
- **Active Directory Domains**: Logical groupings within an Active Directory forest that manage resources and security boundaries.
- **Trust Relationships**: Mechanisms that allow domains to authenticate users and access resources across boundaries.
- **Kerberos Authentication**: A secure method for authenticating requests between systems, often used in cross-domain communication.
- **UNC Hardening**: Security settings that enforce authentication and integrity requirements for accessing network shares.

### System Context
StealthAUDIT for Active Directory relies on service accounts and trust relationships to collect data from multiple domains. Issues often arise due to misconfigurations in trust relationships, permissions, or hardened security settings that block communication between domains.

## Issue Recognition & Triage
### Symptoms
- Missing domains in Active Directory reports.
- Failed data collection jobs for specific domains.
- Authentication errors when accessing resources across domains.
- Inability to retrieve Group Policy Object (GPO) collections.

### Priority Assessment
- **High Priority**: Issues affecting critical reporting or data collection across multiple domains.
- **Medium Priority**: Problems limited to non-critical domains or features.
- **Low Priority**: Configuration questions or minor discrepancies in reporting.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Domain Configuration**: Ensure all domains are listed in the host list and properly configured.
2. **Check Trust Relationships**: Confirm 2-way trust relationships between domains.
3. **Review Authentication Settings**: Investigate Kerberos authentication and UNC hardening settings.
4. **Analyze Logs**: Examine job logs for errors or authentication failures.
5. **Test Connectivity**: Use tools like `ping`, `nslookup`, and `Test-ComputerSecureChannel` to verify domain communication.
6. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.

### Decision Points
- If trust relationships are misconfigured, focus on resolving them first.
- If authentication errors persist, investigate registry settings and permissions.
- If the issue is isolated to specific domains, narrow troubleshooting to those domains.

## Information Collection
### Customer Queries
- How many domains are configured in Active Directory?
- Are there 2-way trust relationships between all domains?
- Are there any hardened security policies in place (e.g., UNC hardening)?
- What error messages are displayed during job execution?

### Data to Collect
- Screenshots of the host list configuration.
- Job logs from successful and failed runs.
- Registry settings related to UNC hardening.
- Details of service account permissions and trust relationships.

## Common Scenarios & Solutions
### Scenario 1: Missing Domains in Reports
#### Symptoms
- Only a subset of configured domains appears in Active Directory reports.

#### Resolution Steps
1. Verify that all domains are listed in the host list.
2. Check trust relationships between service accounts and domains.
3. Confirm that service accounts have appropriate permissions.
4. Test connectivity between the Netwrix server and the missing domains.

#### Key Takeaways
Proper trust relationships and permissions are essential for accurate reporting.

### Scenario 2: Failed GPO Collections Across Domains
#### Symptoms
- GPO collections fail for domains without trust relationships.

#### Resolution Steps
1. Relax UNC hardening settings on the Netwrix server:
   - Set `RequireMutualAuthentication=0`.
   - Set `RequireIntegrity=0`.
   - Set `RequirePrivacy=1`.
2. Test GPO collections after adjusting registry settings.
3. Confirm Kerberos authentication settings and permissions.

#### Key Takeaways
UNC hardening settings can block cross-domain communication; adjust them cautiously.

## Detailed Case Studies
### Case Study 1: Missing Domains in Reports
#### Ticket ID: [500Qk00000CJYVKIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CJYVKIA5/view)
- **Symptoms**: Out of five domains, only two appeared in reports.
- **Diagnostic Steps**:
  1. Verified host list configuration.
  2. Investigated trust relationships between domains.
  3. Reviewed job exports and screenshots.
- **Resolution**: Customer corrected configuration on their end.
- **Key Takeaways**:
  - Trust relationships are critical for cross-domain reporting.
  - Ensure service accounts have proper permissions.

### Case Study 2: Failed GPO Collections
#### Ticket ID: [500Qk00000J2xVkIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000J2xVkIAJ/view)
- **Symptoms**: GPO collections failed due to hardened UNC settings.
- **Diagnostic Steps**:
  1. Reviewed job logs and identified Kerberos authentication issues.
  2. Relaxed UNC hardening settings in the registry.
  3. Conducted tests to confirm resolution.
- **Resolution**: Adjusted UNC hardening settings to allow access.
- **Key Takeaways**:
  - Hardened security settings can block communication; adjust cautiously.
  - Cross-domain access requires careful configuration of permissions and authentication.

## Best Practices & Tips
- **Trust Relationships**: Always verify 2-way trust relationships between domains before running reports.
- **Service Account Permissions**: Ensure service accounts have the necessary permissions for data collection.
- **UNC Hardening**: Adjust UNC hardening settings only when necessary, and document changes for security audits.
- **Logs and Screenshots**: Collect detailed logs and screenshots to expedite troubleshooting.
- **Customer Communication**: Clearly explain the technical reasoning behind solutions and provide actionable steps.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist after verifying trust relationships and permissions.
- Authentication errors cannot be resolved with registry adjustments.
- Problems involve potential product defects or require development team input.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Include relevant logs, screenshots, and configuration details.
3. Submit the case to Tier 3 support or the development team with a detailed summary.

End of Document.