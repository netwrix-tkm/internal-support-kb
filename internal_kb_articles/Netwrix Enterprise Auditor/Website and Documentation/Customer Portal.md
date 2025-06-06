# Knowledge Base Reference Guide: Troubleshooting Customer Portal Issues in Netwrix Enterprise Auditor

## Overview
This guide focuses on troubleshooting issues related to the Customer Portal in Netwrix Enterprise Auditor. The Customer Portal is a critical interface for customers to manage accounts, download resources, and access documentation. Ensuring seamless functionality is vital for customer satisfaction and operational efficiency. This document provides a systematic approach to identifying, diagnosing, and resolving common problems reported by customers.

## Technical Background
The Netwrix Customer Portal is a web-based platform that allows customers to:
- Manage user accounts and passwords.
- Access product documentation and resources.
- Download software components and add-ons.

Key components include:
- **Authentication System**: Validates user credentials and email addresses.
- **Resource Management**: Provides access to downloadable files such as modules and report packs.
- **Navigation and Documentation**: Ensures customers can locate relevant resources efficiently.

Common issues arise due to misconfigured accounts, outdated URLs, or unclear navigation paths.

## Issue Recognition & Triage
### Symptoms
- Inability to log in or reset passwords.
- HTTP errors (e.g., 404) when accessing resources.
- Difficulty locating specific downloads or documentation.

### Priority Assessment
- **High Priority**: Issues preventing access to critical resources (e.g., software downloads).
- **Medium Priority**: Problems with navigation or locating non-critical documentation.
- **Low Priority**: Minor inconveniences or questions about portal functionality.

## Diagnostic Methodology
1. **Verify Account Status**:
   - Check if the customer’s email address is correctly configured in the system.
   - Confirm account activation and permissions.

2. **Reproduce the Issue**:
   - Attempt to replicate the problem using the provided details (e.g., URL, email address).

3. **Analyze Logs and Data**:
   - Review portal logs for authentication errors or invalid URL requests.

4. **Identify Root Cause**:
   - Determine whether the issue is due to account configuration, incorrect URLs, or unclear documentation.

## Information Collection
### Questions to Ask Customers
- What specific issue are you experiencing (e.g., login failure, download error)?
- What email address are you using to access the portal?
- Can you provide the exact URL or steps leading to the error?
- Have you tried accessing the portal from a different browser or device?

### Data to Collect
- Customer email address and account details.
- Screenshots of the error or issue.
- Logs from the portal (if accessible).
- URLs provided by the customer.

## Common Scenarios & Solutions
### Scenario 1: Email Not Recognized
**Symptoms**: Customer’s email address is not recognized as a valid business email.  
**Solution**:
1. Verify the email address in the CRM system.
2. Reset the password and communicate the new credentials to the customer.
3. Confirm successful login and update account configuration if necessary.

### Scenario 2: HTTP 404 Error on Download
**Symptoms**: Customer encounters a 404 error when attempting to download a resource.  
**Solution**:
1. Verify the URL provided on the Customer Portal.
2. Update the URL to the correct link.
3. Share the updated URL with the customer and confirm successful download.

### Scenario 3: Difficulty Locating Resources
**Symptoms**: Customer cannot find specific downloads or documentation.  
**Solution**:
1. Provide step-by-step navigation instructions for accessing the required resources.
2. Confirm the customer’s ability to locate and download the files.

## Detailed Case Studies
### Case Study 1: Email Not Recognized ([Ticket ID: 500Qk00000I0hLxIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000I0hLxIAJ/view))
- **Symptoms**: Customer reported issues accessing the portal and resetting the password. Email was not recognized.
- **Diagnostic Steps**:
  1. Verified account status for `greg.dieter@bofa.com`.
  2. Reset the password and communicated it to the customer.
- **Resolution**:
  - Customer successfully logged in using the new password.
- **Key Takeaways**:
  - Ensure email addresses are correctly configured in the CRM system.
  - Follow up with customers to confirm resolution.

### Case Study 2: HTTP 404 Error ([Ticket ID: 500Qk00000JIy9IIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JIy9IIAT/view))
- **Symptoms**: Customer encountered a 404 error when attempting to download the SDD module.
- **Diagnostic Steps**:
  1. Verified the URL provided on the portal.
  2. Identified and corrected the incorrect URL.
- **Resolution**:
  - Shared the correct URL: `https://releases.netwrix.com/products/auditor-enterprise/11.6/auditor-enterprise-sdd-11.6.0.14.zip`.
  - Customer successfully downloaded the module.
- **Key Takeaways**:
  - Regularly review and update URLs on the portal.
  - Ensure accurate documentation for download links.

### Case Study 3: Difficulty Locating Resources ([Ticket ID: 500Qk00000OyXo8IAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OyXo8IAF/view))
- **Symptoms**: Customer could not locate the Power BI Report Pack for Active Directory and Filesystem.
- **Diagnostic Steps**:
  1. Clarified the customer’s request.
  2. Provided detailed navigation instructions for accessing the download section.
- **Resolution**:
  - Customer successfully located and downloaded the required resources.
- **Key Takeaways**:
  - Enhance portal documentation to improve navigation.
  - Provide clear instructions for accessing specific resources.

## Best Practices & Tips
- **Account Management**:
  - Regularly audit customer accounts to ensure email addresses and permissions are correctly configured.
  - Provide clear instructions for password resets and account recovery.

- **URL Validation**:
  - Implement automated checks to identify outdated or incorrect URLs on the portal.
  - Maintain a centralized repository of verified download links.

- **Documentation Improvements**:
  - Continuously update portal navigation guides based on customer feedback.
  - Include screenshots and step-by-step instructions for accessing resources.

- **Customer Communication**:
  - Use clear and concise language when providing instructions.
  - Follow up with customers to confirm issue resolution and satisfaction.

## Escalation Guidelines
- **Escalation Criteria**:
  - Issues affecting multiple customers or critical resources.
  - Problems requiring changes to portal infrastructure or backend systems.
  - Cases unresolved after following standard troubleshooting steps.

- **Escalation Procedure**:
  1. Document all troubleshooting steps and findings.
  2. Notify the appropriate team (e.g., development or infrastructure) with detailed case information.
  3. Monitor progress and provide updates to the customer.

By adhering to these guidelines, support engineers can effectively resolve Customer Portal issues, ensuring a seamless experience for Netwrix customers.