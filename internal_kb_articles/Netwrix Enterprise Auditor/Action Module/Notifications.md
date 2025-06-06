# Knowledge Base Reference Guide: Troubleshooting Notification Issues in Netwrix Enterprise Auditor

## Overview

This guide focuses on troubleshooting issues related to the **Notifications** feature within the **Action Module** of Netwrix Enterprise Auditor. Notifications are critical for alerting stakeholders about specific events or changes in the IT environment. Ensuring the reliability and accuracy of notifications is essential for maintaining operational awareness and compliance.

This document provides a systematic approach to identifying, diagnosing, and resolving issues with notifications, including real-world case studies and best practices.

---

## Technical Background

### Key Concepts
- **Action Module**: A component of Netwrix Enterprise Auditor responsible for executing actions such as sending notifications based on predefined criteria.
- **Notification Criteria**: Filters or conditions set by users to determine when notifications should be triggered.
- **Notification Trigger Table**: A database table that stores the conditions and triggers for notifications.
- **Source Table**: The table containing the raw data that is evaluated against the notification criteria.
- **Custom Filters**: SQL-like expressions used to define specific conditions for triggering notifications.

### System Context
The Notifications feature relies on:
1. **Database Tables**: Criteria and triggers are stored in specific tables within the Netwrix database.
2. **Email Configuration**: Notifications are sent via email to designated recipients.
3. **Version-Specific Behavior**: Certain issues may arise due to defects in specific software versions.

Understanding these components is crucial for diagnosing and resolving notification-related issues.

---

## Issue Recognition & Triage

### Symptoms
- Notifications are sent regardless of the specified criteria.
- Notifications are not sent even when criteria are met.
- Incorrect recipients receive notifications.

### Priority Assessment
- **High Priority**: Notifications are sent indiscriminately, potentially causing compliance or operational risks.
- **Medium Priority**: Notifications are delayed or not sent, impacting awareness of critical events.
- **Low Priority**: Minor discrepancies in notification content or formatting.

---

## Diagnostic Methodology

### Step 1: Verify Notification Criteria
- Review the criteria set in the **Analysis Notification module**.
- Confirm that the custom filters are correctly configured.

### Step 2: Check Notification Trigger Table
- Validate the entries in the **Notification Trigger Table** to ensure they match the intended criteria.

### Step 3: Review Email Logs
- Examine email logs to determine if notifications are being sent as expected.
- Look for patterns or anomalies in the logs.

### Step 4: Identify Version-Specific Issues
- Check the software version. Known defects in specific versions may cause unexpected behavior.

### Step 5: Engage Development Team (if needed)
- If the issue appears to be a product defect, consult the development team for further analysis.

---

## Information Collection

### Questions to Ask the Customer
1. What criteria have been configured for the notifications?
2. Are there specific events or changes that should trigger notifications?
3. Who are the intended recipients of the notifications?
4. When did the issue first occur, and has it been consistent?

### Data to Collect
- **Notification Criteria**: Screenshots or exported configurations.
- **Custom Filters**: SQL expressions used in the criteria.
- **Email Logs**: Logs showing sent notifications and their timestamps.
- **Software Version**: Current version of Netwrix Enterprise Auditor.

---

## Common Scenarios & Solutions

### Scenario 1: Notifications Sent Regardless of Criteria
- **Cause**: Product defect in the software version.
- **Solution**: Upgrade to the latest version where the defect is resolved.

### Scenario 2: Notifications Not Sent
- **Cause**: Misconfigured custom filters or email settings.
- **Solution**: Correct the custom filters and verify email configuration.

### Scenario 3: Incorrect Recipients
- **Cause**: Misconfigured recipient list.
- **Solution**: Update the recipient list in the notification settings.

---

## Detailed Case Studies

### Case Study: Notifications Sent Regardless of Criteria
- **Ticket ID**: [500Qk00000DRpDSIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DRpDSIA1/view)
- **Initial Symptoms**: Customer reported that notifications were being sent regardless of the specified criteria.
- **Diagnostic Steps**:
  1. Verified the notification criteria and custom filters.
  2. Checked the **Notification Trigger Table** for discrepancies.
  3. Reviewed email logs to confirm the issue.
  4. Identified the software version as 11.5, which had a known defect.
- **Resolution**: Upgraded the software to version 11.6, which included a fix for the defect.
- **Key Takeaways**:
  - Always verify the software version when troubleshooting notification issues.
  - Known defects should be cross-referenced with release notes for potential fixes.
- **Efficiency Improvements**:
  - Maintain a version-specific defect database for quicker identification of known issues.

---

## Best Practices & Tips

1. **Keep Software Updated**: Regularly upgrade to the latest version to benefit from bug fixes and enhancements.
2. **Document Criteria**: Maintain clear documentation of notification criteria and custom filters for easier troubleshooting.
3. **Monitor Logs**: Regularly review email logs to identify anomalies early.
4. **Version Awareness**: Familiarize yourself with known issues in specific software versions.
5. **Customer Communication**: Clearly explain the root cause and resolution steps to the customer to build trust and confidence.

---

## Escalation Guidelines

### When to Escalate
- The issue persists after following all diagnostic steps.
- The root cause is identified as a product defect requiring development intervention.
- The customer is experiencing significant operational or compliance risks.

### How to Escalate
1. Gather all relevant information, including logs, criteria, and software version.
2. Document the troubleshooting steps already taken.
3. Submit a detailed escalation request to the development team or higher-tier support.

---

This guide serves as a comprehensive reference for troubleshooting notification issues in Netwrix Enterprise Auditor. By following the outlined methodologies and leveraging the provided case studies, support engineers can resolve issues efficiently and effectively.