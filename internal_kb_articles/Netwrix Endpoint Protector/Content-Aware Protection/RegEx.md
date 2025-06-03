# Netwrix Endpoint Protector: Content-Aware Protection (RegEx) Knowledge Base

## Overview
Netwrix Endpoint Protector's Content-Aware Protection feature leverages RegEx functionality to identify and protect sensitive data across various platforms. Common issues in this category include discrepancies in reporting, challenges with encrypted communication platforms, and difficulties in applying DPI certificates for web applications. This article provides detailed troubleshooting procedures, root cause analyses, and tested solutions to address these issues effectively.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Missing Regex dictionary name in logs | Reports pulled from Splunk lack item details field indicating major data type | Investigate logs, test build shared with customer, confirm fix in updated version | Update server and client to version 5941 | [Regex Dictionary Missing in Logs](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EPRRZIA5/view) |
| Blocking sensitive data uploads on encrypted platforms | Unable to block Aadhaar and PAN uploads via WhatsApp Web; DPI certificate not applied to Dropbox | Block URLs, restart browser to apply DPI certificate | Block `web.whatsapp.com`, restart browser for DPI certificate application | [Sensitive Data Upload Blocking](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FoEITIA3/view) |

---

## Detailed Issues

### Issue 1: Missing Regex Dictionary Name in Logs

#### Description
The customer reported that the item details field, which previously indicated the major data type protected via Regex, was missing in the current month's logs pulled from Splunk.

#### Symptoms
- Reports pulled from Splunk lack the item details field.
- Regex dictionary name is not displayed in logs.

#### Troubleshooting Procedure
1. Investigate the logs to identify missing Regex dictionary name.
2. Escalate the issue to the development team for further analysis.
3. Share a test build with the customer to verify the fix.
4. Confirm the issue is similar to a previously reported problem in JIRA.
5. Prioritize the fix for an upcoming release.

#### Root Cause
A configuration issue prevented the Regex dictionary name from being included in the logs, resulting in its absence in reports.

#### Solution
1. Update the server and client to version 5941, which includes a fix for the reporting issue.
2. Verify that the Regex dictionary names are displayed correctly in the logs after the update.

#### Warnings/Considerations
- Ensure customers are informed about the importance of keeping their systems updated to the latest versions to avoid similar issues.
- Monitor reporting features after updates to identify any discrepancies.

**Source Ticket:** [Regex Dictionary Missing in Logs](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000EPRRZIA5/view)

---

### Issue 2: Blocking Sensitive Data Uploads on Encrypted Platforms

#### Description
The customer reported issues with blocking sensitive data uploads (e.g., Aadhaar and PAN card details) through platforms such as WhatsApp Web, email, and Dropbox.

#### Symptoms
- Unable to block sensitive data uploads via WhatsApp Web due to encrypted communication.
- DPI certificate not applied to Dropbox web page until browser restart.
- Email domain whitelisting required for specific use cases.

#### Troubleshooting Procedure
1. **WhatsApp Web Blocking:**
   - Attempt to block `web.whatsapp.com` URL.
   - Confirm that communication is encrypted, preventing monitoring by the EPP client.

2. **Email Domain Whitelisting:**
   - Allow `mail.google.com` to permit file attachments.
   - Block personal email accounts from logging in.

3. **Dropbox Data Uploading:**
   - Restart the Chrome browser to apply the DPI certificate to the Dropbox web page.
   - Verify that uploads are blocked after the DPI certificate is applied.

#### Root Cause
- Encrypted communication on WhatsApp Web prevents monitoring by the EPP client.
- DPI certificate was not applied to the Dropbox web page until the browser was restarted.

#### Solution
1. Block the `web.whatsapp.com` URL, acknowledging that encrypted communications cannot be monitored.
2. Allow `mail.google.com` for file attachments while blocking personal accounts.
3. Restart the Chrome browser to enable the EPP client to apply the DPI certificate to the Dropbox web page, effectively blocking uploads.

#### Warnings/Considerations
- Monitoring encrypted communication platforms like WhatsApp Web may not be possible due to encryption limitations.
- Ensure DPI certificates are applied correctly by restarting the browser if similar issues arise with web applications.
- Regularly review and update whitelisting and blocking rules to ensure compliance with data protection policies.

**Source Ticket:** [Sensitive Data Upload Blocking](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000FoEITIA3/view)

---

## Best Practices

1. **Regular Updates:** Ensure systems are updated to the latest versions to benefit from bug fixes and feature improvements.
2. **Monitor Reporting Features:** After updates, verify that reporting features function as expected to identify discrepancies early.
3. **Encrypted Communication Platforms:** Understand the limitations of monitoring encrypted platforms and explore alternative methods for data protection.
4. **DPI Certificate Application:** Restart browsers after applying DPI certificates to ensure proper functionality.
5. **Whitelisting and Blocking Rules:** Periodically review and update rules to align with organizational data protection policies.

---

## Advanced Topics

### Handling Encrypted Communication Platforms
Encrypted communication platforms like WhatsApp Web pose unique challenges for data monitoring. While URL blocking can prevent access, monitoring the actual data exchanged is not feasible due to encryption. Organizations should consider alternative strategies, such as educating users on data protection policies and implementing endpoint-level controls.

### DPI Certificate Troubleshooting
If DPI certificates fail to apply to web applications, restarting the browser is often an effective solution. For persistent issues, verify certificate installation and compatibility with the browser version.

--- 

End of Article.