## Ticket Metadata
- **Ticket ID:** 500Qk00000HNRnJIAX
- **Case Number:** 424816
- **Status:** Closed - Resolved
- **Account/Company:** Renewbuy
- **Contact Name:** Anil Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** EPP Other
- **Feature:** Other
- **Version:** NONE

## Problem Description
The customer reported an issue with the automatic allocation of DLP licenses. When attempting to reassign licenses to a new set of 400 users, removing one user resulted in another user being automatically assigned a license, preventing the customer from assigning licenses to specific users only.

## Environment Details
- The customer is using Netwrix Endpoint Protector.
- The issue pertains to the management of DLP licenses within the system.

## Troubleshooting Steps
1. Confirmed the customer's requirement to reassign licenses to a specific group of users.
2. Explained the automatic license allocation process, which prevents exceeding the number of available licenses.
3. Advised the customer to ensure they have enough free licenses (400 in this case) before attempting to reassign.
4. Suggested uninstalling clients from computers that were to be decommissioned to free up licenses.
5. Provided guidance on how to uninstall clients from the DLP console.

## Root Cause
The automatic allocation of licenses is designed to ensure that the total number of licenses in use does not exceed the number of licenses purchased. This mechanism prevents manual assignment of licenses to specific users unless there are enough free licenses available.

## Solution
The issue was resolved by explaining the automatic license allocation process and advising the customer on the steps needed to free up licenses. The customer was informed that they needed to uninstall clients from systems they wished to decommission to make the licenses available for reassignment to the new group of users.

## Notes
- It is important for customers to understand the automatic license allocation process to manage their licenses effectively.
- Customers should ensure they have sufficient free licenses before attempting to reassign them to avoid similar issues in the future.
- Providing a method for bulk license assignment via an Excel sheet was not addressed in this case but could be a potential enhancement for future discussions.