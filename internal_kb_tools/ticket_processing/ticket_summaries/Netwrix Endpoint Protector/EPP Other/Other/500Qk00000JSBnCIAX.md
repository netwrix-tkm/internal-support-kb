## Ticket Metadata
- **Ticket ID:** 500Qk00000JSBnCIAX
- **Case Number:** 429776
- **Status:** Closed - Resolved
- **Account/Company:** Cubet Techno labs Pvt ltd
- **Contact Name:** Andrei Pop
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported an issue where they were unable to create policies or check for updates in the Netwrix Endpoint Protector. An error message was displayed indicating a potential connectivity issue.

## Environment Details
- The issue occurred on the Netwrix Endpoint Protector platform.
- The error message suggested that the Endpoint Protector Server may not have a functional Internet connection or that necessary domains and ports were not whitelisted for outgoing traffic.

## Troubleshooting Steps
1. Verified the Internet connection of the Endpoint Protector Server.
2. Checked firewall settings to ensure that required domains and ports were whitelisted for outgoing traffic.
3. Confirmed the application blocking and custom content settings of the CAP policy applied to Mac.

## Root Cause
The root cause of the issue was identified as a lack of proper Internet connectivity or firewall restrictions that prevented the Endpoint Protector Server from accessing necessary external resources.

## Solution
The issue was resolved by ensuring that the Endpoint Protector Server had a functional Internet connection and that the required domains and ports were properly whitelisted for outgoing traffic. This allowed the server to create policies and check for updates without errors.

## Notes
- Ensure that the Endpoint Protector Server maintains a stable Internet connection to avoid similar issues in the future.
- Regularly review firewall settings to confirm that all necessary domains and ports are whitelisted for the proper functioning of the Endpoint Protector.