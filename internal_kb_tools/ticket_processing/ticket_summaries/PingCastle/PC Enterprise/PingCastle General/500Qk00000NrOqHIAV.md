## Ticket Metadata
- **Ticket ID:** 500Qk00000NrOqHIAV
- **Case Number:** 441448
- **Status:** Closed - Resolved
- **Account/Company:** Thales Group
- **Contact Name:** Julien Maltaverne
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.3

## Problem Description
The customer, Julien Maltaverne, reported difficulties in using custom rules with the standalone PingCastle client. Specifically, he was unsure about the correct syntax to increase the maturity level of the rule with RiskId "P-DsHeuristicsDoListObject" to level 5.

## Environment Details
- The customer was using the PingCastle Enterprise version under a trial license.
- The issue was related to the syntax used in the custom rules configuration.

## Troubleshooting Steps
1. The customer attempted to modify the custom rules using various syntaxes but was unsuccessful.
2. The support team provided guidance on the correct syntax for modifying custom rules.
3. The customer confirmed that he was using the auditor version of PingCastle, which does not support custom rules.
4. The support team clarified that custom rules are only functional in the Professional and Enterprise editions.
5. The customer was advised to check the configuration in the PingCastle.exe.config file.

## Root Cause
The issue stemmed from the customer's use of the auditor version of PingCastle, which does not support custom rules. The customer was attempting to apply custom rules syntax without having the appropriate version that allows such modifications.

## Solution
The support team provided the correct syntax for modifying the custom rules and confirmed that the customer needed to use the Enterprise version to implement custom rules effectively. The customer was able to test the solution after receiving a new trial license for the Enterprise version, which resolved the issue.

## Notes
- Custom rules are a paid feature and are only available in the Professional and Enterprise editions of PingCastle.
- Users should ensure they are using the correct version of PingCastle to utilize custom rules.
- For disconnected networks, users can specify custom rules in the PingCastle.exe.config file, but they must first configure them in the web UI and download the necessary XML configuration.