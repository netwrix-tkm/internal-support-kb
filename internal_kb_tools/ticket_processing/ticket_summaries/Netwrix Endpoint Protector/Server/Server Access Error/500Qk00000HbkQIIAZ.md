## Ticket Metadata
- **Ticket ID:** 500Qk00000HbkQIIAZ
- **Case Number:** 425339
- **Status:** Closed - Resolved
- **Account/Company:** Astorg Group Sàrl
- **Contact Name:** Julien Millet
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer reported that they were unable to access the Endpoint Protector admin console via their designated URL, resulting in a timeout error in all internet browsers.

## Environment Details
- **URL:** [https://xm861dp.hosted.endpointprotector.com/index.php/](https://xm861dp.hosted.endpointprotector.com/index.php/)
- **Contact Information:** Julien Millet, Chief Technologies Officer, Astorg Group Sàrl

## Troubleshooting Steps
1. The customer initially reported the issue and provided a screenshot of the timeout error.
2. The support engineer requested additional details about the error message and asked for a screenshot.
3. Access to the EPP server backend was requested from the DevOps team for further investigation.
4. After obtaining access, the support team performed a server restart and checked the status of all services.

## Root Cause
The issue was caused by a temporary service disruption on the server, which led to the admin console being inaccessible and resulted in timeout errors for users attempting to connect.

## Solution
The issue was resolved by restarting the server, which restored all services to operational status. The customer was then able to access the admin console successfully.

## Notes
- Ensure that server health checks are regularly performed to prevent similar issues in the future.
- If users report access issues, consider server restarts as a potential troubleshooting step, especially if service disruptions are suspected.