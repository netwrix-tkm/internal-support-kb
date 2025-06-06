## Ticket Metadata
- **Ticket ID:** 500Qk00000NrDxxIAF
- **Case Number:** 441420
- **Status:** Closed - Resolved
- **Account/Company:** Eurofins GSC IT Poland Sp. z.o.o.
- **Contact Name:** Korepu Akhil Kumar
- **Product:** PingCastle
- **Component:** PC Enterprise
- **Feature:** PingCastle General
- **Version:** 3.2.0.1

## Problem Description
The customer requested assistance with upgrading the PingCastle version on their development server, seeking documentation or steps to perform the upgrade.

## Environment Details
- Current PingCastle Version: 3.2.0.1
- Planned Upgrade Version: 3.3.0 (ASP.NET 6 to ASP.NET 8)

## Troubleshooting Steps
1. Initial communication established with the customer to understand their requirements.
2. Provided the customer with a detailed upgrade process, including:
   - Checking upgrade documentation for prerequisites.
   - Downloading the upgrade pack zip file.
   - Stopping IIS.
   - Extracting the zip over the installation directory.
   - Ensuring all prerequisites are met.
   - Restarting IIS.
3. Scheduled a call to discuss the current configuration and upgrade process.
4. Followed up on the customer's progress and addressed any issues encountered during the upgrade process.

## Root Cause
The customer faced challenges in downloading the upgrade package due to proxy restrictions, which blocked access to the necessary files.

## Solution
- Conducted a meeting with the customer to walk through the upgrade process step-by-step.
- Provided the customer with the upgrade package via email to bypass the proxy issue.
- Confirmed that the customer was able to perform the upgrade successfully on the development server.

## Notes
- It is crucial to ensure that customers are aware of the need to check for prerequisites before performing upgrades.
- Always confirm the customer's ability to access necessary files and provide alternative methods (like email) if they encounter proxy issues.
- Encourage customers to take backups of their databases before proceeding with upgrades to prevent data loss.