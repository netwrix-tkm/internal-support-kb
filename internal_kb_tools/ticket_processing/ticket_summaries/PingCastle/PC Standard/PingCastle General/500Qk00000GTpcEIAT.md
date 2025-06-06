## Ticket Metadata
- **Ticket ID:** 500Qk00000GTpcEIAT
- **Case Number:** 422522
- **Status:** Closed - Resolved
- **Account/Company:** Arlafoods
- **Contact Name:** Thomas Olesen
- **Product:** PingCastle
- **Component:** PC Standard
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer was running Pingcastle – auditor on multiple domains and sought to consolidate health check reports from these domains. They were uncertain whether they needed the enterprise version of Pingcastle for this consolidation or if they could continue using the auditor version while consolidating the reports.

## Environment Details
- Total domains: 12-15
- Pingcastle running on 5 domains
- Versions in use: Open source edition and auditor version

## Troubleshooting Steps
1. Clarified the customer's requirements regarding report consolidation.
2. Explained the capabilities of the open-source edition, specifically the 'conso' feature for report consolidation.
3. Provided information on the enterprise version's additional features such as action plans, exceptions, and trends.
4. Addressed the customer's question about report generation from separate domains and the requirement for a single Pingcastle source executable.

## Root Cause
The customer was unclear about the capabilities of the different versions of Pingcastle regarding report consolidation and whether the enterprise version was necessary for their needs.

## Solution
The issue was resolved by informing the customer that they could utilize the 'conso' feature in the open-source edition to consolidate health check reports. They were advised to place all XML files for the domains in the PingCastle directory and run the consolidation process by copying and pasting the reports into the same folder after generation.

## Notes
- The 'conso' feature allows for report consolidation without needing all reports to be generated from the same Pingcastle source executable.
- For users requiring advanced features like action plans and trends, upgrading to the enterprise version is recommended.