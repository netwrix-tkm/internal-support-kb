# Knowledge Base Reference Guide: Troubleshooting StealthAUDIT for Active Directory Configuration Issues

## Overview
This guide focuses on troubleshooting configuration-related issues in the StealthAUDIT for Active Directory component of Netwrix Enterprise Auditor. These issues often involve database constraints, LDAP configurations, query behaviors, and report inaccuracies. Understanding and resolving these problems is critical for ensuring seamless data collection, accurate reporting, and optimal system performance.

## Technical Background
### Key Concepts
- **StealthAUDIT for Active Directory**: A data collection tool within Netwrix Enterprise Auditor designed to gather information from Active Directory environments.
- **PRIMARY KEY Constraints**: Database rules that prevent duplicate entries in specific tables, ensuring data integrity.
- **LDAP (Lightweight Directory Access Protocol)**: A protocol used for accessing and maintaining distributed directory information services, such as Active Directory.
- **SSL (Secure Sockets Layer)**: A security protocol for encrypting data transmitted over networks, often used with LDAP.
- **Stale User Reports**: Reports generated to identify inactive or unused accounts in Active Directory based on configurable thresholds.

### System Context
StealthAUDIT interacts with Active Directory and databases to collect, store, and analyze data. Misconfigurations, product defects, or outdated versions can lead to issues such as constraint violations, incorrect query mappings, or inaccurate reporting.

## Issue Recognition & Triage
### Symptoms
- **Database Errors**: Messages indicating PRIMARY KEY constraint violations or duplicate key insertions.
- **Unexpected Query Behavior**: Data stored in incorrect tables or mismatched query results.
- **LDAP Configuration Questions**: Uncertainty about ports and services used by StealthAUDIT.
- **Report Inaccuracies**: Active users incorrectly flagged as stale.

### Priority Assessment
- **High Priority**: Issues causing data integrity problems (e.g., constraint violations).
- **Medium Priority**: Configuration-related inquiries or minor report inaccuracies.
- **Low Priority**: General questions about system behavior or documentation.

## Diagnostic Methodology
### Systematic Approach
1. **Error Identification**: Review error messages and logs to pinpoint the issue.
2. **Version Verification**: Check the software version for known defects or updates.
3. **Configuration Review**: Analyze job settings and thresholds for misconfigurations.
4. **Reproduction**: Attempt to replicate the issue in a controlled environment.
5. **Documentation Reference**: Consult internal and external documentation for guidance.
6. **Patch or Upgrade**: Apply relevant patches or upgrade to the latest version if necessary.

## Information Collection
### Customer Queries
- What is the exact error message or behavior observed?
- What version of Netwrix Enterprise Auditor is currently in use?
- Are there any recent changes to the configuration or environment?
- What troubleshooting steps have already been attempted?

### Logs and Data
- **Database Logs**: For constraint violations or query errors.
- **Job Configurations**: Exported settings for affected jobs.
- **Debug Logs**: Enabled logging for detailed analysis.
- **Screenshots or Reports**: Visual evidence of the issue.

## Common Scenarios & Solutions
### Scenario 1: PRIMARY KEY Constraint Violation
- **Symptoms**: Error message indicating duplicate key insertion into a database table.
- **Solution**: Upgrade to the latest version (e.g., from 11.5 to 11.6) to resolve product defects causing the issue.

### Scenario 2: LDAP Configuration Inquiry
- **Symptoms**: Questions about ports and services used by StealthAUDIT.
- **Solution**: Confirm LDAP usage over port 636 and provide documentation on additional Active Directory services and port requirements.

### Scenario 3: Incorrect Query Behavior
- **Symptoms**: Sites query results stored in the Trusts table when SSL is enabled.
- **Solution**: Apply the patch released in version 11.6.0.134 to correct the query behavior.

### Scenario 4: Stale User Report Inaccuracy
- **Symptoms**: Active users flagged as stale due to default inactivity threshold settings.
- **Solution**: Adjust the stale user inactivity threshold to align with customer requirements.

## Detailed Case Studies
### Case Study 1: PRIMARY KEY Constraint Violation
- **Ticket ID**: [500Qk00000FGEpeIAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FGEpeIAH/view)
- **Symptoms**: Duplicate key insertion error in the `dbo.SA_ADInventory_EffectiveGroupMembers` table.
- **Diagnostic Steps**:
  - Reviewed error message and database entries.
  - Investigated configuration settings and consulted documentation.
  - Upgraded from version 11.5 to 11.6.
- **Resolution**: Product defect resolved in version 11.6.
- **Key Takeaways**: Always verify software versions for known defects and apply updates promptly.

### Case Study 2: LDAP Configuration Inquiry
- **Ticket ID**: [500Qk00000GIp65IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GIp65IAD/view)
- **Symptoms**: Customer sought clarification on LDAP usage and port requirements.
- **Diagnostic Steps**:
  - Reviewed configuration and routing through F5 VIP.
  - Confirmed LDAP usage over port 636 and additional Active Directory services.
  - Provided relevant documentation links.
- **Resolution**: Issue resolved through clarification and documentation.
- **Key Takeaways**: Clear communication and documentation are essential for resolving configuration inquiries.

### Case Study 3: Incorrect Query Behavior
- **Ticket ID**: [500Qk00000M75ZOIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000M75ZOIAZ/view)
- **Symptoms**: Sites query results stored in the Trusts table when SSL was enabled.
- **Diagnostic Steps**:
  - Verified job configuration and observed behavior.
  - Reproduced issue in lab environment.
  - Identified product defect and applied patch.
- **Resolution**: Patch in version 11.6.0.134 resolved the issue.
- **Key Takeaways**: Reproducing issues in a lab environment helps confirm root causes.

### Case Study 4: Stale User Report Inaccuracy
- **Ticket ID**: [500Qk00000NAvHVIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NAvHVIA1/view)
- **Symptoms**: Active users flagged as stale due to default inactivity threshold.
- **Diagnostic Steps**:
  - Gathered details on affected users and impact.
  - Enabled debug logging and analyzed job configurations.
  - Adjusted inactivity threshold settings.
- **Resolution**: Threshold adjustment resolved the issue.
- **Key Takeaways**: Customizing default settings to customer needs prevents report inaccuracies.

## Best Practices & Tips
- **Version Management**: Regularly update Netwrix Enterprise Auditor to the latest version to avoid known defects.
- **Configuration Review**: Periodically audit job settings and thresholds to ensure alignment with customer requirements.
- **Documentation Utilization**: Leverage internal and external resources for troubleshooting and customer communication.
- **Lab Testing**: Reproduce issues in a controlled environment to confirm root causes.
- **Customer Communication**: Maintain clear and consistent communication to gather necessary information and provide timely updates.

## Escalation Guidelines
### Criteria for Escalation
- Issues unresolved after applying patches or updates.
- Problems requiring development team intervention (e.g., new product defects).
- High-impact issues affecting multiple customers or critical systems.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Gather relevant logs, configurations, and screenshots.
3. Submit a detailed escalation request to the development team or senior support engineers.
4. Communicate escalation status and expected timelines to the customer.