# Netwrix Enterprise Auditor Knowledge Base: Upgrade Guide for StealthAUDIT and Related Components

## **Overview**

Upgrading Netwrix Enterprise Auditor (NEA) and its associated components, including StealthAUDIT, Access Information Center (AIC), Sensitive Data Discovery (SDD), and FSAA Proxy, is essential for maintaining compatibility, enhancing functionality, and addressing security vulnerabilities. This guide provides a comprehensive approach to diagnosing, resolving, and preventing upgrade-related issues, ensuring smooth transitions and minimal downtime.

---

## **Technical Background**

### **Key Concepts**
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, including Active Directory, file systems, databases, and sensitive data.
- **StealthAUDIT:** A legacy component of NEA responsible for data collection and reporting.
- **Access Information Center (AIC):** A web-based portal for accessing audit reports and managing configurations.
- **Sensitive Data Discovery (SDD):** A module for identifying sensitive data across file systems and databases.
- **FSAA Proxy:** File System Access Agent proxies used for distributed data collection.

### **Terminology**
- **Upgrade Path:** The sequence of steps required to transition from an older version to a newer version of NEA and its components.
- **Schema Migration:** The process of updating database structures to align with new software versions.
- **SSL Certificate Binding:** The process of associating an SSL certificate with a specific service or port for secure communication.
- **Scheduled Tasks:** Windows Task Scheduler jobs used to automate NEA processes.
- **Pre-flight Checks:** Preparatory steps to ensure readiness for upgrades, including backups and compatibility verification.

### **System Context**
NEA upgrades involve multiple components, including the NEA console, AIC, FSAA proxies, and SDD modules. Each component must be upgraded in sequence to ensure compatibility and functionality. Upgrades may also require adjustments to server configurations, database schemas, and SSL bindings.

---

## **Issue Recognition & Triage**

### **Symptoms of Upgrade Issues**
- Application or service fails to start post-upgrade.
- Errors during schema migration (e.g., "SQL Script Executing: 1 of 3").
- Missing or inaccessible scheduled tasks.
- SSL certificate errors preventing access to AIC or Published Reports.
- Slow performance of the NEA console or AIC.
- Excessive log retention or database deadlocks.

### **Priority Assessment**
- **Critical:** Issues affecting production environments, such as service outages or data loss.
- **High:** Problems preventing scheduled jobs or scans from running.
- **Medium:** Errors related to non-critical components, such as reporting or configuration.
- **Low:** Cosmetic issues or minor inconveniences.

---

## **Diagnostic Methodology**

### **Systematic Approach**
1. **Pre-flight Checks:**
   - Verify current versions of NEA and associated components.
   - Ensure backups of the NEA server, SQL database, and configuration files.
   - Confirm admin access and permissions for the upgrade process.

2. **Upgrade Execution:**
   - Follow documented upgrade procedures for each component.
   - Monitor logs and job statuses during the upgrade.

3. **Post-upgrade Validation:**
   - Test functionality of scans, reports, and web services.
   - Verify SSL bindings and scheduled task registrations.

4. **Troubleshooting:**
   - Analyze error logs and database configurations.
   - Check for missing dependencies or misaligned settings.

---

## **Information Collection**

### **Customer Queries**
- What version of NEA and its components were installed prior to the upgrade?
- Were any errors encountered during the upgrade process?
- Are there specific symptoms or error messages?
- Are backups available for the NEA server and SQL database?
- Are there any custom jobs or configurations in use?

### **Logs and Data to Collect**
- NEA console logs (`C:\ProgramData\Netwrix\Logs`).
- SQL Server logs for schema migration jobs.
- Windows Event Viewer logs (Application and System).
- IIS logs for AIC and Published Reports.
- Scheduled task history and status.

---

## **Common Scenarios & Solutions**

### **Scenario 1: SSL Certificate Binding Errors**
**Symptoms:** Unable to access AIC or Published Reports due to SSL issues.  
**Resolution:**
1. Verify that the SSL certificate is installed in the correct store (Personal > Certificates).
2. Check SSL bindings using:
   ```bash
   netsh http show sslcert
   ```
3. Bind the correct certificate to the required port:
   ```bash
   netsh http add sslcert ipport=0.0.0.0:443 appid= certhash=
   ```
4. Restart IIS and NEA services.

---

### **Scenario 2: Schema Migration Failure**
**Symptoms:** "SQL Script Executing: 1 of 3" error during schema migration.  
**Resolution:**
1. Enable debug logging to capture detailed error messages.
2. Remove foreign key constraints from affected tables:
   ```sql
   ALTER TABLE SA_FSAA_ResourcesScanTypeDetails NOCHECK CONSTRAINT ALL;
   ALTER TABLE SA_FSAA_ResourceMap NOCHECK CONSTRAINT ALL;
   ```
3. Rerun the schema migration job.

---

### **Scenario 3: Missing Scheduled Tasks**
**Symptoms:** Scheduled tasks not appearing post-upgrade.  
**Resolution:**
1. Verify permissions on `C:\Windows\System32\Tasks`.
2. Remove unzipped archives from the Jobs directory.
3. Re-import tasks into Windows Task Scheduler.

---

### **Scenario 4: Slow NEA Console Performance**
**Symptoms:** NEA console runs sluggishly post-upgrade.  
**Resolution:**
1. Monitor server resource usage (CPU, memory).
2. Increase vCPUs and RAM allocation for the NEA server.
3. Optimize database queries and indexes.

---

### **Scenario 5: Excessive Log Retention**
**Symptoms:** FSAA logs exceed configured retention limits.  
**Resolution:**
1. Confirm log retention settings in NEA.
2. Manually delete old logs from the file system.
3. Schedule a cleanup job to prevent future issues.

---

## **Best Practices & Tips**

1. **Pre-flight Preparation:**
   - Always verify compatibility and prerequisites before upgrades.
   - Take full backups of servers and databases.

2. **Documentation:**
   - Follow official upgrade guides for each component.
   - Document any custom configurations for replication post-upgrade.

3. **Monitoring:**
   - Enable debug logging during upgrades to capture detailed error messages.
   - Monitor job statuses and server performance post-upgrade.

4. **Customer Communication:**
   - Provide clear instructions and timelines for upgrades.
   - Follow up with customers to confirm functionality post-upgrade.

---

## **Escalation Guidelines**

### **Criteria for Escalation**
- Persistent errors despite troubleshooting (e.g., schema migration failures).
- Critical functionality impacted (e.g., inaccessible reports or failed scans).
- Performance issues requiring development team intervention.

### **Escalation Process**
1. Gather detailed logs and error messages.
2. Document all troubleshooting steps taken.
3. Submit a ticket to the development team with relevant data and context.
4. Communicate escalation status to the customer and provide updates regularly.

---

## **Detailed Case Studies**

### **Case Study 1: Schema Migration Failure**
**Ticket ID:** [500Qk00000OB5GHIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OB5GHIA1/view)  
**Symptoms:** Schema migration job stuck on "SQL Script Executing: 1 of 3."  
**Resolution:** Removed foreign key constraints, allowing the job to complete successfully.  
**Key Takeaways:** Monitor schema jobs closely and address constraints early.

---

### **Case Study 2: Missing Scheduled Tasks**
**Ticket ID:** [500Qk00000Oe3EHIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Oe3EHIAZ/view)  
**Symptoms:** Scheduled tasks missing post-upgrade.  
**Resolution:** Verified permissions and re-imported tasks successfully.  
**Key Takeaways:** Avoid unzipping archives in the Jobs directory.

---

### **Case Study 3: SSL Certificate Binding Errors**
**Ticket ID:** [500Qk00000GeLz0IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GeLz0IAF/view)  
**Symptoms:** SSL certificate errors when accessing AIC and Published Reports.  
**Resolution:** Deleted old bindings and created new bindings for the updated certificate.  
**Key Takeaways:** Always verify SSL bindings post-upgrade.

---

This guide consolidates all known upgrade-related issues and solutions for NEA and its components. For further assistance, contact Netwrix Support with detailed logs and error descriptions.