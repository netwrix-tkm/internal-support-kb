# Knowledge Base Reference Guide: Troubleshooting Access Auditing Issues in NEA for Nutanix

## Overview

Access Auditing in Netwrix Enterprise Auditor (NEA) for Nutanix enables organizations to monitor and report on file share access activities. This functionality is critical for ensuring compliance, detecting unauthorized access, and maintaining security across Nutanix file shares. Issues in this category typically involve configuration errors, permission mismatches, or environmental factors that prevent successful auditing. This guide provides a systematic approach to diagnosing and resolving these issues.

## Technical Background

### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing IT infrastructure, including file shares, Active Directory, and more.
- **Access Auditing:** A feature that tracks and reports file access activities, providing visibility into user actions.
- **Nutanix File Shares:** Domain-joined file servers managed within Nutanix environments, often used for shared storage.
- **Service Account:** An Active Directory account configured in NEA to access file shares and collect audit data.

### System Context
- NEA communicates with Nutanix file shares using service account credentials.
- Proper permissions and configurations are required for NEA to access file shares and execute auditing jobs.
- Nutanix environments may include security features like "Filesystem Allowlist," which restricts access to specific systems.

## Issue Recognition & Triage

### Symptoms
- "Access Denied" errors when running File Share Access Auditing (FSAA) jobs.
- Failed audit job execution with no data collected.
- Logs indicating permission or connectivity issues.

### Priority Assessment
- **High Priority:** Issues affecting compliance reporting or critical security monitoring.
- **Medium Priority:** Errors in non-critical environments or test configurations.
- **Low Priority:** Minor misconfigurations with no immediate impact.

## Diagnostic Methodology

### Step-by-Step Approach
1. **Verify Configuration:** Ensure NEA and Nutanix settings match the user guide recommendations.
2. **Permission Check:** Confirm the service account has the required roles and access rights.
3. **Connectivity Test:** Use the UNC path to access the file share from the NEA server with service account credentials.
4. **Allowlist Validation:** Ensure the NEA server is included in the Nutanix "Filesystem Allowlist."
5. **Log Analysis:** Collect and review NEA logs for error messages or anomalies.
6. **Engage Product Team:** If necessary, consult with the Netwrix product team for advanced troubleshooting.

## Information Collection

### Customer Questions
- What error messages are displayed when running the FSAA job?
- Has the service account been assigned the "Backup Admin: Backup Access" role?
- Is the NEA server included in the Nutanix "Filesystem Allowlist"?
- Are there any recent changes to the Nutanix environment or Active Directory permissions?

### Logs and Data
- NEA logs from the affected server.
- Screenshots or descriptions of the error messages.
- Configuration details for the Nutanix file share and NEA connection profile.

## Common Scenarios & Solutions

### Scenario 1: Service Account Permission Issues
- **Symptoms:** "Access Denied" error during FSAA job execution.
- **Resolution:** Assign the "Backup Admin: Backup Access" role to the service account and verify file share permissions.

### Scenario 2: NEA Server Not in Allowlist
- **Symptoms:** Connectivity issues when accessing Nutanix file shares.
- **Resolution:** Add the NEA server to the Nutanix "Filesystem Allowlist."

### Scenario 3: Incorrect Configuration in NEA
- **Symptoms:** FSAA job fails without clear error messages.
- **Resolution:** Review NEA settings and ensure the connection profile matches the Nutanix environment.

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000Ks5glIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ks5glIAB/view)
- **Initial Symptoms:** Customer reported "Access Denied" errors when running FSAA jobs against Nutanix file shares.
- **Diagnostic Steps:**
  1. Verified NEA and Nutanix configurations.
  2. Checked service account permissions and roles.
  3. Tested UNC path access from NEA server.
  4. Confirmed NEA server inclusion in the Nutanix "Filesystem Allowlist."
  5. Collected NEA logs for analysis.
- **Key Information:** Service account lacked necessary permissions for file share access.
- **Resolution:** Customer updated permissions for the service account, enabling successful FSAA job execution.
- **Takeaways:** Always verify service account roles and permissions during initial troubleshooting.
- **Efficiency Improvements:** Create a pre-checklist for service account configuration to streamline diagnostics.

## Best Practices & Tips

1. **Pre-Deployment Checklist:** Ensure NEA server configurations, service account permissions, and Nutanix settings are validated before running FSAA jobs.
2. **Permission Documentation:** Maintain clear documentation of required roles and access rights for service accounts.
3. **Log Analysis:** Familiarize yourself with NEA log formats and common error codes to expedite troubleshooting.
4. **Customer Communication:** Provide clear instructions for resolving permission issues and validate changes with the customer.
5. **Escalation Protocols:** Establish criteria for escalating complex cases to the product team or engineering.

## Escalation Guidelines

### Criteria for Escalation
- Persistent issues after verifying configurations and permissions.
- Errors indicating potential bugs or compatibility issues.
- Cases requiring advanced troubleshooting beyond standard procedures.

### Escalation Process
1. Collect all relevant logs, screenshots, and configuration details.
2. Document troubleshooting steps already performed.
3. Submit the case to the product team with a detailed summary of findings.
4. Follow up with the customer regularly to provide updates and ensure resolution.