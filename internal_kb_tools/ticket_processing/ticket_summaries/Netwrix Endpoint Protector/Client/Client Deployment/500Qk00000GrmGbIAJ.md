## Ticket Metadata
- **Ticket ID:** 500Qk00000GrmGbIAJ
- **Case Number:** 423525
- **Status:** Closed - Resolved
- **Account/Company:** IT Webster Limited
- **Contact Name:** Support IT Webster
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** 13.1

## Problem Description
The customer requested the deployment of the Endpoint Protector mac client using Jamf Pro, specifically asking for the `EndpointProtector.pkg` package and the `epp_change_ip.sh` script to be uploaded to their Jamf Pro environment.

## Environment Details
- The issue pertains to the deployment of the Netwrix Endpoint Protector client on macOS devices managed by Jamf Pro.

## Troubleshooting Steps
1. Verified the availability of the `EndpointProtector.pkg` package and `epp_change_ip.sh` script.
2. Ensured that the Jamf Pro server was configured correctly to accept the package and script.
3. Checked for any compatibility issues between the Endpoint Protector version and the Jamf Pro version.
4. Reviewed the deployment logs in Jamf Pro for any errors or warnings during the upload process.

## Root Cause
The root cause of the issue was not explicitly identified in the case; however, it was determined that the necessary files for deployment were not initially available to the customer.

## Solution
The issue was resolved by providing the customer with the correct links to download the `EndpointProtector.pkg` package and the `epp_change_ip.sh` script. Once the customer uploaded these files to their Jamf Pro, the deployment proceeded successfully.

## Notes
- Ensure that customers have access to the latest versions of deployment packages and scripts to avoid similar issues in the future.
- It is advisable to confirm the compatibility of the Endpoint Protector version with the Jamf Pro version before deployment to prevent potential conflicts.