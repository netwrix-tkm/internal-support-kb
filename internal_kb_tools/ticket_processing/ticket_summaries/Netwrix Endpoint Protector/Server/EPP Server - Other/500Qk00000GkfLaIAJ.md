## Ticket Metadata
- **Ticket ID:** 500Qk00000GkfLaIAJ
- **Case Number:** 423202
- **Status:** Closed - Resolved
- **Account/Company:** Blue Halo
- **Contact Name:** Michael Almaguer
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** EPP Server - Other
- **Version:** 5.9.3.0

## Problem Description
Blue Halo reported that they needed assistance with the Azure Monitoring Agent installation on their EPP server, which was hosted in Azure. They indicated that they did not have access to the host itself and required guidance on how to proceed with the installation.

## Environment Details
- **Hosting:** Azure Cloud
- **Operating System:** Ubuntu 22.04.2 LTS
- **EPP Server Version:** 5.9.3.0

## Troubleshooting Steps
1. Confirmed the hosting environment and server details with the customer.
2. Engaged the legal department to create a supplemental user account for installation purposes.
3. Communicated with the customer regarding the need for a signed Non-Disclosure Agreement (NDA) and waiver for installation.
4. Provided instructions for the customer to install the Azure ARC agent prior to the Azure Monitoring Agent installation.
5. Followed up with the customer regarding the stuck update at 64% on the EPP server.

## Root Cause
The issue stemmed from the lack of access to the host machine for the installation of the Azure Monitoring Agent, compounded by the requirement for legal documentation to allow installation on a customer-hosted environment.

## Solution
- Created a supplemental SSH account for the customer after receiving confirmation from the legal department.
- Provided the customer with the necessary documentation and instructions to proceed with the installation of the Azure Monitoring Agent.
- Ensured that the customer was aware of the requirement to install the Azure ARC agent before proceeding with the Azure Monitoring Agent installation.

## Notes
- Ensure that all legal documentation is in place before attempting installations on customer-hosted environments.
- Always confirm the hosting details and server version with the customer to tailor the support provided.
- Advise customers to check for any pending updates that may affect the installation process.