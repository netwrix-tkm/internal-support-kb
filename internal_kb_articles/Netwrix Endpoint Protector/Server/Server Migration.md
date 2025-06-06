# Netwrix Endpoint Protector: Server Migration Knowledge Base Reference Guide

## Overview

Server migration is a critical process for customers transitioning their Netwrix Endpoint Protector (EPP) environments between platforms, operating systems, or hosting providers. This category encompasses migrations involving on-premises servers, cloud platforms (AWS, Azure, GCP), and virtualized environments (VMware, Hyper-V). Understanding the nuances of server migration ensures minimal downtime, data integrity, and seamless client-server communication post-migration.

This guide provides a systematic approach to diagnosing, troubleshooting, and resolving server migration issues. It includes technical background, diagnostic methodologies, common scenarios, and real-world case studies to equip support engineers with the tools to handle these cases effectively.

---

## Technical Background

### Key Concepts
- **System Backup V2**: A critical feature for exporting and importing server configurations, database content, and application sources during migrations.
- **Blob SAS URL**: Used for uploading EPP images to Azure Blob storage during migrations to Azure.
- **AMI (Amazon Machine Image)**: Pre-configured virtual machine images used for deploying EPP servers on AWS.
- **Nginx Configuration**: The web server configuration often requires adjustments during migrations, especially for file upload limits and IP address changes.
- **Endpoint Communication**: Ensuring that EPP clients can connect to the new server post-migration is essential. This often involves updating IP addresses or DNS configurations.

### Terminology
- **DC, DLP, DISCOVERY, ENCRYPTION**: Features of EPP that may require specific configurations during migration.
- **Static IP Address**: A fixed IP assigned to the server, critical for maintaining endpoint communication.
- **SIEM Integration**: Log forwarding to Security Information and Event Management systems, which may require reconfiguration post-migration.

### System Context
- **On-Premises to Cloud**: Migrations often involve transitioning from physical or virtual on-premises servers to cloud platforms like AWS, Azure, or GCP.
- **Operating System Upgrades**: Many migrations include upgrading from older Ubuntu versions (e.g., 14.04, 18.04) to newer versions (e.g., 22.04) for compatibility and security.
- **Resource Optimization**: Cloud environments may require adjustments to CPU, memory, and storage allocations to match workload requirements.

---

## Issue Recognition & Triage

### Common Symptoms
- **Performance Issues**: Slow server response or errors during policy changes post-migration.
- **Client Connectivity Problems**: Clients unable to locate the server due to IP address changes or misconfigurations.
- **Backup/Restore Failures**: System Backup V2 hanging or failing to import/export configurations.
- **Agent Control Issues**: Inability to uninstall or manage agents after server crashes or migrations.
- **Configuration Discrepancies**: Missing settings (e.g., Rights Functionality Priority) after database imports.

### Priority Assessment
- **High Priority**: Cases involving complete server downtime, inability to connect clients, or data loss risks.
- **Medium Priority**: Performance degradation or partial functionality loss.
- **Low Priority**: Non-critical configuration discrepancies or optimization requests.

---

## Diagnostic Methodology

### Systematic Approach
1. **Understand the Migration Scope**:
   - Identify the source and target environments (e.g., on-premises to AWS, Ubuntu 18.04 to 22.04).
   - Confirm the features and configurations in use (e.g., DC, DLP, DISCOVERY).

2. **Verify Prerequisites**:
   - Ensure the source and target servers are running compatible EPP versions.
   - Confirm licensing requirements for the new environment.

3. **Collect Logs and Data**:
   - Gather server logs (`/var/log/nginx/error.log`, `/var/log/syslog`).
   - Request System Backup V2 files and configuration details.

4. **Reproduce the Issue**:
   - Attempt to replicate the reported problem in a controlled environment.

5. **Analyze and Isolate**:
   - Identify root causes using logs, configuration files, and customer-provided details.

6. **Implement and Validate Solutions**:
   - Apply fixes systematically and confirm resolution with the customer.

---

## Information Collection

### Questions to Ask Customers
- What is the source and target environment for the migration?
- Are you using System Backup V2 for the migration? If not, what method are you using?
- Have you updated the server's IP address or DNS configuration?
- Are there any specific error messages or logs available?
- What features (e.g., DC, DLP) are enabled, and how many endpoints are connected?

### Logs and Data to Collect
- **System Logs**: `/var/log/nginx/error.log`, `/var/log/syslog`
- **Backup Files**: System Backup V2 export files
- **Configuration Files**: `epp.yml`, `setup.nginx.conf`
- **Network Details**: IP address, subnet, and firewall rules
- **Resource Allocation**: CPU, memory, and storage details for the server

---

## Common Scenarios & Solutions

### Scenario 1: Performance Issues Post-Migration
- **Symptoms**: Slow server response, errors during policy changes.
- **Solution**: Optimize server settings for the new environment (e.g., adjust Nginx memory limits, allocate additional resources).

### Scenario 2: Client Connectivity Problems
- **Symptoms**: Clients unable to connect to the server after IP address changes.
- **Solution**: Update client configurations with the new server IP or use a dynamic DNS solution.

### Scenario 3: Backup/Restore Failures
- **Symptoms**: System Backup V2 hangs at 99% or fails to import.
- **Solution**: Use the latest version of System Backup V2 and verify backup file integrity.

### Scenario 4: Agent Control Issues
- **Symptoms**: Inability to uninstall or manage agents after server crashes.
- **Solution**: Reinstall the server using the same IP address and reconfigure agents.

### Scenario 5: Configuration Discrepancies
- **Symptoms**: Missing settings (e.g., Rights Functionality Priority) after database imports.
- **Solution**: Manually update configuration files (e.g., `epp.yml`) to restore missing settings.

---

## Detailed Case Studies

### Case Study 1: [500Qk00000BZqyHIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BZqyHIAT/view)
- **Symptoms**: Customer lacked a Blob SAS URL for Azure migration; Nginx memory allocation was insufficient.
- **Diagnostic Steps**:
  1. Provided steps to generate the Blob SAS URL.
  2. Increased Nginx memory allocation.
- **Resolution**: Migration completed successfully after resolving both issues.
- **Key Takeaways**: Ensure prerequisites (e.g., Blob SAS URL) are met before migration. Verify Nginx settings for large file uploads.

### Case Study 2: [500Qk00000DrBfOIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DrBfOIAV/view)
- **Symptoms**: AWS instance flagged as over-provisioned; storage partition size issues.
- **Diagnostic Steps**:
  1. Recommended switching to a smaller instance type (`t3.medium`).
  2. Addressed storage partition size concerns.
- **Resolution**: Customer optimized instance type and resolved storage issues.
- **Key Takeaways**: Differentiate between CPU/RAM and storage-related issues during optimization.

### Case Study 3: [500Qk00000E0mEHIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E0mEHIAZ/view)
- **Symptoms**: "Request Entity Too Large" error during backup import.
- **Diagnostic Steps**:
  1. Identified Nginx upload limit as the root cause.
  2. Increased the `client_max_body_size` parameter in Nginx.
- **Resolution**: Backup import succeeded after adjusting Nginx settings.
- **Key Takeaways**: Review Nginx configuration for large file imports during migrations.

---

## Best Practices & Tips

1. **Pre-Migration Preparation**:
   - Verify compatibility of EPP versions between source and target servers.
   - Back up all data and configurations before initiating migration.

2. **Post-Migration Validation**:
   - Test client connectivity and server performance after migration.
   - Confirm that all configurations and licenses are correctly applied.

3. **Documentation**:
   - Maintain detailed records of migration steps, configurations, and troubleshooting actions.

4. **Communication**:
   - Keep customers informed throughout the migration process.
   - Provide clear instructions for updating client configurations.

5. **Resource Planning**:
   - Allocate sufficient CPU, memory, and storage based on workload requirements.
   - Optimize server settings for the target environment (e.g., cloud platforms).

---

## Escalation Guidelines

### When to Escalate
- Persistent performance issues despite optimization.
- Backup/restore failures that cannot be resolved with standard tools.
- Licensing or configuration discrepancies requiring engineering intervention.

### How to Escalate
1. Gather all relevant logs, backup files, and configuration details.
2. Document troubleshooting steps taken and results observed.
3. Submit a detailed escalation request to the appropriate team (e.g., DevOps, Engineering).

--- 

This guide serves as a comprehensive reference for handling server migration cases in Netwrix Endpoint Protector, ensuring consistent and effective support for customers.