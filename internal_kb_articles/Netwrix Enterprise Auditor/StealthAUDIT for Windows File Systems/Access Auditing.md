# Comprehensive Knowledge Base Guide: Troubleshooting StealthAUDIT for Windows File Systems - Access Auditing

## Overview

This guide provides a systematic approach to troubleshooting issues related to the **StealthAUDIT for Windows File Systems** component of **Netwrix Enterprise Auditor (NEA)**, specifically focusing on the **Access Auditing** feature. It is designed to help support engineers efficiently diagnose, resolve, and prevent common problems encountered in this category. By leveraging real-world case studies and proven methodologies, this guide ensures consistent and effective issue resolution.

---

## Technical Background

### Key Concepts
- **File System Access Auditing (FSAA):** A feature that collects and analyzes access permissions, activity, and configurations for file systems.
- **StealthAUDIT Proxy:** A component that facilitates communication between the NEA console and target hosts for scanning and data collection.
- **Tier 1 and Tier 2 Databases:** Tier 1 stores raw scan data, while Tier 2 processes and organizes data for reporting and analysis.
- **Certificates:** Used for secure communication between the NEA console, proxies, and target hosts.
- **Job Types:**
  - **FSAA Scans:** Collect access permissions and configurations.
  - **Bulk Import Jobs:** Import scan data into the database for analysis.
  - **Reset Hosts:** Clears existing data for a fresh scan.

### Terminology
- **Access Information Center (AIC):** The interface for viewing and managing access-related data.
- **DFS (Distributed File System):** A file system that organizes shared resources across multiple servers.
- **NTFS Permissions:** File system permissions that control access to files and folders.
- **T2 Folders:** Temporary storage for scan data on proxy servers.

### System Context
- **Environment:** NEA operates in a distributed architecture with components such as the NEA console, proxies, and target hosts.
- **Dependencies:** FSAA relies on network connectivity, proper permissions, and third-party services (e.g., Crowdstrike, firewalls).

---

## Issue Recognition & Triage

### Common Symptoms
- **Performance Issues:** Scans taking excessively long to complete.
- **Scan Failures:** Errors such as "Failed to connect to HOSTNAMEIPC$" or "System.IndexOutOfRangeException."
- **Data Discrepancies:** Outdated or missing data in reports.
- **Configuration Errors:** Issues with certificates, proxies, or job schedules.

### Priority Assessment
- **High Priority:** Scans failing across multiple hosts, critical data missing, or security compliance impacted.
- **Medium Priority:** Performance degradation or isolated scan failures.
- **Low Priority:** Cosmetic issues or minor discrepancies in reports.

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Problem:**
   - Gather details about the issue, environment, and recent changes.
   - Identify whether the problem is isolated or widespread.

2. **Verify Configuration:**
   - Check job schedules, proxy settings, and certificate configurations.
   - Ensure all components are running compatible versions.

3. **Analyze Logs:**
   - Review NEA logs, proxy logs, and Windows Event Viewer for errors.
   - Look for patterns or recurring issues.

4. **Test Connectivity:**
   - Use tools like `ping`, `telnet`, or `Test-NetConnection` to verify network paths.
   - Confirm that required ports (e.g., 445, 8766) are open.

5. **Reproduce the Issue:**
   - Run test scans or jobs in debug mode to capture detailed logs.
   - Isolate variables (e.g., specific hosts, job types) to narrow down the root cause.

6. **Implement Fixes:**
   - Apply configuration changes, clear caches, or update software as needed.
   - Monitor results to confirm resolution.

---

## Information Collection

### Key Questions for Customers
- What is the specific error message or behavior observed?
- When did the issue start, and were there any recent changes to the environment?
- Which hosts, shares, or jobs are affected?
- Are there any third-party dependencies (e.g., Crowdstrike, firewalls) involved?

### Logs and Data to Collect
- **NEA Logs:** Located in the installation directory.
- **Proxy Logs:** Found in the proxy server's log directory.
- **Windows Event Logs:** Application and System logs for errors.
- **Job Configuration:** Export job settings for analysis.
- **Network Diagnostics:** Results from `ping`, `telnet`, or `Test-NetConnection`.

---

## Common Scenarios & Solutions

### Scenario 1: Slow FSAA Scans
- **Symptoms:** Scans taking days to complete.
- **Root Cause:** Unlimited probable owners setting.
- **Solution:** Limit probable owners to 4 and upgrade to the latest version. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BkTrvIAF/view)

### Scenario 2: Scan Failures Due to Third-Party Outages
- **Symptoms:** Errors like "Failed to connect to HOSTNAMEIPC$."
- **Root Cause:** Crowdstrike outage affecting network paths.
- **Solution:** Wait for service restoration and verify connectivity. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E55tSIAR/view)

### Scenario 3: Certificate Validation Errors
- **Symptoms:** "Failed to validate certificate" during scans.
- **Root Cause:** Certificates not stored in the FSAA Certificate Authority store.
- **Solution:** Reconfigure certificates using the FSAACertificateManager.exe tool. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PGErpIAH/view)

### Scenario 4: Database Locking Issues
- **Symptoms:** UNIQUE constraint violations or jobs stuck in "Running" status.
- **Root Cause:** Overlapping job schedules or database conflicts.
- **Solution:** Reschedule jobs to avoid overlaps and reset hosts. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I9ostIAB/view)

---

## Detailed Case Studies

### Case Study 1: FSAA Scan Performance Issue
- **Ticket ID:** [500Qk00000BkTrvIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BkTrvIAF/view)
- **Symptoms:** FSAA scan taking 15 days to complete.
- **Diagnostic Steps:** Reviewed scan settings, identified unlimited probable owners as the cause.
- **Resolution:** Limited probable owners to 4 and recommended upgrading to version 11.6.
- **Key Takeaways:** Default settings may not be optimal for large environments.

### Case Study 2: Proxy Configuration Error
- **Ticket ID:** [500Qk00000LFbb5IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LFbb5IAD/view)
- **Symptoms:** Scheduled scans failing but working manually.
- **Diagnostic Steps:** Verified permissions, cleared certificates, and reviewed logs.
- **Resolution:** Assigned the Infrastructure account in job properties to resolve certificate exchange issues.
- **Key Takeaways:** Ensure consistent credential usage across manual and scheduled tasks.

### Case Study 3: Outdated Data in Reports
- **Ticket ID:** [500Qk00000OiMbhIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OiMbhIAF/view)
- **Symptoms:** Reports showing data from decommissioned servers.
- **Diagnostic Steps:** Ran FSDropTables job and reviewed database for residual data.
- **Resolution:** Dropped old data and re-ran jobs to update reports.
- **Key Takeaways:** Regular database maintenance is critical for accurate reporting.

---

## Best Practices & Tips

1. **Optimize Job Schedules:** Avoid overlapping scans to prevent resource contention and database locking.
2. **Monitor Certificates:** Use the FSAACertificateManager.exe tool to manage certificates consistently.
3. **Regular Maintenance:** Periodically clear outdated data and reset hosts to ensure clean scans.
4. **Document Changes:** Maintain a log of environment changes to aid in troubleshooting.
5. **Proactive Monitoring:** Use debug logs and network diagnostics to identify potential issues early.

---

## Escalation Guidelines

### When to Escalate
- Persistent issues after applying documented solutions.
- Errors involving unsupported configurations or third-party dependencies.
- Requests for new features or enhancements.

### How to Escalate
- Collect all relevant logs, configurations, and diagnostic results.
- Provide a detailed summary of steps taken and outcomes.
- Submit the case to R&D or escalate to Tier 3 support with all supporting documentation.