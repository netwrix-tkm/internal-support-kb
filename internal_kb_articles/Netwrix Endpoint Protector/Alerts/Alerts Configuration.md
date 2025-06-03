# Netwrix Endpoint Protector: Alerts Configuration Knowledge Base

## Overview
The Alerts Configuration feature in Netwrix Endpoint Protector (EPP) allows administrators to set up notifications for various events, such as device control violations, content-aware protection alerts, and system activity. While this feature is critical for maintaining security and compliance, misconfigurations or environmental factors can lead to issues such as unwanted alerts, missing notifications, or email delivery failures. This article provides a comprehensive guide to troubleshooting and resolving common issues related to Alerts Configuration.

---

## Issue Summary Table

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Unwanted alerts during UAT | Alerts triggered for all device connections instead of prohibited actions | Verify notification settings and customize alerts | Configure custom notifications for Device Control and Content-Aware Protection | [Unwanted Alerts During UAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BhcIFIAZ/view) |
| Pop-up notifications for monitoring policies | Users see unwanted pop-ups | Disable Client Notifications in Content-Aware Policies | Turn off Client Notifications in policy settings | [Pop-up Notifications for Monitoring Policies](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bm0sGIAR/view) |
| Email alerts not received for external email monitoring | No email alerts triggered for external domain emails | Verify email settings and test SMTP configuration | Correct email settings and test alerts | [Email Alerts for External Emails](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BmsvpIAB/view) |
| Alerts not sent for blocked devices | No email alerts for blocked USB connections | Clear alert queues and reset notification system | Clear alert queues and restart notification system | [Alerts Not Sent for Blocked Devices](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bq3l3IAB/view) |
| Email alerts sent to deleted admin | Alerts sent to removed admin email | Check alert configuration and remove old admin settings | Remove super admin tag for deleted users | [Email Alerts Sent to Deleted Admin](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BQ6EjIAL/view) |
| Email alerts not configured for Gmail | Unable to configure Gmail SMTP | Provide Gmail-specific SMTP settings and App password instructions | Configure Gmail SMTP with App password | [Gmail SMTP Configuration](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C7TzFIAV/view) |
| Invalid sender error in email alerts | Test emails flagged as "Invalid Sender" | Verify email security system and sender configuration | Correct sender configuration in email security system | [Invalid Sender Error](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000C862yIAB/view) |
| Alerts not triggered for DLP policy changes | No alerts for admin changes to DLP policies | Confirm feature availability and log enhancement request | Feature request added to roadmap | [DLP Policy Change Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E5GIiIAN/view) |
| SMTP alerts not sent due to TLS 1.3 | SMTP alerts fail in legacy mode | Disable TLS 1.3 for legacy SMTP | Adjust SMTP settings to disable TLS 1.3 | [SMTP Alerts and TLS 1.3](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CPonVIAT/view) |
| Alerts not sent due to missing root email | No alerts sent for CAP and Device Control policies | Verify root user email configuration | Configure root user email address | [Missing Root Email for Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000LIkQ5IAL/view) |

---

## Detailed Issues

### Unwanted Alerts During UAT
**Symptoms:** Alerts triggered for all device connections during User Acceptance Testing (UAT), instead of only prohibited actions.  
**Troubleshooting Steps:**
1. Verify the EPP server and client versions.
2. Check notification settings under **System Parameters > Device Types and Notifications**.
3. Clarify customer requirements for specific alerts (e.g., file copying to USB).  
**Root Cause:** Default notification settings were not customized for UAT.  
**Solution:**  
- Configure custom notifications for Device Control (DC) and Content-Aware Protection (CAP) modules.  
**Source Ticket:** [Unwanted Alerts During UAT](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BhcIFIAZ/view)

---

### Pop-up Notifications for Monitoring Policies
**Symptoms:** Users see unwanted pop-up notifications due to monitoring policies.  
**Troubleshooting Steps:**
1. Navigate to **Content Aware Protection > Content Aware Policies**.
2. Edit the policies and disable **Client Notifications**.  
**Root Cause:** Enabled Client Notifications in Content-Aware Policies.  
**Solution:**  
- Disable Client Notifications in the policy settings.  
**Source Ticket:** [Pop-up Notifications for Monitoring Policies](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bm0sGIAR/view)

---

### Email Alerts for External Emails
**Symptoms:** No email alerts triggered for emails sent to external domains (e.g., @gmail.com).  
**Troubleshooting Steps:**
1. Verify email settings in the EPP web console.
2. Conduct a test email to confirm SMTP functionality.
3. Schedule a remote session for further investigation if needed.  
**Root Cause:** Incorrect email settings in the EPP web console.  
**Solution:**  
- Correct email settings and test alerts to ensure functionality.  
**Source Ticket:** [Email Alerts for External Emails](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BmsvpIAB/view)

---

### Alerts Not Sent for Blocked Devices
**Symptoms:** No email alerts triggered when blocked USB devices are connected.  
**Troubleshooting Steps:**
1. Verify alert notification rules.
2. Clear alert queues to remove any backlog.
3. Reset the notification system by deleting old entries.  
**Root Cause:** Backlog in alert queues prevented notifications.  
**Solution:**  
- Clear alert queues and reset the notification system.  
**Source Ticket:** [Alerts Not Sent for Blocked Devices](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000Bq3l3IAB/view)

---

### Email Alerts Sent to Deleted Admin
**Symptoms:** Email alerts sent to an administrator who was removed from the system.  
**Troubleshooting Steps:**
1. Check if the deleted admin is still listed in alert configurations.
2. Remove the super admin tag for deleted users.  
**Root Cause:** Old configurations retained in the system for deleted administrators.  
**Solution:**  
- Remove the super admin tag for deleted users and verify alert recipients.  
**Source Ticket:** [Email Alerts Sent to Deleted Admin](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BQ6EjIAL/view)

---

## Best Practices
1. **Customize Alerts:** Tailor notification settings to align with organizational requirements, especially during UAT phases.
2. **Verify Email Settings:** Ensure SMTP configurations are correct and test email functionality after any changes.
3. **Monitor Alert Queues:** Regularly check and clear alert queues to prevent backlogs.
4. **Document Changes:** Maintain a record of all configuration changes for future reference and troubleshooting.
5. **Use App Passwords:** For Gmail and other services requiring App passwords, ensure they are correctly configured.

---

## Advanced Topics

### Handling High Log Volumes
- **Scenario:** High CPU usage due to excessive logs prevents access to the Alerts menu.  
- **Solution:** Upgrade server hardware (CPU and RAM) to handle the increased load.  
**Source Ticket:** [High Log Volume Impacting Alerts Menu](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NgOOtIAN/view)

### Feature Requests for Missing Alert Types
- **Scenario:** No alerts for DLP policy modifications by administrators.  
- **Solution:** Submit a feature request to the Netwrix development team for future implementation.  
**Source Ticket:** [DLP Policy Change Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000E5GIiIAN/view)