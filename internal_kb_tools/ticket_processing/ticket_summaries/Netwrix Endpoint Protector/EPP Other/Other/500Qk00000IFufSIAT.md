## Ticket Metadata
- **Ticket ID:** 500Qk00000IFufSIAT
- **Case Number:** 426914
- **Status:** Closed - Resolved
- **Account/Company:** Jukshio
- **Contact Name:** Naveen Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** Not specified

## Problem Description
The customer reported that the Brave browser was not listed in the EPP console for Ubuntu, yet it was widely used within their organization. They requested guidance on how to restrict the use of the Brave browser across the organization.

## Environment Details
- **Operating System:** Ubuntu
- **Browser in Question:** Brave

## Troubleshooting Steps
1. Suggested creating an Application denylist under Denylists and Allowlists >> Denylists >> Applications.
2. Instructed to create a new denylist and enter "brave*" in the Application & CLI Command field.
3. Advised to add the entry to the denylist and generate the list.
4. Recommended creating a custom Content Aware Protection Policy and applying the denylist to test machines.
5. Followed up to confirm the policy was working after closing any active Brave browser sessions.

## Root Cause
The Brave browser was not included in the existing application denylist options for the EPP console on Ubuntu, which led to the inability to restrict its usage.

## Solution
The issue was resolved by guiding the customer through the process of creating a custom denylist for the Brave browser. The steps included:
- Creating a denylist for applications with the entry "brave*".
- Generating the denylist and applying it to a custom Content Aware Protection Policy.
- Testing the policy on test machines to ensure it effectively blocked the Brave browser.

## Notes
- It was noted that while the initial guidance blocked the launch of the Brave browser, the customer later expressed a need to restrict file transfers and certain websites similarly to other browsers. This indicates that additional configurations may be necessary for comprehensive control over browser usage.
- A feature request was suggested to be submitted for future updates to include the Brave browser as a recognized application in the EPP console for Linux OS.