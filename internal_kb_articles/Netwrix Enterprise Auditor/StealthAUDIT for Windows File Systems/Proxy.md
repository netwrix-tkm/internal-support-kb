# Netwrix Enterprise Auditor: StealthAUDIT for Windows File Systems - Proxy Troubleshooting Guide

## Overview
This guide provides a comprehensive reference for troubleshooting issues related to the Proxy component of StealthAUDIT for Windows File Systems in Netwrix Enterprise Auditor (NEA). The Proxy feature is critical for enabling efficient data collection and scanning in distributed environments. Understanding and resolving Proxy-related issues ensures uninterrupted auditing and compliance operations.

This document is designed to help support engineers systematically diagnose, resolve, and prevent Proxy-related issues, leveraging insights from real-world cases.

---

## Technical Background
### Key Concepts
- **Proxy Servers**: Proxy servers act as intermediaries between the NEA host and target systems, facilitating data collection and scans.
- **FSAA (File System Access Auditing)**: A feature that monitors and audits file system activity.
- **Sensitive Data Discovery (SDD)**: A feature that identifies sensitive data within file systems.
- **Applet Mechanism**: A configuration setting that determines how applets are deployed and executed on target systems.
- **Tier2 Databases**: SQLite databases used to store intermediate scan data.

### System Context
- **Proxy Configuration**: Proxies must be correctly configured to communicate with the NEA host and target systems.
- **Version Compatibility**: Proxy versions must align with the NEA version to ensure functionality.
- **Environment Variables**: Changes to environment variables can impact Proxy operations.

---

## Issue Recognition & Triage
### Symptoms
- Scans fail to initialize or complete.
- Errors related to authentication, certificates, or missing components.
- Scans produce warnings about special characters or corrupted databases.
- Installer crashes or fails to locate license files.

### Priority Assessment
- **High Priority**: Scans fail across multiple proxies or critical systems.
- **Medium Priority**: Errors are isolated to specific proxies or non-critical systems.
- **Low Priority**: Warnings or minor issues that do not impact scan results.

---

## Diagnostic Methodology
### Systematic Approach
1. **Verify Service Status**: Ensure the FSAA Proxy Service is running on all Proxy servers.
2. **Check Version Compatibility**: Confirm that Proxy versions match the NEA version.
3. **Review Logs**: Analyze Proxy logs for errors or warnings.
4. **Test Connectivity**: Verify network connectivity and open ports between the NEA host, Proxy servers, and target systems.
5. **Reproduce the Issue**: Attempt to replicate the problem in a controlled environment.
6. **Isolate Variables**: Test with different configurations, credentials, or target systems to narrow down the root cause.

---

## Information Collection
### Customer Questions
- What is the current version of NEA and the Proxy component?
- When did the issue first occur, and were there any recent changes (e.g., updates, configuration changes)?
- Are all Proxy servers affected or only specific ones?
- What error messages or warnings are displayed?

### Logs and Data to Collect
- Proxy logs (`FSAA_Proxy_Details` and `SA_JOBs_troubleshooting` scripts).
- NEA host logs.
- Screenshots or descriptions of error messages.
- Configuration files and environment variable settings.

---

## Common Scenarios & Solutions
### Scenario 1: Authentication Failures After Update
- **Symptoms**: Scans fail to initialize; logs show expired certificates or authentication errors.
- **Solution**: Update applet mechanism settings to "Require applet to be running as a service on target." Reinstall the Proxy if necessary. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BgxdFIAR/view)

### Scenario 2: Missing Components After Upgrade
- **Symptoms**: Errors indicating missing components (e.g., `README.txt`).
- **Solution**: Prevent log maintenance from removing critical files. Copy missing files manually and restart scans. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CI6CxIAL/view)

### Scenario 3: Special Character Recognition Issues
- **Symptoms**: Scans fail to process filenames with special characters.
- **Solution**: Upgrade Proxy to the latest version to resolve character recognition bugs. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EEiFhIAL/view)

### Scenario 4: Session Errors Due to Outdated Proxies
- **Symptoms**: Errors indicating sessions have "gone away."
- **Solution**: Update all Proxy servers to the latest version and adjust scan performance settings. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EQlPqIAL/view)

### Scenario 5: Scans Failing Without Errors
- **Symptoms**: Scans disappear from the Running Instances list without producing results.
- **Solution**: Configure strong proxy affinity and split scan credentials into separate jobs. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ETeutIAD/view)

### Scenario 6: Corrupted Tier2 Databases
- **Symptoms**: SDD scans fail with warnings about bulk imports.
- **Solution**: Drop corrupted databases, recreate schemas, and run zero-level scans. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GIxBiIAL/view)

### Scenario 7: Installation Issues on Server Core
- **Symptoms**: Installer crashes or fails to locate license files.
- **Solution**: Use command line arguments to specify the license file during installation. [Example Case](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NpuPZIAZ/view)

---

## Detailed Case Studies
### Case 1: Authentication Failures After Update
- **Ticket**: [500Qk00000BgxdFIAR](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BgxdFIAR/view)
- **Symptoms**: Scans failed to initialize; logs showed expired certificates.
- **Key Information**: Incorrect applet mechanism settings.
- **Resolution**: Updated applet settings and reinstalled Proxy.
- **Takeaways**: Always verify applet settings after updates.

### Case 2: Missing Components After Upgrade
- **Ticket**: [500Qk00000CI6CxIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CI6CxIAL/view)
- **Symptoms**: Missing `README.txt` file caused scan failures.
- **Key Information**: Log maintenance process removed critical files.
- **Resolution**: Adjusted log maintenance settings and restored missing files.
- **Takeaways**: Ensure critical files are excluded from cleanup processes.

### Case 3: Special Character Recognition Issues
- **Ticket**: [500Qk00000EEiFhIAL](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EEiFhIAL/view)
- **Symptoms**: Scans failed to process filenames with special characters.
- **Key Information**: Outdated Proxy version.
- **Resolution**: Upgraded Proxy to the latest version.
- **Takeaways**: Keep Proxy versions up to date to avoid compatibility issues.

### Case 4: Installation Issues on Server Core
- **Ticket**: [500Qk00000NpuPZIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NpuPZIAZ/view)
- **Symptoms**: Installer crashed when browsing for license files.
- **Key Information**: Server Core environment lacks GUI support.
- **Resolution**: Used command line arguments to specify the license file.
- **Takeaways**: Document command line installation procedures for Server Core environments.

---

## Best Practices & Tips
1. **Version Management**: Always ensure Proxy versions match the NEA version.
2. **Configuration Validation**: Verify applet mechanism settings and Proxy affinity configurations after updates.
3. **Log Analysis**: Regularly review logs for errors and warnings.
4. **File Retention**: Exclude critical files from cleanup processes during log maintenance.
5. **Database Integrity**: Monitor scan completion to prevent database corruption.
6. **Command Line Expertise**: Familiarize yourself with command line installation options for non-GUI environments.

---

## Escalation Guidelines
- Escalate to Tier 2 support if:
  - The issue persists after following all resolution steps.
  - Logs indicate unrecognized errors or system-level failures.
  - The customer environment involves unsupported configurations or customizations.
- Provide detailed logs, configuration files, and a summary of troubleshooting steps taken before escalation.