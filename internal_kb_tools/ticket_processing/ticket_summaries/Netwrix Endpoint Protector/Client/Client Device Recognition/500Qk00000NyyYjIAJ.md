## Ticket Metadata
- **Ticket ID:** 500Qk00000NyyYjIAJ
- **Case Number:** 441824
- **Status:** Closed - Resolved
- **Account/Company:** Techsol Infosec
- **Contact Name:** Umesh Shetty
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Device Recognition
- **Version:** 12.04

## Problem Description
The client, Techsol Infosec, faced challenges in connecting an out-of-office (OOO) user to their on-premises server after recently purchasing Data Loss Prevention (DLP) software. They inquired about the feasibility of using NAT (Network Address Translation) to facilitate this connection, especially since there was no Fully Qualified Domain Name (FQDN) option available for internet connectivity.

## Environment Details
- The client was using Netwrix Endpoint Protector with a focus on Client Device Recognition.
- The version in use was 12.04.

## Troubleshooting Steps
1. The client reached out to support for guidance on how to connect the OOO user to the on-premises server.
2. Technical support engineer Andrei provided information on using NAT or port forwarding from a public IP to allow the Endpoint Protector client to communicate with the server.
3. It was emphasized that the method used should not involve SSL termination, as this could affect the client-server certificate.

## Root Cause
The issue stemmed from the lack of a proper method for the OOO user to connect to the on-premises server without an FQDN, which is typically necessary for secure and reliable communication over the internet.

## Solution
The client successfully implemented the suggested NAT configuration, allowing the Endpoint Protector client to communicate with the on-premises server. This solution resolved the connectivity issue for the OOO user.

## Notes
- Ensure that any NAT or port forwarding configurations do not introduce SSL termination to avoid issues with client-server certificate validation.
- Future clients facing similar issues should be advised to consider alternative methods for remote connectivity, such as VPNs, if NAT does not meet their security requirements.