## Ticket Metadata
- **Ticket ID:** 500Qk00000MtbezIAB
- **Case Number:** 438720
- **Status:** Closed - Resolved
- **Account/Company:** Andbank Brasil
- **Contact Name:** Renato Coutinho
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device not recognized
- **Version:** 14.1

## Problem Description
The customer reported issues with their EPP administration panel where approximately 30 out of 212 computers were not receiving licenses despite having 225 available licenses. Additionally, some machines appeared offline in the panel even though they were online and had the agent installed.

## Environment Details
- **Platform:** On-premise EPP server
- **Licensing Configuration:** Automatic License release configured for 240 days

## Troubleshooting Steps
1. The customer attempted to uninstall and reinstall the agent on affected machines.
2. The customer used the zap tool to remove the agent and then reinstalled it.
3. The customer changed the IP using the tool without success.
4. The customer reported that some machines did not appear in the dashboard after reinstallation.
5. The customer provided screenshots showing discrepancies in license usage.

## Root Cause
The issue was identified as a problem with the client installation of the EPP agent, which prevented the agent from properly connecting to the server and registering the licenses.

## Solution
The resolution involved using the zap tool to completely remove the existing agent installations. After running the zap tool twice and rebooting, the customer was instructed to reinstall the EPP client using the command line provided by support. This process successfully resolved the licensing issues for the affected machines.

## Notes
- The zap tool is an internal tool and should only be used in extraordinary situations. It must be deleted from each machine after use and not shared with any third party.
- The customer was advised to monitor the situation and report any further issues. If new problems arise, they should reach out for additional support.