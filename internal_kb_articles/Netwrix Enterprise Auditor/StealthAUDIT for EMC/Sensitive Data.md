# Knowledge Base Reference Guide: Troubleshooting Assembly Loading Issues in StealthAUDIT for EMC (Sensitive Data Feature)

## Overview
This guide provides a comprehensive reference for troubleshooting assembly loading issues in the **Sensitive Data** feature of **StealthAUDIT for EMC**, a component of **Netwrix Enterprise Auditor**. These issues typically arise when the application encounters mismatched or outdated assemblies during job processing, leading to errors that disrupt functionality. Understanding and resolving these issues is critical to maintaining seamless operation and ensuring accurate data analysis.

## Technical Background
### Key Concepts
- **Assembly Loading**: In .NET applications, assemblies are dynamically loaded at runtime. A mismatch between the required and available assembly versions can cause runtime errors.
- **System.Data.SQLite**: A key assembly used by StealthAUDIT for EMC for database interactions. The correct version must be present in the installation directory for proper functionality.
- **Local Mode Scan**: A scanning mode where the application processes data locally on the host, requiring all dependencies to be correctly configured.

### System Context
- **Installation Directory**: Assemblies are stored in `%SAInstallDir%FSAA`. This directory must contain the correct versions of all required assemblies.
- **Isilon Host**: A type of storage system often used in conjunction with StealthAUDIT for EMC. Issues on Isilon hosts may require specific configurations.

## Issue Recognition & Triage
### Symptoms
- Error message: "Could not load file or assembly 'System.Data.SQLite, Version=1.0.117.0, Culture=neutral, PublicKeyToken=db937bc2d44ff139' or one of its dependencies."
- SEEK job processing fails during Local Mode scans.

### Priority Assessment
- **High Priority**: If the issue disrupts critical job processing or affects sensitive data analysis.
- **Medium Priority**: If the issue is isolated to a non-critical host or job.

## Diagnostic Methodology
1. **Verify the Error Message**: Confirm the exact error details, including the assembly name and version.
2. **Check the Installation Directory**: Navigate to `%SAInstallDir%FSAA` and inspect the presence and version of the required assembly.
3. **Identify Version Mismatches**: Compare the installed assembly version with the version specified in the error message.
4. **Validate Dependencies**: Ensure all dependencies of the required assembly are present and correctly configured.

## Information Collection
### Questions to Ask the Customer
1. What is the exact error message and when does it occur?
2. What is the scan mode (e.g., Local Mode)?
3. What type of host is being scanned (e.g., Isilon)?
4. Have there been any recent updates or changes to the installation directory?

### Logs and Data to Collect
- Application logs from the affected host.
- A screenshot or copy of the error message.
- A list of assemblies in `%SAInstallDir%FSAA` with their versions.

## Common Scenarios & Solutions
### Scenario 1: Outdated Assembly Version
- **Symptom**: Error message indicates a mismatch in the `System.Data.SQLite` assembly version.
- **Solution**: Replace the outdated assembly in `%SAInstallDir%FSAA` with the correct version (e.g., 1.0.117.0).

### Scenario 2: Missing Dependencies
- **Symptom**: Error message references a missing dependency.
- **Solution**: Identify and install the missing dependency in the installation directory.

### Scenario 3: Corrupted Installation
- **Symptom**: Multiple errors related to assembly loading.
- **Solution**: Reinstall the application or repair the installation to restore all required assemblies.

## Detailed Case Studies
### Case Study 1: Ticket [500Qk00000GWDiVIAX](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GWDiVIAX/view)
#### Initial Symptoms and Customer Report
- Customer reported an error during a SEEK job on a single Isilon host using Local Mode scan.
- Error message: "Could not load file or assembly 'System.Data.SQLite, Version=1.0.117.0, Culture=neutral, PublicKeyToken=db937bc2d44ff139' or one of its dependencies."

#### Diagnostic Steps
1. Verified the error message and identified the affected assembly (`System.Data.SQLite`).
2. Checked the `%SAInstallDir%FSAA` directory and found an outdated version of the assembly.
3. Confirmed that the required version was 1.0.117.0.

#### Key Information Leading to the Solution
- The error message explicitly referenced the required assembly version.
- Inspection of the installation directory revealed a version mismatch.

#### Resolution
- Replaced the outdated `System.Data.SQLite` assembly with version 1.0.117.0.
- Verified that the SEEK job processed successfully after the replacement.

#### Key Takeaways
- Always verify assembly versions in the installation directory when encountering loading errors.
- Maintain an up-to-date repository of required assemblies for quick replacement.

#### Efficiency Improvements
- Implement a script to automate version checks in the installation directory.
- Develop a pre-scan validation tool to identify potential assembly mismatches.

## Best Practices & Tips
1. **Maintain Version Control**: Regularly update and verify the versions of all assemblies in the installation directory.
2. **Automate Checks**: Use scripts to automate the detection of outdated or missing assemblies.
3. **Document Changes**: Keep a log of updates and changes to the installation directory for future reference.
4. **Preemptive Validation**: Run pre-scan checks to ensure all dependencies are correctly configured before initiating jobs.
5. **Customer Communication**: Clearly explain the issue and resolution steps to the customer to build trust and confidence.

## Escalation Guidelines
### When to Escalate
- If the issue persists after replacing the assembly with the correct version.
- If multiple dependencies are missing or corrupted.
- If the issue affects multiple hosts or job types.

### How to Escalate
1. Gather all relevant logs, error messages, and details of troubleshooting steps taken.
2. Document the impact on the customer's operations.
3. Escalate to the development team with a detailed summary of findings and actions.

By following this guide, support engineers can systematically diagnose and resolve assembly loading issues in StealthAUDIT for EMC, ensuring efficient and effective support for customers.