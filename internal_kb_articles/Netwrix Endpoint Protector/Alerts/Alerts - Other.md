# Netwrix Endpoint Protector: Alerts - Other  
## Overview  
The **Alerts - Other** feature in Netwrix Endpoint Protector (EPP) is designed to notify administrators of specific events or policy violations. Common issues include email alerts not being sent, duplicate alerts, misconfigured notifications, and functionality limitations. This document provides a comprehensive guide to troubleshooting, resolving, and preventing these issues.  

---

## Issue Summary Table  

| Issue | Symptoms | Key Troubleshooting Steps | Solution | Case Reference |
|-------|----------|---------------------------|----------|----------------|
| Email alerts not sent | Alerts not received via email | Verify SMTP settings, test email functionality | Reconfigure SMTP settings or rebuild alert cache | [Email Alerts Not Sent](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BizhOIAR/view) |
| Duplicate alerts | Multiple alerts for the same event | Review alert configuration | Adjust alert settings to prevent duplicates | [Duplicate Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NL5ymIAD/view) |
| Alerts stuck in processing | No alerts generated or sent | Check alert history and rebuild alert cache | Delete and rebuild alert cache | [Alerts Stuck in Processing](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PARLdIAP/view) |
| Disk space issues | Alerts fail due to full disk | Clear logs and unnecessary files | Free up disk space and vacuum logs | [Disk Space Full](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CZaePIAT/view) |
| Notifications to end users | Pop-ups displayed to users | Change client mode to Silent | Disable client notifications | [Disable End-User Notifications](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ObTGZIA3/view) |
| SMTP integration failure | Unable to configure SMTP | Test connectivity, verify port settings | Use app passwords or clear/reconfigure SMTP | [SMTP Integration Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000N5uIsIAJ/view) |
| Alerts for mass file deletions not supported | Unable to configure alerts for bulk deletions | Review alert capabilities | Feature not supported; create feature request | [Mass File Deletion Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PKd6uIAD/view) |

---

## Detailed Issues  

### Email Alerts Not Sent  
**Symptoms:**  
- Alerts configured but not received via email.  
- Test emails fail or are not sent.  

**Troubleshooting Steps:**  
1. Verify SMTP server settings in the EPP console.  
2. Test email functionality using the configured SMTP settings.  
3. Check the `/var/spool` directory for pending emails.  
4. Rebuild the alert cache if necessary.  

**Root Cause:**  
- Misconfigured SMTP settings.  
- Alert cache corruption.  

**Solution:**  
1. Reconfigure SMTP settings:  
   - Ensure correct server address, port, and authentication details.  
   - Use app passwords for email providers like Gmail with 2FA enabled.  
2. Rebuild the alert cache:  
   ```bash
   sudo service epp restart
   ```  
3. Test email functionality after changes.  

**Source Ticket:** [Email Alerts Not Sent](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000BizhOIAR/view)  

---

### Duplicate Alerts  
**Symptoms:**  
- Multiple email alerts for the same event.  

**Troubleshooting Steps:**  
1. Review alert configuration settings in the EPP console.  
2. Check for overlapping or redundant alert rules.  

**Root Cause:**  
- Misconfigured alert rules causing duplicate notifications.  

**Solution:**  
1. Adjust alert configuration to ensure unique triggers for each event.  
2. Test alerts to confirm only one notification is sent per event.  

**Source Ticket:** [Duplicate Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000NL5ymIAD/view)  

---

### Alerts Stuck in Processing  
**Symptoms:**  
- No alerts generated or sent.  
- Alert history shows no recent entries.  

**Troubleshooting Steps:**  
1. Check the alert history in the EPP console.  
2. Delete and rebuild the alert cache.  

**Root Cause:**  
- Alerts stuck in processing due to a large backlog or cache corruption.  

**Solution:**  
1. Delete the existing alert cache:  
   ```bash
   sudo rm -rf /var/cache/epp/alerts
   ```  
2. Rebuild the alert cache:  
   ```bash
   sudo service epp restart
   ```  

**Source Ticket:** [Alerts Stuck in Processing](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PARLdIAP/view)  

---

### Disk Space Issues  
**Symptoms:**  
- Alerts fail to send.  
- Disk space usage exceeds 90%.  

**Troubleshooting Steps:**  
1. Check disk usage with `df -h`.  
2. Identify large files in `/var/log` or `/root` using `du -sh`.  
3. Vacuum logs to reduce size.  

**Root Cause:**  
- Excessive log accumulation or backups consuming disk space.  

**Solution:**  
1. Clear unnecessary files:  
   ```bash
   sudo rm -rf /var/log/*.old
   ```  
2. Vacuum logs:  
   ```bash
   sudo journalctl --vacuum-size=100M
   ```  

**Source Ticket:** [Disk Space Full](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CZaePIAT/view)  

---

### Disable End-User Notifications  
**Symptoms:**  
- Pop-up notifications displayed to end users.  

**Troubleshooting Steps:**  
1. Navigate to **Device Control -> Global Settings**.  
2. Change **Client Mode** to Silent.  
3. Disable notifications in Content Aware Policies.  

**Root Cause:**  
- Client mode set to Normal, allowing notifications.  

**Solution:**  
1. Change client mode to Silent:  
   - Navigate to **Device Control -> Global Settings**.  
   - Select **Silent** mode.  
2. Disable notifications in policies:  
   - Navigate to **Content Aware Protection -> Policies**.  
   - Uncheck **Client Notifications**.  

**Source Ticket:** [Disable End-User Notifications](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000ObTGZIA3/view)  

---

### SMTP Integration Failure  
**Symptoms:**  
- Unable to configure SMTP for email alerts.  
- Test emails fail.  

**Troubleshooting Steps:**  
1. Verify SMTP server details and port settings.  
2. Test connectivity using `telnet`.  
3. Use app passwords for email providers with 2FA.  

**Root Cause:**  
- Port 25 blocked by hosting provider.  
- Incorrect authentication method.  

**Solution:**  
1. Open port 25 if blocked by the hosting provider.  
2. Use app passwords for SMTP authentication.  
3. Test email functionality after changes.  

**Source Ticket:** [SMTP Integration Failure](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000N5uIsIAJ/view)  

---

### Mass File Deletion Alerts Not Supported  
**Symptoms:**  
- Unable to configure alerts for bulk file deletions.  

**Troubleshooting Steps:**  
1. Review alert capabilities in the EPP console.  
2. Confirm whether mass deletion alerts are supported.  

**Root Cause:**  
- Feature not supported in the current version of EPP.  

**Solution:**  
- Inform the customer of the limitation and create a feature request for future updates.  

**Source Ticket:** [Mass File Deletion Alerts](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000PKd6uIAD/view)  

---

## Best Practices  

1. **Regular Maintenance:**  
   - Monitor disk space and clear logs periodically.  
   - Rebuild alert cache after major updates or configuration changes.  

2. **SMTP Configuration:**  
   - Use app passwords for email providers with 2FA.  
   - Test email functionality after any changes.  

3. **Alert Configuration:**  
   - Avoid overlapping or redundant alert rules.  
   - Regularly review and update alert settings.  

4. **Client Notifications:**  
   - Use Silent mode to suppress end-user notifications.  

5. **Feature Requests:**  
   - Submit feature requests for unsupported functionalities, such as mass deletion alerts.  

---

## Advanced Topics  

### Debugging SMTP Issues  
1. Test connectivity to the SMTP server:  
   ```bash
   telnet smtp.example.com 25
   ```  
2. Check logs for errors:  
   ```bash
   tail -f /var/log/maillog
   ```  

### Managing Disk Space  
1. Identify large files:  
   ```bash
   du -sh /var/*  
   ```  
2. Automate log rotation:  
   - Configure `logrotate` to manage log sizes.  

--- 

End of Document.