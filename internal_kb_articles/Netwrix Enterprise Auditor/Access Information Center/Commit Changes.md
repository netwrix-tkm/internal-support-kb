# Knowledge Base Reference Guide: Troubleshooting Data Discrepancies in the Access Information Center (AIC)

## Overview
This guide provides a comprehensive reference for troubleshooting data discrepancies in the Access Information Center (AIC) of Netwrix Enterprise Auditor. The AIC is a critical component for managing and analyzing permissions data, and ensuring its accuracy is essential for maintaining data integrity and compliance. This document outlines systematic approaches, common scenarios, and best practices to help support engineers effectively diagnose and resolve issues in this category.

## Technical Background
The Access Information Center (AIC) is a feature within Netwrix Enterprise Auditor that consolidates and displays permissions data collected from various servers. The data is gathered through permission scans and imported into the AIC via the FSAA Bulk Import process. Key components involved in this process include:
- **FSAA Bulk Import**: Responsible for transferring scanned data into the AIC.
- **Proxy Server**: Facilitates communication between the collector and the AIC.
- **Ports**: Specific network ports must remain open for seamless data transfer.

Failures in any of these components can lead to discrepancies in the AIC, such as missing or outdated permissions data.

## Issue Recognition & Triage
### Symptoms
- Permissions data in the AIC is outdated or missing.
- Successful scan completion is reported, but data does not appear in the AIC.
- Errors such as `System.TimeoutException` appear in scan logs.

### Priority Assessment
- **High Priority**: If the issue impacts compliance reporting or critical business operations.
- **Medium Priority**: If the issue is isolated to non-critical servers or environments.
- **Low Priority**: If the issue is intermittent and does not affect core functionality.

## Diagnostic Methodology
1. **Verify Scan Completion**: Confirm that permission scans completed successfully without errors.
2. **Check FSAA Bulk Import**: Ensure the bulk import process is running and completing without failures.
3. **Review Logs**: Analyze scan logs and error reports for specific issues (e.g., timeouts, connectivity errors).
4. **Test Proxy Server**: Verify that the proxy server is operational and that required ports are open.
5. **Enable Debug Mode**: Collect detailed logs by setting the job to Debug mode for deeper analysis.

## Information Collection
### Questions to Ask the Customer
- Which servers are affected by the data discrepancies?
- When was the issue first noticed?
- Have there been any recent changes to the network or server environment?
- Are there any known issues with the proxy server or network connectivity?

### Logs and Data to Collect
- FSAA scan logs and error reports.
- DEBUG logs from the most recent scan run.
- Proxy server status and configuration details.
- Network port status (e.g., firewall rules, open/closed ports).

## Common Scenarios & Solutions
### Scenario 1: Bulk Import Failure
- **Symptoms**: Data does not update in the AIC despite successful scans.
- **Root Cause**: FSAA Bulk Import process failure.
- **Resolution**: Restart the bulk import process and monitor for errors. If the issue persists, escalate to the development team for further investigation.

### Scenario 2: Proxy Server Issues
- **Symptoms**: Scans fail with connectivity errors or timeouts.
- **Root Cause**: Proxy server is unresponsive or required ports are blocked.
- **Resolution**: Verify the proxy server's operational status and ensure all necessary ports are open.

### Scenario 3: Timeout Exceptions
- **Symptoms**: `System.TimeoutException` appears in scan logs.
- **Root Cause**: Network latency or server performance issues.
- **Resolution**: Optimize server performance and reduce network latency. Increase timeout settings if necessary.

## Detailed Case Studies
### Case Study: Ticket [500Qk00000Npk3cIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Npk3cIAB/view)
#### Initial Symptoms
The customer reported that permissions data from several servers was not updating in the AIC, despite successful scans.

#### Diagnostic Steps
1. Confirmed that the FSAA Bulk Import process was running.
2. Reviewed scan logs, which revealed a `System.TimeoutException` and session errors.
3. Enabled Debug mode to collect detailed logs.
4. Verified the proxy server's status and checked network ports.

#### Key Information
- The bulk import process was failing due to an unresolved issue tracked in a separate ticket.
- The proxy server was intermittently unresponsive, and some required ports were blocked.

#### Resolution
- Addressed the bulk import failure by resolving the related issue in ticket [442548](https://nwxcorp.lightning.force.com/lightning/r/Case/442548/view).
- Ensured the proxy server was operational and opened the necessary ports.
- Verified that the AIC data updated correctly after these actions.

#### Key Takeaways
- Always verify the bulk import process when discrepancies are observed in the AIC.
- Proxy server and port configurations are critical for data transfer integrity.
- Debug logs provide valuable insights for diagnosing complex issues.

#### Efficiency Improvements
- Automate monitoring of the bulk import process to detect failures early.
- Develop a checklist for verifying proxy server and port configurations.

## Best Practices & Tips
- **Monitor Critical Processes**: Regularly check the status of the FSAA Bulk Import process and proxy server.
- **Enable Debug Mode**: Use Debug mode for detailed logging when troubleshooting complex issues.
- **Proactive Communication**: Keep customers informed about known issues and resolution timelines.
- **Document Resolutions**: Maintain detailed records of resolved issues to build a robust knowledge base.
- **Network Configuration**: Work with customers to ensure network ports are configured correctly and remain open.

## Escalation Guidelines
- **When to Escalate**:
  - If the bulk import process fails repeatedly without a clear resolution.
  - If proxy server issues persist despite troubleshooting.
  - If the issue impacts multiple customers or critical business operations.

- **How to Escalate**:
  - Collect all relevant logs and diagnostic data.
  - Provide a detailed summary of troubleshooting steps and findings.
  - Escalate to the development team or senior engineers with a clear problem statement and supporting evidence.