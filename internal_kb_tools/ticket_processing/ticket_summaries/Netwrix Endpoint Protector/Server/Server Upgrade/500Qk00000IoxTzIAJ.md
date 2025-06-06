## Ticket Metadata
- **Ticket ID:** 500Qk00000IoxTzIAJ
- **Case Number:** 428202
- **Status:** Closed - Resolved
- **Account/Company:** GUIDEWIRE
- **Contact Name:** Brett Atwell
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** 5.9.4.0

## Problem Description
The customer reported that their virtual appliance was running an unsupported version of Ubuntu. Their internal security team mandated an upgrade of the base OS or a migration to a new version, but the customer was unsure how to proceed due to the lack of an internal update mechanism in the Endpoint Protector (EPP).

## Environment Details
- **Hosting:** Amazon EC2 Cloud
- **Current OS Version:** Ubuntu 18.x
- **Current EPP Server Version:** 5.9.4.0

## Troubleshooting Steps
1. Requested details about the current appliance setup from the customer, including whether it was on-premise or cloud-hosted, the OS version, and the EPP server version.
2. Confirmed that the appliance was hosted on Amazon EC2 and running Ubuntu 18.x.
3. Informed the customer that the procedure would involve migrating data and settings from the old server to a new one.
4. Requested the customer's AWS Account ID and region to share the latest EPP appliance image.
5. Coordinated with DevOps to share the AWS AMI with the customer.
6. Provided the customer with instructions to deploy the new appliance image and scheduled a remote session for data migration.

## Root Cause
The root cause of the issue was the use of an unsupported version of the Ubuntu operating system on the virtual appliance, which did not comply with the security requirements set by the customer's internal team.

## Solution
The issue was resolved by:
1. Sharing the latest Endpoint Protector AWS AMI with the customer.
2. Guiding the customer through the deployment of the new appliance image on their AWS account.
3. Successfully performing the data migration from the old server to the new one during a scheduled remote session.

## Notes
- Ensure that customers are aware of the importance of running supported versions of operating systems to comply with security policies.
- Future cases involving appliance upgrades should follow a similar procedure of verifying the current environment, sharing the appropriate AMI, and assisting with data migration.