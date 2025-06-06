# Knowledge Base Reference Guide: Troubleshooting Guest Account Authentication Issues in StealthAUDIT for Windows

## Overview
This guide addresses troubleshooting issues related to guest account authentication attempts in StealthAUDIT for Windows, a component of Netwrix Enterprise Auditor. These issues can lead to account lockouts and security concerns, making it critical to identify root causes and resolve them efficiently. This document provides a systematic approach to diagnosing and resolving such problems, ensuring consistent and effective support.

## Technical Background
StealthAUDIT for Windows is a data collection and analysis tool used for auditing and compliance. It interacts with various systems and accounts to gather information. Misconfigurations or environmental factors can sometimes result in unexpected authentication attempts, such as those involving guest accounts. Understanding the following concepts is essential for troubleshooting:

- **Guest Accounts**: Built-in accounts with limited privileges, often disabled by default for security reasons.
- **Authentication Mechanisms**: Processes by which accounts are validated during system interactions.
- **Windows Security Event Logs**: Logs that record authentication attempts, including successes and failures.
- **Event IDs**: Specific identifiers in Windows logs that provide details about authentication events (e.g., 4625 for failed logons, 4648 for explicit credential use).
- **BESClient.exe**: A process associated with IBM BigFix, which can generate local user activity unrelated to StealthAUDIT.

## Issue Recognition & Triage
### Symptoms
- Reports of account lockouts, specifically involving guest accounts.
- Security team observations of authentication attempts originating from StealthAUDIT servers or other hosts.

### Priority Assessment
- **High Priority**: If the issue results in widespread account lockouts or impacts critical systems.
- **Medium Priority**: If the issue is isolated to non-critical systems or accounts.
- **Low Priority**: If the issue is reported but does not actively impact operations.

## Diagnostic Methodology
### Step 1: Verify the Reported Behavior
- Confirm the account experiencing lockouts (e.g., guest account).
- Identify the systems involved and the frequency of the issue.

### Step 2: Analyze Logs
- Search StealthAUDIT logs for references to the affected account:
  ```powershell
  gci "D:\Program Files (x86)\STEALTHbits\StealthAUDIT\SADatabase\Logs\*.log" -Recurse | Select-String <AccountName>
  gci "D:\Program Files\STEALTHbits\Access Information Center\*.log" -Recurse | Select-String <AccountName>
  gci "D:\Program Files (x86)\STEALTHbits\StealthAUDIT\Jobs" -Include ConnectStatus.csv -Recurse | Select-String <AccountName>
  ```
- Review Windows Security Event Logs for relevant Event IDs (e.g., 4625, 4648) to trace authentication attempts.

### Step 3: Verify Auditing Configuration
- Ensure OS auditing is enabled on relevant servers:
  ```powershell
  auditpol /get /category:Logon/Logoff
  auditpol /get /category:'Account Logon'
  ```

### Step 4: Identify the Source of Authentication Attempts
- Correlate log entries with processes or applications (e.g., BESClient.exe) to determine the origin of the activity.

## Information Collection
### Questions to Ask Customers
1. Which account(s) are experiencing lockouts?
2. What systems are involved in the issue?
3. Are there any recent changes to the environment (e.g., updates, configuration changes)?
4. Are there any third-party applications running on the affected systems?

### Data to Collect
- StealthAUDIT logs from the affected server.
- Windows Security Event Logs filtered for the affected account and relevant Event IDs.
- Details of any third-party applications running on the systems.

## Common Scenarios & Solutions
### Scenario 1: Authentication Attempts from StealthAUDIT
- **Cause**: Misconfiguration in StealthAUDIT settings.
- **Solution**: Review and correct the configuration to ensure proper account usage.

### Scenario 2: Authentication Attempts from Third-Party Applications
- **Cause**: Local user activity or third-party processes (e.g., BESClient.exe).
- **Solution**: Identify and address the third-party application causing the activity.

### Scenario 3: Incorrect Auditing Configuration
- **Cause**: OS auditing not enabled or misconfigured.
- **Solution**: Enable and configure auditing on all relevant servers.

## Detailed Case Studies
### Case Study: Guest Account Lockouts Due to BESClient.exe
- **Ticket ID**: [500Qk00000EPREhIAP](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EPREhIAP/view)
- **Initial Symptoms**: Reports of the MISOGUEST account being locked out, with suspicion on StealthAUDIT.
- **Diagnostic Steps**:
  1. Searched StealthAUDIT logs for references to MISOGUEST – no results found.
  2. Verified OS auditing settings on the Netwrix server and a Windows 2019 host.
  3. Filtered Windows Security Event Logs for Event IDs 4625 and 4648 – identified activity from BESClient.exe.
- **Key Information**: Authentication attempts were not originating from StealthAUDIT but from local user activity via BESClient.exe.
- **Resolution**: Confirmed StealthAUDIT was not responsible. Advised monitoring local user activity and reviewing third-party application configurations.
- **Key Takeaways**:
  - Always verify the source of authentication attempts using logs and process analysis.
  - Third-party applications can generate unexpected activity unrelated to Netwrix products.

## Best Practices & Tips
1. **Enable Comprehensive Auditing**: Ensure OS auditing is configured on all relevant servers to capture detailed authentication events.
2. **Regular Log Reviews**: Periodically review application and system logs to identify potential issues early.
3. **Collaborate with Security Teams**: Work closely with internal security teams to correlate findings and address concerns.
4. **Document Findings**: Maintain detailed records of troubleshooting steps and resolutions for future reference.
5. **Educate Customers**: Provide guidance on monitoring and managing guest accounts to prevent similar issues.

## Escalation Guidelines
- Escalate to Tier 2 or Tier 3 support if:
  - The issue persists after following the diagnostic methodology.
  - Logs indicate unexpected behavior from StealthAUDIT that cannot be resolved.
  - The customer requires advanced configuration assistance or custom solutions.
- Provide the following when escalating:
  - Detailed description of the issue and steps taken.
  - Relevant logs and event data.
  - Customer environment details and any third-party application information.