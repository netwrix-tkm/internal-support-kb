# Knowledge Base Reference Guide: Troubleshooting Data Collection Issues in StealthAUDIT for SQL

## Overview
This guide provides a comprehensive reference for troubleshooting data collection issues in the StealthAUDIT for SQL component of Netwrix Enterprise Auditor. It is designed to help support engineers systematically diagnose and resolve common problems related to SQL data collection, ensuring consistent and effective customer support. Understanding these issues is critical for maintaining the reliability of SQL data collection processes, which are essential for auditing and compliance.

---

## Technical Background
### Key Concepts
- **StealthAUDIT for SQL**: A component of Netwrix Enterprise Auditor designed to collect and analyze SQL Server data for auditing purposes.
- **Data Collection Jobs**: Automated tasks that gather information from SQL servers, such as permissions, configurations, and activity logs.
- **Host List**: A configuration that specifies the SQL servers targeted for data collection.
- **FQDN (Fully Qualified Domain Name)**: The complete domain name for a specific computer or host on the network.
- **Timeout Settings**: Parameters that define how long a job will wait for a response before failing.
- **Dynamic Host Lists**: Automatically updated lists of SQL servers based on discovery jobs.

### Common Components
- **SQL Instance Discovery Job**: Identifies SQL servers in the environment.
- **SQL Collection Jobs**: Perform specific data collection tasks, such as permissions scans or activity monitoring.
- **CyberArk Integration**: A password management system that can be used with StealthAUDIT for secure credential storage.

---

## Issue Recognition & Triage
### Symptoms
- Host mismatch errors during SQL collection scans.
- SQL data not being reliably collected or jobs failing with errors.
- Excessively long scan durations for large-scale SQL environments.
- Jobs aborting mid-execution without generating logs.
- Transport-level errors and execution timeouts during SQL activity scans.

### Priority Assessment
- **High Priority**: Jobs failing without logs, critical data not being collected, or errors affecting multiple SQL servers.
- **Medium Priority**: Performance issues, such as long scan durations or intermittent errors.
- **Low Priority**: Configuration-related issues that do not impact critical operations.

---

## Diagnostic Methodology
1. **Initial Assessment**
   - Review the problem description and environment details provided by the customer.
   - Categorize the issue based on symptoms and priority.

2. **Connectivity Verification**
   - Use tools like `ping` and `nslookup` to confirm network connectivity to SQL servers.
   - Verify that the correct FQDNs are being used.

3. **Log Analysis**
   - Request and review job logs to identify specific errors or patterns.
   - Look for indications of deadlocks, timeout errors, or permission issues.

4. **Configuration Review**
   - Check host list settings, timeout configurations, and firewall rules.
   - Validate integration settings (e.g., CyberArk) if applicable.

5. **Testing & Validation**
   - Apply configuration changes or hotfixes as needed.
   - Monitor job performance and error rates after adjustments.

---

## Information Collection
### Questions to Ask Customers
- What specific errors or symptoms are being observed?
- Are there any recent changes to the environment (e.g., network, permissions)?
- What version of StealthAUDIT for SQL is being used?
- Are there any third-party integrations (e.g., CyberArk) in use?

### Data to Collect
- Job logs and error messages.
- Screenshots of configuration settings.
- Results of `ping` and `nslookup` commands for affected servers.
- Details of firewall rules and SQL server permissions.

---

## Common Scenarios & Solutions
### Scenario 1: Host Mismatch Errors
- **Symptoms**: Target host name changes during SQL collection scans.
- **Root Cause**: Incorrect configuration in the host list settings.
- **Solution**: Rebuild the host list using FQDNs instead of host names. Ensure the "use Host name" option is selected in the target settings.  
  [Example Case: Wipro - Ticket ID 500Qk00000C2N3IIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C2N3IIAV/view)

### Scenario 2: SQL Data Not Collected
- **Symptoms**: SQL jobs fail due to login errors or network issues.
- **Root Cause**: Misconfigured permissions and firewall settings.
- **Solution**: Correct firewall rules, enable SQL services on appropriate protocols, and create a dynamic SQL host list for automated discovery.  
  [Example Case: Eglin Federal Credit Union - Ticket ID 500Qk00000IdtqJIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IdtqJIAR/view)

### Scenario 3: Long Scan Durations
- **Symptoms**: SQL scans take excessively long to complete.
- **Root Cause**: Attempting to scan too many SQL servers simultaneously.
- **Solution**: Break scans into smaller groups and use filtering options to exclude unnecessary databases.  
  [Example Case: Allstate Insurance Company - Ticket ID 500Qk00000KgVVNIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KgVVNIA3/view)

### Scenario 4: Jobs Aborting Mid-Execution
- **Symptoms**: Jobs abort without logs; CyberArk password errors noted.
- **Root Cause**: Product defect causing deadlocks during scans of multiple SQL hosts.
- **Solution**: Apply the hotfix **Stealthaudit-hotfix-11.6.0.065** to resolve the defect.  
  [Example Case: Axos Bank - Ticket ID 500Qk00000L83eCIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000L83eCIAR/view)

### Scenario 5: Transport-Level Errors
- **Symptoms**: Execution timeouts and skipped audit files.
- **Root Cause**: Insufficient timeout settings for SQL jobs.
- **Solution**: Increase the command timeout setting in the job configuration XML.  
  [Example Case: Oak Hill Advisors - Ticket ID 500Qk00000LWd5PIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LWd5PIAT/view)

---

## Detailed Case Studies
### Case Study 1: Host Mismatch Errors
- **Initial Symptoms**: Host name changes during scans.
- **Diagnostic Steps**: Verified FQDN settings and tested new configurations.
- **Resolution**: Rebuilt host list using FQDNs.  
  [Full Case Details](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C2N3IIAV/view)

### Case Study 2: SQL Data Not Collected
- **Initial Symptoms**: Login failures and unresponsive SQL servers.
- **Diagnostic Steps**: Reviewed logs, corrected firewall rules, and created a dynamic host list.
- **Resolution**: Automated discovery and targeted SQL jobs resolved the issue.  
  [Full Case Details](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IdtqJIAR/view)

### Case Study 3: Long Scan Durations
- **Initial Symptoms**: Scans running for over 30 days.
- **Diagnostic Steps**: Analyzed job statistics and recommended breaking scans into smaller groups.
- **Resolution**: Reduced scan size and applied filtering options.  
  [Full Case Details](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KgVVNIA3/view)

### Case Study 4: Jobs Aborting Mid-Execution
- **Initial Symptoms**: Jobs aborting without logs; CyberArk errors noted.
- **Diagnostic Steps**: Reviewed logs and applied a hotfix to address the defect.
- **Resolution**: Hotfix resolved the issue without reconfiguration.  
  [Full Case Details](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000L83eCIAR/view)

### Case Study 5: Transport-Level Errors
- **Initial Symptoms**: Timeout errors during SQL activity scans.
- **Diagnostic Steps**: Increased command timeout settings in job configuration.
- **Resolution**: Adjusted timeout resolved the issue.  
  [Full Case Details](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LWd5PIAT/view)

---

## Best Practices & Tips
- Always use FQDNs in host lists to avoid connectivity issues.
- Regularly review and update dynamic host lists to reflect changes in the environment.
- Monitor timeout settings and adjust them based on the complexity of SQL operations.
- Break large-scale scans into smaller groups to improve performance and manageability.
- Apply hotfixes promptly to address known defects and improve system stability.
- Communicate clearly with customers, ensuring they understand the steps being taken and the expected outcomes.

---

## Escalation Guidelines
- **When to Escalate**:
  - Persistent issues after applying standard solutions.
  - Errors indicating potential product defects.
  - Complex configurations requiring advanced expertise.
- **How to Escalate**:
  - Document all troubleshooting steps and findings.
  - Provide detailed logs, screenshots, and environment details.
  - Submit the case to the appropriate regional or product-specific escalation team.