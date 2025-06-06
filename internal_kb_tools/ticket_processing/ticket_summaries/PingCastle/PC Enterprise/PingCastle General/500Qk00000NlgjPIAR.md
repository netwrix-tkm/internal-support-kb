## Ticket Metadata
- **Ticket ID:** 500Qk00000NlgjPIAR
- **Case Number:** 441124
- **Status:** Closed - Resolved
- **Account/Company:** Würth IT GmbH
- **Contact Name:** Corvin Schmid
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer reported that non-default ASCII characters, such as German umlauts (ö, ä, ü, ß) and characters from Turkish, Czech, or Polish languages, were being replaced with a "?" in the Netwrix Enterprise Web view. This issue raised concerns about the integrity of user and domain data in their Active Directory.

## Environment Details
- The customer operates in an international environment with multiple companies using local language Active Directories.
- The issue was observed in the Enterprise Web view after scanning accounts with non-default ASCII characters.

## Troubleshooting Steps
1. Created an account with a `samaccountname` containing non-default ASCII characters.
2. Ensured the account appeared in a check.
3. Selected the option for "this account supports DES encryption" in the account tab.
4. Added the account directly to the User Rights Assignment policy in Group Policy (e.g., "Logon as batch" or "Act as part of the operating system").
5. Ran a scan and noted that the generated HTML file displayed the characters correctly.
6. Imported the data to the WebUI, where the characters were displayed as "???".

## Root Cause
The issue was identified as a product defect related to how the Enterprise Web view processed and displayed non-default ASCII characters. The raw data was correctly generated, but the WebUI failed to render these characters properly.

## Solution
The issue was resolved following a product release that included updates to the agents. After updating to version 3.3.0.11, the WebUI correctly displayed non-default ASCII characters without replacing them with "?" marks.

## Notes
- Ensure that all agents are updated to the latest version to avoid similar issues in the future.
- Monitor for any future occurrences of character display issues, especially after product updates or changes in the environment.
- Consider documenting any similar cases to assist in quicker resolutions for future incidents involving character encoding issues.