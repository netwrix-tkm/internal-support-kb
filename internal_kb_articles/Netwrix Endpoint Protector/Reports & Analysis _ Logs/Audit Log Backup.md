# Knowledge Base Reference Guide: Audit Log Backup in Netwrix Endpoint Protector

## Overview

The **Audit Log Backup** feature in Netwrix Endpoint Protector (EPP) is a critical component for managing log retention and ensuring compliance with organizational and regulatory requirements. This guide provides a comprehensive reference for support engineers to troubleshoot and resolve issues related to log retention, customization, and backup configuration. Understanding this category is essential for maintaining system performance, ensuring data integrity, and meeting compliance standards.

---

## Technical Background

### Key Concepts
- **Audit Logs**: Logs generated by Netwrix Endpoint Protector to track system activities, user actions, and device interactions.
- **Log Retention**: The duration for which logs are stored on the server before being archived or deleted.
- **Audit Log Backup**: A feature that allows administrators to configure the retention period for logs and manage their backup settings.

### System Context
- Logs are stored in the EPP database and can be accessed via the **Reports & Analysis** section.
- The **Audit Log Backup** feature is located under **System Maintenance** and provides options for configuring retention periods and backup settings.
- Log customization (e.g., saving specific types of logs) is not supported in the current version of EPP.

---

## Issue Recognition & Triage

### Common Symptoms
- Customer inquiries about log retention duration.
- Requests to customize the types of logs being saved (e.g., exclude device logs).
- Concerns about database size due to excessive log storage.

### Priority Assessment
- **High Priority**: Issues impacting compliance (e.g., PCI, GDPR) or causing database performance degradation.
- **Medium Priority**: General inquiries about log retention or backup configuration.
- **Low Priority**: Requests for unsupported features, such as log type customization.

---

## Diagnostic Methodology

1. **Understand the Customer's Environment**:
   - Confirm the version of Netwrix Endpoint Protector being used.
   - Identify the customer's compliance requirements or specific concerns.

2. **Clarify the Problem**:
   - Determine whether the issue is related to log retention, backup configuration, or unsupported customization requests.

3. **Access Relevant System Areas**:
   - Navigate to **Reports & Analysis** to review current log data.
   - Check **System Maintenance** -> **Audit Log Backup** for existing configurations.

4. **Evaluate Impact**:
   - Assess whether the issue affects compliance, system performance, or user expectations.

---

## Information Collection

### Questions to Ask the Customer
- What is the desired log retention period?
- Are there specific compliance requirements (e.g., PCI, GDPR) that need to be met?
- Is the concern related to database size or system performance?
- Have any changes been made recently to the Audit Log Backup settings?

### Data to Collect
- Screenshots of the **Audit Log Backup** configuration.
- Logs from the **Reports & Analysis** section to verify retention settings.
- System version details to confirm compatibility with the requested features.

---

## Common Scenarios & Solutions

### Scenario 1: Inquiry About Log Retention Duration
- **Symptoms**: Customer asks how long logs are retained on the server.
- **Resolution**:
  1. Guide the customer to **System Maintenance** -> **Audit Log Backup**.
  2. Explain the default retention settings and how to configure them.
  3. Provide steps to set the retention period to one year or another desired duration.

### Scenario 2: Request to Customize Log Types
- **Symptoms**: Customer wants to stop collecting specific logs (e.g., device logs).
- **Resolution**:
  1. Inform the customer that log type customization is not supported.
  2. Suggest alternative approaches, such as filtering logs during analysis or exporting only relevant data.

### Scenario 3: Concerns About Database Size
- **Symptoms**: Customer reports excessive database growth due to log storage.
- **Resolution**:
  1. Verify the current retention settings in **Audit Log Backup**.
  2. Advise the customer to enable the option to remove older logs after backup.
  3. Recommend regular reviews of log retention policies to align with organizational needs.

---

## Detailed Case Studies

### Case Study: Ticket [500Qk00000NvpdRIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NvpdRIAR/view)
- **Initial Symptoms**: Customer inquired about log retention duration and requested to stop collecting device logs.
- **Diagnostic Steps**:
  1. Confirmed the customer was using Netwrix Endpoint Protector.
  2. Directed the customer to the **Reports & Analysis** section to review stored logs.
  3. Explained the capabilities and limitations of the **Audit Log Backup** feature.
- **Key Information**:
  - Log type customization is not supported.
  - Retention settings can be configured for up to one year.
- **Resolution**:
  1. Guided the customer to **System Maintenance** -> **Audit Log Backup**.
  2. Provided steps to configure the retention period to one year.
  3. Ensured the option to remove older logs after backup was enabled.
- **Key Takeaways**:
  - Clear communication about feature limitations is essential.
  - Providing step-by-step guidance ensures customer satisfaction.
- **Efficiency Improvements**:
  - Develop a pre-written guide for common log retention inquiries to reduce resolution time.

---

## Best Practices & Tips

1. **Proactive Communication**:
   - Clearly explain the capabilities and limitations of the Audit Log Backup feature to set accurate customer expectations.

2. **Compliance Awareness**:
   - Familiarize yourself with common compliance requirements (e.g., PCI, GDPR) to provide tailored recommendations.

3. **Efficient Troubleshooting**:
   - Use a systematic approach to quickly identify and resolve log retention issues.
   - Maintain a repository of pre-written responses for common inquiries.

4. **Regular Reviews**:
   - Encourage customers to periodically review their log retention settings to ensure alignment with organizational needs.

5. **Documentation**:
   - Document all steps taken during troubleshooting to create a reference for future cases.

---

## Escalation Guidelines

### When to Escalate
- The issue involves a potential bug or feature request (e.g., log type customization).
- The customer has compliance-related concerns that require advanced configuration or legal consultation.
- The problem persists despite following standard troubleshooting steps.

### Escalation Procedure
1. Gather all relevant information, including screenshots, logs, and customer requirements.
2. Document the troubleshooting steps already taken.
3. Submit the case to the appropriate escalation team with a detailed summary of the issue and findings.

