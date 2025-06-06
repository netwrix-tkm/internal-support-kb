# Netwrix Enterprise Auditor Knowledge Base Reference Guide  
## StealthAUDIT for Windows File Systems - Data Collection  

### Overview  
This guide provides a comprehensive reference for troubleshooting and resolving issues related to the **Data Collection** feature in the **StealthAUDIT for Windows File Systems** component of **Netwrix Enterprise Auditor**. It is designed to help support engineers systematically diagnose and resolve problems, ensuring consistent and effective handling of customer cases.  

### Technical Background  
#### Key Concepts  
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, including file systems, Active Directory, and Exchange.  
- **StealthAUDIT for Windows File Systems:** A collector module within NEA designed to scan file systems for permissions, activity, and sensitive data.  
- **Data Collection:** The process of gathering information about file system activity, permissions, and configurations.  

#### Terminology  
- **FSAA:** File System Access Auditing, used for scanning permissions and activity.  
- **FSAC:** File System Activity Collection, used for monitoring file system events.  
- **NAM:** Netwrix Activity Monitor, responsible for collecting and archiving activity data.  
- **Proxy Mode:** A configuration where scans are executed through a proxy server.  
- **Local Mode:** A configuration where scans are executed directly on the NEA host.  
- **Applet Mode:** A configuration where scans are executed using applets running on target systems.  

#### System Context  
- **Certificate Stores:** FSAA Certificate Authority Store and FSAA Client Certificate Store are used for secure communication during scans.  
- **Ports:** Commonly used ports include 8766 and 8767 for communication between NEA and target systems.  
- **Database Tables:** Key tables include `FSAA_Gates`, `SA_FSAA_Resources`, and `SA_FSAC_ActivityEvents`.  

### Issue Recognition & Triage  
#### Symptoms  
- Scans fail to initiate or complete.  
- Errors related to SSL/TLS certificates, missing libraries, or database constraints.  
- Reports display outdated or incomplete data.  
- Excessive scan durations or resource contention.  

#### Priority Assessment  
- **High Priority:** Issues affecting legal or compliance-related data collection.  
- **Medium Priority:** Performance-related issues or incomplete scans.  
- **Low Priority:** Configuration inquiries or feature requests.  

### Diagnostic Methodology  
#### Systematic Approach  
1. **Verify Environment Details:** Confirm NEA version, collector mode, and system configuration.  
2. **Review Logs:** Analyze error messages and warnings in NEA logs.  
3. **Test Connectivity:** Use tools like `Test-NetConnection` to verify communication on required ports.  
4. **Check Permissions:** Ensure service accounts have necessary access to file systems and network shares.  
5. **Inspect Certificates:** Validate the integrity of FSAA Certificate Authority and Client Certificate Stores.  
6. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment.  

#### Decision Points  
- **Configuration Issue:** Adjust settings (e.g., scan depth, thread count).  
- **Resource Contention:** Limit concurrent scans or optimize hardware resources.  
- **Software Bug:** Apply hotfixes or escalate to development teams.  

### Information Collection  
#### Customer Questions  
- What is the NEA version and build number?  
- What mode is the collector configured in (Local, Proxy, Applet)?  
- Are there any third-party security tools installed (e.g., Trellix, Crowdstrike)?  
- Have there been recent system updates or changes?  

#### Logs and Data  
- **Error Logs:** Collect logs from NEA and proxy servers.  
- **Database Queries:** Query relevant tables (e.g., `SA_FSAA_Resources`, `SA_FSAC_ActivityEvents`).  
- **Screenshots:** Capture error messages and job configurations.  
- **Network Tests:** Results from `Test-NetConnection` or similar tools.  

### Common Scenarios & Solutions  
#### Scenario 1: Missing Libraries Preventing Scan Initiation  
- **Symptoms:** Errors referencing `CPasswordSDK.dll` or `libeay32.dll`.  
- **Solution:** Ensure libraries are installed in the correct directories. Delete corrupted certificates from FSAA stores.  
- **Reference Case:** [500Qk00000DB8HJIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DB8HJIA1/view)  

#### Scenario 2: Scheduled Tasks Failing to Execute  
- **Symptoms:** `running.lck` file left behind; tasks complete manually but fail when scheduled.  
- **Solution:** Adjust third-party security tool settings (e.g., Trellix). Verify Group Policy settings.  
- **Reference Case:** [500Qk00000E2QWDIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E2QWDIA3/view)  

#### Scenario 3: SSL/TLS Certificate Validation Errors  
- **Symptoms:** "The remote certificate is invalid according to the validation procedure."  
- **Solution:** Upgrade NEA to the latest version and restart the server. Validate SSL/TLS settings.  
- **Reference Case:** [500Qk00000FpHPeIAN](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FpHPeIAN/view)  

#### Scenario 4: Excessive Scan Durations  
- **Symptoms:** Scans taking 70+ hours to complete.  
- **Solution:** Increase thread count and scan processes. Disable DEBUG logging.  
- **Reference Case:** [500Qk00000LE9fKIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LE9fKIAT/view)  

### Detailed Case Studies  
#### Case Study 1: Duplicate Entries in FSAA_Gates Table  
- **Ticket ID:** [500Qk00000EhvKjIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EhvKjIAJ/view)  
- **Symptoms:** Duplicate entries with matching Share, Folder, and Policy IDs.  
- **Diagnostic Steps:** Coordinated upgrade to NEA v11.6.0.98. Ran `0-CreateSchema` job.  
- **Resolution:** Upgraded NEA and ran schema creation job.  
- **Key Takeaways:** Monitor FSAA_Gates table after upgrades.  

#### Case Study 2: Connection Failures on Ports 8766 and 8767  
- **Ticket ID:** [500Qk00000IH9AzIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IH9AzIAL/view)  
- **Symptoms:** "A connection attempt failed because the connected host has failed to respond."  
- **Diagnostic Steps:** Verified firewall rules and enabled inbound traffic on required ports.  
- **Resolution:** Adjusted firewall settings and re-ran FSAC job.  
- **Key Takeaways:** Ensure consistent firewall configurations across cluster nodes.  

#### Case Study 3: Foreign Key Constraint Errors During Schema Creation  
- **Ticket ID:** [500Qk00000KAkSlIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KAkSlIAL/view)  
- **Symptoms:** "The ALTER TABLE statement conflicted with the FOREIGN key."  
- **Diagnostic Steps:** Investigated SQL script and reset host data.  
- **Resolution:** Reset host and re-ran schema creation job.  
- **Key Takeaways:** Check SQL scripts for compatibility after upgrades.  

### Best Practices & Tips  
- **Certificate Management:** Regularly validate FSAA Certificate Authority and Client Certificate Stores.  
- **Firewall Configuration:** Ensure ports 8766 and 8767 are open and properly configured.  
- **Resource Optimization:** Limit concurrent scans and adjust thread counts in resource-constrained environments.  
- **Regular Updates:** Apply hotfixes and upgrades promptly to benefit from bug fixes and performance improvements.  
- **Documentation:** Maintain clear records of job configurations and system changes for future reference.  

### Escalation Guidelines  
#### Criteria for Escalation  
- Issues involving legal or compliance-related data.  
- Persistent software bugs not resolved by hotfixes.  
- Performance problems affecting critical business operations.  

#### Escalation Procedure  
1. Collect all relevant logs, screenshots, and configuration details.  
2. Document troubleshooting steps taken and results observed.  
3. Submit a detailed escalation request to the development or product management team.  
4. Follow up regularly and communicate updates to the customer.  