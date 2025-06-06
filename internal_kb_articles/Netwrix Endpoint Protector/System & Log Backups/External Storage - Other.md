# Knowledge Base Reference Guide: System & Log Backups - External Storage Configuration

## Overview
This guide focuses on troubleshooting and resolving issues related to the configuration of external storage for system and log backups in Netwrix Endpoint Protector (EPP). External storage is a critical feature for ensuring data redundancy, disaster recovery, and compliance with organizational backup policies. Understanding common issues and their resolutions is essential for maintaining system reliability and customer satisfaction.

## Technical Background
### Key Concepts
- **External Storage**: Refers to the use of network shares (e.g., SMB, SFTP) or cloud-based storage solutions for storing system backups and shadow files.
- **Shadow Files**: Copies of files created by EPP for monitoring and compliance purposes.
- **System Backup Versions**: EPP supports multiple backup versions, including "System Backup v1" and "System Backup v2," with varying compatibility for external storage.
- **Content Aware Protection**: A feature that scans files for sensitive content and applies policies to protect them.

### Terminology
- **SMB (Server Message Block)**: A protocol for sharing files, printers, and other resources over a network.
- **SFTP (Secure File Transfer Protocol)**: A secure method for transferring files over a network.
- **Azure SMB**: A cloud-based storage solution compatible with EPP for external storage.

### System Context
Netwrix Endpoint Protector integrates with external storage solutions to facilitate backups and shadow file management. Compatibility and proper configuration are essential for seamless operation. Certain features, such as Content Aware Protection and specific backup versions, may have limitations that impact external storage functionality.

## Issue Recognition & Triage
### Symptoms
- Shadow files not appearing on external storage.
- System backups failing to transfer to external storage.
- Authentication errors when configuring external storage.
- Compatibility issues with specific storage solutions (e.g., Azure Blobs).

### Priority Assessment
- **High Priority**: Issues affecting system backups or shadow file compliance.
- **Medium Priority**: Configuration errors or compatibility concerns.
- **Low Priority**: General inquiries about best practices or feature limitations.

## Diagnostic Methodology
### Step-by-Step Approach
1. **Verify External Storage Configuration**:
   - Confirm network share details (e.g., SMB/SFTP credentials).
   - Test accessibility of the external storage from the EPP server.

2. **Check Feature Compatibility**:
   - Determine if the backup version or storage solution is supported.
   - Review documentation for known limitations (e.g., Azure Blobs incompatibility).

3. **Inspect Local Directories**:
   - Check the local shadow file directory (`C:\Windows\System32\config\systemprofile\AppData\Local\CoSoSys\EPP\shadows`) for file presence.

4. **Engage Engineering Team**:
   - For unresolved issues, consult the engineering team to verify compatibility or identify potential bugs.

5. **Communicate Findings**:
   - Provide clear explanations to the customer, including workarounds or feature requests.

## Information Collection
### Customer Questions
- What type of external storage is being used (e.g., SMB, SFTP, Azure)?
- Are the credentials and network share details correctly configured?
- What version of EPP is installed?
- Are there specific error messages or logs available?

### Logs and Data to Collect
- EPP server logs related to backups and shadowing.
- Screenshots of external storage configuration settings.
- Network connectivity test results (e.g., ping or traceroute to the storage server).

## Common Scenarios & Solutions
### Scenario 1: Shadow Files Not Transferred to External Storage
- **Root Cause**: Files with Content Aware Protection are not shadowed due to feature limitations.
- **Solution**: Test shadowing with files that do not have Content Aware Protection enabled. Inform the customer of the limitation and recommend monitoring shadowing for compliance.

### Scenario 2: System Backups Not Appearing on External Storage
- **Root Cause**: "System Backup v2" is not supported for external storage.
- **Solution**: Advise the customer to use "System Backup v1" for external storage until future updates include support for "System Backup v2."

### Scenario 3: Authentication Errors with Azure Blobs
- **Root Cause**: Azure Blobs are not officially supported for external storage in EPP.
- **Solution**: Recommend switching to Azure SMB for external storage configuration. Provide guidance on setup and testing.

## Detailed Case Studies
### Case Study 1: Shadowing Issue with Content Aware Protection
- **Ticket ID**: [500Qk00000IcDl4IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IcDl4IAF/view)
- **Symptoms**: Shadow files with Content Aware Protection were not appearing on external storage.
- **Diagnostic Steps**:
  - Verified external storage configuration.
  - Tested shadowing with and without Content Aware Protection.
  - Checked local shadow file directory.
- **Resolution**: Recommended testing with files without Content Aware Protection. Informed the customer of the feature limitation.
- **Key Takeaways**: Monitor shadowing for compliance and communicate feature limitations clearly.

### Case Study 2: Weekly Backup Configuration via SMB
- **Ticket ID**: [500Qk00000IfDGhIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IfDGhIAN/view)
- **Symptoms**: Customer needed assistance configuring weekly backups to external storage.
- **Diagnostic Steps**:
  - Confirmed Samba/Network share details and credentials.
  - Verified external storage accessibility.
  - Discussed best practices for system backups.
- **Resolution**: Guided the customer through the configuration process. Customer successfully created a snapshot of the EPP server on Nutanix.
- **Key Takeaways**: Regular backups are essential for server restoration. Include all relevant stakeholders in troubleshooting discussions.

### Case Study 3: Azure Blobs Authentication Error
- **Ticket ID**: [500Qk00000OICZbIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OICZbIAP/view)
- **Symptoms**: "Incorrect credentials" error when configuring external storage using Azure Blobs.
- **Diagnostic Steps**:
  - Conducted remote session to verify SFTP access and TLS settings.
  - Consulted engineering team regarding Azure Blobs compatibility.
  - Tested Azure SMB as an alternative.
- **Resolution**: Switched to Azure SMB for external storage configuration. Customer successfully set up external storage.
- **Key Takeaways**: Azure Blobs are not supported; always recommend Azure SMB. Verify compatibility with engineering for unusual storage solutions.

## Best Practices & Tips
- **Configuration Validation**: Always verify external storage settings, including credentials and network accessibility.
- **Feature Awareness**: Stay informed about feature limitations and compatibility updates.
- **Customer Communication**: Clearly explain limitations and provide actionable recommendations.
- **Proactive Monitoring**: Encourage customers to regularly test backups and shadowing processes.
- **Documentation**: Maintain detailed records of troubleshooting steps and resolutions for future reference.

## Escalation Guidelines
### Criteria for Escalation
- Issues involving unsupported storage solutions requiring engineering input.
- Persistent errors despite following standard troubleshooting steps.
- Requests for feature enhancements or compatibility updates.

### Escalation Procedure
1. Gather all relevant logs, screenshots, and configuration details.
2. Submit a detailed report to the engineering team, including customer impact and urgency.
3. Communicate escalation status to the customer and provide regular updates.

End of document.