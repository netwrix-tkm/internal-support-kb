## Ticket Metadata
- **Ticket ID:** 500Qk00000CEVppIAH
- **Case Number:** 412833
- **Status:** Closed - Resolved
- **Account/Company:** Halodata International Pte Ltd
- **Contact Name:** Denni Prima Putra Roli
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** EPP Server - Other
- **Version:** NONE

## Problem Description
The customer requested assistance with sizing an EPP server for a deployment involving 300 Windows endpoints and 200 macOS endpoints. They needed recommendations for server specifications and information regarding support options and High Availability (HA) setup.

## Environment Details
- **Endpoints:** 
  - 300 Windows endpoints
  - 200 macOS endpoints
- **File Shadowing:** 20-30% of endpoints will have file shadowing enabled.
- **Deployment Platform:** Google Cloud Platform (GCP).

## Troubleshooting Steps
1. Initial response provided minimum resource requirements for a server hosting 500 endpoints:
   - **CPU:** 4 CPUs
   - **RAM:** 8GB
   - **Storage:** 300GB disk space
2. Advised that for 20% of endpoints with file shadowing, increased specifications and disk space would be necessary.
3. Clarified that further questions regarding support options and HA setup would be addressed by the account manager.

## Root Cause
The issue stemmed from the customer's need for specific server sizing recommendations and support options for their deployment, which required clarification on resource requirements and support availability.

## Solution
The technical support engineer provided the following recommendations:
- For a cloud-hosted server with 500 endpoints, the minimum specifications are:
  - **CPU:** 4 CPUs
  - **RAM:** 8GB
  - **Storage:** 300GB disk space
- Suggested increasing specifications if file shadowing is enabled for a portion of the endpoints.
- Informed the customer that questions regarding support options and HA setup would be forwarded to the sales team for further assistance.

## Notes
- It is important to note that file shadowing should not be enabled at all times due to potential performance impacts.
- For future reference, ensure that customers are aware of the need to consult with their account manager for specific support options and HA deployment requirements.