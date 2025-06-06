## Ticket Metadata
- **Ticket ID:** 500Qk00000FkJyJIAV
- **Case Number:** 421041
- **Status:** Closed - Resolved
- **Account/Company:** Vinmar International
- **Contact Name:** Paul Pitas
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** NEA Web Report Console
- **Version:** 11.6

## Problem Description
The customer reported that the CDSA job was producing inaccurate information, specifically indicating that SharePoint and weak passwords were showing 100% in summaries, which appeared to be incorrect.

## Environment Details
- **Product Version:** 11.6
- **Build Number:** 11.6.0.64

## Troubleshooting Steps
1. Conducted a thorough regression test of the CDSA.
2. Compiled a list of known issues related to the CDSA, including inaccuracies in sensitive data counts, shadow access rights, and open access calculations.
3. Reviewed the calculations for open access in SharePoint and weak passwords to identify discrepancies.
4. Engaged R&D to investigate the identified bugs and provide a fix.

## Root Cause
The inaccuracies were attributed to a bug in the calculation logic for open access in SharePoint and the handling of weak passwords. Specifically, the calculations were incorrectly aggregating data from multiple sources, leading to inflated percentages.

## Solution
A hotfix was developed and made available to resolve the identified issues. The fix was documented in a knowledge base article, which can be accessed [here](https://nwxcorp.lightning.force.com/lightning/r/General__kav/ka0Qk0000008xcPIAQ/view). The fix was implemented successfully, and the ticket was subsequently closed.

## Notes
- It is important to ensure that the data sources used for calculations are consistent and that duplicate entries are managed to avoid similar issues in the future.
- Future regression tests should include checks for data aggregation logic to prevent inaccuracies in reporting.
- Keep track of known issues and their resolutions to streamline troubleshooting for similar cases.