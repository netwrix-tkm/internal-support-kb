# Knowledge Base Reference Guide: Handling Vulnerabilities in the Survey Action Module of Netwrix Enterprise Auditor

## Overview

This guide provides a comprehensive reference for identifying, diagnosing, and resolving vulnerabilities related to the Survey Action Module in Netwrix Enterprise Auditor (NEA). It is designed to help support engineers systematically address issues involving third-party components, such as Apache Struts, which may introduce security risks. Understanding and mitigating these vulnerabilities is critical to maintaining customer trust and ensuring the security of their environments.

## Technical Background

### Key Concepts
- **Survey Action Module**: A feature in NEA that utilizes Apache Struts for web-based survey functionality. This module is optional and may not be used in all customer environments.
- **Apache Struts**: A popular open-source framework for creating Java-based web applications. Vulnerabilities in Apache Struts can lead to critical security risks, such as remote code execution (RCE).
- **CVE-2024-53677**: A specific vulnerability in Apache Struts version 6.3.0.2 that allows RCE. This vulnerability was identified in NEA installations where the Survey Action Module was deployed.

### System Context
- The vulnerable file (`struts2-core-6.3.0.2.jar`) is located in the following path:
  ```
  C:\Program Files (x86)\STEALTHbits\StealthAUDIT\Actions\SurveyWebServlet\WEB-INF\lib\
  ```
- Customers not using the Survey Action Module can safely remove the vulnerable file without impacting other NEA functionality.
- A patch addressing this vulnerability is available in NEA version 11.6.0.132+, which upgrades Apache Struts to version 6.7.0.

## Issue Recognition & Triage

### Identifying Vulnerabilities
- **Customer Reports**: Customers may report vulnerabilities flagged by internal security teams or external vulnerability scans.
- **Symptoms**: The presence of outdated or vulnerable third-party libraries, such as Apache Struts, in the NEA installation.
- **Impact Assessment**: Determine whether the affected component (e.g., Survey Action Module) is actively used in the customer's environment.

### Priority Assessment
- **Critical**: If the vulnerable component is actively used, immediate action is required to mitigate the risk.
- **Moderate**: If the vulnerable component is not in use, the risk is lower, but remediation is still necessary to maintain a secure environment.

## Diagnostic Methodology

1. **Confirm Vulnerability**:
   - Verify the presence of the vulnerable file (`struts2-core-6.3.0.2.jar`) in the customer's environment.
   - Cross-check the reported vulnerability (e.g., CVE-2024-53677) with known issues in the NEA release notes or vulnerability databases.

2. **Assess Usage**:
   - Determine whether the customer is actively using the Survey Action Module.
   - If the module is not in use, confirm that removing the vulnerable file will not impact other NEA functionality.

3. **Engage Development Team**:
   - If necessary, consult with the development team to confirm the scope of the vulnerability and the availability of patches.

4. **Communicate Findings**:
   - Clearly explain the vulnerability, its impact, and the recommended resolution to the customer.

## Information Collection

### Questions to Ask Customers
- Are you actively using the Survey Action Module in NEA?
- Have any security scans flagged vulnerabilities in your NEA installation?
- What version of NEA are you currently running?

### Data to Collect
- NEA version details (e.g., 11.6.0.74).
- Logs or screenshots of the vulnerability scan results.
- Confirmation of the file path where the vulnerable component is located.

## Common Scenarios & Solutions

### Scenario 1: Vulnerable Component Present, Module Not in Use
- **Symptoms**: Vulnerability scan identifies `struts2-core-6.3.0.2.jar`, but the Survey Action Module is not in use.
- **Resolution**:
  1. Confirm the module is not in use.
  2. Advise the customer to remove the vulnerable file.
  3. Inform the customer about the patch in NEA version 11.6.0.132+.

### Scenario 2: Vulnerable Component Present, Module in Use
- **Symptoms**: Vulnerability scan identifies `struts2-core-6.3.0.2.jar`, and the Survey Action Module is actively used.
- **Resolution**:
  1. Advise the customer to upgrade to NEA version 11.6.0.132+ to apply the patch.
  2. Provide assistance with the upgrade process if needed.

## Detailed Case Studies

### Case Study 1: [Ticket ID: 500Qk00000JbfcMIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JbfcMIAR/view)
- **Initial Symptoms**: Vulnerability scan flagged `struts2-core-6.3.0.2.jar`. Customer was not using the Survey Action Module.
- **Diagnostic Steps**:
  1. Verified the presence of the vulnerable file.
  2. Confirmed the module was not in use.
  3. Advised the customer to remove the file.
- **Resolution**: The file was removed, and the customer was informed about the upcoming patch in NEA version 11.6.0.132+.
- **Key Takeaways**:
  - Always confirm module usage before recommending file removal.
  - Proactively communicate patch availability to customers.

### Case Study 2: [Ticket ID: 500Qk00000JkZfmIAF](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JkZfmIAF/view)
- **Initial Symptoms**: Customer inquired about a vulnerability flagged on the NEA server.
- **Diagnostic Steps**:
  1. Verified the vulnerability with the SWAT team.
  2. Confirmed the customer was not using the Survey Action Module.
  3. Recommended removing the vulnerable file.
- **Resolution**: The file was removed, and the customer was informed about the patch in NEA version 11.6.0.132+.
- **Key Takeaways**:
  - Collaborate with internal teams (e.g., SWAT, development) to validate vulnerabilities.
  - Ensure clear communication of resolution steps and future patch availability.

## Best Practices & Tips

- **Proactive Communication**: Regularly inform customers about updates and patches to address vulnerabilities in third-party components.
- **Module Usage Assessment**: Always confirm whether a module is actively used before recommending file removal.
- **Documentation**: Maintain detailed records of diagnostic steps and resolutions for future reference.
- **Collaboration**: Engage with internal teams to validate vulnerabilities and confirm patch availability.
- **Customer Education**: Emphasize the importance of keeping software up to date to mitigate security risks.

## Escalation Guidelines

- **When to Escalate**:
  - If the customer is actively using the vulnerable module and cannot immediately apply the patch.
  - If the vulnerability impacts other NEA components beyond the Survey Action Module.
  - If the customer encounters issues during the patching or upgrade process.

- **How to Escalate**:
  1. Gather all relevant information, including logs, NEA version details, and customer environment specifics.
  2. Submit a detailed escalation request to the development or SWAT team.
  3. Keep the customer informed about the escalation status and expected resolution timeline.