# Netwrix Enterprise Auditor Knowledge Base  
## StealthAUDIT Sensitive Data Discovery: Proxy Configuration and Version Compatibility  

### Overview  
This guide addresses issues related to the configuration and version compatibility of Proxy servers in the StealthAUDIT Sensitive Data Discovery (SDD) feature of Netwrix Enterprise Auditor. Proper configuration and version alignment are critical to ensure seamless integration and functionality of Proxy servers. This document provides a systematic approach to diagnosing and resolving issues, along with best practices to prevent future occurrences.  

### Technical Background  
#### Key Concepts  
- **Proxy Servers in SDD**: Proxy servers act as intermediaries between the SDD application and target systems, facilitating data collection and analysis.  
- **Version Compatibility**: All Proxy servers in the environment must run compatible versions to avoid integration issues.  
- **TLS 1.2**: Secure communication between components often requires TLS 1.2, necessitating proper certificate configuration.  

#### Terminology  
- **SDD**: Sensitive Data Discovery, a feature of StealthAUDIT that identifies sensitive information across systems.  
- **Proxy Application**: Software installed on servers to enable communication between SDD and target systems.  
- **Manual Certificate Configuration**: A process to configure certificates for secure communication when automatic configuration fails.  

#### System Context  
- Proxy servers are integral to the SDD feature, enabling secure and efficient data collection.  
- Version mismatches between Proxy servers can lead to communication failures or degraded performance.  

### Issue Recognition & Triage  
#### Symptoms  
- Errors during Proxy server installation or configuration.  
- Communication failures between Proxy servers and the SDD application.  
- Customer concerns about version mismatches.  

#### Priority Assessment  
- **High Priority**: Communication failures affecting data collection.  
- **Medium Priority**: Installation issues with no immediate impact on operations.  
- **Low Priority**: General inquiries about version compatibility.  

### Diagnostic Methodology  
1. **Verify Version Compatibility**  
   - Confirm the version of the new Proxy server application.  
   - Compare it with the versions of existing Proxy servers.  

2. **Check Documentation**  
   - Refer to the latest Netwrix documentation for version compatibility and configuration requirements.  

3. **Review Security Protocols**  
   - Ensure TLS 1.2 is enabled and certificates are correctly configured.  

4. **Test Connectivity**  
   - Perform connectivity tests between the Proxy server and the SDD application.  

5. **Analyze Logs**  
   - Collect and review logs from the Proxy server and SDD application for errors.  

### Information Collection  
#### Questions to Ask the Customer  
- What is the version of the new Proxy server application?  
- What are the versions of the existing Proxy servers?  
- Are there any error messages during installation or configuration?  
- Is TLS 1.2 enabled in the environment?  

#### Logs and Data to Collect  
- Installation logs from the new Proxy server.  
- Configuration files for the Proxy server.  
- Communication logs between the Proxy server and the SDD application.  

### Common Scenarios & Solutions  
#### Scenario 1: Version Mismatch  
- **Symptoms**: Customer reports concerns about version discrepancies.  
- **Resolution**:  
  1. Verify the versions of all Proxy servers.  
  2. Update all Proxy servers to a compatible version.  
  3. Provide guidance on manual certificate configuration if required.  

#### Scenario 2: TLS 1.2 Configuration Issues  
- **Symptoms**: Communication failures due to security protocol mismatches.  
- **Resolution**:  
  1. Confirm that TLS 1.2 is enabled.  
  2. Follow the manual certificate configuration steps in the documentation.  
  3. Test connectivity after configuration.  

### Detailed Case Studies  
#### Case Study 1: Version Compatibility Concern  
- **Ticket ID**: [500Qk00000KGEYFIA5](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KGEYFIA5/view)  
- **Initial Symptoms**: Customer reported concerns about adding a new Proxy server with a different version.  
- **Diagnostic Steps**:  
  1. Reviewed version compatibility.  
  2. Provided documentation links for manual certificate configuration.  
  3. Confirmed potential issues with version mismatches.  
- **Key Information Leading to Solution**: Customer confirmed the version discrepancy and followed the provided configuration steps.  
- **Resolution**: Guided the customer to update all Proxy servers to compatible versions and configure certificates manually.  
- **Key Takeaways**:  
  - Always verify version compatibility before installation.  
  - Provide clear documentation for manual configuration.  
- **Efficiency Improvements**: Develop a pre-installation checklist for customers to verify version compatibility.  

### Best Practices & Tips  
- **Version Management**: Maintain consistent versions across all Proxy servers to avoid compatibility issues.  
- **Documentation Access**: Always refer to the latest Netwrix documentation for configuration and troubleshooting steps.  
- **Pre-Installation Checks**: Verify version compatibility and TLS 1.2 requirements before installing new Proxy servers.  
- **Customer Communication**: Clearly explain the importance of version alignment and provide step-by-step guidance for manual configurations.  

### Escalation Guidelines  
- **When to Escalate**:  
  - If the issue persists after following all troubleshooting steps.  
  - If there are unresolved errors in logs that require development team input.  
  - If the customer environment has unique configurations not covered in standard documentation.  
- **How to Escalate**:  
  1. Collect all relevant logs and configuration files.  
  2. Document the troubleshooting steps already taken.  
  3. Submit a detailed escalation request to the appropriate team.  

