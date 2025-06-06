# Knowledge Base Reference Guide: Troubleshooting "RESTRICTEDTOUSER" Permissions in PingCastle Health Check Reports

## Overview

This guide provides a systematic approach to understanding and resolving issues related to the "RESTRICTEDTOUSER" legend in PingCastle Health Check Reports. These issues arise when permissions described in the report are not visible in the Access Control List (ACL) but are context-dependent. Understanding this behavior is critical for accurately diagnosing and addressing customer concerns without unnecessary changes to the ACL.

### Scope
- **Platform:** PingCastle  
- **Component:** PC Standard  
- **Feature:** Health Check Request  
- **Version:** 3.3  

### Importance
Resolving these issues ensures customers can interpret health check reports correctly, maintain confidence in the product, and avoid unnecessary configuration changes.

---

## Technical Background

### Key Concepts
- **Health Check Report:** A diagnostic tool in PingCastle that evaluates the security posture of Active Directory environments.
- **Access Control List (ACL):** A list of permissions attached to an object that specifies which users or system processes can access the object and what operations they can perform.
- **"RESTRICTEDTOUSER" Legend:** A designation in PingCastle reports indicating that permissions apply only during user interactions with the object. These permissions are context-sensitive and may not appear explicitly in the ACL.

### System Context
PingCastle analyzes Active Directory permissions and generates a report highlighting potential security risks. The "RESTRICTEDTOUSER" designation is a feature designed to flag permissions that are user-specific and not universally applied.

---

## Issue Recognition & Triage

### Symptoms
- The customer reports seeing the "RESTRICTEDTOUSER" legend in the health check report.
- The corresponding privilege is not visible in the ACL for the object.
- The customer is unsure of the implications of the "RESTRICTEDTOUSER" designation.

### Priority Assessment
- **Low Priority:** If the customer is seeking clarification without reporting functional issues.
- **Medium Priority:** If the customer believes the absence of the privilege in the ACL is a misconfiguration.
- **High Priority:** If the customer reports security concerns or operational disruptions due to misunderstanding the designation.

---

## Diagnostic Methodology

1. **Review the Health Check Report:**
   - Locate the "RESTRICTEDTOUSER" legend and the associated object/privilege.
   - Confirm the context in which the legend appears.

2. **Examine the ACL:**
   - Verify the absence of the privilege in the ACL.
   - Cross-reference with the object’s permissions to ensure no misconfigurations.

3. **Understand the Context:**
   - Determine if the object is designed to have user-specific permissions.
   - Assess whether the designation aligns with expected behavior.

4. **Clarify the Legend:**
   - Explain the context-dependent nature of "RESTRICTEDTOUSER" permissions to the customer.

---

## Information Collection

### Questions to Ask the Customer
- What specific object or privilege is associated with the "RESTRICTEDTOUSER" legend?
- Are there any operational issues or security concerns related to this designation?
- Has the customer made any recent changes to the ACL or object permissions?

### Data to Collect
- A copy of the health check report.
- Screenshots or exports of the ACL for the object in question.
- Any relevant logs or configuration details.

---

## Common Scenarios & Solutions

### Scenario 1: Customer Sees "RESTRICTEDTOUSER" but No ACL Entry
- **Cause:** The designation indicates user-specific permissions that are not explicitly listed in the ACL.
- **Solution:** Clarify that this behavior is by design and does not require changes to the ACL.

### Scenario 2: Customer Believes the ACL Is Misconfigured
- **Cause:** Misunderstanding of the "RESTRICTEDTOUSER" legend.
- **Solution:** Provide a detailed explanation of the legend and confirm that the ACL is functioning as intended.

### Scenario 3: Security Concerns Related to "RESTRICTEDTOUSER"
- **Cause:** Customer perceives a potential security risk due to the absence of explicit ACL entries.
- **Solution:** Reassure the customer that the permissions are context-dependent and do not pose a security risk.

---

## Detailed Case Studies

### Case Study: Ticket [500Qk00000LDORpIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LDORpIAP/view)

#### Initial Symptoms
The customer reported encountering the "RESTRICTEDTOUSER" legend in a health check report and was unable to locate the corresponding privilege in the ACL.

#### Diagnostic Steps
1. Reviewed the health check report to identify the "RESTRICTEDTOUSER" legend.
2. Examined the ACL for the object and confirmed the absence of the privilege.
3. Investigated the implications of the "RESTRICTEDTOUSER" designation.

#### Key Information
The "RESTRICTEDTOUSER" legend signifies that permissions are context-dependent and apply only during user interactions with the object.

#### Resolution
Explained to the customer that the designation is by design and does not require changes to the ACL. Reassured the customer that the permissions are functioning as intended.

#### Key Takeaways
- The "RESTRICTEDTOUSER" legend is not an error but a feature.
- Clear communication is essential to address customer concerns effectively.

#### Efficiency Improvements
- Develop a standard explanation template for "RESTRICTEDTOUSER" inquiries.
- Include a knowledge base link in health check reports for quick reference.

---

## Best Practices & Tips

1. **Educate Customers:** Proactively explain the "RESTRICTEDTOUSER" legend and its implications during onboarding or training sessions.
2. **Standardize Responses:** Use consistent language and templates to address common inquiries about the legend.
3. **Leverage Documentation:** Direct customers to relevant knowledge base articles for self-service support.
4. **Focus on Context:** Emphasize the context-dependent nature of "RESTRICTEDTOUSER" permissions to avoid unnecessary ACL modifications.
5. **Collaborate with Development:** Provide feedback to the product team to enhance report clarity and include tooltips for legends.

---

## Escalation Guidelines

### When to Escalate
- The customer reports functional issues or security risks that cannot be resolved through clarification.
- The "RESTRICTEDTOUSER" designation appears in unexpected contexts or objects.
- The issue involves potential bugs or inconsistencies in the health check report.

### How to Escalate
1. Collect all relevant data, including the health check report, ACL details, and customer logs.
2. Document the troubleshooting steps taken and the customer’s concerns.
3. Escalate to the development or product team with a detailed summary of the issue.

