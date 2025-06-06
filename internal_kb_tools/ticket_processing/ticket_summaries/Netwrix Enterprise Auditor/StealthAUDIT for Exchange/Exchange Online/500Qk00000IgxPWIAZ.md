## Ticket Metadata
- **Ticket ID:** 500Qk00000IgxPWIAZ
- **Case Number:** 427951
- **Status:** Closed - Resolved
- **Account/Company:** West Yavapai Guidance Clinic, DBA Polara Health
- **Contact Name:** Josh Taylor
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for Exchange
- **Feature:** Exchange Online
- **Version:** 11.6

## Problem Description
The customer requested guidance on configuring connections for Exchange Online, specifically regarding the requirements, permissions, and ports necessary for successful integration with Netwrix Enterprise Auditor.

## Environment Details
- **Platform:** Netwrix Enterprise Auditor
- **Collector Code:** StealthAUDIT for Exchange
- **Feature:** Exchange Online

## Troubleshooting Steps
1. Reviewed the target Exchange Online requirements, permissions, and ports as outlined in the Netwrix documentation.
2. Consulted the recommended configurations for the Exchange Online Job Group.
3. Examined the Exchange Custom Connection Profile and Host List setup.
4. Investigated issues related to termed users showing up as errors during the Exchange Online job processing.

## Root Cause
The issue stemmed from the presence of termed (disabled) user accounts in the Exchange Online environment, which were being processed by the auditing job, resulting in errors.

## Solution
The resolution involved configuring the Exchange Online job to automatically exclude termed users from being processed. This adjustment was made following the review of the relevant documentation and configurations provided by Netwrix.

## Notes
- It is important to regularly review and update the configurations for Exchange Online jobs to ensure that termed users do not cause processing errors.
- Future configurations should consider implementing filters to automatically exclude disabled accounts from auditing processes to enhance efficiency and reduce error occurrences.