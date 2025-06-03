## Ticket Metadata
- **Ticket ID:** 500Qk00000HwoHBIAZ
- **Case Number:** 426166
- **Status:** Closed - Resolved
- **Account/Company:** Bridgecom Semiconductors GmbH
- **Contact Name:** Amy Zhang
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client/OS Performance
- **Version:** NONE

## Problem Description
The customer inquired whether Data Loss Prevention (DLP) could prevent Windows Subsystem for Linux (WSL) from uploading files to the external network, similar to the restrictions applied to Windows hosts.

## Environment Details
- The inquiry pertains to the Netwrix Endpoint Protector platform.
- The specific version of the product was not provided.

## Troubleshooting Steps
1. Reviewed the current capabilities of Netwrix Endpoint Protector regarding application exit points.
2. Confirmed that WSL is not currently listed as an exit point under the applications in Endpoint Protector.
3. Suggested the possibility of submitting a feature request to the R&D team to add WSL as an exit point.

## Root Cause
The root cause of the issue was identified as the absence of WSL in the list of applications that can be monitored or restricted by the Netwrix Endpoint Protector. As a result, existing DLP policies could not be enforced on WSL.

## Solution
The issue was resolved by informing the customer that, at the moment, Endpoint Protector does not support WSL as an exit point for DLP policies. The support team offered to submit a feature request to the R&D team to consider adding WSL in future updates. The customer acknowledged this information and requested to close the ticket.

## Notes
- It is important to note that while WSL is not currently supported, customers can request features for future releases.
- Future inquiries regarding similar restrictions should include checking the latest updates from Netwrix for any changes in supported applications.