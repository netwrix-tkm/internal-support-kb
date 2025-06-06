# Netwrix Enterprise Auditor (NEA) for Oracle: Configuration Troubleshooting Guide

## Overview

This guide provides a comprehensive reference for troubleshooting configuration issues related to Netwrix Enterprise Auditor (NEA) for Oracle. It is designed to help support engineers systematically diagnose and resolve connectivity and configuration problems, ensuring seamless integration between NEA and Oracle databases. Proper configuration is critical for accurate auditing and compliance reporting, making it essential to address these issues efficiently.

---

## Technical Background

### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring changes across IT environments, including Oracle databases.
- **Oracle Database Role:** Determines the level of access and permissions for database connections. Common roles include `Sysdba` (administrative privileges) and `Default` (standard user access).
- **Connection Profile:** A configuration in NEA that defines how the system connects to the Oracle database, including credentials, roles, and host details.

### System Context
- **Oracle Database Version:** 11.2.0.4
- **Operating System:** Solaris 11.3
- **NEA Version:** 11.6

NEA relies on properly configured connection profiles to establish communication with Oracle databases. Misconfigurations, such as incorrect roles or missing host entries, can prevent successful connections.

---

## Issue Recognition & Triage

### Symptoms
- NEA fails to connect to the Oracle database.
- Error messages indicating authentication or connectivity issues.
- Successful connection to the database using external tools (e.g., Oracle SQL Developer) but not through NEA.

### Priority Assessment
- **High Priority:** If the issue disrupts critical auditing or compliance reporting.
- **Medium Priority:** If the issue occurs during initial setup or testing without immediate operational impact.

---

## Diagnostic Methodology

1. **Verify External Connectivity:**
   - Test the connection to the Oracle database using Oracle SQL Developer or similar tools.
   - Confirm that the credentials and network settings are correct.

2. **Review NEA Connection Profile:**
   - Check the configured Oracle role (e.g., `Sysdba` vs. `Default`).
   - Ensure all relevant hosts are included in the profile.

3. **Test Connection from NEA:**
   - Use the "Test Connection" feature in NEA to validate the configuration.

4. **Engage Relevant Teams:**
   - Collaborate with the customer’s database or Linux team to verify network and firewall settings.

5. **Iterative Testing:**
   - Make incremental changes to the connection profile and test after each adjustment.

---

## Information Collection

### Questions to Ask the Customer
- What version of Oracle Database and Solaris are you using?
- Are you able to connect to the database using external tools (e.g., Oracle SQL Developer)?
- What role is configured in the NEA connection profile (e.g., `Sysdba`, `Default`)?
- Are there any network restrictions or firewalls between the NEA server and the Oracle database?

### Logs and Data to Collect
- NEA configuration logs.
- Oracle database connection logs.
- Screenshots of the NEA connection profile settings.
- Results of test connections from Oracle SQL Developer.

---

## Common Scenarios & Solutions

### Scenario 1: Incorrect Oracle Role Configuration
- **Symptoms:** NEA fails to connect; external tools connect successfully.
- **Root Cause:** The Oracle role in the connection profile is set to `Sysdba`, which restricts access.
- **Resolution:**
  1. Edit the connection profile in NEA.
  2. Change the Oracle role from `Sysdba` to `Default`.
  3. Test the connection to confirm resolution.

### Scenario 2: Missing Host Entries in Connection Profile
- **Symptoms:** NEA cannot connect to certain Oracle database instances.
- **Root Cause:** Not all relevant hosts are included in the connection profile.
- **Resolution:**
  1. Add all required hosts to the connection profile.
  2. Test the connection for each host.

---

## Detailed Case Studies

### Case Study: Ticket [500Qk00000LlYQQIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LlYQQIA3/view)
- **Initial Symptoms:** Customer reported that NEA could not connect to their Oracle database hosted on Solaris.
- **Diagnostic Steps:**
  1. Verified credentials and tested connectivity using Oracle SQL Developer (successful).
  2. Reviewed the NEA connection profile and identified the Oracle role as `Sysdba`.
  3. Collaborated with the customer’s Linux team to confirm network settings.
  4. Edited the connection profile to switch the Oracle role to `Default`.
  5. Added all relevant hosts to the connection profile.
  6. Tested the connection, which was successful.
- **Resolution:** Adjusted the Oracle role and updated the connection profile.
- **Key Takeaways:**
  - Always verify the Oracle role in the connection profile.
  - Test connectivity using external tools before troubleshooting NEA settings.
- **Efficiency Improvements:** Develop a checklist for connection profile validation during initial setup.

---

## Best Practices & Tips

1. **Validate External Connectivity First:**
   - Use tools like Oracle SQL Developer to confirm that the database is accessible with the provided credentials.

2. **Standardize Connection Profile Settings:**
   - Default to the `Default` Oracle role unless specific administrative privileges are required.

3. **Document Configuration Details:**
   - Maintain a record of connection profile settings for future reference.

4. **Collaborate with Customer Teams:**
   - Engage database and network teams early to rule out environmental factors.

5. **Test Incrementally:**
   - Make one change at a time and test to isolate the root cause.

---

## Escalation Guidelines

### When to Escalate
- The issue persists despite following all diagnostic and resolution steps.
- Network or database-level issues are suspected but cannot be confirmed.
- The customer requires advanced configuration beyond standard support capabilities.

### How to Escalate
1. Collect all relevant logs, screenshots, and test results.
2. Document the steps already taken and their outcomes.
3. Escalate to the appropriate team (e.g., Development or Advanced Support) with a detailed summary.

--- 

This guide serves as a definitive reference for troubleshooting NEA configuration issues with Oracle databases, enabling support engineers to resolve problems efficiently and consistently.