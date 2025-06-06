# Knowledge Base Reference Guide: Troubleshooting NEA for AnyID Connectors - Salesforce Feature

## Overview
This guide focuses on troubleshooting issues related to the Salesforce feature within the NEA for AnyID Connectors component of Netwrix Enterprise Auditor. These issues often involve custom jobs failing to operate as expected, impacting data collection and reporting. Understanding this category is critical for ensuring seamless integration and functionality of Salesforce-related jobs, which are essential for auditing and compliance purposes.

## Technical Background
### Key Concepts
- **Netwrix Enterprise Auditor (NEA):** A platform for auditing and monitoring IT environments, including Salesforce integrations.
- **AnyID Connectors:** Customizable connectors designed to integrate with third-party systems like Salesforce.
- **Salesforce Feature:** Includes jobs such as `AnyID_salesforce`, `AnyData_SalesforceLibraries`, and `AnyData_SalesforceNotes`, which collect specific data from Salesforce environments.

### System Context
- **Custom Jobs:** These are tailored scripts or configurations created by the Professional Services (PS) team to meet specific customer requirements.
- **Version Details:** The issues discussed pertain to NEA version 11.6 (build 11.6.0.112).

## Issue Recognition & Triage
### Symptoms
- Specific Salesforce jobs fail to execute or produce expected results.
- Jobs like `AnyData_SalesforceLibraries` and `AnyData_SalesforceNotes` fail, while others (e.g., `AnyID_salesforce`) function correctly.

### Priority Assessment
- **High Priority:** If the failure impacts critical auditing or compliance reporting.
- **Medium Priority:** If the failure affects non-essential data collection but does not disrupt overall functionality.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Job Functionality:** Confirm which jobs are failing and which are operational.
2. **Review Logs:** Examine job-specific logs for error messages or anomalies.
3. **Check Documentation:** Refer to feature-specific documentation for setup and operational guidelines.
4. **Engage Professional Services:** If custom jobs are involved, coordinate with the PS team for deeper analysis.

### Decision Points
- **Custom Job Errors:** If errors are identified in custom jobs, escalate to the PS team.
- **Configuration Issues:** If setup discrepancies are found, guide the customer through corrective actions using documentation.

## Information Collection
### Customer Queries
- What specific jobs are failing?
- Are there any error messages or logs available?
- Has the Professional Services team been engaged for custom job creation or troubleshooting?

### Logs and Data
- Job execution logs from NEA.
- Configuration files for the failing jobs.
- Screenshots or descriptions of error messages.

## Common Scenarios & Solutions
### Scenario 1: Custom Job Errors
- **Symptoms:** Jobs fail due to errors in custom scripts provided by the PS team.
- **Resolution:** Advise the customer to work directly with the PS team to resolve script-related issues.

### Scenario 2: Configuration Issues
- **Symptoms:** Jobs fail due to incorrect setup or missing prerequisites.
- **Resolution:** Provide documentation links and guide the customer through the setup process:
  - [SF Libraries Documentation](https://helpcenter.netwrix.com/bundle/StealthAUDIT_AnyData_SalesforceLibraries/resource/StealthAUDIT_AnyData_SalesforceLibraries.pdf)
  - [SF Notes Documentation](https://helpcenter.netwrix.com/bundle/StealthAUDIT_AnyData_SalesforceNotes/resource/StealthAUDIT_AnyData_SalesforceNotes.pdf)

## Detailed Case Studies
### Case Study: Ticket ID [500Qk00000HPt9BIAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000HPt9BIAT/view)
#### Initial Symptoms
The customer reported that while the `AnyID_salesforce` job was functioning correctly, the `AnyData_SalesforceLibraries` and `AnyData_SalesforceNotes` jobs were failing.

#### Diagnostic Steps
1. Verified the functionality of the operational job (`AnyID_salesforce`).
2. Reviewed logs for the failing jobs.
3. Provided documentation links for feature setup and functionality.

#### Key Information Leading to Resolution
- Errors were traced back to custom jobs created by the Professional Services team.
- The customer was already engaged with the PS team through Matt Harris.

#### Resolution
The customer was advised to continue working with the PS team to address the errors in the custom jobs.

#### Key Takeaways
- Custom jobs require close collaboration with the PS team for troubleshooting.
- Providing documentation links helps customers understand feature functionality and setup.

#### Efficiency Improvements
- Establish a standardized process for escalating custom job issues to the PS team.
- Create a checklist for verifying job configurations before escalation.

## Best Practices & Tips
- **Documentation First:** Always provide relevant documentation links to customers for self-service troubleshooting.
- **Engage Professional Services Early:** For custom job issues, involve the PS team as soon as possible.
- **Log Analysis:** Encourage customers to share detailed logs to expedite diagnostics.
- **Customer Communication:** Maintain clear and consistent communication, ensuring customers understand the next steps.

## Escalation Guidelines
### Criteria for Escalation
- Errors in custom jobs that cannot be resolved through documentation or basic troubleshooting.
- Issues requiring modifications to scripts or configurations created by the PS team.

### Escalation Procedure
1. Collect all relevant logs and error messages.
2. Document the troubleshooting steps already taken.
3. Engage the PS team with a detailed summary of the issue and supporting data.
4. Ensure the customer is informed about the escalation and expected timelines.