# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## Sales, Renewals, and Licensing: License Request  

### Overview  
This guide addresses issues related to license requests for the Netwrix Endpoint Protector platform, specifically focusing on scenarios where licenses appear expired despite renewal orders being placed. Understanding and resolving these issues is critical to ensuring uninterrupted functionality for customers and maintaining their trust in the platform.  

### Technical Background  
Netwrix Endpoint Protector requires a valid license file to operate. When a customer renews their license, they must receive and import the updated license file into the system. Failure to complete this process can result in the system displaying an expired license status, even if the renewal order has been processed.  

#### Key Concepts:  
- **License File**: A digital file that activates the product for a specified period.  
- **System Licensing**: The configuration area in the platform where license files are managed.  
- **Renewal Process**: The procedure customers follow to extend their license validity, including receiving and importing the updated license file.  

### Issue Recognition & Triage  
#### Symptoms:  
- The system displays an "expired license" message.  
- Customers report that they have renewed their license but functionality remains restricted.  

#### Priority Assessment:  
- **High Priority**: If the expired license status disrupts critical operations.  
- **Medium Priority**: If the issue is reported but does not immediately impact functionality.  

### Diagnostic Methodology  
1. **Confirm Renewal Status**: Verify with the customer whether they have placed a renewal order.  
2. **Check for License File Delivery**: Determine if the customer has received the updated license file via email.  
3. **Inspect System Licensing**: Guide the customer to check the current license status in the "System Configuration > System Licensing" section.  
4. **Verify Import Process**: Ensure the customer has correctly imported the license file.  

### Information Collection  
When troubleshooting, gather the following details:  
- **Renewal Confirmation**: Proof of the renewal order (e.g., order number, invoice).  
- **License File**: Confirm whether the customer has received the updated license file.  
- **System Logs**: Collect logs from the licensing module if the issue persists after importing the license file.  
- **Screenshots**: Request screenshots of the "System Licensing" page to verify the current status.  

### Common Scenarios & Solutions  
#### Scenario 1: License File Not Received  
- **Symptoms**: Customer reports placing a renewal order but has not received the license file.  
- **Resolution**:  
  1. Verify the renewal order in internal systems.  
  2. Resend the license file to the customer’s registered email address.  
  3. Guide the customer to import the license file.  

#### Scenario 2: License File Not Imported  
- **Symptoms**: Customer has received the license file but the system still shows an expired license.  
- **Resolution**:  
  1. Confirm the customer has the correct license file.  
  2. Instruct the customer to navigate to "System Configuration > System Licensing" and click the "Import Licenses" button.  
  3. Verify that the license status updates successfully.  

#### Scenario 3: Incorrect License File Imported  
- **Symptoms**: Customer reports importing a license file, but the system still shows an expired license.  
- **Resolution**:  
  1. Verify the license file matches the customer’s account and product version.  
  2. Provide the correct license file if necessary.  
  3. Guide the customer through the import process again.  

### Detailed Case Studies  
#### Case Study 1: License File Not Received  
- **Ticket ID**: [500Qk00000O4fWdIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000O4fWdIAJ/view)  
- **Initial Symptoms**: Customer reported that the license was showing as expired despite placing a renewal order.  
- **Diagnostic Steps**:  
  1. Verified the renewal order status internally.  
  2. Confirmed the customer had not received the updated license file.  
  3. Resent the license file to the customer.  
- **Resolution**: The customer successfully imported the license file, resolving the issue.  
- **Key Takeaways**:  
  - Always confirm that the license file has been sent and received.  
  - Proactively guide customers through the import process to ensure proper implementation.  
- **Efficiency Improvements**: Automate email notifications with license file attachments upon renewal completion.  

### Best Practices & Tips  
- **Proactive Communication**: Remind customers to check their email (including spam/junk folders) for the license file after placing a renewal order.  
- **Clear Instructions**: Provide step-by-step guidance for importing license files, including screenshots or video tutorials if possible.  
- **Internal Verification**: Always confirm the renewal order status and license file delivery before escalating.  
- **Automation**: Implement automated systems to send license files immediately upon renewal processing.  

### Escalation Guidelines  
Escalate the issue to the licensing or development team if:  
- The license file is not generated or cannot be located in internal systems.  
- The customer reports errors during the license import process that cannot be resolved through standard troubleshooting.  
- The issue persists despite verifying the correct license file and import process.  

#### Escalation Steps:  
1. Document all troubleshooting steps and findings.  
2. Attach relevant logs, screenshots, and customer communications.  
3. Submit the case to the appropriate team with a detailed summary of the issue and actions taken.  

