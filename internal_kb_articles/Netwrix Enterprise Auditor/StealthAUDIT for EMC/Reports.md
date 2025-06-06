# Knowledge Base Reference Guide: Troubleshooting Open Access Report Data Issues in StealthAUDIT for EMC

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to incorrect data in Open Access reports within the StealthAUDIT for EMC component of Netwrix Enterprise Auditor. Accurate reporting is critical for identifying and remediating open shares, ensuring compliance, and maintaining security. This document outlines systematic approaches, common scenarios, and best practices to resolve these issues effectively.

---

## Technical Background

### Key Concepts
- **Open Access Report**: A report that identifies shared resources (e.g., files, folders, drives) with open or excessive access permissions.
- **FSAA_Exceptions Job**: A scheduled task that processes exceptions and updates the data used by the Open Access report. Consistent execution of this job is essential for accurate reporting.
- **Stale Data**: Data that is outdated or no longer reflects the current state of the environment, often caused by skipped or failed jobs.

### System Context
- **StealthAUDIT for EMC**: A module within Netwrix Enterprise Auditor designed to audit and report on file shares and permissions for EMC storage systems.
- **Data Flow**: The FSAA_Exceptions job processes raw scan data, applies exceptions, and updates the database. The Open Access report queries this database to generate its output.

---

## Issue Recognition & Triage

### Symptoms
- Shares that have been removed or remediated reappear in the Open Access report.
- Inconsistent report results between scans.

### Priority Assessment
- **High Priority**: If the issue impacts compliance reporting or security audits.
- **Medium Priority**: If the issue is identified during routine checks but does not affect critical operations.

---

## Diagnostic Methodology

1. **Verify Report Data**: Run the Open Access report and confirm the presence of incorrect or stale data.
2. **Check FSAA_Exceptions Job Status**:
   - Verify if the job is enabled and scheduled correctly.
   - Check the job execution history for failures or inconsistencies.
3. **Review Affected Servers**:
   - Identify servers with discrepancies in the report.
   - Confirm the current state of shares on these servers.
4. **Analyze Logs**:
   - Review job logs for errors or skipped executions.
   - Check scan logs for anomalies in data collection.

---

## Information Collection

### Questions to Ask the Customer
- When was the issue first noticed?
- Have there been any recent changes to the environment (e.g., share removals, server updates)?
- Is the FSAA_Exceptions job enabled and running on schedule?

### Data to Collect
- Open Access report output showing the incorrect data.
- FSAA_Exceptions job logs and execution history.
- Scan logs for the affected servers.
- Current share configuration on the affected servers.

---

## Common Scenarios & Solutions

### Scenario 1: FSAA_Exceptions Job Not Running Consistently
- **Symptoms**: Stale data in the Open Access report; shares reappear after remediation.
- **Resolution**:
  1. Verify the FSAA_Exceptions job status.
  2. Enable and schedule the job if it is disabled.
  3. Run the job manually to update the data.
  4. Rerun the Open Access report to confirm the issue is resolved.

### Scenario 2: Job Execution Errors
- **Symptoms**: FSAA_Exceptions job fails to complete successfully.
- **Resolution**:
  1. Review job logs for error messages.
  2. Address any configuration or permission issues causing the failure.
  3. Restart the job and verify successful completion.

---

## Detailed Case Studies

### Case Study: Ticket [500Qk00000KygAfIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KygAfIAJ/view)

#### Initial Symptoms
The customer reported that the Open Access report displayed shares that had been removed, with discrepancies appearing every other scan.

#### Diagnostic Steps
1. Ran the Open Access report to confirm the issue.
2. Reviewed the FSAA_Exceptions job for the affected servers and found it had not been run consistently.
3. Conducted a meeting with the customer to review findings and discuss remediation steps.

#### Key Information Leading to Resolution
- The FSAA_Exceptions job for one of the affected servers (CARVSQLRDSMS003) was disabled, leading to stale data in the report.

#### Resolution
- Enabled and ran the FSAA_Exceptions job for the affected server.
- Instructed the customer to rerun the Open Access report, which confirmed the issue was resolved.

#### Key Takeaways
- Consistent execution of the FSAA_Exceptions job is critical for accurate reporting.
- Regularly review job schedules and execution history to prevent similar issues.

#### Efficiency Improvements
- Implement automated alerts for job failures or skipped executions.
- Provide customers with guidelines for verifying job status.

---

## Best Practices & Tips

1. **Ensure Job Consistency**:
   - Regularly verify that the FSAA_Exceptions job is enabled and running on schedule.
   - Use monitoring tools to detect and alert on job failures.

2. **Proactive Data Validation**:
   - Periodically review Open Access reports for anomalies.
   - Cross-check report data with the current state of shares on servers.

3. **Customer Communication**:
   - Clearly explain the importance of the FSAA_Exceptions job to customers.
   - Provide step-by-step instructions for verifying and running the job.

4. **Documentation**:
   - Maintain detailed records of job configurations and schedules.
   - Document common issues and their resolutions for future reference.

---

## Escalation Guidelines

### When to Escalate
- The issue persists after running the FSAA_Exceptions job and verifying its configuration.
- Job logs indicate errors that cannot be resolved through standard troubleshooting.
- The problem impacts multiple servers or environments, suggesting a systemic issue.

### How to Escalate
1. Gather all relevant information, including:
   - Open Access report output.
   - FSAA_Exceptions job logs and execution history.
   - Scan logs for affected servers.
2. Submit a detailed escalation request to the development or product engineering team.
3. Provide regular updates to the customer during the escalation process.

--- 

This guide serves as a definitive reference for troubleshooting Open Access report data issues in StealthAUDIT for EMC, enabling support engineers to resolve problems efficiently and maintain customer satisfaction.