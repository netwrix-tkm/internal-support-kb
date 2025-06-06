# Troubleshooting Guide: Entra Collection Job Failures in Netwrix Enterprise Auditor

## Overview

This guide provides a systematic approach to diagnosing and resolving issues related to Entra collection job failures in Netwrix Enterprise Auditor (EA), specifically within the StealthAUDIT for AzureAD component. These issues often involve database connectivity, SQL execution errors, or configuration problems. Understanding and addressing these problems is critical to ensuring accurate inventory collection and maintaining system reliability.

---

## Technical Background

### Key Concepts
- **Entra Collection Jobs**: These are tasks within Netwrix EA designed to collect inventory data from Azure Active Directory (AAD) environments.
- **Connection Profiles**: Configuration settings that define how Netwrix EA connects to an Entra tenant.
- **SQL Execution**: The process by which Netwrix EA interacts with its database to store and retrieve data during job execution.
- **Secrets and Credentials**: Authentication tokens or keys required for secure communication with the Entra tenant.

### System Context
- **Netwrix Enterprise Auditor**: A platform for auditing and monitoring IT environments, including AzureAD.
- **StealthAUDIT for AzureAD**: A component of Netwrix EA focused on inventory collection and analysis for AzureAD.
- **Inventory Feature**: Collects detailed information about AzureAD objects, such as users, groups, and devices.

---

## Issue Recognition & Triage

### Symptoms
- Entra collection jobs fail consistently.
- Error messages in logs, such as:
  - `"PrepareTask for DC 'AZUREADINVENTORY' for task 'AAD Inventory' failed: Unspecified error."`
  - `"ExecuteScalar requires an open and available Connection. The connection's current state is closed."`
- SQL timeout errors during specific steps, such as "Adding Domain."

### Priority Assessment
- **High Priority**: If the failure impacts critical reporting or compliance requirements.
- **Medium Priority**: If the failure is isolated to non-critical jobs or environments.
- **Low Priority**: If the issue is intermittent and does not affect overall functionality.

---

## Diagnostic Methodology

### Step-by-Step Approach
1. **Verify Connection Profile**:
   - Confirm that the connection profile for the Entra tenant is current and valid.
   - Test connectivity to the Entra tenant using the Netwrix EA interface.

2. **Analyze Error Messages**:
   - Review logs for specific error messages.
   - Focus on SQL-related errors and timeout issues.

3. **Check SQL Server Health**:
   - Verify that the SQL Server hosting the Netwrix database is operational.
   - Check for resource constraints (CPU, memory, disk I/O).

4. **Monitor Execution Times**:
   - Identify steps in the job process that take longer than expected.
   - Pay special attention to the "Adding Domain" step.

5. **Review Secrets and Credentials**:
   - Ensure that all secrets and credentials used for Entra tenant access are up to date.

6. **Collect Debug Logs**:
   - Enable debug logging in Netwrix EA.
   - Gather logs for detailed analysis of failure points.

7. **Test with Clean Tables**:
   - As a last resort, drop and recreate relevant database tables (e.g., EntraID tables) to eliminate potential data corruption.

---

## Information Collection

### Questions to Ask Customers
- When did the issue first occur?
- Have there been any recent changes to the Entra tenant or connection profile?
- Are there any other Netwrix EA components experiencing issues?

### Logs and Data to Collect
- Debug logs from Netwrix EA.
- SQL Server logs, including error logs and execution plans.
- Event Viewer logs from the server hosting Netwrix EA.

---

## Common Scenarios & Solutions

### Scenario 1: Expired Secret
- **Symptoms**: Access denied errors in logs.
- **Resolution**: Update the secret in the connection profile and test connectivity.

### Scenario 2: SQL Timeout During "Adding Domain"
- **Symptoms**: Job fails with timeout errors during the "Adding Domain" step.
- **Resolution**:
  1. Optimize SQL Server performance (e.g., increase resources, tune queries).
  2. Drop and recreate the EntraID tables to resolve potential data corruption.

### Scenario 3: General Database Connectivity Issues
- **Symptoms**: Errors indicating closed or unavailable SQL connections.
- **Resolution**:
  1. Verify SQL Server availability and connectivity.
  2. Check for network issues between the Netwrix EA server and SQL Server.

---

## Detailed Case Studies

### Case Study: Ticket [500Qk00000KvlulIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KvlulIAB/view)
#### Initial Symptoms
- All Entra collection jobs failed with database connectivity and execution errors.
- SQL timeout occurred during the "Adding Domain" step.

#### Diagnostic Steps
1. Verified the connection profile and confirmed successful connectivity to the Entra tenant.
2. Analyzed error messages and identified SQL timeout issues.
3. Collected debug logs for further analysis.
4. Dropped EntraID tables as a last resort.

#### Resolution
- Dropped the EntraID tables, which resolved the timeout issues.
- Jobs completed successfully after the tables were recreated.

#### Key Takeaways
- Expired secrets can cause access issues; ensure they are regularly updated.
- SQL timeouts during specific steps may indicate data corruption or performance bottlenecks.
- Dropping and recreating tables can be an effective last resort but should be used cautiously.

#### Efficiency Improvements
- Implement proactive monitoring of job execution times to detect potential issues early.
- Automate secret expiration alerts to prevent access issues.

---

## Best Practices & Tips

1. **Monitor Job Execution Times**:
   - Regularly review execution times for critical steps, such as "Adding Domain."

2. **Maintain Secrets and Credentials**:
   - Use automated tools to track and renew secrets before they expire.

3. **Optimize SQL Server Performance**:
   - Allocate sufficient resources to the SQL Server hosting the Netwrix database.
   - Regularly review and optimize database queries.

4. **Enable Debug Logging**:
   - Use debug logs to gain deeper insights into job failures.

5. **Document Changes**:
   - Maintain a log of changes to the Entra tenant, connection profiles, and Netwrix EA configurations.

---

## Escalation Guidelines

### Criteria for Escalation
- Issue persists after following all troubleshooting steps.
- SQL Server performance issues cannot be resolved locally.
- Debug logs indicate a potential bug in Netwrix EA.

### Escalation Procedure
1. Gather all relevant logs and diagnostic data.
2. Document the steps taken and their outcomes.
3. Submit a detailed escalation request to the Netwrix development or advanced support team.

--- 

End of Document.