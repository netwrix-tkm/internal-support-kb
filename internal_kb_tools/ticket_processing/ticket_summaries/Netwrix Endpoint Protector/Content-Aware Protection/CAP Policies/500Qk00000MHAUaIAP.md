## Ticket Metadata
- **Ticket ID:** 500Qk00000MHAUaIAP
- **Case Number:** 436890
- **Status:** Closed - Resolved
- **Account/Company:** Tayana Mobility Technologies Pvt Ltd
- **Contact Name:** Manoj Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** 6.2.4.2000 (EPP Client)

## Problem Description
The customer reported that the Endpoint Protector (EPP) was not enforcing the Content-Aware Protection (CAP) policy on the MobaXterm application, specifically failing to log file transfers.

## Environment Details
- **Operating System:** Windows 11
- **EPP Client Version:** 6.2.4.2000
- **Server Version:** 5.9.4.1
- **Platform:** On-prem - ESXi

## Troubleshooting Steps
1. The customer created a CAP policy targeting MobaXterm and the SCP protocol.
2. Both block and report actions were attempted without generating logs.
3. The EPP agent was reinstalled to ensure proper functionality.
4. A remote session was scheduled to reproduce the issue and collect logs.

## Root Cause
The root cause was identified as the encryption of SSH protocols, which prevents the inspection of encrypted exit points like MobaXterm. Consequently, the EPP only reports on the protocol used (e.g., SSH or FTP) and does not log the application name.

## Solution
During a remote session, it was confirmed that:
- The "Destination Details" column does not display due to the encryption of the SSH protocol.
- The EPP only logs the protocol used for file transfers, not the application name.
- The customer was advised to submit a feature request to have the application name displayed in the logs instead of just the protocol.

## Notes
- Customers can raise feature requests for improvements to the EPP, such as displaying application names in logs.
- This limitation is inherent to the nature of encrypted protocols and cannot be bypassed without changes to the product's capabilities.