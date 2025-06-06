# Comprehensive Knowledge Base Guide: Handling Feature Requests in Netwrix Endpoint Protector

## Overview

Feature requests in Netwrix Endpoint Protector (EPP) involve customer inquiries or suggestions for new functionalities, enhancements to existing features, or clarifications about product capabilities. These requests are critical for improving the product, addressing customer needs, and maintaining satisfaction. This guide provides a systematic approach to handling feature requests, ensuring consistency, efficiency, and clarity in support interactions.

---

## Technical Background

### Key Concepts
- **Feature Requests**: Suggestions or inquiries about adding or modifying product functionality.
- **EPP Components**: Includes server, client agents, reporting tools, and integrations.
- **Hotfixes and Updates**: Periodic patches or updates that may introduce new features or address limitations.
- **System Configuration**: Settings and policies that govern EPP behavior, such as CAP policies, tamper protection, and transfer limits.

### Terminology
- **CAP (Content Aware Protection)**: A feature for monitoring and controlling sensitive data transfers.
- **ICAP (Internet Content Adaptation Protocol)**: A protocol for integrating with third-party tools like Zscaler CASB.
- **Partitions**: Logical divisions in reporting tools that affect data visibility.
- **Tamper Protection**: A security feature preventing unauthorized modifications to EPP services.

### System Context
Netwrix Endpoint Protector operates as a centralized platform for endpoint security, with features spanning device control, content protection, and reporting. Feature requests often arise due to evolving customer environments, regulatory requirements, or integration needs.

---

## Issue Recognition & Triage

### Identifying Feature Requests
Feature requests typically fall into one of the following categories:
1. **Enhancements to Existing Features**: Requests to improve current functionality (e.g., export capabilities, terminology updates).
2. **New Feature Implementation**: Suggestions for entirely new capabilities (e.g., API access, ICAP integration).
3. **Clarifications**: Questions about existing features or their limitations.

### Assessing Priority
- **High Priority**: Requests impacting critical business operations or compliance (e.g., SSL certificate automation, disk space issues).
- **Medium Priority**: Enhancements that improve usability or efficiency (e.g., export functionality, terminology updates).
- **Low Priority**: General inquiries or non-urgent suggestions (e.g., trial activations, version requests).

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Request**: Clarify the customer's needs and expectations.
2. **Verify Current Capabilities**: Check if the requested feature already exists or can be achieved through existing settings.
3. **Investigate Limitations**: Identify any technical or design constraints preventing the requested functionality.
4. **Document the Request**: Record the details for internal tracking and product team review.
5. **Communicate Clearly**: Provide transparent explanations about current capabilities, limitations, and next steps.

---

## Information Collection

### Questions to Ask Customers
- What specific functionality are you requesting?
- How does the current limitation impact your operations?
- Are there any workarounds you’ve tried?
- Can you provide screenshots or examples for clarity?

### Data to Collect
- Product version and environment details.
- Screenshots or error messages (if applicable).
- Logs or reports demonstrating the issue or limitation.

---

## Common Scenarios & Solutions

### Scenario 1: Missing Export Columns
**Case Reference**: [414527](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CqhjVIAR/view)  
- **Issue**: License status column missing in exported data.
- **Solution**: Explained the limitation and documented a feature request for future updates.

### Scenario 2: API Access for Reporting
**Case Reference**: [423077](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GifshIAB/view)  
- **Issue**: Customer requested API access for live dashboards.
- **Solution**: Confirmed API functionality would be available in a future release (EPP Unify).

### Scenario 3: ICAP Integration with Zscaler
**Case Reference**: [439861](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NIStRIAX/view)  
- **Issue**: Inquiry about ICAP integration for Zscaler CASB.
- **Solution**: Confirmed ICAP is not supported, raised a feature request, and suggested testing the latest client version.

### Scenario 4: Terminology Update in Password Notifications
**Case Reference**: [446086](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PVOrDIAX/view)  
- **Issue**: Misleading terminology in password change notifications.
- **Solution**: Raised a feature request to update the terminology for clarity.

---

## Detailed Case Studies

### Case Study 1: Hotfix Application and Agent Updates
**Case Reference**: [414254](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CljVpIAJ/view)  
- **Symptoms**: Agents did not auto-update after applying a hotfix.  
- **Diagnostic Steps**: Verified hotfix application, identified UI limitation.  
- **Resolution**: Provided direct download links for updated agents.  
- **Key Takeaways**: Ensure future updates include client updates in the UI.

### Case Study 2: Disk Space Issues on EPP Server
**Case Reference**: [432972](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ksj4kIAB/view)  
- **Symptoms**: EPP Server disk space at 0%.  
- **Diagnostic Steps**: Reviewed disk usage, identified lack of monitoring.  
- **Resolution**: Increased disk space and recommended regular monitoring.  
- **Key Takeaways**: Implement automated alerts for low disk space.

### Case Study 3: SSL Certificate Automation
**Case Reference**: [437893](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000McU5FIAV/view)  
- **Symptoms**: Customer requested automatic SSL renewal via ACME protocol.  
- **Diagnostic Steps**: Checked existing settings, confirmed feature unavailability.  
- **Resolution**: Documented feature request for future consideration.  
- **Key Takeaways**: Proactively communicate feature request timelines to customers.

---

## Best Practices & Tips

1. **Clarify Requests Early**: Avoid miscommunication by asking detailed questions upfront.
2. **Leverage Existing Features**: Check if current settings or workarounds can address the request.
3. **Document Thoroughly**: Record all feature requests for tracking and prioritization.
4. **Communicate Transparently**: Be honest about limitations and timelines for feature implementation.
5. **Proactively Monitor**: Use alerts and regular checks to prevent recurring issues (e.g., disk space, log exports).

---

## Escalation Guidelines

### When to Escalate
- Requests involving critical business impact or compliance risks.
- Complex technical limitations requiring product team input.
- Repeated customer dissatisfaction due to unresolved feature gaps.

### How to Escalate
1. Document the issue thoroughly, including customer impact and urgency.
2. Submit the feature request to the product team with supporting details.
3. Follow up regularly and keep the customer informed of progress.

---

This guide serves as a comprehensive reference for handling feature requests in Netwrix Endpoint Protector, ensuring consistent and effective support for customers.