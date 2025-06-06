# Knowledge Base Reference Guide: Troubleshooting SSO Login Issues in Netwrix Endpoint Protector

## Overview

This guide provides a comprehensive reference for troubleshooting Single Sign-On (SSO) login issues in Netwrix Endpoint Protector (EPP). SSO is a critical feature that simplifies user authentication by integrating with identity providers (IDPs) like Okta, Azure AD, and CyberArk. However, misconfigurations, updates, or environmental changes can disrupt SSO functionality, leading to login failures, access restrictions, or other issues. Understanding and resolving these problems efficiently is essential to maintaining system accessibility and minimizing downtime.

---

## Technical Background

### Key Concepts
- **Single Sign-On (SSO):** A user authentication process that allows users to log in once and gain access to multiple systems without re-entering credentials.
- **Identity Provider (IDP):** A service that authenticates users and provides identity information to the application (e.g., Okta, Azure AD, CyberArk).
- **Failover URL:** A backup login URL that bypasses SSO, allowing access to the system in case of SSO failure.
- **SSO Configuration:** Settings that define how the EPP server communicates with the IDP, including redirect URLs, certificates, and user roles.

### Common Components
- **EPP Server:** Hosts the application and manages SSO configurations.
- **SSO Settings:** Includes parameters like redirect URLs, certificates, and user role mappings.
- **Backend Procedures:** Administrative actions performed directly on the server to modify or reset SSO configurations.

### Terminology
- **Super Admin:** A user role with full administrative privileges.
- **Authentication Loop:** A scenario where users are repeatedly redirected to the login page without successful authentication.
- **Session State:** The server's ability to maintain a user's authenticated session.

---

## Issue Recognition & Triage

### Symptoms
- Users unable to log in via SSO.
- Authentication loops or repeated login prompts.
- Error messages such as:
  - "There has been an issue with your Single Sign On Process."
  - `{"code":401,"message":"Authentication with credentials is currently unavailable due to enabled Single Sign-On."}`
- Restricted dashboard access for SSO users.
- Redirection to an IP address instead of a domain.

### Priority Assessment
- **High Priority:** Complete lockout of admin accounts, authentication loops, or production impact.
- **Medium Priority:** Limited access for specific user roles or non-critical environments.
- **Low Priority:** Configuration questions or non-urgent requests for assistance.

---

## Diagnostic Methodology

### Systematic Approach
1. **Verify the Environment:**
   - Confirm the IDP in use (e.g., Okta, Azure AD, CyberArk).
   - Check the EPP server version and hosting platform (e.g., AWS).
2. **Reproduce the Issue:**
   - Attempt to log in using SSO credentials.
   - Test failover URL access if available.
3. **Review Configuration:**
   - Inspect SSO settings, including redirect URLs, certificates, and user roles.
   - Check for recent changes (e.g., updates, configuration modifications).
4. **Analyze Logs:**
   - Collect server logs for error messages related to SSO authentication.
   - Look for discrepancies in time synchronization or session handling.
5. **Engage the Customer:**
   - Gather additional details about the issue and recent changes.
   - Schedule a remote session if necessary.

---

## Information Collection

### Questions to Ask the Customer
- What is the IDP being used (e.g., Okta, Azure AD)?
- Have there been any recent changes to the SSO configuration or server environment?
- Are all users affected, or only specific roles/groups?
- Can you access the failover URL or local admin account?
- What error messages are displayed during login attempts?

### Data to Collect
- SSO configuration details (redirect URLs, certificates, user roles).
- Server logs related to authentication.
- Time synchronization settings on the EPP server.
- Screenshots or recordings of the issue.

---

## Common Scenarios & Solutions

### Scenario 1: Admin Lockout After SSO Configuration
- **Symptoms:** Admin unable to log in after enabling SSO.
- **Resolution:** Disable SSO from the backend, update user roles to Super Admin, and re-enable SSO.  
  [Example Case: Viskase Companies](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BXshdIAD/view)

### Scenario 2: Authentication Loop After Update
- **Symptoms:** Users stuck in a login loop after a server update.
- **Resolution:** Apply backend procedure to fix session handling or roll back the update.  
  [Example Case: Addleshaw Goddard LLP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JXXgbIAH/view)

### Scenario 3: Incorrect Redirect URL
- **Symptoms:** Redirection to an IP address instead of a domain.
- **Resolution:** Correct the SSO settings to use the DNS name.  
  [Example Case: SambaSafety](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Ha61uIAB/view)

### Scenario 4: Misconfigured Certificates
- **Symptoms:** Login failure after uploading an SSL certificate.
- **Resolution:** Remove incorrect SSO settings and recreate them with the correct certificate.  
  [Example Case: Tata Consultancy Services](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PSJPXIA5/view)

### Scenario 5: Limited Dashboard Access for SSO Users
- **Symptoms:** SSO users lack Super Admin permissions.
- **Resolution:** Manually update user roles in the System Configuration.  
  [Example Case: Helsing](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Opv4sIAB/view)

---

## Detailed Case Studies

### Case Study: Viskase Companies
- **Symptoms:** Admin locked out after enabling Okta SSO.
- **Diagnostic Steps:** Disabled SSO, updated user role, re-enabled SSO.
- **Resolution:** Restored access by modifying user roles and SSO settings.
- **Key Takeaways:** Always configure a backup admin account not tied to SSO.

### Case Study: Addleshaw Goddard LLP
- **Symptoms:** Authentication loop after applying update 5.9.4.1.
- **Diagnostic Steps:** Verified update, analyzed logs, rolled back to a stable version.
- **Resolution:** Restored functionality by reverting the update.
- **Key Takeaways:** Test updates in staging environments before production deployment.

### Case Study: Tata Consultancy Services
- **Symptoms:** Lost access after uploading an SSL certificate.
- **Diagnostic Steps:** Removed incorrect SSO settings, recreated configuration.
- **Resolution:** Restored access by correcting the SSO setup.
- **Key Takeaways:** Verify SSL certificates before applying changes.

---

## Best Practices & Tips

1. **Pre-Deployment Checks:**
   - Test SSO configurations in a staging environment.
   - Ensure all admin accounts are configured with appropriate roles.

2. **Backup and Failover:**
   - Maintain a failover URL for emergency access.
   - Document all configuration changes for rollback purposes.

3. **Monitoring and Maintenance:**
   - Regularly update security certificates and time synchronization settings.
   - Monitor server logs for early detection of authentication issues.

4. **Customer Communication:**
   - Provide clear instructions for accessing failover URLs.
   - Educate customers on the importance of maintaining backup admin accounts.

---

## Escalation Guidelines

### When to Escalate
- Persistent issues after applying standard troubleshooting steps.
- Critical production impact with no immediate resolution.
- Complex backend issues requiring development team intervention.

### How to Escalate
- Provide a detailed summary of the issue, including:
  - Customer environment details.
  - Steps taken and results observed.
  - Relevant logs and configuration data.
- Use the internal escalation process to involve the appropriate team.

--- 

This guide serves as a definitive reference for handling SSO login issues in Netwrix Endpoint Protector, ensuring consistent and effective troubleshooting.