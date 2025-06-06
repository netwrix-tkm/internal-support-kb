# Knowledge Base Reference Guide: Troubleshooting Certificate Exchange Issues in StealthAUDIT for Windows File Systems

## Overview

This guide focuses on troubleshooting certificate exchange issues encountered in StealthAUDIT for Windows File Systems, specifically related to the "Credentials" feature. These issues typically arise during scan sessions when authentication fails due to misconfigured permissions or certificate-related errors. Understanding and resolving these problems is critical to ensuring seamless scanning operations across hosts in customer environments.

## Technical Background

### Key Concepts
- **Certificate Exchange**: A process where systems authenticate each other using digital certificates to establish secure communication.
- **Service Account**: A dedicated account used by applications or services to perform automated tasks, often requiring specific permissions.
- **Default Profile**: A pre-configured set of credentials and permissions used by StealthAUDIT for scanning tasks.
- **Fallback Mechanism**: When the default profile fails, StealthAUDIT may attempt to use the local system account or other configured accounts.

### System Context
StealthAUDIT for Windows File Systems relies on secure authentication mechanisms to scan hosts. Proper configuration of service accounts and certificates is essential to avoid disruptions in scanning tasks. Permissions issues or misconfigured profiles can lead to authentication failures, preventing scan sessions from initializing.

## Issue Recognition & Triage

### Symptoms
- Error messages indicating failure to initialize scan sessions.
- Logs showing certificate exchange errors during authentication.
- Scanning tasks failing across multiple hosts.

### Priority Assessment
- **High Priority**: If scanning tasks are critical to the customer's operations and the issue affects multiple hosts.
- **Medium Priority**: If the issue is isolated to specific hosts or non-critical tasks.

## Diagnostic Methodology

### Systematic Approach
1. **Review Error Logs**: Examine logs for certificate exchange errors or authentication failures.
2. **Verify Service Account Permissions**: Check if the service account has the necessary permissions to perform scanning tasks.
3. **Test Default Profile**: Attempt to run scan jobs using the default profile to identify potential misconfigurations.
4. **Check Fallback Behavior**: Determine if the system account or other configured accounts are being used as fallback options.
5. **Validate Certificate Configuration**: Ensure certificates are properly installed and accessible by the service account.

### Decision Points
- If the default profile fails, investigate permissions and configuration.
- If fallback accounts also fail, focus on certificate accessibility and permissions.

## Information Collection

### Customer Questions
- Are you using a default service account or a custom account for scanning tasks?
- Have any recent changes been made to the permissions or configurations of the service account?
- Are certificates installed and accessible on the affected hosts?

### Logs to Examine
- StealthAUDIT scan logs for certificate exchange errors.
- Windows Event Viewer logs for authentication-related events.
- Configuration files for service account and profile settings.

## Common Scenarios & Solutions

### Scenario 1: Default Profile Permissions Issue
- **Symptoms**: Scan jobs fail with certificate exchange errors; fallback to system account also fails.
- **Resolution**: Update permissions for the default profile to ensure the service account can access certificates.

### Scenario 2: Misconfigured Service Account
- **Symptoms**: Scan jobs fail when using a specific service account; other accounts work correctly.
- **Resolution**: Reconfigure the service account with the necessary permissions and validate certificate access.

### Scenario 3: Certificate Installation Problem
- **Symptoms**: Scan jobs fail across all hosts; logs indicate missing or inaccessible certificates.
- **Resolution**: Reinstall certificates on affected hosts and verify their accessibility by the service account.

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000KxAUVIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KxAUVIA3/view)

#### Initial Symptoms
The customer reported scan failures across newly added servers, with error messages indicating certificate exchange issues.

#### Diagnostic Steps
1. Reviewed error logs, confirming certificate exchange failures.
2. Tested scan jobs using the default profile, which failed due to insufficient permissions.
3. Attempted fallback to the system account, which also failed.
4. Changed job configuration to use a specified service account.

#### Key Information Leading to Solution
- Logs indicated that the default profile lacked necessary permissions.
- The fallback mechanism was unable to resolve the issue due to similar permission problems.

#### Resolution
The job configuration was updated to use a specified service account with proper permissions. Scan jobs were successfully completed across all hosts.

#### Key Takeaways
- Always verify permissions for the default profile before initiating scan jobs.
- Document changes to job configurations for future reference.
- Monitor certificate exchange processes closely when adding new hosts.

#### Efficiency Improvements
- Implement automated checks for service account permissions during initial setup.
- Develop a checklist for validating certificate installation and accessibility.

## Best Practices & Tips

1. **Service Account Configuration**: Ensure service accounts have the necessary permissions to access certificates and perform scanning tasks.
2. **Default Profile Validation**: Regularly test the default profile to confirm it is correctly configured.
3. **Certificate Management**: Maintain an inventory of installed certificates and their associated permissions.
4. **Documentation**: Record all changes to job configurations and account settings for future troubleshooting.
5. **Proactive Monitoring**: Use monitoring tools to detect authentication or certificate exchange issues early.

## Escalation Guidelines

### Criteria for Escalation
- The issue persists despite following standard troubleshooting steps.
- The problem affects critical scanning tasks across multiple hosts.
- Logs indicate deeper system-level issues, such as corrupted certificates or network-related authentication failures.

### Escalation Procedure
1. Collect all relevant logs and configuration details.
2. Document troubleshooting steps already performed.
3. Escalate to the appropriate team with a detailed summary of the issue and findings.
4. Provide recommendations for further investigation based on collected data.