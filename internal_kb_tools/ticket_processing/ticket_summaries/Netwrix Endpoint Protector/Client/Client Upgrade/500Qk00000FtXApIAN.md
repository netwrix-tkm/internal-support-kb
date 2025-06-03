## Ticket Metadata
- **Ticket ID:** 500Qk00000FtXApIAN
- **Case Number:** 421306
- **Status:** Closed - Resolved
- **Account/Company:** Uniphore
- **Contact Name:** Walt McClelland
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Upgrade
- **Version:** 6.2.3.1010

## Problem Description
The customer reported that after upgrading the admin console to version 5.9.4.0 and pushing the latest Windows version of Endpoint Protector (6.2.3.1010) using the "Client Software Upgrade" feature, a new popup appeared prompting users to accept an "End User Agreement." The customer requested assistance in suppressing this alert to avoid alarming over 1000 users during the upgrade process.

## Environment Details
- **Admin Console Version:** 5.9.4.0
- **Client Software Version:** 6.2.3.1010
- **Number of Users Affected:** 1000+

## Troubleshooting Steps
1. Confirmed the version of the admin console and client software being used.
2. Reviewed the upgrade process and the appearance of the End User Agreement popup.
3. Informed the customer about the behavior of the End User License Agreement (EULA) during client upgrades.

## Root Cause
The EULA popup is designed to appear only on the Endpoint Protector Server during the upgrade process and does not affect client installations. This behavior is by design and is not indicative of a malfunction.

## Solution
The issue was resolved by informing the customer that the EULA prompt only appears on the EPP Server and that there is no need for concern regarding the client upgrade process. Users will not be required to accept the EULA during their client upgrades.

## Notes
- The EULA prompt is a standard feature and does not require suppression for client upgrades.
- It is important to communicate to customers that this behavior is expected and does not impact the client upgrade experience.