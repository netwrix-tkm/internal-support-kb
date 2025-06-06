# Netwrix Endpoint Protector Knowledge Base: EPP Client - Other  

## **Overview**  
This guide provides a comprehensive reference for troubleshooting and resolving issues related to the "EPP Client - Other" feature of the Netwrix Endpoint Protector (EPP). It is designed to help support engineers systematically diagnose, resolve, and escalate issues, ensuring consistent and effective customer support. This category encompasses a wide range of client-side issues, including installation, configuration, compatibility, network connectivity, and operational challenges.  

### **Purpose**  
- To streamline the resolution of EPP Client-related issues.  
- To provide a structured framework for identifying root causes and implementing solutions.  
- To enhance customer satisfaction through efficient and accurate support.  

### **Scope**  
This guide focuses on issues involving the EPP Client, including installation, configuration, compatibility, connectivity, and functionality across various operating systems.  

---

## **Technical Background**  

### **Key Concepts**  
- **Netwrix Endpoint Protector (EPP):** A data loss prevention (DLP) solution designed to secure endpoints by controlling device access, monitoring data transfers, and enforcing security policies.  
- **EPP Client:** The software installed on endpoint devices to enforce policies and communicate with the EPP server.  
- **Content Aware Protection (CAP):** A DLP feature that scans files for sensitive data and enforces policies based on predefined rules.  
- **Deep Packet Inspection (DPI):** Analyzes network traffic to enforce security policies, which may cause compatibility issues with certain applications.  
- **Device Control:** Manages access to external devices like USB drives.  
- **Tamper Mode:** A security feature that prevents unauthorized modifications to the EPP client.  
- **Stealthy DPI Driver:** A feature that minimizes interference with third-party applications while maintaining DPI functionality.  

### **Terminology**  
- **Minifilter:** A driver-level setting that intercepts file system operations for enhanced control.  
- **Shadowing:** The process of creating copies of files for auditing purposes.  
- **Advanced Scanning Exceptions:** A configuration list that excludes specific processes or applications from EPP scanning.  
- **Policy Interval Refresh Rate:** The frequency at which the EPP client retrieves updated policies from the server.  
- **Debug Logging:** A mode that captures detailed logs for troubleshooting purposes.  

### **System Context**  
- **Client-Server Communication:** The EPP client communicates with the server to receive policies, report logs, and enforce configurations.  
- **Supported Platforms:** Windows, macOS, and Linux (specific distributions and versions vary).  
- **Third-Party Interactions:** The EPP client may interact with other software, such as VPNs, antivirus programs, and browsers, which can lead to compatibility challenges.  

---

## **Issue Recognition & Triage**  

### **Identifying Issues**  
- **Symptoms:** Common symptoms include blocked access to websites, failed installations, policy enforcement errors, application conflicts, and network connectivity issues (e.g., certificate errors, WebSocket failures).  
- **Customer Reports:** Look for keywords like "offline," "blocked," "not recognized," or "error message."  
- **Logs and Screenshots:** Request logs and screenshots to confirm the reported behavior and identify patterns.  

### **Categorizing Issues**  
1. **Connectivity Issues:** Clients not appearing online or failing to communicate with the server.  
2. **Policy Enforcement Errors:** Issues where policies are not applied as expected.  
3. **Compatibility Challenges:** Conflicts with operating systems, third-party software, or hardware.  
4. **Installation/Uninstallation Errors:** Problems during setup or removal of the EPP Client.  
5. **Performance Issues:** Delays, crashes, or excessive notifications.  

### **Assessing Priority**  
- **High Priority:** Issues affecting multiple users, critical business functions, or security vulnerabilities.  
- **Medium Priority:** Isolated incidents or non-critical functionality issues.  
- **Low Priority:** Informational requests or minor inconveniences.  

---

## **Diagnostic Methodology**  

### **Systematic Approach**  
1. **Understand the Problem:**  
   - Gather detailed information from the customer.  
   - Confirm the environment details (OS, EPP version, network setup).  
2. **Reproduce the Issue:**  
   - Attempt to replicate the problem in a controlled environment.  
   - Use logs and screenshots to verify the reported behavior.  
3. **Analyze Logs:**  
   - Review debug logs, CAP logs, and system logs for errors or anomalies.  
4. **Test Solutions:**  
   - Apply potential fixes incrementally, testing after each change.  
5. **Document Findings:**  
   - Record the steps taken, observations, and outcomes for future reference.  

### **Decision Points**  
- **Connectivity Issue:** Check firewall rules, server certificates, and network routes.  
- **Policy Issue:** Review CAP/DLP settings and whitelist configurations.  
- **Compatibility Issue:** Verify supported OS versions and dependencies.  
- **Installation Issue:** Use offline installation packages and ensure compatibility with the OS version.  

---

## **Information Collection**  

### **Questions to Ask Customers**  
1. What is the affected operating system and version?  
2. What version of the EPP Client and server are in use?  
3. What specific error messages or symptoms are observed?  
4. Are there any recent changes (e.g., upgrades, policy updates)?  
5. Is the issue isolated to specific endpoints or widespread?  

### **Logs and Data to Collect**  
- **EPP Logs:** `eppclient.log`, `eppsupporttool.log` (Windows: `%ProgramFiles%\Netwrix Endpoint Protector\Logs`, Linux: `/var/log/epp-client/`).  
- **Server Logs:** Policy update logs, device exception logs.  
- **System Logs:** Event Viewer (Windows), Console logs (macOS).  
- **Network Logs:** Ping, traceroute, and telnet results.  

---

## **Common Scenarios & Solutions**  

### **Scenario 1: USB Devices Blocked**  
- **Symptoms:** USB keyboards or external drives are blocked.  
- **Solution:** Enable the Minifilter option in EPP settings or adjust device control policies.  

### **Scenario 2: Application Conflicts**  
- **Symptoms:** Applications like Microsoft Teams or Outlook fail to function.  
- **Solution:** Add affected applications to the Advanced Scanning Exceptions list.  

### **Scenario 3: Network Connectivity Issues**  
- **Symptoms:** Certificate errors or WebSocket failures during browsing.  
- **Solution:** Disable DPI temporarily or install a test build with DPI fixes.  

### **Scenario 4: Excessive Temporary File Generation**  
- **Symptoms:** Thousands of `.tmp` files accumulate in the temp directory.  
- **Solution:** Update the EPP client to a version with a fixed `libevent` library.  

### **Scenario 5: Logging Discrepancies**  
- **Symptoms:** Missing file transfer logs for encrypted USB devices.  
- **Solution:** Deploy a test build that resolves logging issues for encrypted partitions.  

---

## **Detailed Case Studies**  

### **Case Study 1: USB Devices Blocked on Windows 11**  
- **Symptoms:** USB keyboards blocked on Windows 11.  
- **Resolution:** Enabled Minifilter in EPP settings.  
- **Key Takeaway:** Ensure compatibility checks during OS upgrades.  

### **Case Study 2: DPI Interfering with Web Browsing**  
- **Symptoms:** WebSocket failures and browsing issues.  
- **Resolution:** Installed a test build with DPI fixes.  
- **Key Takeaway:** Monitor DPI settings for compatibility with web applications.  

### **Case Study 3: VPN Access Blocked**  
- **Symptoms:** SSO sign-in to Proton VPN failed with the EPP client installed.  
- **Resolution:** Enabled the Stealthy DPI Driver to resolve the conflict.  
- **Key Takeaway:** Adjust DPI settings for compatibility with VPNs.  

---

## **Best Practices & Tips**  
1. **Regular Updates:** Keep the EPP Client and server updated to the latest versions.  
2. **Pre-Deployment Testing:** Test policies and configurations in a controlled environment before rollout.  
3. **Clear Communication:** Provide detailed instructions and follow up with customers to confirm resolution.  
4. **Documentation:** Maintain updated guides for common tasks like installation, uninstallation, and policy configuration.  
5. **Proactive Monitoring:** Use alerts and logs to identify issues before they escalate.  

---

## **Escalation Guidelines**  

### **When to Escalate**  
- Issues involving widespread outages or critical functionality.  
- Problems unresolved after applying standard troubleshooting steps.  
- Cases requiring R&D team involvement (e.g., unidentified bugs).  

### **How to Escalate**  
1. Collect all relevant logs and customer details.  
2. Document steps already taken and their outcomes.  
3. Submit a detailed escalation request to the appropriate team.  
4. Follow up regularly to ensure timely resolution and communicate updates to the customer.  

---  

This guide serves as a comprehensive reference for handling EPP Client-related issues, ensuring consistent and effective support delivery.  