# Netwrix Endpoint Protector Knowledge Base: CAP Clipboard Issues

## Overview
The Content-Aware Protection (CAP) Clipboard feature in Netwrix Endpoint Protector is designed to enforce data loss prevention (DLP) policies by monitoring and restricting clipboard activities. Common issues with this feature include misconfigurations, policy enforcement limitations, and compatibility problems across different operating systems and applications. This article provides a detailed guide to troubleshooting, resolving, and preventing these issues.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Sensitive data bypasses clipboard restrictions | Credit card numbers copied from Excel/Word can be pasted into WhatsApp Desktop | Verify policy settings, test clipboard functionality, check logs | Adjust policy to restrict image data transfer | [Sensitive Data Bypass](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BMifCIAT/view) |
| Clipboard restrictions block internal activities | All copy-paste activities are blocked, including internal ones | Review CAP policy configuration, test clipboard functionality | Adjust policies to allow internal copy-paste activities | [Internal Clipboard Block](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DN5cIIAT/view) |
| Source code copy-paste not blocked | Source code can be copied and pasted despite configured policies | Verify policy application to user groups, analyze logs | Reconfigure policy settings and apply to correct user groups | [Source Code Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EyXCNIA3/view) |
| SQL code paste blocked in SQL Management Studio | SQL code cannot be pasted into SQL Management Studio, but works in other apps | Check CAP policy settings, review CAP logs | Confirm paste restrictions are enabled; behavior is expected | [SQL Code Paste Restriction](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JhYLHIA3/view) |
| Policy not applied to specific websites | Policy fails to block copy-pasting of source code on specific websites | Verify policy settings, confirm user and computer selection | Select specific computer in CAP policy settings | [Website Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JjyjSIAR/view) |
| Clipboard restrictions fail on Ubuntu systems | Clipboard restrictions not enforced; users can bypass policies | Verify regex settings, restart EPP service, test builds | Deploy updated build with corrected regex functionality | [Ubuntu Clipboard Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LgofRIAR/view) |

---

## Detailed Issues

### Sensitive Data Bypasses Clipboard Restrictions
**Symptoms:** Sensitive data, such as credit card numbers, can be copied from Excel or Word and pasted into WhatsApp Desktop despite configured policies.

**Troubleshooting Steps:**
1. Verify CAP policy settings:
   - Ensure "Clipboard" is enabled.
   - Confirm "Credit Card" is added to the denylist.
   - Check "Apply paste restrictions to all monitored applications" is enabled.
2. Test clipboard functionality by attempting to copy and paste sensitive data.
3. Collect logs for further analysis.
4. Schedule a remote session to investigate:
   - Check EPP client rights.
   - Verify DPI certificate status.
   - Review exit points and file extensions in the policy.

**Root Cause:** Clipboard restrictions were bypassed by transferring sensitive data as an image.

**Solution:**
- Adjust CAP policy settings to include restrictions on image data transfer.
- Confirm EPP client rights and policy enforcement.
- Forward logs to R&D for further investigation.

**Source Ticket:** [Sensitive Data Bypass](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BMifCIAT/view)

---

### Clipboard Restrictions Block Internal Activities
**Symptoms:** All copy-paste activities are blocked, including internal ones.

**Troubleshooting Steps:**
1. Review CAP policy configuration to identify misconfigurations.
2. Test clipboard functionality across different applications.
3. Check for updates or patches affecting clipboard functionality.

**Root Cause:** Misconfiguration in CAP policies restricted all clipboard activities instead of external ones.

**Solution:**
- Adjust CAP policies to allow internal copy-paste activities while enforcing external restrictions.
- Test policies to confirm functionality.

**Source Ticket:** [Internal Clipboard Block](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000DN5cIIAT/view)

---

### Source Code Copy-Paste Not Blocked
**Symptoms:** Users can copy and paste source code despite configured policies.

**Troubleshooting Steps:**
1. Verify CAP policy settings for clipboard protection.
2. Confirm policy application to relevant user groups.
3. Conduct tests to replicate the issue.
4. Analyze logs for policy enforcement errors.
5. Schedule a remote session for further investigation.

**Root Cause:** Policy settings were not correctly applied to user groups.

**Solution:**
- Reconfigure CAP policy settings.
- Apply policies to the correct user groups.
- Test clipboard functionality to confirm enforcement.

**Source Ticket:** [Source Code Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EyXCNIA3/view)

---

### SQL Code Paste Blocked in SQL Management Studio
**Symptoms:** SQL code cannot be pasted into SQL Management Studio, but works in other applications like Notepad and Outlook.

**Troubleshooting Steps:**
1. Verify copy-paste functionality in other applications.
2. Check CAP policy settings and confirm "report only" mode.
3. Review CAP logs to confirm SQL code detection.

**Root Cause:** Paste restrictions in CAP policy prevented SQL code from being pasted into SQL Management Studio.

**Solution:**
- Confirm paste restrictions are enabled; behavior is expected.
- Inform customer of expected functionality.

**Source Ticket:** [SQL Code Paste Restriction](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JhYLHIA3/view)

---

### Policy Not Applied to Specific Websites
**Symptoms:** Policy fails to block copy-pasting of source code on specific websites.

**Troubleshooting Steps:**
1. Review CAP policy settings for correct configuration.
2. Confirm denylist includes appropriate file types and source codes.
3. Verify policy application to the correct user and computer.

**Root Cause:** Policy was not applied correctly to the intended computer.

**Solution:**
- Select the specific computer in CAP policy settings.
- Test functionality to confirm enforcement.

**Source Ticket:** [Website Policy Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000JjyjSIAR/view)

---

### Clipboard Restrictions Fail on Ubuntu Systems
**Symptoms:** Clipboard restrictions are not enforced on Ubuntu systems, allowing users to bypass policies.

**Troubleshooting Steps:**
1. Verify CAP policy configuration and regex settings.
2. Restart EPP service on affected endpoints.
3. Collect logs and video evidence for analysis.
4. Provide test builds to the customer for evaluation.

**Root Cause:** Initial Linux build had flawed regex implementation, failing to detect all text.

**Solution:**
- Deploy updated build "v2.4.4.1" with corrected regex functionality.
- Confirm clipboard restrictions are enforced.

**Source Ticket:** [Ubuntu Clipboard Issue](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LgofRIAR/view)

---

## Best Practices
- **Policy Configuration:** Regularly review and update CAP policies to cover all potential data transfer methods, including text and image data.
- **Testing:** Thoroughly test clipboard restrictions across all monitored applications after policy changes.
- **Documentation:** Maintain detailed records of policy configurations and changes for future reference.
- **Monitoring:** Monitor EPP client performance, especially after updates, to identify service interruptions early.
- **Regex Validation:** Test regex configurations extensively before deployment to ensure proper enforcement.

---

## Advanced Topics
### Handling Large-Scale Deployments
For environments with multiple endpoints (e.g., 90+ Ubuntu systems), ensure:
- Consistent policy enforcement across all machines.
- Regular service checks to prevent unresponsiveness.
- Deployment of test builds to address compatibility issues.

### Image Data Transfer Restrictions
When clipboard restrictions fail due to image data transfer:
- Enable image detection in CAP policies.
- Test functionality across applications that support image-based clipboard transfers.

--- 
End of Article.