```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GXLXbIAP
- **Case Number:** 422675
- **Status:** Closed - Resolved
- **Account/Company:** Tech Elecon Pvt. Ltd. (Elecon Engineering Group)
- **Contact Name:** Mohit Shastri
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Network Share
- **Version:** 5.9.3

## Problem Description
The customer reported that the network share functionality was not operational without the Data Loss Prevention (DLP) system in place. They were previously able to use this feature on server version 5.9.3.

## Environment Details
- The issue was observed on Netwrix Endpoint Protector version 5.9.3.
- The customer planned to update the EPP server to version 5.9.4.1 in April to check if the issue persisted.

## Troubleshooting Steps
1. The customer was advised to check the functionality of the network share without the DLP system.
2. It was noted that the client logs were not attached for further analysis.
3. The customer was encouraged to install the latest client version (6.2.2.1006) to see if the behavior changed.
4. The support team reviewed the customer's use case and confirmed that the absence of "File copy" logs was expected behavior given the current setup.

## Root Cause
The root cause was identified as the absence of the EPP client on the machine attempting to access the network share. The client was unable to log file copy actions because it could not track the source of the file transfer from a machine that did not have the client installed.

## Solution
The issue was resolved by advising the customer to update their EPP server to version 5.9.4.1 and to ensure that the EPP client was installed on all relevant machines. This would allow for proper logging and functionality of the network share feature.

## Notes
- Ensure that the EPP client is installed on all machines involved in file transfers to enable proper logging and functionality.
- Future cases should verify the client installation status before troubleshooting network share issues.
```