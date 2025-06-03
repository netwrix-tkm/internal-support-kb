```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000JGilKIAT
- **Case Number:** 429264
- **Status:** Closed - Resolved
- **Account/Company:** The Stars Group Interactive Services / Flutter International
- **Contact Name:** Denis Pasca
- **Product:** Netwrix Endpoint Protector
- **Component:** Content-Aware Protection
- **Feature:** Upload Not Blocked
- **Version:** Sequoia 15.1.1

## Problem Description
The customer reported that the Endpoint Protector (EPP) was not blocking uploads for Mac users, specifically those using the Sequoia 15.1.1 OS version. This issue was inconsistent, affecting some users but not all. The problem arose after the integration of MiP policies for production groups, which led to the failure of EPP to block uploads regardless of whether files were labeled.

## Environment Details
- **Operating System:** MacOS Sequoia 15.1.1
- **Integration:** MiP (Microsoft Information Protection) policies activated for both Windows and Mac users.

## Troubleshooting Steps
1. Collected logs from an affected user.
2. Disabled the MiP policy and had the user restart their laptop, which temporarily resolved the blocking issue.
3. Investigated the network extension settings, noting that it was being disabled intermittently.
4. Discussed potential conflicts with the Palo Alto VPN, which might be affecting the EPP's ability to scan traffic.

## Root Cause
The root cause was identified as an intermittent disabling of the network extension, which is crucial for EPP to function correctly. This issue appeared to be exacerbated by the presence of the Palo Alto VPN, which could be tunneling traffic before EPP could scan it.

## Solution
The issue was resolved by performing a clean installation of the EPP client on the affected machines. This ensured that the network extension was properly installed and functioning, allowing EPP to block uploads as intended.

## Notes
- After a MacOS upgrade, it is recommended to restart the computer to ensure that the network extension is installed correctly.
- Monitor for similar issues in the future, especially after OS updates or changes to network configurations.
- If the problem recurs, collect logs with the latest agent version to assist in further troubleshooting.
```