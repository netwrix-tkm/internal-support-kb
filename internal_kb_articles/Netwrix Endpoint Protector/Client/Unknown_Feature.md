# Technical Knowledge Base: Device Whitelisting in Netwrix Endpoint Protector

## Overview
Device Whitelisting is a critical feature in Netwrix Endpoint Protector (EPP) that allows administrators to control access to devices by maintaining a whitelist of approved devices. This ensures secure and efficient device management within an organization. However, issues may arise during the whitelisting process, such as the failure of the existing devices list to populate, which can disrupt workflows and increase administrative overhead.

This article provides a detailed guide to troubleshooting, resolving, and preventing issues related to Device Whitelisting in Netwrix Endpoint Protector.

---

## Issue Summary Table

| Issue                          | Symptoms                                                                 | Key Troubleshooting Steps                              | Solution                                                                 | Case Reference                                                                                     |
|--------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Device list not populating     | Existing devices list fails to load, forcing manual entry of device info | Verify recent updates/upgrades and check server logs | Confirm updates restored functionality; monitor future updates          | [Device list not populating](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CwcduIAB/view) |

---

## Detailed Issues

### Issue: Device List Not Populating
**Symptoms:**  
- The list of existing devices fails to populate in the Device Whitelisting interface.  
- Administrators are forced to manually enter device details, increasing the risk of errors and consuming additional time.

**Troubleshooting Procedure:**  
1. **Verify the Issue:**  
   - Confirm with the customer that the device list is not populating.  
   - Check if the issue is consistent across all devices or specific to certain devices.  

2. **Investigate Recent Updates/Upgrades:**  
   - Ask the customer if any recent updates or upgrades were applied to the Netwrix Endpoint Protector platform.  
   - Review the update/upgrade logs to identify any changes that might have impacted the Device Whitelisting functionality.  

3. **Schedule a Remote Session:**  
   - Request a remote session with the customer to investigate the EPP Server.  
   - During the session, check the server logs for errors or warnings related to the Device Whitelisting feature.  

4. **Test Functionality Post-Update:**  
   - If updates/upgrades were applied, verify whether the issue persists after the update.  
   - Test the Device Whitelisting feature to confirm if the device list is now populating correctly.  

**Root Cause:**  
The issue was caused by a problem in recent functionality updates/upgrades that temporarily disrupted the population of the existing devices list.

**Solution:**  
- The issue was resolved when the customer confirmed that the recent updates/upgrades restored the functionality.  
- The device requests became visible on the server, allowing the admin team to proceed with the whitelisting process as expected.  

**Warnings/Considerations:**  
- Monitor the impact of future updates/upgrades on critical functionalities like Device Whitelisting.  
- Implement a rollback plan for updates that significantly affect user workflows to minimize downtime.  

**Source Ticket:** [Device list not populating](https://nwxcorp.lightning.force.com/lightning/r/Case/500Qk00000CwcduIAB/view)

---

## Best Practices

1. **Pre-Update Testing:**  
   - Before applying updates or upgrades, test them in a staging environment to identify potential issues with critical features like Device Whitelisting.  

2. **Monitor Critical Features Post-Update:**  
   - After applying updates, monitor key functionalities to ensure they are working as expected.  

3. **Maintain a Rollback Plan:**  
   - Always have a rollback plan in place to revert to the previous version if an update causes significant disruptions.  

4. **Regular Backups:**  
   - Perform regular backups of the EPP Server configuration and logs to facilitate troubleshooting and recovery in case of issues.  

5. **Documentation of Changes:**  
   - Maintain detailed documentation of all updates/upgrades, including version numbers, release notes, and known issues, to assist in troubleshooting.  

---

## Advanced Topics

### Handling Edge Cases in Device Whitelisting
In rare scenarios, issues with Device Whitelisting may persist even after updates are applied. These edge cases may require advanced troubleshooting steps, such as:  
- **Database Integrity Checks:**  
   - Verify the integrity of the database storing device information. Corrupted entries may prevent the device list from populating.  

- **Custom Configuration Conflicts:**  
   - Check for custom configurations or policies that might conflict with the Device Whitelisting feature.  

- **Network Connectivity Issues:**  
   - Ensure that the EPP Server has stable network connectivity to all endpoints. Intermittent connectivity issues can disrupt the device list population process.  

For assistance with these advanced scenarios, contact Netwrix Support with detailed logs and configuration files.  

---