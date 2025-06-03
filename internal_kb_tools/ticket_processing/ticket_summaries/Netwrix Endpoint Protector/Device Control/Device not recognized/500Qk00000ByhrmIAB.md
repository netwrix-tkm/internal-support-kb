## Ticket Metadata
- **Ticket ID:** 500Qk00000ByhrmIAB
- **Case Number:** 412213
- **Status:** Closed - Resolved
- **Account/Company:** Alcatel-Lucent Enterprise
- **Contact Name:** ALE Team
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** 5940

## Problem Description
The customer reported that their USB headset and laptop's built-in camera were not detected by the Rainbow application after enabling Data Loss Prevention (DLP) features.

## Environment Details
- The issue occurred on devices managed by Netwrix Endpoint Protector.
- The problem was specifically noted after enabling DLP.

## Troubleshooting Steps
1. Initial communication established with the impacted user to gather details about the issue.
2. A remote session was scheduled to investigate the problem further.
3. Logs were collected from the affected devices and uploaded to the support ticket.
4. The support team escalated the issue to the R&D team for deeper analysis.
5. A test build was prepared and provided to the customer for further testing.

## Root Cause
The root cause was identified as a conflict between the DLP settings and the recognition of USB audio and video devices by the Rainbow application. This issue was exacerbated by the specific configuration of the DLP features enabled on the devices.

## Solution
The issue was resolved by providing a test build that included improvements for audio device recognition. The customer confirmed that the test build fixed the problem for both the headset and the camera in the Rainbow application. The fix will be included in the official release version 5.9.5.0.

## Notes
- Ensure that any future DLP configurations are tested for compatibility with USB audio and video devices.
- Monitor for any similar reports after updates to the Endpoint Protector software.
- Advise users to report any issues immediately after enabling DLP features to facilitate quicker resolution.