## Ticket Metadata
- **Ticket ID:** 500Qk00000GFPcpIAH
- **Case Number:** 422100
- **Status:** Closed - Resolved
- **Account/Company:** Comerica Bank
- **Contact Name:** Maria De La Garza
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** Not specified

## Problem Description
The customer reported that while validating the masking of US Tax IDs, unmasked International Tax IDs (ITINs) were identified, which needed to be masked in accordance with Comerica's policy.

## Environment Details
- The issue was related to the Netwrix Endpoint Protector platform.
- The unmasked ITINs predated September 2023.

## Troubleshooting Steps
1. Reviewed the database for unmasked ITINs.
2. Analyzed the performance of the script used for masking, noting that it was running single-threaded and took a long time to complete.
3. Created a temporary table in QA with both unmasked and masked forms of ITINs.
4. Suggested scheduling a long change window (approximately 6 hours) to run the update in the production environment, preferably on a Sunday.

## Root Cause
The unmasked ITINs were remnants from before September 2023 and were not properly masked due to the database's retention policy. The performance issues during the masking process were attributed to the script's single-threaded execution and potential server load at the time of execution.

## Solution
The unmasked ITINs were removed from the database using the Audit Log Backup for logs older than one year. The update was successfully executed in the production environment during a scheduled maintenance window, ensuring minimal disruption.

## Notes
- Future masking operations should consider the performance implications of single-threaded scripts, especially with large datasets.
- It is advisable to schedule significant updates during off-peak hours to avoid conflicts with operational activities.
- Regular audits of tax ID masking compliance should be conducted to ensure adherence to company policies.