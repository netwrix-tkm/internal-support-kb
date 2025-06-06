## Ticket Metadata
- **Ticket ID:** 500Qk00000JPPbNIAX
- **Case Number:** 429642
- **Status:** Closed - Resolved
- **Account/Company:** Naukri
- **Contact Name:** Vaneet Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** Not specified

## Problem Description
The customer, Naukri, requested the provision of a root account for their EPP Virtual Appliance to perform specific operations, including clearing file shadows. The initial account created had limited rights and did not meet their operational needs.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Initial Account Created:** "eppsupport" with limited rights (not sudo)

## Troubleshooting Steps
1. Created the "eppsupport" account for SSH access to the EPP server backend with limited rights.
2. Customer reopened the ticket due to insufficient permissions for their required operations.
3. Connected again to the server to add sudo rights to the "eppsupport" account.

## Root Cause
The initial account created for the customer did not have the necessary permissions (sudo rights) to perform the required operations, leading to the reopening of the ticket.

## Solution
The issue was resolved by creating a root user account for the customer, which provided the necessary permissions to perform all required operations, including clearing file shadows.

## Notes
- Ensure that when creating accounts for customers, the permissions are thoroughly reviewed to meet their operational needs.
- Future requests for root access should be assessed carefully to avoid similar issues with insufficient permissions.