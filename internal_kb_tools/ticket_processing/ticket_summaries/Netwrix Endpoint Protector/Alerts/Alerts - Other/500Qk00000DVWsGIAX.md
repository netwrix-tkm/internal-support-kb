## Ticket Metadata
- **Ticket ID:** 500Qk00000DVWsGIAX
- **Case Number:** 416013
- **Status:** Closed - Resolved
- **Account/Company:** Florida Lottery
- **Contact Name:** Anthony Davis
- **Product:** Netwrix Endpoint Protector
- **Component:** Alerts
- **Feature:** Alerts - Other
- **Version:** Not specified

## Problem Description
The customer reported that Cyber alerts and advisories from Netwrix were being sent to Lottery Staff who were not part of the ISM distribution list. These staff members were not administrators and did not have access to sensitive vulnerability information. The customer requested assistance to ensure that alerts were only sent to the designated distribution list: ISM@flalottery.com.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Alerts

## Troubleshooting Steps
1. Reviewed the current alert configuration settings in Netwrix Endpoint Protector.
2. Identified that alerts were being sent to a broader audience than intended.
3. Attempted to modify the alert settings to restrict notifications to the specified distribution list.
4. Noted an initial communication issue where no agent was communicating with the server, which was escalated for resolution.

## Root Cause
The root cause of the issue was a misconfiguration in the alert settings, which allowed alerts to be sent to all Lottery Staff instead of restricting them to the ISM distribution list. Additionally, there was a temporary communication issue between the agents and the server that needed to be addressed before changes could be implemented.

## Solution
The issue was resolved by correctly configuring the alert settings in Netwrix Endpoint Protector to ensure that Cyber alerts and advisories were only sent to the specified distribution list (ISM@flalottery.com). After the configuration was updated, the alerts functioned as intended.

## Notes
- Ensure that alert configurations are regularly reviewed to prevent similar issues in the future.
- Be aware of potential communication issues between agents and the server, as these can impact the ability to modify settings effectively.
- It is advisable to document any changes made to alert settings for future reference and troubleshooting.