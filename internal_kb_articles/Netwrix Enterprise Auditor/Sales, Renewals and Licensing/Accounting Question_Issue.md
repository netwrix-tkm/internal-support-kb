# Knowledge Base Reference Guide: Handling Account Deletion and Verification Requests

## Overview
This guide covers the process of handling account deletion and verification requests related to Netwrix Enterprise Auditor. These issues often involve sensitive customer data and legal compliance, making it critical to address them accurately and efficiently. Support engineers must ensure clear communication, proper documentation, and adherence to legal and privacy protocols.

## Technical Background
### Key Concepts
- **Account Deletion Requests**: Customers may request the removal of their accounts and associated data due to privacy concerns or non-use of the product.
- **Data Rights Compliance**: Requests must comply with data protection regulations, such as GDPR or CCPA, which mandate timely and complete processing of deletion requests.
- **Salesforce (SF)**: Netwrix uses Salesforce as its CRM system, where customer accounts and contacts are managed.
- **Account Control Panel**: A platform used to verify the status of customer accounts and their activity.

### Terminology
- **Active Account**: An account that remains accessible and operational within Netwrix systems.
- **Legal Escalation**: Involves forwarding requests to the legal team for compliance verification and processing.
- **Email Domain Verification**: Ensuring no active users exist under specific email domains provided by the customer.

## Issue Recognition & Triage
### Identifying Account Deletion Requests
- Customers typically initiate requests via email to privacy@netwrix.com or through direct communication with support.
- Requests may include:
  - Removal of specific accounts or contacts.
  - Verification of active users under certain email domains.

### Assessing Priority
- **High Priority**: Requests involving legal compliance or sensitive data rights.
- **Medium Priority**: Requests for verification of account status without immediate deletion.
- **Low Priority**: General inquiries about account activity.

## Diagnostic Methodology
### Systematic Approach
1. **Initial Review**: Confirm the nature of the request and gather relevant details from the customer.
2. **Verify Account Status**:
   - Check Salesforce for account and contact activity.
   - Use the Account Control Panel to confirm account status.
3. **Legal Coordination**:
   - Forward the request to privacy@netwrix.com for legal review.
   - Confirm whether the deletion request has been submitted and processed.
4. **Customer Communication**:
   - Provide updates to the customer regarding the status of their request.
   - Ensure clarity on next steps and expected timelines.

### Decision Points
- If the account is still active after legal confirmation, escalate the issue for further investigation.
- If no active users are found under the specified email domains, communicate the findings to the customer.

## Information Collection
### Customer Inputs
- Specific account details (e.g., account name, contact name).
- Email domains to verify (e.g., `@vu.com`, `@veteransunited.com`).
- Confirmation of the request type (deletion or verification).

### Logs and Data
- Salesforce account and contact activity logs.
- Account Control Panel status reports.
- Email correspondence with privacy@netwrix.com and legal team.

## Common Scenarios & Solutions
### Scenario 1: Account Deletion Request
- **Symptoms**: Customer requests account removal but finds the account still active.
- **Resolution**:
  1. Verify the deletion request with legal.
  2. Confirm account status in Salesforce and Account Control Panel.
  3. Escalate to legal if the account remains active.
  4. Communicate resolution to the customer.

### Scenario 2: Email Domain Verification
- **Symptoms**: Customer requests confirmation of no active users under specific email domains.
- **Resolution**:
  1. Search Salesforce for contacts associated with the provided domains.
  2. Verify account activity in the Account Control Panel.
  3. Provide confirmation to the customer.

## Detailed Case Studies
### Case Study: Ticket ID [500Qk00000Lo4QyIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Lo4QyIAJ/view)
#### Initial Symptoms
- Customer requested account deletion and verification of active users under `@vu.com` and `@veteransunited.com`.
- Legal confirmed the deletion request was submitted, but the account remained active.

#### Diagnostic Steps
1. Verified the deletion request with legal.
2. Checked Salesforce and found only the contact was removed, not the account.
3. Used the Account Control Panel to confirm the account was still active.

#### Key Information Leading to Resolution
- Legal had submitted the deletion request but did not complete the process for the account itself.

#### Resolution
- Escalated the issue to legal as a data rights request.
- Legal confirmed the necessary actions were taken, and the account was fully deleted.
- Communicated resolution to the customer.

#### Key Takeaways
- Ensure deletion requests are fully processed, including both contacts and accounts.
- Maintain clear communication with legal and the customer throughout the process.

#### Efficiency Improvements
- Implement a follow-up mechanism for pending deletion requests to prevent delays.
- Develop a checklist for verifying account and contact status during deletion requests.

## Best Practices & Tips
- **Clear Documentation**: Record all customer requests and actions taken in Salesforce for future reference.
- **Proactive Follow-Up**: Regularly check the status of deletion requests with legal to ensure timely processing.
- **Customer Communication**: Provide clear and concise updates to customers, including expected timelines and next steps.
- **Verification Protocols**: Use both Salesforce and the Account Control Panel to confirm account and contact status.
- **Escalation Readiness**: Escalate issues promptly if discrepancies are found or if legal compliance is at risk.

## Escalation Guidelines
### Criteria for Escalation
- Account remains active despite confirmed deletion request.
- Legal compliance concerns arise during the process.
- Customer dissatisfaction due to delays or incomplete actions.

### Escalation Procedures
1. Notify the legal team via privacy@netwrix.com with detailed case information.
2. Document the escalation in Salesforce, including all correspondence and updates.
3. Inform the customer of the escalation and provide expected timelines for resolution.