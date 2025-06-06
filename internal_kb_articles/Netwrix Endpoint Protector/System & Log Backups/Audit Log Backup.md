# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## System & Log Backups: Audit Log Backup  

### Overview  
The Audit Log Backup feature in Netwrix Endpoint Protector is critical for maintaining system performance, ensuring compliance, and managing disk space effectively. This category covers issues related to audit log backups, including disk space management, log export, shadow file handling, and backup process failures. Understanding these issues is essential for troubleshooting and resolving problems efficiently, minimizing downtime, and ensuring data integrity.  

---

### Technical Background  
#### Key Concepts  
- **Audit Log Backup**: A feature that allows users to back up audit logs to external storage or manage logs within the appliance.  
- **Shadow Files**: Temporary files created during log processing, which can accumulate and consume disk space.  
- **Disk Partitioning**: The allocation of storage space on the appliance, which directly impacts log backup functionality.  
- **Log Retention Policies**: Configurations that determine how long logs are stored before being deleted or backed up.  

#### System Context  
- Netwrix Endpoint Protector appliances rely on sufficient disk space and optimized configurations to perform audit log backups.  
- Logs are exported in CSV format, which can be analyzed using external tools.  
- Backup processes may fail due to expired licenses, insufficient disk space, or misconfigured settings.  

---

### Issue Recognition & Triage  
#### Symptoms  
- Low disk space alerts or warnings.  
- Errors during log backup or export (e.g., "File not found" or "Backup running indefinitely").  
- Logs not being deleted after backup despite configured policies.  
- Missing logs in the Report and Analysis section.  
- Application hangs or unresponsiveness during backup operations.  

#### Priority Assessment  
- **Critical**: Disk space below 10% capacity, application hangs, or inability to perform backups.  
- **High**: Persistent errors preventing log deletion or export.  
- **Medium**: Misconfigured settings or minor delays in backup processes.  

---

### Diagnostic Methodology  
#### Systematic Approach  
1. **Verify Disk Space**: Check available storage on the appliance and identify partitions consuming excessive space.  
2. **Review Configuration**: Ensure log backup and retention policies are correctly set.  
3. **Check Permissions**: Verify directory ownership and permissions for shadow files and backups.  
4. **Analyze Logs**: Collect system logs to identify errors or bottlenecks.  
5. **Test Backup Process**: Attempt manual backups to confirm functionality.  
6. **Engage External Teams**: If network or firewall issues are suspected, collaborate with relevant teams.  

---

### Information Collection  
#### Customer Queries  
- What error messages are being displayed?  
- When did the issue first occur?  
- Have there been any recent changes to the appliance (e.g., upgrades, license renewals)?  
- What is the current disk space status?  

#### Logs/Data to Collect  
- System logs from `/var/eppfiles`.  
- Audit log backup configuration settings.  
- Shadow file directory permissions.  
- Disk usage statistics for all partitions.  

---

### Common Scenarios & Solutions  
#### Scenario 1: Expired or Invalid License  
- **Symptoms**: Unable to delete logs; error during license import.  
- **Solution**: Apply a valid license and verify functionality.  
- **Reference Case**: [500Qk00000CsXRWIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CsXRWIA3/view)  

#### Scenario 2: Low Disk Space  
- **Symptoms**: Backup failures due to insufficient storage.  
- **Solution**: Extend disk partitions or delete older logs and shadow files.  
- **Reference Case**: [500Qk00000Cw4txIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cw4txIAB/view)  

#### Scenario 3: Log Deletion Failure  
- **Symptoms**: Logs not deleted despite configured policies.  
- **Solution**: Verify firewall settings and ensure proper communication with the server.  
- **Reference Case**: [500Qk00000En7AYIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000En7AYIAZ/view)  

#### Scenario 4: Shadow File Directory Ownership  
- **Symptoms**: "File not found" error during log download.  
- **Solution**: Change directory ownership to `www-data`.  
- **Reference Case**: [500Qk00000KaLTpIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KaLTpIAN/view)  

---

### Detailed Case Studies  
#### Case Study 1: [500Qk00000CsXRWIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CsXRWIA3/view)  
- **Symptoms**: Unable to delete old logs due to expired license.  
- **Diagnostic Steps**: Verified license status; identified invalid license file.  
- **Resolution**: Applied valid license; logs successfully deleted.  
- **Key Takeaways**: Always verify license validity before troubleshooting log deletion issues.  

#### Case Study 2: [500Qk00000Cw4txIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cw4txIAB/view)  
- **Symptoms**: Low disk space preventing backups.  
- **Diagnostic Steps**: Accessed disk partition via SSH; extended partition.  
- **Resolution**: Increased disk space; backups resumed successfully.  
- **Key Takeaways**: Monitor disk space regularly and implement alerts for proactive management.  

#### Case Study 3: [500Qk00000KaLTpIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KaLTpIAN/view)  
- **Symptoms**: Error during log download due to shadow file upload issues.  
- **Diagnostic Steps**: Checked directory permissions; identified ownership mismatch.  
- **Resolution**: Changed ownership to `www-data`; logs became downloadable.  
- **Key Takeaways**: Always verify directory permissions and ownership when troubleshooting shadow file issues.  

---

### Best Practices & Tips  
1. **Disk Space Monitoring**: Implement automated alerts for low disk space thresholds.  
2. **Regular Cleanup**: Schedule periodic deletion of older logs and shadow files.  
3. **License Verification**: Ensure customers have valid licenses before troubleshooting.  
4. **Documentation**: Maintain detailed records of configuration changes and troubleshooting steps.  
5. **Customer Education**: Provide training on log backup and export processes to reduce support requests.  

---

### Escalation Guidelines  
#### Criteria for Escalation  
- Persistent application hangs despite troubleshooting.  
- Backup failures due to suspected bugs or system limitations.  
- Network-related issues requiring firewall team intervention.  

#### Escalation Procedure  
1. Collect all relevant logs and configuration details.  
2. Document troubleshooting steps taken.  
3. Submit a detailed escalation request to the appropriate team, including case history and findings.  

---  
End of Document.