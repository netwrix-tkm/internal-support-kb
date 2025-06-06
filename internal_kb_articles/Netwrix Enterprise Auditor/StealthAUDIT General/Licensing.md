# Netwrix Enterprise Auditor Licensing Troubleshooting Guide

## Overview
Licensing issues in Netwrix Enterprise Auditor (NEA) are critical to address as they directly impact the functionality and accessibility of the product. This guide provides a systematic approach to identifying, diagnosing, and resolving licensing-related problems, ensuring minimal disruption to customer operations. It covers common scenarios, resolution strategies, and best practices for handling licensing issues effectively.

---

## Technical Background
### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, formerly known as StealthAUDIT.
- **Licensing Model:** NEA licenses are typically tied to active Active Directory (AD) user counts or specific features (e.g., AD monitoring, Azure integration).
- **License File:** A digital file that activates specific features and permissions within NEA. Incorrect or expired licenses can lead to functionality issues.
- **Customer Portal:** A platform where customers can manage licenses, download software, and access support resources.

### Terminology
- **Active Directory (AD):** A directory service used for managing user accounts and permissions.
- **Azure License:** Required for certain integrations, such as retrieving detailed user information.
- **NFR License:** Non-Production licenses provided for testing or evaluation purposes.

---

## Issue Recognition & Triage
### Symptoms
- Application displays messages about expired or invalid licenses.
- Specific features (e.g., AD monitoring) fail to function due to licensing restrictions.
- Missing download links for licensed products in the customer portal.
- Unexpected behavior, such as Security Identifiers (SIDs) displayed instead of user names.

### Priority Assessment
- **High Priority:** Issues causing complete application inaccessibility or critical feature failure.
- **Medium Priority:** Licensing renewal requests with impending expiration dates.
- **Low Priority:** General inquiries about licensing models or compatibility.

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Licensing Status:** Check the customer's license details, including expiration date and included features.
2. **Review Logs:** Analyze application logs for error messages related to licensing.
3. **Confirm File Properties:** Ensure the license file is unblocked and correctly applied.
4. **Check Portal Access:** Verify if the customer can access the necessary download links.
5. **Engage Account Manager:** Coordinate with the sales or licensing team for unresolved issues.

### Decision Points
- If the license is expired, proceed with renewal steps.
- If the license file is invalid or missing features, request a corrected file.
- If the issue is related to portal access, escalate to the sales team.

---

## Information Collection
### Customer Questions
- What error message or behavior are you experiencing?
- When did the issue first occur?
- Have you recently updated or renewed your license?
- Are you using the correct license file for your product version?

### Logs/Data to Collect
- Application logs showing licensing-related errors.
- Screenshot of the error message or behavior.
- License file details (e.g., file name, permissions).
- Machine ID for license renewal requests.

---

## Common Scenarios & Solutions
### Scenario 1: Expired License
- **Symptoms:** Application displays "license expired" message.
- **Solution:** Generate a new license file and provide step-by-step instructions for updating the license. Ensure all instances of NEA are closed before applying the new file.

### Scenario 2: Missing Features in License File
- **Symptoms:** Specific features (e.g., AD monitoring) are unavailable.
- **Solution:** Verify the license file contents and request a corrected file from the licensing team.

### Scenario 3: Incorrect License Applied
- **Symptoms:** Customer attempts to apply a license for a different product (e.g., Netwrix Auditor instead of NEA).
- **Solution:** Clarify product differences and provide the correct license file.

### Scenario 4: Portal Access Issues
- **Symptoms:** Customer cannot find download links for NEA.
- **Solution:** Verify licensing status and escalate to the sales team to update portal access.

### Scenario 5: User Identification Issues
- **Symptoms:** SIDs displayed instead of user names in the Activity Information Center (AIC).
- **Solution:** Inform the customer that an Azure license is required for detailed user information.

---

## Detailed Case Studies
### Case Study 1: Expired License Issue  
**Ticket ID:** [500Qk00000BX406IAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BX406IAD/view)  
- **Symptoms:** Application displayed "license expired" message.  
- **Diagnostic Steps:** Verified license expiration, generated a new license file, and provided instructions for updating the file.  
- **Resolution:** Customer successfully activated the new license during a follow-up meeting.  
- **Key Takeaways:** Ensure all instances of NEA are closed before applying a new license. Verify file properties to ensure the license file is unblocked.

### Case Study 2: Missing Features in License File  
**Ticket ID:** [500Qk00000EJ1V0IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EJ1V0IAL/view)  
- **Symptoms:** StealthAUDIT job failed due to licensing restrictions for AD actions.  
- **Diagnostic Steps:** Reviewed logs and confirmed the license file did not include necessary permissions.  
- **Resolution:** Provided a corrected license file with AD monitoring permissions.  
- **Key Takeaways:** Verify license contents upon receipt to ensure all required features are included.

### Case Study 3: Incorrect License Applied  
**Ticket ID:** [500Qk00000EP9G9IAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EP9G9IAL/view)  
- **Symptoms:** Customer attempted to apply a Netwrix Auditor license to NEA.  
- **Diagnostic Steps:** Identified the incorrect license and coordinated with the Account Manager for resolution.  
- **Resolution:** Provided the correct NEA license file.  
- **Key Takeaways:** Ensure clear communication regarding product differences to avoid similar issues.

### Case Study 4: Portal Access Issues  
**Ticket ID:** [500Qk00000GEvQGIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GEvQGIA1/view)  
- **Symptoms:** Customer could not find NEA download links in the portal.  
- **Diagnostic Steps:** Verified licensing status and escalated to the sales team.  
- **Resolution:** Updated portal access to reflect correct product licensing.  
- **Key Takeaways:** Verify portal access during initial troubleshooting to avoid delays.

### Case Study 5: User Identification Issues  
**Ticket ID:** [500Qk00000PDjsBIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PDjsBIAT/view)  
- **Symptoms:** SIDs displayed instead of user names in AIC.  
- **Diagnostic Steps:** Confirmed Azure license requirement for detailed user information.  
- **Resolution:** Informed the customer about the licensing requirement.  
- **Key Takeaways:** Verify Azure licensing status for customers using AIC.

---

## Best Practices & Tips
- **Proactive Monitoring:** Track license expiration dates to prevent service interruptions.
- **Clear Communication:** Ensure customers understand licensing requirements and product differences.
- **Documentation:** Maintain detailed records of previous license issues for reference.
- **Portal Verification:** Check customer portal access during initial troubleshooting.
- **Escalation Protocols:** Escalate unresolved licensing issues promptly to the sales or licensing team.

---

## Escalation Guidelines
### Criteria for Escalation
- License renewal requests with no response from the licensing team within 48 hours.
- Portal access issues requiring sales team intervention.
- Complex licensing inquiries beyond the scope of technical support.

### Escalation Procedure
1. Notify the Account Manager or Licensing team via email.
2. Provide detailed case information, including ticket ID, customer details, and issue description.
3. Follow up within 24 hours to ensure visibility and progress.

--- 

End of Document.