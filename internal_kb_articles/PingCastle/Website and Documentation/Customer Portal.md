# Knowledge Base Reference Guide: Troubleshooting Customer Portal Access Issues

## Overview

This guide provides a comprehensive reference for troubleshooting issues related to accessing the Customer Portal in PingCastle. These issues typically involve customers being unable to log in, complete the sign-up process, or receive confirmation emails. Understanding and resolving these problems is critical to ensuring a seamless user experience and maintaining customer satisfaction.

## Technical Background

The PingCastle Customer Portal is a web-based platform that allows customers to manage their accounts, access documentation, and interact with support. Key components include:

- **Account Activation**: Customers must activate their accounts via a confirmation email sent during the sign-up process.
- **Email Delivery**: The confirmation email is sent to the email address provided during registration. Proper email server configuration and spam filtering are critical to successful delivery.
- **Authentication**: Customers log in using their email address and password. Password resets are available if needed.

Common issues in this category often stem from email delivery failures, incorrect account configurations, or user errors during the sign-up process.

## Issue Recognition & Triage

### Symptoms
- Customer reports not receiving the confirmation email.
- Customer is unable to log in despite completing the sign-up process.
- Customer requests a password reset but does not receive the reset email.

### Priority Assessment
- **High Priority**: Customer is unable to access critical resources or documentation.
- **Medium Priority**: Customer is experiencing delays but has alternative access to required information.
- **Low Priority**: Customer inquiry is informational or non-urgent.

## Diagnostic Methodology

1. **Verify Account Status**:
   - Confirm whether the customer's account is activated in the system.
   - Check for any errors or discrepancies in the account setup.

2. **Check Email Delivery**:
   - Verify that the confirmation email was sent from the system.
   - Instruct the customer to check their SPAM or junk folder.
   - Confirm the email address provided by the customer is correct.

3. **Test Login Credentials**:
   - If the account is activated, provide a temporary password and test login functionality.

4. **Investigate Email Server Issues**:
   - Check for potential blocks or filtering rules on the recipient's email provider.
   - Verify that the email server is functioning correctly and not blacklisted.

## Information Collection

When troubleshooting, gather the following information from the customer:

- **Email Address**: Confirm the email address used for registration.
- **Error Messages**: Ask if any error messages were displayed during the sign-up or login process.
- **SPAM Folder Check**: Confirm whether the customer has checked their SPAM or junk folder.
- **Email Server Logs**: If possible, request logs from the customer's email provider to identify delivery issues.

## Common Scenarios & Solutions

### Scenario 1: Confirmation Email Not Received
- **Symptoms**: Customer reports not receiving the confirmation email.
- **Resolution**:
  1. Verify the customer's email address and account status.
  2. Resend the confirmation email.
  3. Instruct the customer to check their SPAM folder.
  4. If the issue persists, provide a temporary password and confirm login functionality.

### Scenario 2: Login Issues After Activation
- **Symptoms**: Customer cannot log in despite completing the sign-up process.
- **Resolution**:
  1. Verify the account is activated.
  2. Reset the customer's password and provide a new one.
  3. Test the new credentials to ensure successful login.

### Scenario 3: Email Delivery Blocked by Provider
- **Symptoms**: Confirmation or reset emails are not delivered, and the customer confirms they are not in the SPAM folder.
- **Resolution**:
  1. Check the email server logs for delivery status.
  2. Advise the customer to whitelist the sender's domain.
  3. Escalate to the email server administrator if necessary.

## Detailed Case Studies

### Case Study 1: Confirmation Email Not Delivered
- **Ticket ID**: [500Qk00000JAuduIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JAuduIAD/view)
- **Initial Symptoms**: Customer reported not receiving the confirmation email and confirmed it was not in the SPAM folder.
- **Diagnostic Steps**:
  1. Verified that the customer's account was activated.
  2. Confirmed the email address was correct.
  3. Resent the confirmation email and instructed the customer to check again.
  4. Provided a temporary password when the email was still not received.
- **Resolution**: The customer successfully logged in using the temporary password.
- **Key Takeaways**:
  - Always verify account activation and email address accuracy.
  - Providing a temporary password is an effective workaround for email delivery issues.
  - Document similar cases to identify patterns and improve resolution efficiency.

## Best Practices & Tips

- **Proactive Communication**: Clearly explain each troubleshooting step to the customer and set expectations for resolution timelines.
- **Email Delivery Monitoring**: Regularly monitor email server logs to identify and address delivery issues proactively.
- **Documentation**: Maintain detailed records of similar cases to streamline future troubleshooting.
- **Customer Education**: Provide guidance on whitelisting domains and checking SPAM folders to prevent recurring issues.

## Escalation Guidelines

Escalate the issue to the appropriate team or administrator if:

- The email server logs indicate a systemic delivery issue.
- The customer's email provider is blocking emails despite whitelisting.
- The issue cannot be resolved through standard troubleshooting steps.

When escalating, provide all relevant information, including account details, email logs, and a summary of troubleshooting steps already performed.