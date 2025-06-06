# Netwrix Endpoint Protector: Troubleshooting Content Aware Report and Logging Issues

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to the Content Aware Report and logging mechanisms in Netwrix Endpoint Protector. These issues often involve incorrect or missing log details, which can impact reporting accuracy and system functionality. Understanding and resolving these problems is critical for maintaining system reliability and ensuring accurate data capture for compliance and auditing purposes.

## Technical Background

Netwrix Endpoint Protector is a data loss prevention (DLP) solution designed to monitor, control, and protect sensitive data across endpoints. Key features include Content Aware Protection, which scans and logs sensitive data transfers, and advanced logging mechanisms that capture detailed activity reports.

### Key Concepts
- **Content Aware Report**: A feature that generates logs detailing sensitive data detected during transfers or uploads.
- **Logging Mechanism**: The system responsible for capturing and reporting endpoint activity, including file uploads and website interactions.
- **DPI (Deep Packet Inspection)**: A technology used to analyze network traffic and identify sensitive data transfers.
- **Reporting V2**: An enhanced reporting framework that improves log accuracy and detail.

### Common Challenges
- Missing or incorrect log details in Content Aware Reports.
- Logs capturing generic URLs (e.g., `s3.amazonaws.com`) instead of specific websites used during file uploads.
- Bugs or limitations in older software versions affecting reporting accuracy.

## Issue Recognition & Triage

### Symptoms
- Missing log details in Content Aware Reports.
- Logs showing generic URLs instead of specific websites during file uploads.
- Reports failing to display expected data.

### Priority Assessment
- **High Priority**: Issues affecting compliance or auditing requirements.
- **Medium Priority**: Problems impacting reporting accuracy but not critical operations.
- **Low Priority**: Minor discrepancies in logs with no operational impact.

## Diagnostic Methodology

### Systematic Approach
1. **Verify Symptoms**: Confirm the issue reported by the customer (e.g., missing log details or incorrect URLs).
2. **Check Software Version**: Identify the version of Netwrix Endpoint Protector in use and compare it against known issues or bugs.
3. **Review Configuration**: Examine Content Aware Report settings and logging configurations.
4. **Test Environment**: Reproduce the issue in a controlled environment using similar endpoints, browsers, and websites.
5. **Analyze Logs**: Collect and analyze logs to identify patterns or anomalies.
6. **Escalate if Necessary**: If the issue cannot be resolved through standard troubleshooting, escalate to R&D for further investigation.

## Information Collection

### Customer Questions
- What version of Netwrix Endpoint Protector is currently installed?
- Are all endpoints affected, or only specific ones?
- Which browsers are being used, and does the issue occur across all browsers?
- Have there been any recent system updates or configuration changes?

### Logs and Data to Collect
- Content Aware Report logs.
- Endpoint activity logs.
- Browser-specific logs (if applicable).
- Screenshots or video recordings of the issue.
- Details of websites used during testing (e.g., `Smartsheets.com`, `WeTransfer`).

## Common Scenarios & Solutions

### Scenario 1: Missing Log Details in Content Aware Report
- **Root Cause**: Bug in the previous software version preventing log details from displaying.
- **Solution**: Upgrade to the latest version (e.g., version 5940) to resolve the issue.

### Scenario 2: Logs Capturing Generic URLs Instead of Specific Websites
- **Root Cause**: Limitation in the logging mechanism for websites redirecting uploads to Amazon S3.
- **Solution**: Deploy a test build with modifications to the logging mechanism to capture accurate website information.

## Detailed Case Studies

### Case Study 1: Missing Log Details in Content Aware Report
- **Ticket ID**: [500Qk00000FM0qLIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FM0qLIAT/view)
- **Initial Symptoms**: Customer reported missing Content Detected log details in the Content Aware Report.
- **Diagnostic Steps**:
  1. Reviewed report settings and configurations.
  2. Checked for known issues in the current software version.
  3. Verified recent system changes.
  4. Identified a bug in the previous version causing the issue.
- **Resolution**: Upgraded the software to version 5940, which included fixes for the bug.
- **Key Takeaways**:
  - Always verify the software version against known issues.
  - Ensure customers are on the latest version to avoid recurring problems.

### Case Study 2: Logs Capturing Generic URLs Instead of Specific Websites
- **Ticket ID**: [500Qk00000KbPdWIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KbPdWIAV/view)
- **Initial Symptoms**: Logs showed generic Amazon URLs (`s3.amazonaws.com`) instead of specific websites used during file uploads.
- **Diagnostic Steps**:
  1. Collected logs and conducted remote testing using Edge browser.
  2. Verified the issue persisted across different websites (`Smartsheets.com`, `WeTransfer`).
  3. Escalated to R&D for investigation.
  4. Provided a test build to the customer to address the issue.
- **Resolution**: Test build successfully resolved the issue by modifying the logging mechanism.
- **Key Takeaways**:
  - Escalation to R&D is critical for issues involving system limitations.
  - Test builds should be thoroughly vetted to ensure comprehensive fixes.

## Best Practices & Tips

- **Regular Updates**: Encourage customers to keep their software updated to benefit from bug fixes and enhancements.
- **Thorough Testing**: Reproduce issues in a controlled environment to confirm symptoms and identify root causes.
- **Effective Communication**: Provide clear instructions and updates to customers throughout the troubleshooting process.
- **Documentation**: Maintain detailed records of troubleshooting steps and resolutions for future reference.
- **Proactive Monitoring**: Regularly review logs and reports to identify potential issues before they impact customers.

## Escalation Guidelines

### Criteria for Escalation
- Issues involving system limitations or unresolvable bugs.
- Problems requiring modifications to the software (e.g., test builds).
- Cases where standard troubleshooting steps fail to resolve the issue.

### Escalation Procedure
1. Collect all relevant logs, screenshots, and customer details.
2. Document troubleshooting steps taken and findings.
3. Submit the case to R&D with a detailed summary and supporting data.
4. Follow up regularly to ensure timely resolution and communicate updates to the customer.