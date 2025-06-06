## Ticket Metadata
- **Ticket ID:** 500Qk00000BehzBIAR
- **Case Number:** 411494
- **Status:** Closed - Resolved
- **Account/Company:** Federal Home Loan Bank of Pittsburgh
- **Contact Name:** Mike Gaetano
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT for NetApp
- **Feature:** Configuration
- **Version:** 11.5

## Problem Description
The customer, Mike Gaetano, inquired whether the Stealthbits Activity Monitor could be used to monitor file shares on a NetApp appliance running in Azure after migrating from an on-premise Windows server. He expressed concerns about not having direct access to the NetApp appliance.

## Environment Details
- The customer is transitioning file shares from an on-premise Windows server to a NetApp appliance hosted in Azure.
- The specific types of NetApp appliances considered were:
  - NetApp Cloud Volumes ONTAP
  - Azure NetApp Files

## Troubleshooting Steps
1. Confirmed the customer's intention to migrate file shares to a NetApp appliance in Azure.
2. Discussed the importance of ensuring open ports and valid credentials for the Activity Monitor to function correctly.
3. Inquired about the type of NetApp appliance being used, as different models have varying support for monitoring protocols.
4. Provided information on the FPolicy protocol, which is essential for activity collection, and noted that Azure NetApp Files did not support it at the time of inquiry.

## Root Cause
The primary concern was the compatibility of the Stealthbits Activity Monitor with the NetApp appliance in Azure, specifically regarding the FPolicy protocol's availability, which is necessary for monitoring file system activity.

## Solution
The support team clarified that:
- The effectiveness of the Stealthbits Activity Monitor would depend on the specific type of NetApp appliance chosen.
- For **NetApp Cloud Volumes ONTAP**, it was indicated that it should work similarly to an on-premise version, allowing monitoring.
- For **Azure NetApp Files**, it was noted that it did not support the FPolicy protocol at the time, which could hinder monitoring capabilities. However, it was mentioned that support for this protocol was on their roadmap.

The customer was advised to investigate further regarding the availability of the FPolicy protocol for their specific NetApp setup.

## Notes
- Ensure that the customer has the correct ports open and valid credentials for the Activity Monitor to function effectively.
- If the customer does not have access to the NetApp appliance, they need to consider how to provide the Activity Monitor with the necessary access.
- Future inquiries should confirm the specific type of NetApp appliance being used to provide accurate guidance on monitoring capabilities.