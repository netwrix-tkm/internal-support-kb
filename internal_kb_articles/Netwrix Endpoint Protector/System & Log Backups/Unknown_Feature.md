# Knowledge Base Reference Guide: Troubleshooting System & Log Backup Issues in Netwrix Endpoint Protector

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to System & Log Backups in Netwrix Endpoint Protector (EPP). It is designed to help support engineers systematically diagnose, resolve, and prevent problems in this category. Understanding backup-related issues is critical to ensuring data integrity, optimizing system performance, and facilitating seamless migrations.

## Technical Background

### Key Concepts
- **System Backup v2**: A feature in EPP that allows administrators to back up system configurations, policies, and other critical data.
- **Backup Configuration**: Determines what data is included in the backup (e.g., settings, policies, logs, entities).
- **AWS Hosting**: EPP servers hosted on Amazon Web Services (AWS) may have unique considerations for storage and performance.
- **PHP Patch**: A code-level update applied to the EPP server to address specific issues, such as optimizing backup processes.

### Terminology
- **Entities**: Includes computers, users, and devices managed by EPP.
- **Event Logs**: Records of system and user activities within EPP.
- **Multi-Factor Authentication (MFA)**: An additional security layer requiring multiple forms of verification for login.

### System Context
System backups are essential for disaster recovery, migrations, and maintaining system integrity. However, misconfigured backups can lead to excessive file sizes, impacting storage and performance.

## Issue Recognition & Triage

### Symptoms
- Discrepancy between the indicated backup size in the EPP console and the actual downloaded file size.
- Unexpectedly large backup files, often including unnecessary data such as logs and entities.
- Issues with restoring backups, such as login failures due to MFA or time synchronization problems.

### Priority Assessment
- **High Priority**: Backup issues affecting production environments or critical migrations.
- **Medium Priority**: Backup size discrepancies in non-critical environments.
- **Low Priority**: General inquiries about backup configuration.

## Diagnostic Methodology

1. **Initial Assessment**:
   - Confirm the reported issue (e.g., backup size discrepancy).
   - Identify the environment (production or test) and EPP version.

2. **Reproduce the Issue**:
   - Attempt to replicate the backup process in the customer's environment.
   - Verify the backup size in the EPP console and compare it to the downloaded file size.

3. **Analyze Backup Configuration**:
   - Check what data is included in the backup (settings, policies, logs, entities).
   - Determine if unnecessary data is contributing to the file size.

4. **Consult Internal Teams**:
   - Engage the server or development team for insights into potential software-level issues.

5. **Apply Fixes and Verify**:
   - Implement patches or configuration changes.
   - Create a new backup and verify the size and contents.

## Information Collection

### Customer Queries
- What is the intended purpose of the backup (e.g., migration, disaster recovery)?
- What data needs to be included in the backup (settings, policies, logs, entities)?
- Are there any specific errors or issues encountered during the backup or restore process?

### Data to Collect
- Full-page screenshot of the EPP system information page.
- Backup configuration settings.
- Logs from the EPP server (if applicable).
- Details about the hosting environment (e.g., AWS).

## Common Scenarios & Solutions

### Scenario 1: Backup Size Discrepancy
- **Symptoms**: Indicated backup size is smaller than the actual downloaded file size.
- **Root Cause**: Inclusion of unnecessary data (logs, entities) in the backup.
- **Resolution**:
  1. Apply a PHP patch to optimize the backup process.
  2. Reconfigure the backup to exclude unnecessary data.
  3. Verify the new backup size.

### Scenario 2: Restore Issues After Migration
- **Symptoms**: Login failures after restoring a backup on a test server.
- **Root Cause**: MFA settings or time synchronization issues.
- **Resolution**:
  1. Reset MFA settings on the test server.
  2. Manually synchronize the server time.
  3. Verify successful login and system functionality.

## Detailed Case Studies

### Case Study: Backup Size Discrepancy (Ticket ID: [500Qk00000C7aZKIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C7aZKIAZ/view))

#### Initial Symptoms
The customer reported that the System Backup v2 size was indicated as 2GB in the EPP console, but the actual downloaded size was approximately 14GB.

#### Diagnostic Steps
1. Reviewed the backup configuration and identified the inclusion of unnecessary data (logs, entities).
2. Consulted the server team to confirm the issue.
3. Scheduled a remote session to access the server back-end via SSH.
4. Applied a PHP patch to optimize the backup process.

#### Key Information Leading to the Solution
- The customer clarified that only settings and policies were required for migration.
- Analysis revealed that event logs and entities were unnecessarily included in the backup.

#### Resolution
- Applied the PHP patch to the production server.
- Created a new System Backup v2, reducing the size to 69MB.
- Reset MFA and synchronized the server time on the test server to ensure successful login.

#### Key Takeaways
- Always confirm the intended purpose of the backup and exclude unnecessary data.
- Verify backup size and contents before proceeding with migrations.
- Address MFA and time synchronization issues during restore processes.

#### Efficiency Improvements
- Develop a pre-migration checklist to ensure optimized backup configurations.
- Automate backup size verification to identify discrepancies early.

## Best Practices & Tips

- **Optimize Backup Configurations**: Exclude unnecessary data (logs, entities) unless explicitly required.
- **Verify Backup Integrity**: Always compare the indicated size in the console with the downloaded file size.
- **Pre-Migration Checklist**: Include steps for verifying backup configurations, resetting MFA, and synchronizing server time.
- **Engage Internal Teams Early**: Consult server or development teams for complex issues.
- **Document Resolutions**: Maintain detailed records of resolved cases for future reference.

## Escalation Guidelines

- **When to Escalate**:
  - Backup issues persist despite applying patches and configuration changes.
  - Critical migrations are at risk due to unresolved backup problems.
  - The root cause involves software-level bugs requiring development intervention.

- **How to Escalate**:
  - Provide a detailed summary of the issue, including logs, screenshots, and diagnostic steps taken.
  - Clearly state the impact on the customer’s environment.
  - Assign the case to the appropriate internal team (e.g., server or development).

