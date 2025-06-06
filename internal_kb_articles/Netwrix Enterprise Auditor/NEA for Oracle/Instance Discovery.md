# Knowledge Base Reference Guide: Troubleshooting Instance Discovery Issues in NEA for Oracle

## Overview

This guide focuses on troubleshooting issues related to the **Instance Discovery** feature in **Netwrix Enterprise Auditor (NEA) for Oracle**. Instance Discovery is a critical functionality that enables NEA to identify Oracle database instances for auditing purposes. Understanding and resolving issues in this category is essential for ensuring seamless database auditing and maintaining customer satisfaction.

Support engineers will find systematic approaches, diagnostic methodologies, and best practices to effectively address Instance Discovery problems, particularly in environments using Oracle container databases (CDB) with pluggable databases (PDB).

---

## Technical Background

### Key Concepts
- **Instance Discovery**: A feature in NEA for Oracle that scans servers to identify Oracle database instances for auditing.
- **Container Database (CDB)**: A single Oracle database that can host multiple pluggable databases (PDBs).
- **Pluggable Database (PDB)**: A portable collection of schemas, objects, and data that resides within a CDB.
- **Connection Profile**: A set of credentials and configuration details used by NEA to connect to Oracle databases.

### System Context
- NEA relies on Oracle connection profiles to authenticate and access database instances during Instance Discovery scans.
- Permissions and user credentials must be correctly configured for both CDBs and PDBs to ensure successful discovery.

---

## Issue Recognition & Triage

### Symptoms
- Instance Discovery jobs fail to identify Oracle database instances.
- Error messages in logs indicate permission issues, such as "username/password logon denied."
- Manual connection to the Oracle database succeeds, but automated scans fail.

### Priority Assessment
- **High Priority**: If Instance Discovery failure impacts auditing operations or compliance requirements.
- **Medium Priority**: If the issue is isolated to a single database instance without broader operational impact.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify Manual Connectivity**: Confirm that the Oracle database can be accessed manually using the connection profile credentials.
2. **Review Logs**: Examine Instance Discovery job logs for error messages or permission-related issues.
3. **Check User Credentials**: Ensure that the connection profile has the necessary permissions for both the CDB and PDB.
4. **Validate Configuration**: Confirm that the Oracle server and NEA configuration align with the customer's environment (e.g., operating system changes, database architecture).

### Decision Points
- If manual connectivity fails, focus on resolving credential or network issues.
- If logs indicate permission errors, investigate user credential configuration for the CDB and PDB.

---

## Information Collection

### Customer Questions
- What operating system is the Oracle server running on (e.g., AIX, RHEL)?
- Are container databases (CDB) and pluggable databases (PDB) being used?
- Have there been recent changes to the environment, such as migrations or upgrades?
- Can the Oracle database be accessed manually using the connection profile credentials?

### Logs and Data to Collect
- Instance Discovery job logs from NEA.
- Oracle database logs for authentication attempts.
- Connection profile details (username, password, permissions).
- Configuration files for NEA and Oracle server.

---

## Common Scenarios & Solutions

### Scenario 1: Permission Errors in Logs
**Symptoms**: Logs show "username/password logon denied" errors during Instance Discovery scans.  
**Root Cause**: Missing user credentials for the container database (CDB).  
**Resolution**:  
1. Create a user account for the CDB with appropriate permissions.  
   ```sql
   CONTAINER_DATA=ALL FOR %NAME_OF_PLUGGABLE_DATABASE% CONTAINER = CURRENT;
   ```
2. Verify the connection profile permissions for both the CDB and PDB.  
3. Re-run the Instance Discovery job.

---

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000ExrY5IAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ExrY5IAJ/view)

#### Initial Symptoms
The customer reported that Instance Discovery jobs failed to identify Oracle database instances after migrating from AIX to RHEL. Manual connections to the database succeeded, but automated scans failed.

#### Diagnostic Steps
1. Reviewed Instance Discovery job logs and identified "username/password logon denied" errors.
2. Investigated the Oracle server configuration and discovered that no user credential was created for the container database (CDB).
3. Recommended creating a user account for the CDB and verifying connection profile permissions.

#### Resolution
The customer created a user credential for the CDB and updated the Instance Discovery Oracle servers job. The job successfully identified the Oracle database instance.

#### Key Takeaways
- Always verify user credentials for container databases when using the CDB/PDB architecture.
- Ensure connection profiles have the necessary permissions to avoid permission-related errors.

#### Efficiency Improvements
- Develop a checklist for validating user credentials and permissions during initial setup.
- Automate log analysis to quickly identify common error patterns.

---

## Best Practices & Tips

1. **Credential Validation**: Always ensure that user credentials are created for both CDBs and PDBs, with appropriate permissions.
2. **Environment Awareness**: Account for changes in operating systems or database architecture during migrations or upgrades.
3. **Log Analysis**: Regularly review logs for Instance Discovery jobs to identify recurring issues.
4. **Customer Communication**: Clearly explain the importance of user credentials and permissions to customers during setup and troubleshooting.
5. **Documentation**: Maintain detailed records of connection profiles, permissions, and configuration changes for future reference.

---

## Escalation Guidelines

### Criteria for Escalation
- The issue persists despite following all troubleshooting steps.
- Logs indicate a deeper problem with NEA or Oracle server integration.
- The customer requires urgent resolution due to compliance or operational impact.

### Escalation Procedure
1. Collect all relevant logs, configuration files, and customer environment details.
2. Document the troubleshooting steps taken and their outcomes.
3. Escalate the case to the development or product engineering team with a detailed summary of findings.

--- 

End of Document