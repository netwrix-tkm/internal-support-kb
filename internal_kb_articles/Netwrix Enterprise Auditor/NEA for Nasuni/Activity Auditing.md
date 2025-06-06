# Knowledge Base Reference Guide: Troubleshooting NEA for Nasuni Activity Auditing Issues

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the **Netwrix Enterprise Auditor (NEA) for Nasuni** component, specifically within the **Activity Auditing** feature. It is designed to help support engineers systematically diagnose, resolve, and prevent common problems encountered in this category. Understanding these issues is critical for ensuring accurate data collection, maintaining audit integrity, and delivering reliable solutions to customers.

## Technical Background
### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring activity across various systems, including Nasuni file storage.
- **Nasuni:** A cloud-based file storage solution that integrates with NEA for auditing purposes.
- **Activity Auditing:** A feature that tracks and reports file system activity, including changes, access events, and security configurations.
- **FSAC Scan Job:** A File System Activity Collection (FSAC) job that gathers activity data from monitored hosts.
- **Access Zones:** Logical partitions within a file system, such as Isilon, that segregate data for auditing purposes.
- **Hidden Shares:** File shares that are not visible by default but may require auditing.

### System Context
- **Netwrix Activity Monitor Agent:** A critical component installed on monitored hosts to facilitate data collection.
- **StealthAUDIT Host Management:** A tool used to manage host configurations and verify system details.
- **Scan Depth Levels:** Determines the granularity of data collection during FSAC scans (e.g., 0-level for basic scans, deeper levels for detailed audits).

## Issue Recognition & Triage
### Symptoms
- Errors during FSAC scan jobs, such as missing registry keys or failed scans for specific access zones.
- Missing data for certain Nasuni hosts or hidden shares.
- Extended scan durations or performance bottlenecks during system scans.

### Priority Assessment
- **High Priority:** Issues affecting critical audit data collection (e.g., missing data for multiple hosts or access zones).
- **Medium Priority:** Configuration errors that can be resolved without significant impact on audit integrity.
- **Low Priority:** Performance optimization or minor discrepancies in scan results.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Error Messages:** Review logs and error details to identify the specific failure point.
2. **Check Agent Installation:** Confirm the presence and status of the Netwrix Activity Monitor agent on affected hosts.
3. **Review Host Configuration:** Use StealthAUDIT Host Management to validate OS details and scan settings.
4. **Analyze Scan Configuration:** Ensure FSAC jobs are targeting the correct host list and scan depth levels.
5. **Investigate Nasuni Settings:** Examine configuration settings on Nasuni filers for potential issues affecting data collection.

### Decision Points
- If the agent is missing, proceed with installation.
- If scan configuration is incorrect, adjust settings and re-run the job.
- If Nasuni settings are misconfigured, guide the customer to correct them.

## Information Collection
### Customer Queries
- What error messages or symptoms are being observed?
- Are all affected hosts running the Netwrix Activity Monitor agent?
- Have there been recent changes to Nasuni filer configurations or access zones?

### Logs and Data
- FSAC scan job logs and error reports.
- Host details from StealthAUDIT, including OS Name and OS Type.
- Nasuni filer configuration settings and logs.

## Common Scenarios & Solutions
### Scenario 1: Missing Netwrix Activity Monitor Agent
- **Symptoms:** FSAC scan fails with registry key errors (e.g., "Could not open registry key SYSTEMCurrentControlSetServicesSBTLoggingParameters").
- **Resolution:** Install the Netwrix Activity Monitor agent on the affected host and re-run the scan.

### Scenario 2: Incorrect Scan Configuration
- **Symptoms:** Data not collected for multiple Nasuni hosts; FSAC System Scan targets an individual host instead of the host list.
- **Resolution:** Reconfigure the FSAC System Scan to target the Nasuni host list and verify thread count settings.

### Scenario 3: Hidden Shares Not Audited
- **Symptoms:** Hidden shares on Nasuni filers do not appear in FSAA/SDD scan results.
- **Resolution:** Correct configuration settings on the Nasuni side to include hidden shares in audit results.

## Detailed Case Studies
### Case Study 1: Missing Agent on Isilon Host
- **Ticket ID:** [500Qk00000EOZRBIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EOZRBIA5/view)
- **Symptoms:** FSAC scan failed for one access zone with a registry key error.
- **Diagnostic Steps:** Verified error message, checked agent installation, reviewed host details in StealthAUDIT.
- **Resolution:** Installed the Netwrix Activity Monitor agent on the affected host and re-ran the scan successfully.
- **Key Takeaways:** Always confirm agent installation on all monitored hosts before running FSAC jobs.

### Case Study 2: Incorrect Scan Configuration
- **Ticket ID:** [500Qk00000LIhFJIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LIhFJIA1/view)
- **Symptoms:** Data not collected for 3-4 Nasuni hosts; extended scan duration.
- **Diagnostic Steps:** Investigated scan configuration, verified thread count, adjusted target from individual host to Nasuni host list.
- **Resolution:** Reconfigured FSAC System Scan and successfully collected data.
- **Key Takeaways:** Ensure scan jobs target the correct host list and monitor thread count settings for optimal performance.

### Case Study 3: Hidden Shares Not Audited
- **Ticket ID:** [500Qk00000MbRmCIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MbRmCIAV/view)
- **Symptoms:** Hidden shares on Nasuni filers missing from scan results.
- **Diagnostic Steps:** Reviewed Nasuni filer logs, identified configuration issue preventing hidden shares from being audited.
- **Resolution:** Guided customer to correct Nasuni configuration settings.
- **Key Takeaways:** Regularly verify Nasuni filer settings to ensure all shares are included in audit results.

## Best Practices & Tips
- **Agent Installation:** Confirm the Netwrix Activity Monitor agent is installed on all monitored hosts before initiating FSAC jobs.
- **Scan Configuration:** Regularly review scan settings to ensure they target the correct host list and use appropriate thread counts.
- **Nasuni Settings:** Document and verify Nasuni filer configurations, especially for hidden shares and access zones.
- **Performance Monitoring:** Monitor scan durations and adjust thread counts or scan depth levels to optimize performance.
- **Proactive Communication:** Maintain clear communication with customers regarding configuration requirements and troubleshooting steps.

## Escalation Guidelines
### Criteria for Escalation
- Issues persist after following standard troubleshooting steps.
- Errors indicate potential bugs or compatibility issues requiring development team input.
- Customer impact is critical, such as missing audit data for regulatory compliance.

### Escalation Procedures
1. Gather all relevant logs, error messages, and configuration details.
2. Document troubleshooting steps taken and results observed.
3. Submit a detailed escalation request to the appropriate team, including ticket ID and customer impact summary.
4. Follow up regularly to ensure timely resolution and communicate updates to the customer.