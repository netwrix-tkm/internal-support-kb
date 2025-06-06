# Netwrix Endpoint Protector Knowledge Base: EasyLock License Issues

## Overview

This guide addresses troubleshooting and resolution of issues related to the EasyLock License feature in Netwrix Endpoint Protector. EasyLock is a critical component for enforcing encryption on USB storage devices, ensuring data security and compliance. Understanding and resolving license-related issues is essential to maintaining functionality and protecting sensitive data.

## Technical Background

### Key Concepts
- **EasyLock**: A utility that encrypts USB storage devices, ensuring secure data transfer and storage.
- **License Management**: EasyLock requires a valid license to function. Licenses are managed through the Endpoint Protector Management Console.
- **Enforced Encryption**: Ensures that USB devices are encrypted before use, preventing unauthorized access to data.

### System Context
- **Endpoint Protector Server**: Centralized management system for licenses, policies, and device control.
- **USB Storage Devices**: Devices encrypted using EasyLock must maintain valid licenses to operate correctly.
- **License Expiration**: When a license expires, encrypted devices may prompt recovery processes or fail to function until re-encrypted or re-licensed.

## Issue Recognition & Triage

### Symptoms
- "License expired" error messages when accessing encrypted USB devices.
- Inability to save files to encrypted drives.
- Expired license warnings in the Endpoint Protector Management Console.
- Devices prompting recovery processes due to expired licenses.

### Priority Assessment
- **High Priority**: Cases where encryption functionality is completely unavailable, potentially exposing sensitive data.
- **Medium Priority**: Cases involving warnings or errors that do not immediately impact functionality but may lead to future issues.
- **Low Priority**: Cases related to administrative tasks, such as license renewal or file verification.

## Diagnostic Methodology

### Systematic Approach
1. **Verify Licensing Status**: Check the Endpoint Protector Management Console for active licenses and expiration dates.
2. **Inspect USB Device Configuration**: Confirm that the device is properly encrypted and associated with a valid license.
3. **Review Logs**: Examine system logs for errors related to EasyLock or license management.
4. **Test Alternate Devices**: Use a different USB device to determine if the issue is device-specific.
5. **Reproduce the Issue**: Attempt to replicate the error to identify patterns or inconsistencies.

### Decision Points
- If the license is expired, proceed with renewal or re-adding the license.
- If the issue is device-specific, focus on re-encryption or file restoration.
- If the problem persists across multiple devices, escalate for further investigation.

## Information Collection

### Customer Questions
- What error messages are displayed?
- When did the issue first occur?
- Has the license been renewed recently?
- Are other USB devices experiencing similar issues?

### Data to Collect
- Screenshots of error messages.
- Logs from the Endpoint Protector Management Console.
- Details of the affected USB device (e.g., model, encryption status).
- License file details (e.g., expiration date, included features).

## Common Scenarios & Solutions

### Scenario 1: License Expired on USB Device
- **Symptoms**: "License expired" error when accessing encrypted USB devices.
- **Solution**: Re-encrypt the device using a valid license. If necessary, reinstall EasyLock files on the device.

### Scenario 2: Missing EasyLock Licenses in License File
- **Symptoms**: Expired license warnings after extending Endpoint Protector licenses.
- **Solution**: Verify the contents of the license file and request a corrected file from Netwrix support.

### Scenario 3: Temporary Licenses Causing Device-Specific Issues
- **Symptoms**: Recovery prompts and license expiration errors on specific USB devices.
- **Solution**: Re-encrypt the affected device and confirm licensing status in the Endpoint Protector Management Console.

### Scenario 4: Transition from Trial to Full License
- **Symptoms**: "License expired" error despite transitioning to a full license.
- **Solution**: Reinstall EasyLock files on the USB device and verify licensing status in the console.

## Detailed Case Studies

### Case Study 1: Transition from Trial to Full License  
**Ticket ID**: [500Qk00000C8gxeIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C8gxeIAB/view)  
- **Symptoms**: "License expired" error on Windows 11 workstation.  
- **Diagnostic Steps**: Verified device configuration, deleted corrupted EasyLock files, reinstalled EasyLock utility.  
- **Resolution**: Reinstalled EasyLock files and confirmed functionality.  
- **Key Takeaways**: Ensure proper installation of EasyLock files during license transitions.  

---

### Case Study 2: License Expiration Due to Renewal Delay  
**Ticket ID**: [500Qk00000CNNl2IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CNNl2IAH/view)  
- **Symptoms**: Expired license key causing vulnerabilities.  
- **Diagnostic Steps**: Scheduled remote session, re-added license key to Endpoint Protector server.  
- **Resolution**: Restored functionality by updating the license key.  
- **Key Takeaways**: Encourage customers to monitor license expiration dates to avoid service interruptions.  

---

### Case Study 3: Missing EasyLock Licenses in Extended License File  
**Ticket ID**: [500Qk00000K30MXIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000K30MXIAZ/view)  
- **Symptoms**: Expired license warnings after license extension.  
- **Diagnostic Steps**: Reviewed license file, identified missing EasyLock licenses, requested corrected file.  
- **Resolution**: Applied corrected license file, restoring EasyLock functionality.  
- **Key Takeaways**: Verify license file contents immediately after receipt to catch discrepancies early.  

---

### Case Study 4: Device-Specific Licensing Issue  
**Ticket ID**: [500Qk00000OAEn6IAH](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000OAEn6IAH/view)  
- **Symptoms**: Recovery prompts and license expiration errors on one USB device.  
- **Diagnostic Steps**: Tested alternate devices, confirmed licensing status in console.  
- **Resolution**: Re-encrypted affected device; alternate device functioned correctly.  
- **Key Takeaways**: Clarify expected behavior of encrypted devices when licenses expire.  

## Best Practices & Tips

- **Proactive License Management**: Encourage customers to monitor license expiration dates and renew licenses promptly.
- **Verify License Files**: Always check the contents of license files for completeness before applying them.
- **Snapshot Creation**: Recommend creating a Snapshot of the Endpoint Protector server before making significant changes.
- **Clear Communication**: Provide detailed instructions and explanations to customers during troubleshooting.
- **Documentation**: Maintain detailed records of troubleshooting steps and resolutions for future reference.

## Escalation Guidelines

### Criteria for Escalation
- Issues persist despite following standard troubleshooting steps.
- Problems involve server-side configurations or backend processes.
- License file discrepancies cannot be resolved through standard support channels.

### Escalation Procedure
1. Gather all relevant logs, screenshots, and customer-provided information.
2. Document troubleshooting steps taken and their outcomes.
3. Submit a detailed escalation request to the appropriate team, including all collected data and case history.
4. Follow up with the customer to provide updates and ensure transparency during the escalation process.