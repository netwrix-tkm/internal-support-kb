# Knowledge Base Reference Guide: Troubleshooting Credential Issues in Netwrix Access Information Center (AIC)

## Overview
Credential-related issues in the Netwrix Access Information Center (AIC) are a common category of support cases. These issues typically involve authentication failures, database connection problems, service account misconfigurations, or user role permissions. Understanding and resolving these problems is critical to ensuring seamless access to the AIC and maintaining the integrity of audit data. This guide provides a systematic approach to diagnosing and resolving credential-related issues, along with real-world case studies and best practices.

---

## Technical Background
### Key Concepts
- **Access Information Center (AIC):** A web-based portal in Netwrix Enterprise Auditor (NEA) that provides access to audit data and reports.
- **Service Accounts:** Accounts used by AIC to connect to databases, Active Directory (AD), and other services.
- **Authentication Methods:** AIC supports SQL authentication, Active Directory authentication, and built-in admin accounts.
- **IIS vs. New Web Server:** AIC versions prior to 11.6 used IIS for hosting, while later versions transitioned to a new web server, impacting login behavior and domain handling.
- **Base64 Encoding:** A method to embed images or files directly into email templates, used as a workaround for hosting limitations.

### Common Terminology
- **503 Error:** Indicates that the server is temporarily unavailable, often due to misconfigured credentials or service interruptions.
- **Initialization String Error:** A database connection error caused by improperly formatted connection strings.
- **Domain Prefix:** A domain identifier (e.g., `US.East`) required for user authentication in multi-domain environments.

---

## Issue Recognition & Triage
### Symptoms
- Authentication failures (e.g., incorrect credentials, domain prefix issues).
- Database connection errors (e.g., "Initialization string does not conform to specification").
- Service interruptions (e.g., 503 errors).
- Missing data or permissions in the AIC portal.
- Embedded images in emails not loading.

### Priority Assessment
- **High Priority:** Issues preventing all users from accessing the AIC or critical data.
- **Medium Priority:** Issues affecting specific users or features (e.g., email images not loading).
- **Low Priority:** Cosmetic or non-blocking issues (e.g., domain prefix inconvenience).

---

## Diagnostic Methodology
### Step-by-Step Approach
1. **Verify Environment Details:**
   - Confirm AIC version, database type, and authentication method.
   - Identify recent changes (e.g., password updates, upgrades).

2. **Reproduce the Issue:**
   - Attempt to log in using known credentials.
   - Test database connections and service account configurations.

3. **Review Logs:**
   - Check AIC logs for error messages (e.g., initialization string errors).
   - Analyze IIS or web server logs for service interruptions.

4. **Test Built-in Admin Account:**
   - Use the default admin credentials (`admin/sb`) or re-enable the account via SQL if necessary.

5. **Consult Configuration Settings:**
   - Verify service account credentials in IIS or AIC configuration files.
   - Check Active Directory and database permissions.

6. **Engage R&D or SWAT Teams:**
   - Escalate complex issues (e.g., suspected file corruption or undocumented behavior).

---

## Information Collection
### Questions to Ask Customers
- What version of AIC and NEA are you using?
- Have there been any recent changes (e.g., password updates, upgrades)?
- Are you using SQL or Active Directory authentication?
- What error messages are displayed?

### Logs and Data to Collect
- AIC logs (`C:\ProgramData\Netwrix\Logs\AIC`).
- IIS or web server logs (for versions prior to 11.6).
- SQL Server logs (if database connection issues are suspected).
- Screenshots of error messages.

---

## Common Scenarios & Solutions
### Scenario 1: Database Connection Failure
- **Symptoms:** "Initialization string does not conform to specification."
- **Root Cause:** Improperly formatted password from a password manager.
- **Solution:** Manually enter the password, ensuring proper formatting. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FkZoXIAV/view)

### Scenario 2: 503 Service Unavailable
- **Symptoms:** AIC portal inaccessible.
- **Root Cause:** Service account password updated without updating IIS settings.
- **Solution:** Update IIS with the new service account credentials. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G3NYNIA3/view)

### Scenario 3: Active Directory Authentication Failure
- **Symptoms:** "An unknown error has occurred while logging in."
- **Root Cause:** Outdated AD service account credentials.
- **Solution:** Re-enable the built-in admin account via SQL and update AD credentials. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GIhBmIAL/view)

### Scenario 4: Embedded Images Not Loading
- **Symptoms:** Images in emails not displaying.
- **Root Cause:** Images hosted on a server requiring authentication.
- **Solution:** Use Base64 encoding to embed images directly in emails. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000H92s4IAB/view)

### Scenario 5: Domain Prefix Requirement
- **Symptoms:** Users must include domain prefix during login.
- **Root Cause:** Change in web server technology in version 11.6.
- **Solution:** Inform users of the new requirement and update documentation. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IabxyIAB/view)

### Scenario 6: Missing Data in AIC
- **Symptoms:** No data displayed after login.
- **Root Cause:** Insufficient user permissions.
- **Solution:** Log in with the built-in admin account and adjust user roles. [Case Reference](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OX6DhIAL/view)

---

## Detailed Case Studies
### Case Study 1: Database Connection Failure
- **Ticket ID:** [500Qk00000FkZoXIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FkZoXIAV/view)
- **Symptoms:** AIC unable to connect to the database.
- **Key Diagnostic Step:** Reviewed logs indicating an improperly formatted initialization string.
- **Resolution:** Manually entered the password to ensure proper formatting.
- **Takeaway:** Password managers may introduce formatting issues; manual entry can resolve such problems.

### Case Study 2: 503 Service Unavailable
- **Ticket ID:** [500Qk00000G3NYNIA3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000G3NYNIA3/view)
- **Symptoms:** AIC portal inaccessible.
- **Key Diagnostic Step:** Verified IIS settings and identified outdated service account credentials.
- **Resolution:** Updated IIS with the correct credentials.
- **Takeaway:** Always update IIS settings after service account password changes.

### Case Study 3: Missing Data in AIC
- **Ticket ID:** [500Qk00000OX6DhIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OX6DhIAL/view)
- **Symptoms:** No data displayed after login.
- **Key Diagnostic Step:** Logged in with the built-in admin account to verify permissions.
- **Resolution:** Adjusted user roles to grant appropriate permissions.
- **Takeaway:** Ensure user roles are properly configured to avoid access issues.

---

## Best Practices & Tips
1. **Password Management:**
   - Avoid copying passwords directly from password managers; manually verify formatting.
2. **Service Account Updates:**
   - Always update all related configurations (e.g., IIS, AIC) after password changes.
3. **User Roles:**
   - Regularly audit user roles and permissions to prevent access issues.
4. **Documentation:**
   - Clearly communicate changes (e.g., domain prefix requirements) to end users.
5. **Proactive Monitoring:**
   - Periodically review logs and configurations to identify potential issues early.

---

## Escalation Guidelines
- **When to Escalate:**
  - Suspected file corruption or undocumented behavior.
  - Persistent issues after following standard troubleshooting steps.
  - Complex multi-domain authentication problems.
- **How to Escalate:**
  - Provide detailed logs, environment details, and a summary of troubleshooting steps.
  - Engage the SWAT or R&D teams for advanced analysis.