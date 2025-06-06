# Knowledge Base Reference Guide: Troubleshooting Website Access Issues in Netwrix Endpoint Protector (Content-Aware Protection)

## Overview
This guide provides a comprehensive reference for troubleshooting website access issues within the Content-Aware Protection (CAP) feature of Netwrix Endpoint Protector. Website access issues can arise due to misconfigurations, policy conflicts, or environmental factors such as VPNs or browser settings. Understanding and resolving these issues is critical to maintaining secure and functional web access for end users.

## Technical Background
### Key Concepts
- **Content-Aware Protection (CAP):** A feature that monitors and controls data transfers based on predefined policies, including website access restrictions.
- **Deep Packet Inspection (DPI):** A method used by CAP to analyze network traffic and enforce policies at the packet level.
- **Allowlist/Denylist:** Lists used to explicitly permit or block access to specific URLs or domains.
- **Stealthy DPI Driver:** A configuration that enables DPI functionality while minimizing its visibility to end users.
- **mTLS (Mutual TLS):** A certificate-based authentication mechanism that can be affected by CAP policies.

### System Context
Netwrix Endpoint Protector operates as a security layer between users and the internet, enforcing policies to prevent unauthorized data transfers or access to restricted websites. CAP policies can be configured to block or allow specific URLs, domains, or categories. Misconfigurations or environmental factors (e.g., VPNs, browser compatibility) can lead to unintended website access issues.

## Issue Recognition & Triage
### Symptoms
- Websites are blocked or fail to load.
- Specific content on a website does not render properly.
- Users experience slowness or errors when accessing web applications.
- No logs are generated for blocked websites.
- CAP features (e.g., tabs or policies) are missing on client machines.

### Priority Assessment
- **High Priority:** Critical business websites (e.g., government portals, banking sites) are inaccessible.
- **Medium Priority:** Non-critical websites or applications are affected.
- **Low Priority:** Minor performance issues or cosmetic problems.

## Diagnostic Methodology
### Systematic Approach
1. **Verify Policy Configuration:**
   - Check allowlist/denylist settings.
   - Confirm that the correct CAP policy is applied to the affected endpoints.
2. **Reproduce the Issue:**
   - Attempt to access the website on a test machine.
   - Use different browsers or incognito mode to rule out browser-specific issues.
3. **Analyze Logs:**
   - Review CAP logs for blocked URLs or errors.
   - Check DPI logs for packet inspection details.
4. **Test Environmental Factors:**
   - Disable VPNs or IPv6 temporarily to isolate network-related issues.
   - Test with and without the stealthy DPI driver enabled.
5. **Update Software:**
   - Ensure the Endpoint Protector client and server are running the latest versions.

## Information Collection
### Questions to Ask Customers
- What is the exact URL or domain affected?
- Are all users affected, or only specific ones?
- What browser and version are being used?
- Is the issue occurring on a VPN or specific network?
- Have there been any recent changes to CAP policies or software updates?

### Logs and Data to Collect
- CAP logs and DPI logs.
- Screenshots or videos of the issue.
- Browser developer console logs (if applicable).
- VPN configuration details (if relevant).

## Common Scenarios & Solutions
### Scenario 1: Website Blocked Without Logs
- **Root Cause:** URL not added to the denylist, or denylist not selected in the CAP policy.
- **Solution:** Add the URL to the denylist and ensure the denylist is selected in the CAP policy.

### Scenario 2: VPN Interference
- **Root Cause:** VPN routing rules conflict with CAP policies.
- **Solution:** Update VPN routing rules to allow traffic to the affected URLs. Example: [Ticket 500Qk00000Bh4JmIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bh4JmIAJ/view).

### Scenario 3: Missing CAP Features
- **Root Cause:** Active CAP OTP code prevents policy loading.
- **Solution:** Ensure CAP OTP code is inactive and assign the correct policies. Example: [Ticket 500Qk00000GTc0hIAD](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000GTc0hIAD/view).

### Scenario 4: HTTPS Certificate Issues
- **Root Cause:** Changes in website certificates not recognized by CAP.
- **Solution:** Adjust DPI settings to bypass mTLS errors. Example: [Ticket 500Qk00000F7lxeIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F7lxeIAB/view).

### Scenario 5: Performance Issues with HTTP/2
- **Root Cause:** CAP blocks HTTP/2 connections due to enforced certificates.
- **Solution:** Adjust CAP settings to allow HTTP/2 connections. Example: [Ticket 500Qk00000J8hZWIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000J8hZWIAZ/view).

## Detailed Case Studies
### Case Study 1: VPN Blocking Specific URLs
- **Symptoms:** URLs inaccessible when connected to a VPN.
- **Diagnostic Steps:** Verified CAP policies, disabled IPv6, and tested with updated VPN routing rules.
- **Resolution:** Updated VPN routing rules to allow traffic to the URLs. [Ticket 500Qk00000Bh4JmIAJ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bh4JmIAJ/view).
- **Key Takeaways:** Always test VPN configurations when CAP policies are applied.

### Case Study 2: Missing Logs for Blocked Websites
- **Symptoms:** Website blocked, but no logs generated.
- **Diagnostic Steps:** Reviewed CAP policy and DPI settings.
- **Resolution:** Enabled stealthy DPI driver and added the website to the allowlist. [Ticket 500Qk00000KNjPFIA1](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000KNjPFIA1/view).
- **Key Takeaways:** Ensure DPI settings are configured to log blocked websites.

### Case Study 3: HTTPS Certificate Change
- **Symptoms:** Users unable to log in to a government website.
- **Diagnostic Steps:** Verified certificate changes and DPI settings.
- **Resolution:** Allowed mTLS errors in DPI settings. [Ticket 500Qk00000F7lxeIAB](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000F7lxeIAB/view).
- **Key Takeaways:** Monitor critical website certificates for changes.

### Case Study 4: Slowness Due to HTTP/2 Blocking
- **Symptoms:** Web application performance degraded.
- **Diagnostic Steps:** Reviewed CAP settings and network traffic.
- **Resolution:** Adjusted CAP settings to allow HTTP/2 connections. [Ticket 500Qk00000J8hZWIAZ](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000J8hZWIAZ/view).
- **Key Takeaways:** Test web application performance after CAP policy changes.

## Best Practices & Tips
- **Policy Testing:** Always test CAP policies on a small group of endpoints before wider deployment.
- **Regular Updates:** Keep Endpoint Protector clients and servers updated to the latest versions.
- **Allowlist Management:** Regularly review and update allowlists for critical websites.
- **Log Monitoring:** Continuously monitor CAP and DPI logs for anomalies.
- **Customer Communication:** Clearly explain the steps being taken and provide regular updates during troubleshooting.

## Escalation Guidelines
- **When to Escalate:**
  - Critical business websites remain inaccessible after initial troubleshooting.
  - Logs or diagnostic tools fail to provide actionable insights.
  - Issues involve complex network configurations or third-party software (e.g., VPNs).
- **How to Escalate:**
  - Provide a detailed summary of the issue, including logs, screenshots, and steps already taken.
  - Use the internal escalation process to involve senior engineers or product teams.

By following this guide, support engineers can systematically diagnose and resolve website access issues in Netwrix Endpoint Protector, ensuring minimal disruption to end users.