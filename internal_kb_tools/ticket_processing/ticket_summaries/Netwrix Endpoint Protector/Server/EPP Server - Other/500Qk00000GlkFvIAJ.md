```markdown
## Ticket Metadata
- **Ticket ID:** 500Qk00000GlkFvIAJ
- **Case Number:** 423236
- **Status:** Closed - Resolved
- **Account/Company:** CyberArts Biliim
- **Contact Name:** Yunus ICIN
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Server - Other
- **Feature:** N/A
- **Version:** NONE

## Problem Description
The customer, CyberArts Biliim, requested assistance in deploying the Netwrix Endpoint Protector on the Azure platform. They encountered issues with internet connectivity and access to the web interface after starting the trial version of the product.

## Environment Details
- Deployment on Azure
- Initial DNS settings were not configured correctly, leading to internet access issues.

## Troubleshooting Steps
1. The customer attempted to start the product as a trial but received an error indicating no internet connection.
2. They configured the DNS to 8.8.8.8, which restored internet access.
3. After starting the trial, they lost access to the web interface despite the server being accessible via command line.
4. A remote session was scheduled to further investigate the issue.
5. The latest Endpoint Protector Azure Image was shared with the customer.
6. The customer followed the deployment manual for Azure but continued to experience issues with internet access and module activation.

## Root Cause
The initial DNS configuration was incorrect, which prevented the server from accessing the internet. After correcting the DNS settings, the server was able to connect, but further issues arose related to the web interface and module activation.

## Solution
- The customer was advised to re-deploy the EPP appliance using the provided Azure image and to follow the Azure Deployment guide closely.
- After re-deployment, the customer confirmed that the internet issue was resolved, and the modules were activated.
- The customer was instructed to ensure that the Azure inbound and outbound rules allowed necessary URLs for proper functionality.

## Notes
- Ensure that DNS settings are correctly configured before deployment to avoid connectivity issues.
- If the "Agent Status Not Ready" warning appears, it may indicate that the agent is not properly installed or configured.
- For taking snapshots of the server, ensure that the correct virtual machine settings are selected during the deployment process.
```