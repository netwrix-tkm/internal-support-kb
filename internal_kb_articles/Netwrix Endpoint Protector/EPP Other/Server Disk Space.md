# Netwrix Endpoint Protector Knowledge Base Reference Guide  
## Category: Licensing Discrepancies and Server Disk Space  

---

## Overview  
Licensing discrepancies in Netwrix Endpoint Protector (EPP) can lead to confusion for customers, especially when nearing their license limits. These issues typically involve mismatches in the number of licensed endpoints displayed across different sections of the application. Understanding and resolving these discrepancies is critical to maintaining customer satisfaction and ensuring proper license utilization. This guide provides a systematic approach to diagnosing and resolving licensing-related issues, with a focus on server disk space and license filtering mechanisms.

---

## Technical Background  
### Key Concepts  
- **Licensed Endpoints**: Devices that consume a license in the Endpoint Protector system. Licenses are assigned based on devices, not users.  
- **Automatic Release License Feature**: A feature that automatically releases licenses from inactive devices, helping manage license limits effectively.  
- **System Licensing vs. Device Control**:  
  - **System Licensing**: Displays the total number of licensed endpoints.  
  - **Device Control > Computers**: Lists all devices, including duplicates and inactive ones, which may not align with the licensing count.  

### System Context  
- Licensing discrepancies often arise due to differences in how data is filtered and displayed across sections of the application.  
- Software version updates frequently address known issues, including filtering inconsistencies.  

---

## Issue Recognition & Triage  
### Symptoms  
- Mismatch in the number of licensed endpoints between **System Configuration > System Licensing** and **Device Control > Computers**.  
- Customer nearing license limits and seeking clarification on licensing mechanisms.  
- Reports of inactive or duplicate devices inflating the endpoint count.  

### Priority Assessment  
- **High Priority**: Customer is at or near license limits, potentially impacting operations.  
- **Medium Priority**: Discrepancy noted but no immediate operational impact.  

---

## Diagnostic Methodology  
1. **Verify Software Version**: Confirm the version of Endpoint Protector in use. Known issues may already be resolved in newer versions.  
2. **Export and Compare Data**:  
   - Export the licensed endpoint list from **System Configuration > System Licensing**.  
   - Export the device list from **Device Control > Computers** and remove duplicates.  
3. **Check Feature Status**: Verify whether the Automatic Release License feature is enabled.  
4. **Analyze Last Online Status**: Identify inactive devices contributing to the discrepancy.  
5. **Schedule Remote Session**: If discrepancies persist, conduct a remote session to investigate further.  

---

## Information Collection  
### Questions to Ask the Customer  
- What version of Endpoint Protector are you using?  
- Is the Automatic Release License feature enabled?  
- Have you recently added or removed devices?  
- Are there any known inactive or duplicate devices in your environment?  

### Logs and Data to Collect  
- Exported lists from **System Configuration > System Licensing** and **Device Control > Computers**.  
- Screenshots of the discrepancies.  
- Details on the last online status of devices.  

---

## Common Scenarios & Solutions  
### Scenario 1: Filtering Discrepancy  
- **Symptoms**: Mismatch between licensed endpoints in different sections.  
- **Root Cause**: Filtering issue in how licenses are assigned and displayed.  
- **Solution**: Upgrade to the latest version of Endpoint Protector to resolve filtering inconsistencies.  

### Scenario 2: Inactive Devices Inflating Count  
- **Symptoms**: Endpoint count includes devices that are no longer active.  
- **Root Cause**: Automatic Release License feature not enabled.  
- **Solution**: Enable the Automatic Release License feature to manage inactive devices.  

### Scenario 3: Duplicate Devices in Device Control  
- **Symptoms**: Higher count in **Device Control > Computers** due to duplicates.  
- **Root Cause**: Duplicate entries in the device list.  
- **Solution**: Remove duplicate entries and verify the count.  

---

## Detailed Case Studies  
### Case Study: Ticket [500Qk00000HxlveIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HxlveIAB/view)  
#### Initial Symptoms  
The customer reported a mismatch between licensed endpoints in **System Configuration > System Licensing** (10,001) and **Device Control > Computers** (12,525, later reduced to 10,806 after removing duplicates).  

#### Diagnostic Steps  
1. Verified the software version (pre-upgrade).  
2. Exported and compared data from both sections.  
3. Identified inactive and duplicate devices contributing to the discrepancy.  
4. Scheduled a remote session to investigate further.  

#### Key Information Leading to Solution  
- The discrepancy was traced to a filtering issue in how licenses were assigned to devices.  
- The customer was not using the Automatic Release License feature.  

#### Resolution  
- Upgraded the server to version 5941, which resolved the filtering discrepancies.  
- Recommended enabling the Automatic Release License feature for better license management.  

#### Key Takeaways  
- Always verify the software version as updates may resolve known issues.  
- Encourage customers to enable the Automatic Release License feature to prevent similar issues.  

#### Efficiency Improvements  
- Proactively inform customers about the benefits of enabling the Automatic Release License feature during onboarding.  

---

## Best Practices & Tips  
- **Enable Automatic Release License**: This feature helps manage inactive devices and prevents license overages.  
- **Regularly Update Software**: Ensure customers are using the latest version of Endpoint Protector to benefit from bug fixes and improvements.  
- **Educate Customers**: Provide clear guidance on how licensing works and how to manage licenses effectively.  
- **Proactive Monitoring**: Encourage customers to periodically review their licensed endpoint counts to identify discrepancies early.  

---

## Escalation Guidelines  
### When to Escalate  
- Discrepancies persist after upgrading to the latest version.  
- The issue involves complex filtering or database inconsistencies requiring development team intervention.  
- Customer is at risk of exceeding license limits and requires immediate resolution.  

### How to Escalate  
- Gather all relevant data, including exported lists, screenshots, and logs.  
- Document the troubleshooting steps already taken.  
- Submit a detailed escalation request to the development team with all supporting information.  

---  