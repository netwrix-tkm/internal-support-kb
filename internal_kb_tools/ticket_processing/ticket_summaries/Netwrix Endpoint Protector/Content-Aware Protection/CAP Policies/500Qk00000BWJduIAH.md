## Ticket Metadata
- **Ticket ID:** 500Qk00000BWJduIAH
- **Case Number:** 411217
- **Status:** Closed - Resolved
- **Account/Company:** AconSeg
- **Contact Name:** Mariano Amigo
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Policies
- **Version:** 5.9.4.1

## Problem Description
The customer reported issues configuring the GitHub Client, specifically that remote repositories were unable to receive information about packages for CAP (Content-Aware Protection) detection during commits. They requested the ability to allow only specific domains through the GitHub Client.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Feature in Use:** CAP Policies
- **Customer Requirement:** Use of DPI (Deep Packet Inspection) allowlists for Git.

## Troubleshooting Steps
1. Reviewed the configuration settings for the GitHub Client.
2. Confirmed the issue with remote repositories not receiving package information.
3. Discussed the possibility of implementing DPI allowlists for Git with the customer.
4. Scheduled a remote session to update the system to version 5.9.4.1 to address the issue.
5. Communicated with internal teams regarding the feature request for allowing specific domains.

## Root Cause
The issue was related to limitations in the existing version of the Netwrix Endpoint Protector that prevented proper handling of GitHub Client configurations for specific domain allowlisting.

## Solution
The problem was resolved by updating the Netwrix Endpoint Protector to version 5.9.4.1, which included enhancements to the CAP policies that allowed for better handling of GitHub Client configurations and the implementation of DPI allowlists.

## Notes
- It is important to ensure that customers are aware of the limitations regarding domain allowlisting with GitHub when using DPI.
- Future requests for similar features should be tracked and communicated to the product development team for potential inclusion in upcoming releases.