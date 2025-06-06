# Knowledge Base Reference Guide: AWS S3 Buckets Shadows in Netwrix Endpoint Protector

## Overview

This guide focuses on troubleshooting and resolving issues related to the **AWS S3 Buckets Shadows** feature in **Netwrix Endpoint Protector (EPP)**. This feature is critical for securely storing shadow copies and logs in AWS S3 buckets. Understanding the technical requirements, common issues, and resolution strategies is essential for ensuring seamless operation and compliance with customer needs.

## Technical Background

### Key Concepts
- **AWS S3 Buckets Shadows**: A feature that allows EPP to store shadow copies and logs in AWS S3 buckets for backup and compliance purposes.
- **Authentication Requirements**: The current SDK used by EPP requires an **Access Key ID** and **Secret Access Key** for accessing S3 buckets.
- **Internal AWS IAM Roles**: Customers may configure S3 buckets to use internal IAM roles and policies for enhanced security, but this is not currently supported by the SDK.
- **Region-Specific Compliance**: Financial institutions and other regulated industries may require data storage in specific AWS regions to comply with local regulations.

### System Context
- **EPP Server**: Sends logs and shadow copies to the configured S3 bucket.
- **SDK Limitations**: The SDK mandates explicit credentials for authentication, which may conflict with customer configurations that rely on IAM roles.
- **Indirect Artifacts**: Some regions may not be supported for indirect artifact storage, requiring customers to use existing regions or submit feature requests.

## Issue Recognition & Triage

### Symptoms
- Errors when attempting to access or download shadow copies from S3 buckets.
- Requests for adding unsupported AWS regions to the S3 Bucket Region settings.
- Customer inquiries about accessing S3 buckets without credentials.

### Priority Assessment
- **High Priority**: Issues affecting critical operations, such as the inability to download shadow copies or compliance-related region requests.
- **Medium Priority**: Configuration questions or feature requests that do not immediately impact functionality.
- **Low Priority**: General inquiries about feature capabilities or limitations.

## Diagnostic Methodology

1. **Clarify the Customer's Request**:
   - Determine whether the issue is related to authentication, region support, or feature limitations.
   - Confirm the customer's environment and configuration.

2. **Reproduce the Issue**:
   - If possible, replicate the reported behavior in a test environment to validate the problem.

3. **Analyze Logs and Error Messages**:
   - Review logs from the EPP server and AWS S3 bucket for authentication or communication errors.

4. **Verify SDK Requirements**:
   - Confirm whether the customer's configuration aligns with the SDK's authentication requirements.

5. **Check Region Availability**:
   - Validate whether the requested AWS region is supported for indirect artifacts.

## Information Collection

### Questions to Ask the Customer
- What is the specific issue or error message encountered?
- Are you using Access Key ID and Secret Access Key for authentication, or relying on IAM roles?
- Which AWS region is the S3 bucket configured in?
- Are there any regulatory requirements influencing your configuration?

### Logs and Data to Collect
- EPP server logs related to S3 bucket communication.
- AWS S3 bucket access logs.
- Screenshots or detailed descriptions of error messages.
- Details of the IAM role or policy configuration (if applicable).

## Common Scenarios & Solutions

### Scenario 1: Authentication Errors
- **Symptom**: The EPP server cannot access the S3 bucket, and shadow copies fail to upload or download.
- **Root Cause**: The SDK requires explicit credentials (Access Key ID and Secret Access Key), but the customer is using IAM roles.
- **Solution**:
  1. Inform the customer that IAM roles are not supported by the current SDK.
  2. Recommend disabling externalization of logs to store them on the EPP server instead.
  3. Guide the customer on submitting a feature request for IAM role support if needed.

### Scenario 2: Unsupported AWS Region
- **Symptom**: The customer requests an unsupported AWS region for S3 bucket storage.
- **Root Cause**: The requested region is not available in the current EPP configuration.
- **Solution**:
  1. Provide the customer with a list of supported regions.
  2. Suggest submitting a feature request for the desired region.
  3. Confirm that existing regions meet the customer's compliance requirements.

## Detailed Case Studies

### Case Study 1: Authentication Issue with Internal S3 Buckets
- **Ticket ID**: [500Qk00000O6koqIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O6koqIAB/view)
- **Initial Symptoms**: The customer reported that the EPP server could not access an internal S3 bucket without credentials.
- **Diagnostic Steps**:
  1. Clarified the customer's configuration and requirements.
  2. Verified that the SDK requires explicit credentials.
  3. Conducted a remote session to explain the limitation.
- **Resolution**:
  - Confirmed that the SDK does not support IAM roles.
  - Recommended disabling externalization of logs to store them locally on the EPP server.
- **Key Takeaways**:
  - Always verify the customer's authentication method.
  - Clearly communicate SDK limitations and alternative solutions.

### Case Study 2: Request for Unsupported AWS Region
- **Ticket ID**: [500Qk00000P30hsIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000P30hsIAB/view)
- **Initial Symptoms**: The customer requested the addition of the "Asia Pacific (Seoul) ap-northeast-2" region.
- **Diagnostic Steps**:
  1. Reviewed the customer's compliance requirements.
  2. Checked the availability of the requested region.
  3. Suggested submitting a feature request for the region.
- **Resolution**:
  - Guided the customer on submitting a feature request.
  - Provided a list of existing supported regions.
- **Key Takeaways**:
  - Understand the customer's regulatory requirements.
  - Proactively suggest feature requests for unsupported configurations.

## Best Practices & Tips

- **Proactive Communication**: Clearly explain SDK limitations and available alternatives to customers.
- **Feature Requests**: Encourage customers to submit feature requests for unsupported configurations or regions.
- **Log Analysis**: Always review server and S3 bucket logs for authentication or communication errors.
- **Compliance Awareness**: Be mindful of industry-specific regulations that may influence customer configurations.
- **Documentation**: Maintain up-to-date documentation on supported regions and authentication methods.

## Escalation Guidelines

- **When to Escalate**:
  - The issue involves a critical bug or limitation requiring development team intervention.
  - The customer has regulatory deadlines that cannot be met with existing functionality.
  - The requested feature or region is not documented or supported.

- **How to Escalate**:
  1. Collect all relevant logs, error messages, and configuration details.
  2. Document the customer's requirements and urgency.
  3. Submit the case to the development team with a detailed summary and supporting evidence.

