# Netwrix Endpoint Protector: Comprehensive Guide to Troubleshooting eDiscovery Issues

## Overview

This guide provides a systematic approach to understanding, diagnosing, and resolving issues related to the eDiscovery feature in Netwrix Endpoint Protector (EPP). The eDiscovery feature is critical for identifying, managing, and securing sensitive data across endpoints. This document is designed to equip support engineers with the knowledge and tools necessary to handle common eDiscovery-related issues effectively and consistently.

## Technical Background

### Key Concepts
- **eDiscovery**: A feature in Netwrix Endpoint Protector that scans endpoints for sensitive data based on predefined policies and allows actions such as encryption, deletion, or reporting.
- **Encryption Algorithm**: The method used to secure sensitive data during eDiscovery actions. For example, AES-256 is a widely recognized encryption standard.
- **Log Retention**: The duration for which scan results and logs are stored on the server, which impacts the availability of historical data.
- **Device Whitelisting**: A process to exclude specific devices from eDiscovery actions by adding them to a whitelist based on identifiers like VID (Vendor ID) and PID (Product ID).

### System Context
- **Admin Console**: The primary interface for configuring and managing eDiscovery settings, including scan policies, encryption options, and device control.
- **Audit Log Backup**: A repository for archived logs that may contain historical data beyond the server's active retention period.
- **Display Settings**: Configurations in the admin console that control the number of records displayed in reports or device lists.

## Issue Recognition & Triage

### Common Symptoms
- Customer inquiries about encryption algorithms and strengths.
- Requests for historical eDiscovery scan data beyond the server's log retention period.
- Limitations in the number of devices displayed in the admin console.
- Challenges in whitelisting devices due to incorrect detection or missing serial numbers.

### Priority Assessment
- **High Priority**: Issues involving encryption details or data security concerns.
- **Medium Priority**: Requests for historical data that may require log recovery.
- **Low Priority**: Display limitations or configuration adjustments in the admin console.

## Diagnostic Methodology

1. **Understand the Customer's Request**: Clarify the specific issue or information the customer needs.
2. **Verify the Environment**: Confirm the product version, platform, and relevant settings in the admin console.
3. **Reproduce the Issue**: If applicable, attempt to replicate the problem in a test environment.
4. **Consult Documentation**: Check internal and external resources for relevant information.
5. **Escalate if Necessary**: Engage the engineering team for technical details or unresolved issues.

## Information Collection

### Questions to Ask the Customer
- What specific information or functionality are you looking for?
- What version of Netwrix Endpoint Protector are you using?
- Have you made any recent changes to eDiscovery policies or settings?
- Can you provide screenshots or logs demonstrating the issue?

### Logs and Data to Collect
- **eDiscovery Scan Logs**: For analyzing scan results and actions.
- **Audit Log Backup**: For retrieving historical data.
- **Admin Console Settings**: Screenshots of relevant configurations, such as display settings or device control policies.

## Common Scenarios & Solutions

### Scenario 1: Encryption Algorithm Inquiry
- **Symptom**: Customer requests details about the encryption algorithm used in eDiscovery.
- **Solution**: Confirm with the engineering team that eDiscovery uses AES-256 encryption. Communicate this information to the customer.
- **Reference Case**: [500Qk00000HRdWYIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HRdWYIA1/view)

### Scenario 2: Insufficient Historical Data
- **Symptom**: Customer requests eDiscovery scan results for a period longer than the server's log retention.
- **Solution**: Advise the customer to check the Audit Log Backup for older logs. Recommend adjusting log retention settings to meet future needs.
- **Reference Case**: [500Qk00000LU9zSIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LU9zSIAT/view)

### Scenario 3: Device Display Limitations
- **Symptom**: Admin console displays a maximum of 200 devices, even when higher options are selected.
- **Solution**: Guide the customer to adjust the "Maximum no. of records returned in a report search" setting in the admin console. Provide instructions for configuring devices using VID and PID.
- **Reference Case**: [500Qk00000N77ytIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000N77ytIAB/view)

## Detailed Case Studies

### Case Study 1: Encryption Algorithm Inquiry
- **Initial Symptoms**: Customer requested details about the encryption algorithm used in eDiscovery.
- **Diagnostic Steps**: Escalated the inquiry to the engineering team for confirmation.
- **Key Information**: Engineering confirmed the use of AES-256 encryption.
- **Resolution**: Communicated the encryption details to the customer.
- **Key Takeaways**: Ensure encryption details are documented for future reference. Escalate similar inquiries to the engineering team for accuracy.

### Case Study 2: Insufficient Historical Data
- **Initial Symptoms**: Customer needed eDiscovery scan results for six months, but only two months of logs were available.
- **Diagnostic Steps**: Verified the server's log retention settings and suggested checking the Audit Log Backup.
- **Key Information**: Older logs were available in the Audit Log Backup.
- **Resolution**: Advised the customer to retrieve the necessary data from the backup.
- **Key Takeaways**: Proactively review log retention settings to align with customer needs. Educate customers on using the Audit Log Backup.

### Case Study 3: Device Display Limitations
- **Initial Symptoms**: Admin console displayed only 200 devices, regardless of selecting higher options.
- **Diagnostic Steps**: Guided the customer to adjust display settings and provided instructions for whitelisting devices using VID and PID.
- **Key Information**: The default display limit was causing the issue.
- **Resolution**: Adjusted the display settings and configured devices using VID and PID.
- **Key Takeaways**: Familiarize customers with display settings and alternative device configuration methods.

## Best Practices & Tips

- **Document Encryption Standards**: Maintain up-to-date documentation on encryption algorithms and strengths for quick reference.
- **Proactive Log Management**: Regularly review and adjust log retention settings to meet customer requirements.
- **Educate Customers**: Provide clear instructions for using advanced features, such as VID and PID-based device configuration.
- **Leverage Audit Log Backup**: Use the backup repository to retrieve historical data when server logs are insufficient.
- **Escalate When Necessary**: Engage the engineering team for technical details or unresolved issues to ensure accurate and timely resolutions.

## Escalation Guidelines

- **When to Escalate**:
  - Customer inquiries about encryption algorithms or other technical details not documented.
  - Issues that cannot be resolved through configuration changes or log retrieval.
  - Bugs or limitations in the admin console that require development intervention.

- **How to Escalate**:
  - Provide a detailed summary of the issue, including screenshots, logs, and customer requirements.
  - Use the internal escalation process to engage the engineering or development team.
  - Follow up regularly to ensure timely resolution and communicate updates to the customer.