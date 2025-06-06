# Netwrix Endpoint Protector: Server Performance Troubleshooting Guide

## Overview

Server performance issues in Netwrix Endpoint Protector (EPP) can significantly impact system functionality, user experience, and organizational security. This guide provides a comprehensive reference for identifying, diagnosing, and resolving server performance issues. It is designed to equip support engineers with the tools and methodologies needed to address these problems efficiently and consistently.

## Technical Background

### Key Concepts
- **Netwrix Endpoint Protector (EPP):** A data loss prevention (DLP) solution designed to monitor and control endpoint activity.
- **Server Performance:** Refers to the responsiveness, stability, and resource utilization of the EPP server.
- **Components:** Includes the EPP server, client agents, database, and associated services like nginx, syslog-ng, and JavaScript-based UI elements.
- **Common Features Impacted:** Logging, reporting, licensing, policy enforcement, and user interface responsiveness.

### Terminology
- **Shadow Files:** Temporary files used for logging and monitoring large file activities.
- **DPI (Deep Packet Inspection):** A feature for inspecting network traffic.
- **CAP Policy:** Content-Aware Protection policies used to enforce data security rules.
- **SIEM Integration:** Forwarding logs to Security Information and Event Management systems like Logpoint.
- **Hotfixes and Patches:** Updates applied to address vulnerabilities or improve functionality.

### System Context
- **Hosting Environments:** On-premises, AWS, Azure, and Proxmox.
- **Resource Requirements:** CPU, memory, disk I/O, and network bandwidth must meet minimum specifications for optimal performance.
- **Dependencies:** Services like nginx, syslog-ng, and database configurations are critical for server functionality.

---

## Issue Recognition & Triage

### Symptoms of Server Performance Issues
- High CPU or memory usage.
- Slow response times or timeouts in the web interface.
- Missing or delayed logs.
- Crashes or "500 Internal Server Error" messages.
- Intermittent unavailability (e.g., "504 Gateway Time-Out").
- Licensing discrepancies or false entries.
- Policy misfires or unexpected triggers.

### Priority Assessment
- **Critical:** Server crashes, inability to access the UI, or missing logs affecting compliance/security.
- **High:** Severe slowness or degraded performance impacting multiple users.
- **Medium:** Intermittent issues or isolated performance degradation.
- **Low:** Non-urgent optimization requests or minor anomalies.

---

## Diagnostic Methodology

### Systematic Approach
1. **Confirm the Issue:**
   - Verify the reported symptoms with the customer.
   - Check server logs and resource utilization metrics.

2. **Identify Recent Changes:**
   - Ask about recent updates, patches, or configuration changes.
   - Review deployment methods (e.g., MDM, manual installation).

3. **Reproduce the Problem:**
   - Attempt to replicate the issue in a controlled environment.
   - Use remote sessions to observe the behavior directly.

4. **Analyze Logs and Metrics:**
   - Collect logs from the server, clients, and associated services.
   - Check for errors, warnings, or anomalies.

5. **Isolate the Root Cause:**
   - Narrow down potential causes using elimination techniques.
   - Focus on resource bottlenecks, misconfigurations, or software bugs.

6. **Implement and Test Solutions:**
   - Apply fixes incrementally and test their effectiveness.
   - Monitor the system for stability after resolution.

---

## Information Collection

### Questions to Ask Customers
- What symptoms are being observed, and when did they start?
- Were there any recent updates, patches, or configuration changes?
- How many endpoints are connected to the server?
- What is the hosting environment (e.g., AWS, Azure, on-premises)?
- Are there any specific error messages or logs available?

### Logs and Data to Collect
- **Server Logs:** Application logs, nginx logs, syslog-ng logs.
- **Resource Metrics:** CPU, memory, disk I/O, and network usage.
- **Policy Configurations:** CAP policies, shadow file settings, and DPI configurations.
- **Deployment Details:** Agent versions, deployment methods, and licensing status.

---

## Common Scenarios & Solutions

### Scenario 1: High CPU or Memory Usage
- **Root Cause:** Excessive logs, duplicate devices, or insufficient resources.
- **Solution:** Clear old logs, remove duplicates, and optimize server resources.

### Scenario 2: Missing or Delayed Logs
- **Root Cause:** Misconfigured logging services (e.g., syslog-ng) or insufficient shadow file size.
- **Solution:** Enable and configure logging services, increase shadow file size.

### Scenario 3: Server Crashes or Errors
- **Root Cause:** Disk space issues, corrupted configuration files, or software bugs.
- **Solution:** Free up disk space, repair configurations, and apply hotfixes.

### Scenario 4: Slow UI or Timeouts
- **Root Cause:** JavaScript misconfigurations, large datasets, or resource bottlenecks.
- **Solution:** Optimize UI components, break down large reports, and allocate additional resources.

### Scenario 5: Licensing Discrepancies
- **Root Cause:** Synchronization issues or duplicate entries in the database.
- **Solution:** Perform database cleanup and verify licensing synchronization.

---

## Detailed Case Studies

### Case Study 1: Missing Logs After Hotfix Application
- **Ticket:** [500Qk00000CaoiaIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CaoiaIAB/view)
- **Symptoms:** Logs stopped after applying a hotfix.
- **Diagnostic Steps:** Verified hotfix version, identified known issue with the patch.
- **Resolution:** Deployed a revised hotfix, restoring log functionality.
- **Key Takeaways:** Always test hotfixes in a controlled environment before production deployment.

### Case Study 2: Server Crash Due to Disk Space
- **Ticket:** [500Qk00000E6nXRIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E6nXRIAZ/view)
- **Symptoms:** "500 Internal Server Error" caused by insufficient disk space.
- **Diagnostic Steps:** Checked disk usage, identified excessive file shadows.
- **Resolution:** Deleted file shadows, freeing up disk space.
- **Key Takeaways:** Implement disk space monitoring and alerts.

### Case Study 3: High Memory Usage in AWS
- **Ticket:** [500Qk00000LQLW9IAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LQLW9IAP/view)
- **Symptoms:** Memory usage reached 90% due to log backlog.
- **Diagnostic Steps:** Cleared logs, configured automatic log backups.
- **Resolution:** Reduced memory usage by managing logs effectively.
- **Key Takeaways:** Regularly configure log management to prevent resource exhaustion.

---

## Best Practices & Tips

1. **Proactive Monitoring:**
   - Use monitoring tools to track server resource usage and performance metrics.
   - Set up alerts for disk space, CPU, and memory thresholds.

2. **Regular Maintenance:**
   - Schedule periodic log cleanup and database optimization.
   - Test patches and updates in a staging environment before production.

3. **Effective Communication:**
   - Keep customers informed about known issues and resolution timelines.
   - Provide clear instructions for testing and implementing fixes.

4. **Documentation:**
   - Maintain detailed records of configurations, policies, and troubleshooting steps.
   - Update knowledge base articles with lessons learned from resolved cases.

---

## Escalation Guidelines

### When to Escalate
- Critical issues affecting multiple users or systems.
- Problems requiring development team intervention (e.g., software bugs).
- Cases where standard troubleshooting steps fail to resolve the issue.

### How to Escalate
- Provide a detailed summary of the issue, including logs and diagnostic findings.
- Clearly outline the impact and urgency of the problem.
- Use internal escalation channels to involve the appropriate teams.

---

This guide serves as a definitive reference for handling server performance issues in Netwrix Endpoint Protector. By following the outlined methodologies and leveraging the insights from case studies, support engineers can resolve issues effectively and maintain system reliability.