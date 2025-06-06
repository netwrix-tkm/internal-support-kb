# Knowledge Base Reference Guide: Troubleshooting Logs Issues in Netwrix Endpoint Protector

## Overview

This guide focuses on troubleshooting issues related to the **Logs** feature within the **Reports & Analysis** component of Netwrix Endpoint Protector. Logs are critical for auditing, compliance, and operational insights, making their proper functionality essential for customers. This document provides a systematic approach to identifying, diagnosing, and resolving common issues, ensuring consistent and effective support.

---

## Technical Background

### Key Concepts
- **Logs in Netwrix Endpoint Protector**: Logs capture events and activities within the system, including content-aware protection, device control, and other security-related actions.
- **Artefacts**: Files or data generated as part of logs or reports, often stored for download or archival purposes.
- **Retention Settings**: Configurations that determine how long logs are stored and how many records are displayed in reports.
- **nginx Configuration**: The web server configuration that governs access to artefacts and other resources.

### System Context
- Logs are stored on the server or external storage (e.g., NAS) and accessed via the web interface.
- Artefacts are often stored in specific directories, such as `/var/eppfiles/artifacts`, and accessed through nginx configurations.
- Retention and display settings can impact the visibility and availability of logs.

---

## Issue Recognition & Triage

### Common Symptoms
- **Artefact Download Issues**: Clicking the download button results in no action or an error.
- **Log Retention Problems**: Logs are only retained for a short period or limited in number.

### Priority Assessment
- **High Priority**: Artefacts or logs critical for compliance or investigations are inaccessible.
- **Medium Priority**: Logs are visible but incomplete or limited in scope.
- **Low Priority**: Cosmetic or non-urgent issues with log display.

---

## Diagnostic Methodology

1. **Verify Environment Details**:
   - Confirm the product version and server configuration.
   - Check if external storage (e.g., NAS) is used for artefacts.

2. **Reproduce the Issue**:
   - Attempt to replicate the reported problem in the customer’s environment.

3. **Check Configuration Settings**:
   - Review nginx configuration for artefact download issues.
   - Verify log retention and display settings in the system.

4. **Inspect Storage Locations**:
   - Ensure artefacts or logs are present in the expected directories or storage devices.

5. **Enable Debugging**:
   - Collect diagnostic logs for deeper analysis if the issue persists.

---

## Information Collection

### Questions to Ask Customers
- Are you using external storage (e.g., NAS) for artefacts or logs?
- Have you configured any custom retention or display settings for logs?
- When did the issue first occur, and has it been consistent?

### Data to Collect
- **System Logs**: Collect logs from the server for analysis.
- **nginx Configuration**: Obtain the nginx configuration file to verify settings.
- **Screenshots or Videos**: Request visual evidence of the issue.
- **Storage Details**: Confirm the location and accessibility of artefacts or logs.

---

## Common Scenarios & Solutions

### Scenario 1: Artefact Download Issues
- **Symptoms**: Clicking the download button does nothing.
- **Root Cause**: Artefacts stored on a NAS device were not properly configured for retrieval.
- **Solution**:
  1. Verify nginx configuration for artefact downloads.
  2. Ensure the NAS is correctly configured to handle artefact requests.
  3. Restart the nginx service to apply changes.

### Scenario 2: Limited Log Retention
- **Symptoms**: Logs are only retained for two days or limited to 200 records.
- **Root Cause**: The "Maximum no. of records returned in a report search" setting was too low.
- **Solution**:
  1. Adjust the setting in **Device Control -> Global Settings** to a higher value (e.g., 10,000).
  2. Verify if audit log backups are scheduled to prevent data loss.

---

## Detailed Case Studies

### Case Study 1: Artefact Download Issue
- **Ticket ID**: [500Qk00000IphrpIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IphrpIAB/view)
- **Initial Symptoms**: Customer unable to download artefacts; clicking the download button resulted in no action.
- **Diagnostic Steps**:
  1. Verified server version and nginx configuration.
  2. Inspected the artefacts folder and found it empty.
  3. Identified that artefacts were stored on a NAS device.
- **Resolution**:
  - Configured the NAS to handle artefact requests properly.
  - Confirmed artefacts were accessible and downloadable.
- **Key Takeaways**:
  - Always verify external storage configurations for artefacts.
  - Restart nginx after making configuration changes.

### Case Study 2: Log Retention Issue
- **Ticket ID**: [500Qk00000OPikoIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OPikoIAD/view)
- **Initial Symptoms**: Logs were only retained for two days, limiting visibility.
- **Diagnostic Steps**:
  1. Checked retention and display settings.
  2. Conducted a remote session to adjust the "Maximum no. of records returned in a report search" setting.
- **Resolution**:
  - Increased the setting from 200 to 10,000, allowing more logs to be displayed.
- **Key Takeaways**:
  - Ensure log display settings align with customer needs.
  - Verify audit log backups to prevent unintentional data loss.

---

## Best Practices & Tips

- **nginx Configuration**:
  - Always verify the nginx configuration for artefact-related issues.
  - Restart the nginx service after making changes to apply updates.

- **Retention Settings**:
  - Adjust log retention and display settings based on customer requirements.
  - Educate customers on the impact of these settings on log visibility.

- **Storage Configuration**:
  - Confirm the accessibility and configuration of external storage devices (e.g., NAS).
  - Regularly test artefact retrieval to ensure proper functionality.

- **Proactive Diagnostics**:
  - Enable debugging for extended periods when investigating intermittent issues.
  - Collect comprehensive logs and system details during the initial troubleshooting phase.

---

## Escalation Guidelines

- **When to Escalate**:
  - If artefacts or logs remain inaccessible after verifying configurations and storage.
  - If the issue involves complex storage setups or third-party integrations (e.g., NAS).
  - If debugging logs indicate unresolved system-level errors.

- **How to Escalate**:
  - Provide a detailed summary of the issue, including all diagnostic steps taken.
  - Attach relevant logs, configuration files, and screenshots.
  - Clearly outline the impact on the customer’s operations.

