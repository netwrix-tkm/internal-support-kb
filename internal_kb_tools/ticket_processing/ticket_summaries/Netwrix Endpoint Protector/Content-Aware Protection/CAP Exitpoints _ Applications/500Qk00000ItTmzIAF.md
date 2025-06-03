## Ticket Metadata
- **Ticket ID:** 500Qk00000ItTmzIAF
- **Case Number:** 428425
- **Status:** Closed - Resolved
- **Account/Company:** B3
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** CAP Exitpoints / Applications
- **Version:** Not specified

## Problem Description
The customer, B3, inquired about the functionality of Netwrix Endpoint Protector (EPP) for blocking file transfers in a Linux environment, specifically when using a Windows Subsystem for Linux (WSL) terminal without a graphical user interface (GUI). They provided examples of transfers they wanted to block and sought clarification on whether EPP could handle such scenarios.

## Environment Details
- **Operating Systems:** Windows (with WSL) and Linux
- **Usage Context:** Terminal-based operations without GUI

## Troubleshooting Steps
1. Provided answers to 7 out of 8 questions posed by the customer.
2. Engaged with the EPP team to address the remaining question regarding Bluetooth granularity on Linux.
3. Suggested raising a feature request for Bluetooth granularity on Linux.
4. Communicated with the customer regarding the limitations of EPP in a non-GUI environment, specifically that users would not receive notifications for blocked transfers, but actions would be logged on the EPP server.
5. Offered to schedule a remote session to demonstrate EPP capabilities.

## Root Cause
The primary concern was the lack of GUI in the Linux environment when using WSL, which would prevent users from receiving notifications about blocked file transfers. However, the EPP server would still log these actions.

## Solution
The issue was resolved by:
- Confirming that EPP could function in the described environment, albeit without user notifications.
- Addressing the customer's queries and providing a link to the feature request for Bluetooth granularity on Linux.
- Awaiting further feedback from the customer after providing comprehensive answers to their questions.

## Notes
- Users operating in a terminal-only environment will not receive notifications for blocked actions; however, these actions will be recorded on the EPP server.
- It is advisable to inform customers about the limitations of EPP in non-GUI environments to set proper expectations.
- The feature request for Bluetooth granularity on Linux has been documented and can be tracked via the provided link: [Feature Request](https://netwrix.productboard.com/all-notes/notes/45559479).