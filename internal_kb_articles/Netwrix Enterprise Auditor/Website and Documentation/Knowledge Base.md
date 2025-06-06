# Knowledge Base Reference Guide: Troubleshooting "Request Header Too Long" Errors in Netwrix Enterprise Auditor

## Overview

This guide addresses issues related to "Request Header Too Long" errors encountered in Netwrix Enterprise Auditor when using Single Sign-On (SSO) authentication. These errors typically occur due to excessively large HTTP request headers, often caused by users being members of numerous Active Directory (AD) groups. Understanding and resolving these issues is critical for ensuring seamless user access and maintaining system performance.

## Technical Background

### Key Concepts
- **HTTP Request Headers**: Headers are metadata sent with HTTP requests, including authentication tokens, cookies, and other information. Servers impose limits on header sizes to prevent resource exhaustion.
- **Single Sign-On (SSO)**: An authentication method allowing users to log in once and access multiple systems without re-entering credentials.
- **Active Directory (AD) Groups**: Organizational units in AD that define user permissions and roles. Membership in many groups can increase the size of authentication-related headers.
- **Tomcat Server Configuration**: Netwrix Enterprise Auditor uses Apache Tomcat, which has configurable limits for HTTP header sizes (`maxHttpHeaderSize`).

### System Context
- **Netwrix Enterprise Auditor**: A platform for IT auditing and compliance. It uses web-based modules for user interaction, including survey actions and reporting.
- **Windows Registry Settings**: The server's HTTP parameters (`MaxFieldLength` and `MaxRequestBytes`) define the maximum allowable size for HTTP headers.

## Issue Recognition & Triage

### Symptoms
- Users encounter a "Request Header Too Long" 400 error when attempting to log in via SSO.
- The issue is intermittent and affects specific users, often those with extensive AD group memberships.
- Logging in via incognito mode or clearing browser cookies/cache resolves the issue temporarily.

### Priority Assessment
- **High Priority**: If the error prevents critical user access to the system.
- **Medium Priority**: If the error affects non-critical modules or a small subset of users.
- **Low Priority**: If the issue is resolved by clearing browser data and does not recur.

## Diagnostic Methodology

### Step-by-Step Approach
1. **Verify Error Message**: Confirm the exact error message and affected functionality.
2. **Test Alternate Scenarios**: Check if users can log in using incognito mode or after clearing browser cookies/cache.
3. **Analyze AD Group Memberships**: Identify if affected users are members of an unusually high number of AD groups.
4. **Review Server Logs**: Examine Tomcat and webserver logs for relevant error messages.
5. **Check Header Size Limits**: Investigate `maxHttpHeaderSize` in Tomcat and HTTP registry settings (`MaxFieldLength` and `MaxRequestBytes`).
6. **Reproduce the Issue**: Use a debug build or test environment to replicate the problem and gather additional data.

## Information Collection

### Customer Questions
- Are all users affected, or only specific ones?
- Can affected users log in using incognito mode or after clearing browser data?
- Are the affected users members of many AD groups? If so, how many?
- Has the issue occurred after recent updates or configuration changes?

### Logs and Data to Collect
- Tomcat server logs (`catalina.out`).
- Webserver logs (IIS or Apache logs).
- Debug build logs (if applicable).
- Windows Event Viewer logs for HTTP-related errors.
- Registry settings for `MaxFieldLength` and `MaxRequestBytes`.

## Common Scenarios & Solutions

### Scenario 1: Excessive AD Group Memberships
- **Symptoms**: Users with many AD group memberships encounter the error.
- **Resolution**: Increase `MaxFieldLength` and `MaxRequestBytes` in the Windows registry:
  ```plaintext
  HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\HTTP\Parameters
  - MaxFieldLength: DWORD 65536 (Dec)
  - MaxRequestBytes: DWORD 16777216 (Dec)
  ```
  Reboot the server after applying changes.

### Scenario 2: Browser Cache Issues
- **Symptoms**: Clearing browser cookies/cache resolves the issue temporarily.
- **Resolution**: Recommend users clear browser data regularly. Investigate server-side caching mechanisms for potential optimizations.

### Scenario 3: Tomcat Configuration Limits
- **Symptoms**: Error persists despite registry changes.
- **Resolution**: Increase `maxHttpHeaderSize` in the Tomcat configuration file (`server.xml`):
  ```xml
  <Connector port="8082" protocol="HTTP/1.1"
             maxHttpHeaderSize="65536"
             connectionTimeout="20000"
             redirectPort="8443" />
  ```
  Restart Tomcat after applying changes.

## Detailed Case Studies

### Case Study: Ticket ID [500Qk00000IoK1JIAV](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000IoK1JIAV/view)
#### Initial Symptoms
- Users encountered a "Request Header Too Long" error when logging in via SSO on the survey action module.
- Logging in via incognito mode worked successfully.

#### Diagnostic Steps
1. Verified error message and tested alternate login scenarios.
2. Identified affected users as members of numerous AD groups.
3. Reviewed Tomcat logs and confirmed header size limits were exceeded.
4. Suggested clearing browser cookies/cache and increasing `maxHttpHeaderSize`.

#### Key Information Leading to Solution
- Affected users had extensive AD group memberships, resulting in large authentication headers.
- Default registry settings for `MaxFieldLength` and `MaxRequestBytes` were insufficient.

#### Resolution
- Increased registry settings:
  ```plaintext
  HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\HTTP\Parameters
  - MaxFieldLength: DWORD 65536 (Dec)
  - MaxRequestBytes: DWORD 16777216 (Dec)
  ```
- Rebooted the server, resolving the issue.

#### Key Takeaways
- Always check AD group memberships for affected users.
- Registry settings and Tomcat configuration limits are common root causes.
- Document changes thoroughly to ensure security considerations are addressed.

#### Efficiency Improvements
- Develop automated scripts to check header size limits and AD group memberships.
- Create a pre-configured debug build for faster issue reproduction.

## Best Practices & Tips

1. **Proactive Monitoring**: Regularly review server logs for header size-related errors.
2. **Documentation**: Maintain detailed records of registry and configuration changes for future reference.
3. **Customer Communication**: Clearly explain the technical reasoning behind solutions and potential security implications.
4. **Testing**: Use test environments to replicate issues and validate solutions before applying them in production.
5. **Security Considerations**: Balance increased header size limits with potential risks, such as resource exhaustion or denial-of-service attacks.

## Escalation Guidelines

### Criteria for Escalation
- Issue persists despite registry and Tomcat configuration changes.
- Affected users are unable to access critical system functionality.
- Logs indicate underlying issues beyond header size limits (e.g., authentication server errors).

### Escalation Procedure
1. Gather all relevant logs and diagnostic data.
2. Document steps already taken and their outcomes.
3. Escalate to the development team with a detailed summary of findings.
4. Provide a debug build and test environment for further investigation.

End of document.