## Ticket Metadata
- **Ticket ID:** 500Qk00000OJIHyIAP
- **Case Number:** 442710
- **Status:** Closed - Resolved
- **Account/Company:** Alice Blue
- **Contact Name:** Vijayaraghavan K.
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Client Requests
- **Version:** Not specified

## Problem Description
The customer reported issues while attempting to uninstall the Endpoint Protector (EPP) agent from multiple computers. They encountered error messages indicating that a temporary file was missing and that the installer agent could not be found.

## Environment Details
- The issue was reported on approximately 15 to 20 computers.
- Different users were experiencing various error messages during the uninstallation process.

## Troubleshooting Steps
1. Requested a screenshot of the error messages from the customer.
2. Suggested uninstalling the agent via Control Panel -> Uninstall a program.
3. Scheduled a remote session (RS) to further investigate the issue.
4. Confirmed that the installation file was missing on the affected systems.

## Root Cause
The root cause of the issue was identified as the absence of the installation file required for the uninstallation process, leading to multiple error messages across different systems.

## Solution
The issue was resolved by utilizing the ZAP tool, which successfully uninstalled the EPP agent from the affected computers.

## Notes
- Ensure that the uninstallation tool is only used by authorized administrators.
- The tool should be safely removed from the user's machine once it is no longer needed.
- The tool must not be shared with any third parties.