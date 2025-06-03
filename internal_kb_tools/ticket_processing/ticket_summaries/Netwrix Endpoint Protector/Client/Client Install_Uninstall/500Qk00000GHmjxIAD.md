## Ticket Metadata
- **Ticket ID:** 500Qk00000GHmjxIAD
- **Case Number:** 422177
- **Status:** Closed - Resolved
- **Account/Company:** Addverb Technologies Limited
- **Contact Name:** Jackson Jimmy
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** Not specified

## Problem Description
The customer reported that they attempted to uninstall the Netwrix Endpoint Protector (EPP) from all online and licensed devices as their license was about to expire. However, the devices were not getting uninstalled and continued to reflect in the console after some time.

## Environment Details
- The issue involved multiple online and licensed devices managed through the Netwrix Endpoint Protector console.
- The customer had decommissioned their server, which may have affected the uninstallation process.

## Troubleshooting Steps
1. The customer executed the uninstall command on all online and licensed devices.
2. The customer attempted to remove devices through the admin console.
3. The support team suggested logging in with an admin user on the affected computers to perform manual uninstallation.
4. The customer inquired if decommissioning the server would affect pending uninstallation jobs.

## Root Cause
The root cause of the issue was identified as the decommissioning of the server, which prevented the uninstallation jobs from being applied to the pending devices. Additionally, the uninstallation command may not have been fully effective on all devices due to their online status.

## Solution
The issue was resolved by advising the customer to manually uninstall the EPP from the affected devices by logging in with an admin user. This approach allowed the customer to successfully remove the software from devices that were not responding to the automated uninstall commands.

## Notes
- It is important to ensure that all devices are online and accessible when performing uninstallation commands.
- Decommissioning servers that manage client installations can disrupt ongoing processes, including uninstallation jobs.
- For future cases, recommend manual uninstallation as a fallback option if automated methods fail.