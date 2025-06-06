# Knowledge Base Reference Guide: Troubleshooting Incorrect Logging in Netwrix Endpoint Protector (EPP)

## Overview

This guide addresses issues related to incorrect logging behavior in Netwrix Endpoint Protector (EPP), specifically when browser downloads are misclassified as potential uploads. Accurate logging is critical for effective security monitoring and compliance, and misclassifications can lead to unnecessary noise in reports, reducing their utility. This document provides a systematic approach to identifying, diagnosing, and resolving such issues, ensuring consistent and efficient support.

## Technical Background

Netwrix Endpoint Protector (EPP) is a data loss prevention (DLP) solution designed to monitor and control data transfers across endpoints. It logs file operations, including uploads, downloads, and other data movements, to help organizations maintain data security. 

### Key Concepts
- **Temporary Files**: Many browsers, such as Chrome, create temporary files (e.g., `.crdownload` files) during downloads. These files may trigger logging events in EPP.
- **Stealthy DPI Driver**: A feature available on Windows systems that enhances the accuracy of data inspection and logging. This feature is not available for Mac or Linux environments.
- **Log Noise**: Unnecessary or irrelevant log entries that can obscure meaningful security events.

### System Context
- **Operating Systems**: The issue primarily affects Mac and Linux environments.
- **Browsers**: Chrome is the browser involved in the reported cases.
- **EPP Logging Mechanism**: Logs are generated based on file operations detected by the system, which may include temporary file creation and browser-server interactions.

## Issue Recognition & Triage

### Symptoms
- Logs show browser downloads as potential uploads.
- Duplicate entries appear for temporary files (e.g., `.crdownload`) and completed files.
- The issue is specific to certain operating systems (Mac, Linux) and browsers (Chrome).

### Priority Assessment
- **High Priority**: If the issue significantly impacts the customer's ability to monitor security events.
- **Medium Priority**: If the issue creates log noise but does not impede critical monitoring.
- **Low Priority**: If the issue is intermittent and does not affect overall functionality.

## Diagnostic Methodology

1. **Initial Assessment**
   - Confirm the operating system and browser version.
   - Verify the EPP version and configuration settings.
   - Determine if the issue is reproducible.

2. **Log Analysis**
   - Request detailed logs from the customer.
   - Look for patterns in the log entries, such as duplicate entries for temporary and completed files.

3. **Configuration Review**
   - Check if any advanced features (e.g., Stealthy DPI Driver) are enabled or applicable.
   - Review the customer's logging and monitoring settings.

4. **Replication**
   - Attempt to replicate the issue in a controlled environment using similar OS and browser configurations.

5. **Root Cause Analysis**
   - Analyze browser behavior during downloads.
   - Investigate how EPP interprets file operations.

## Information Collection

### Questions to Ask the Customer
- What operating systems and browser versions are affected?
- When did the issue first occur?
- Is the issue consistent or intermittent?
- Are there any recent changes to the environment (e.g., updates, configuration changes)?

### Data to Collect
- Detailed EPP logs from affected systems.
- Screenshots of the log entries showing the issue.
- Steps to reproduce the issue, if possible.
- Browser and OS version details.

## Common Scenarios & Solutions

### Scenario 1: Temporary Files Logged as Uploads
- **Symptoms**: Duplicate log entries for `.crdownload` and completed files.
- **Root Cause**: EPP misinterprets temporary file creation as an upload.
- **Resolution**: Advise the customer to monitor for recurrence. If persistent, escalate for further analysis.

### Scenario 2: Browser-Server Interactions Logged as Uploads
- **Symptoms**: Logs show file hashes or metadata being sent to a server.
- **Root Cause**: Browser behavior during downloads triggers logging.
- **Resolution**: Inform the customer that this is expected behavior and provide guidance on filtering such entries.

## Detailed Case Studies

### Case Study: Ticket [500Qk00000NBgwTIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NBgwTIAT/view)
- **Initial Symptoms**: Logs showed browser downloads as potential uploads, with duplicate entries for `.crdownload` and completed files.
- **Diagnostic Steps**:
  1. Requested detailed logs from the customer.
  2. Scheduled a remote session to review the issue.
  3. Suggested enabling the "Use Stealthy DPI Driver" option, later clarifying its unavailability on Mac/Linux.
- **Key Information**: The issue could not be replicated during troubleshooting.
- **Resolution**: The issue resolved itself without further intervention. The customer monitored for recurrence and closed the ticket after no further issues were observed.
- **Key Takeaways**:
  - Temporary file creation during downloads can trigger logging.
  - The "Use Stealthy DPI Driver" option is not applicable for Mac/Linux, limiting troubleshooting options.
  - Encourage customers to monitor and provide detailed logs for intermittent issues.
- **Efficiency Improvements**:
  - Develop a knowledge base article to preemptively address similar issues.
  - Enhance documentation on platform-specific feature availability.

## Best Practices & Tips

1. **Proactive Communication**
   - Clearly explain the limitations of certain features (e.g., Stealthy DPI Driver) on specific platforms.
   - Set realistic expectations for issue resolution timelines.

2. **Efficient Log Analysis**
   - Use filters to isolate relevant entries in large log files.
   - Look for patterns that indicate browser-specific behavior.

3. **Documentation**
   - Maintain up-to-date documentation on known issues and their resolutions.
   - Share insights from resolved cases to improve team knowledge.

4. **Customer Guidance**
   - Provide clear instructions for collecting logs and reproducing issues.
   - Encourage customers to monitor and report intermittent issues promptly.

## Escalation Guidelines

### Criteria for Escalation
- The issue persists despite following standard troubleshooting steps.
- The root cause cannot be identified or resolved within a reasonable timeframe.
- The issue affects multiple customers or has a significant impact on functionality.

### Escalation Procedure
1. Document all troubleshooting steps and findings.
2. Include detailed logs, screenshots, and replication steps.
3. Submit the case to the appropriate escalation team with a summary of the issue and actions taken.

By following this guide, support engineers can systematically address logging issues in Netwrix Endpoint Protector, ensuring efficient resolution and high customer satisfaction.