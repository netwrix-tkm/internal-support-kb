# Netwrix Endpoint Protector Server Troubleshooting Guide

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the Netwrix Endpoint Protector (EPP) Server component. It covers common scenarios, diagnostic methodologies, and resolution strategies to ensure consistent and effective support. Understanding this category is critical for maintaining server functionality, resolving customer issues efficiently, and ensuring optimal performance of the Endpoint Protector platform.

---

## Technical Background
Netwrix Endpoint Protector is a Data Loss Prevention (DLP) solution designed to protect sensitive data across endpoints. The Server component acts as the central hub for managing policies, logs, and configurations. Key concepts include:
- **Endpoint Protection Policies (EPP):** Rules applied to endpoints to enforce security measures.
- **Content Aware Protection (CAP):** Policies that monitor and block sensitive data transfers.
- **Virtual Appliance:** A pre-configured virtual machine used to deploy the Endpoint Protector server.
- **Hotfixes:** Updates applied to address vulnerabilities or improve functionality.
- **Migration to SaaS:** Transitioning from on-premises to cloud-based deployment.

---

## Issue Recognition & Triage
### Symptoms to Identify
- Errors during server operations (e.g., boot failures, log display issues).
- Inability to access the web interface or Virtual Appliance.
- Problems with policy enforcement or data collection.
- Requests for administrative tasks (e.g., password resets, migrations).

### Priority Assessment
- **High Priority:** Issues affecting multiple users or critical business operations (e.g., server downtime, data collection failures).
- **Medium Priority:** Configuration or access issues that do not disrupt core functionality.
- **Low Priority:** Administrative requests or minor inconveniences.

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Environment Details:** Confirm server version, policies, and configurations.
2. **Reproduce the Issue:** Attempt to replicate the problem in a controlled environment.
3. **Analyze Logs:** Review server and client logs for error messages or anomalies.
4. **Check Dependencies:** Ensure prerequisites (e.g., network cards, hotfixes) are correctly configured.
5. **Test Solutions Incrementally:** Apply changes step-by-step and validate results.

---

## Information Collection
### Customer Queries
- What is the exact error message or behavior observed?
- When did the issue first occur?
- Have any recent changes been made to the server or environment?
- Are all users affected, or is the issue isolated?

### Logs and Data to Collect
- Server logs and client logs capturing violations or errors.
- Network configurations and firewall settings.
- Hotfix application history.
- Policy settings and applied configurations.

---

## Common Scenarios & Solutions
### Scenario 1: Virtual Appliance Access Failure
**Symptoms:** Unable to access the Virtual Appliance via HTTPS.  
**Solution:** Add a second network card to the Virtual Appliance to enable proper communication.  
**Reference Case:** [500Qk00000DaDFNIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DaDFNIA3/view)

---

### Scenario 2: CAP Logs Not Displayed
**Symptoms:** CAP policy logs missing in the admin console despite correct policy application.  
**Solution:** Reapply updated hotfixes after server upgrades to ensure compatibility.  
**Reference Case:** [500Qk00000DBM7NIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DBM7NIAX/view)

---

### Scenario 3: Data Collection Failure
**Symptoms:** Logs not processed due to insufficient server resources.  
**Solution:** Increase server resources and perform a reboot to resume data collection.  
**Reference Case:** [500Qk00000DlXHBIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DlXHBIA3/view)

---

### Scenario 4: Hotfix Application Errors
**Symptoms:** Unable to apply hotfix due to invalid license.  
**Solution:** Regenerate the license and verify compatibility before applying updates.  
**Reference Case:** [500Qk00000DSU5JIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DSU5JIAX/view)

---

### Scenario 5: Migration to SaaS
**Symptoms:** Assistance required for transitioning from on-premises to SaaS.  
**Solution:** Schedule a migration session, prepare migration images, and ensure smooth execution.  
**Reference Case:** [500Qk00000Dul1cIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Dul1cIAB/view)

---

## Detailed Case Studies
### Case Study 1: Framework Error on macOS
**Ticket ID:** [500Qk00000Cwi8IIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Cwi8IIAR/view)  
**Symptoms:** Error while running Xcode framework; inconsistent behavior across users.  
**Diagnostic Steps:**  
- Verified policies, macOS versions, and EPP settings.  
- Disabled EPP for affected users and analyzed build commands.  
**Resolution:** Adjusted EPP settings and user permissions during remote sessions.  
**Key Takeaways:** Ensure consistent configurations and permissions across users.

---

### Case Study 2: Password Reset Request
**Ticket ID:** [500Qk00000DQjhzIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DQjhzIAD/view)  
**Symptoms:** Request to reset DLP admin console password.  
**Diagnostic Steps:**  
- Confirmed the request and reset the password.  
**Resolution:** Password reset completed successfully.  
**Key Takeaways:** Categorize administrative requests clearly to streamline resolution.

---

### Case Study 3: Server Health Check
**Ticket ID:** [500Qk00000EJTHaIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EJTHaIAP/view)  
**Symptoms:** Scheduled health check session requested.  
**Diagnostic Steps:**  
- Conducted health check remotely and verified results.  
**Resolution:** Health check completed successfully.  
**Key Takeaways:** Communicate prerequisites for health checks in advance.

---

## Best Practices & Tips
- **Consistency:** Ensure uniform configurations across users and endpoints to minimize discrepancies.
- **Documentation:** Maintain detailed records of hotfix applications, migrations, and troubleshooting steps.
- **Proactive Monitoring:** Regularly check server resource usage and apply updates promptly.
- **Customer Communication:** Confirm time zones, language preferences, and prerequisites for sessions.
- **Escalation:** Escalate issues involving critical server failures or unresolved errors after initial troubleshooting.

---

## Escalation Guidelines
### Criteria for Escalation
- Persistent issues after applying standard troubleshooting steps.
- Critical server failures affecting multiple users or business operations.
- Complex problems requiring development team intervention.

### Escalation Procedure
1. Document all troubleshooting steps and collected data.
2. Notify the customer of the escalation and expected timelines.
3. Submit the case to the appropriate team with detailed notes and logs.

--- 

This guide serves as a definitive reference for handling Netwrix Endpoint Protector Server issues, ensuring consistent and effective support delivery.