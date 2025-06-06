# Netwrix Endpoint Protector Knowledge Base: License Management and Errors

## Overview

This guide addresses issues related to license management and errors within the Netwrix Endpoint Protector platform. Effective license management is critical for ensuring uninterrupted service and compliance with licensing agreements. This document provides a systematic approach to identifying, diagnosing, and resolving license-related issues, with a focus on common scenarios such as license allocation errors, renewal concerns, and discrepancies in license usage.

## Technical Background

### Key Concepts
- **License Allocation**: The process by which licenses are assigned to endpoints or users within the Netwrix Endpoint Protector system.
- **Emergency License**: A temporary license issued to ensure continuity of service during licensing transitions or unexpected usage spikes.
- **Automatic License Renewal**: A feature that automates the renewal of licenses based on predefined intervals.
- **License Usage Metrics**: Data reflecting the number of active, assigned, and unassigned licenses within the system.

### System Context
Netwrix Endpoint Protector tracks license usage based on endpoint activity. Licenses are allocated to endpoints that are actively communicating with the system. Unused or inactive licenses may remain allocated unless explicitly unassigned or removed. The platform provides tools for filtering and managing licenses, but bulk operations may have limitations.

## Issue Recognition & Triage

### Symptoms of License Issues
- Discrepancies between the number of purchased licenses and the number reported as in use.
- Unexpected increases in license counts after attempting to delete inactive endpoints.
- Inability to reconcile license usage with endpoint activity logs.
- Confusion regarding the transition from Emergency Licenses to standard licenses.

### Priority Assessment
- **High Priority**: License errors causing service interruptions or non-compliance risks.
- **Medium Priority**: Discrepancies in license counts without immediate operational impact.
- **Low Priority**: General inquiries about license management or renewal settings.

## Diagnostic Methodology

1. **Verify License Details**:
   - Confirm the number of purchased licenses and their validity period.
   - Check if the customer is operating under an Emergency License or standard licenses.

2. **Review License Usage**:
   - Use the "Last Seen Date" filter to identify inactive endpoints.
   - Sort endpoints by "Licensed/Offline" status to locate unused licenses.

3. **Test License Management Actions**:
   - Attempt to delete or unassign licenses for inactive endpoints.
   - Observe changes in the license count and system behavior.

4. **Analyze System Logs**:
   - Review logs for errors or inconsistencies in license allocation processes.

## Information Collection

### Questions to Ask Customers
- What is the current license count, and how does it compare to the purchased quantity?
- Have there been recent changes to the license configuration (e.g., renewal settings)?
- Are there specific endpoints or users causing discrepancies in license usage?

### Data to Collect
- Screenshots of the license management interface.
- Exported lists of endpoints with their "Last Seen Date" and license status.
- System logs related to license allocation and renewal processes.

## Common Scenarios & Solutions

### Scenario 1: License Count Increases After Deleting Endpoints
- **Symptoms**: Customer deletes inactive endpoints, but the license count unexpectedly increases.
- **Root Cause**: The system may reallocate licenses to previously unlicensed endpoints or misinterpret the deletion action.
- **Resolution**:
  1. Confirm the total number of endpoints in the system.
  2. Reconcile the license count with the endpoint list.
  3. Advise the customer to monitor license usage and avoid bulk deletions without prior analysis.

### Scenario 2: No Change in License Count After Renewal
- **Symptoms**: Automatic License Renewal is set, but the license count remains unchanged.
- **Root Cause**: The renewal process may not immediately reflect in the license usage metrics.
- **Resolution**:
  1. Verify that the renewal settings are correctly configured.
  2. Check for pending system updates or synchronization delays.
  3. Reassure the customer that the renewal will take effect within the specified interval.

## Detailed Case Studies

### Case Study: License Management Confusion at Queensland Treasury
- **Ticket ID**: [500Qk00000MGwzmIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000MGwzmIAD/view)
- **Initial Symptoms**: Customer observed no change in license count after setting Automatic License Renewal and deleting inactive endpoints.
- **Diagnostic Steps**:
  1. Reviewed the customer's license configuration and renewal settings.
  2. Analyzed the endpoint list using "Last Seen Date" and "Licensed/Offline" filters.
  3. Tested deletion of inactive endpoints to observe system behavior.
- **Key Information**: Thousands of endpoints had not been seen since 2020, indicating potential mismanagement of inactive licenses.
- **Resolution**:
  - Confirmed that the customer had transitioned to a new set of 1800 licenses.
  - Clarified that the increase in license count was due to system handling of license allocation.
  - Advised the customer to monitor license usage and avoid bulk deletions.
- **Key Takeaways**:
  - Ensure clear communication about system behavior during license transitions.
  - Encourage customers to regularly audit their endpoint activity and license usage.

## Best Practices & Tips

1. **Regular Audits**: Encourage customers to periodically review their endpoint activity and license allocation to identify inactive licenses.
2. **Avoid Bulk Deletions**: Deleting large numbers of endpoints without prior analysis can lead to unexpected license count changes.
3. **Clear Communication**: Provide detailed explanations of system behavior during license transitions or renewals to prevent confusion.
4. **Proactive Monitoring**: Use the "Last Seen Date" and "Licensed/Offline" filters to identify and address inactive endpoints before they cause discrepancies.

## Escalation Guidelines

### Criteria for Escalation
- Persistent discrepancies in license counts despite troubleshooting.
- Errors in the license management interface or renewal processes.
- Customer dissatisfaction or inability to resolve the issue within a reasonable timeframe.

### Escalation Procedure
1. Gather all relevant information, including screenshots, logs, and customer communications.
2. Document the troubleshooting steps taken and their outcomes.
3. Escalate the case to the Product Development or Licensing Team with a detailed summary of the issue and supporting data.

