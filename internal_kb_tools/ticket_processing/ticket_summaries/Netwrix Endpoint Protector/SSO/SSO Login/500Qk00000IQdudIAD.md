## Ticket Metadata
- **Ticket ID:** 500Qk00000IQdudIAD
- **Case Number:** 427320
- **Status:** Closed - Resolved
- **Account/Company:** BioCatch
- **Contact Name:** Daniel Itenberg
- **Product:** Netwrix Endpoint Protector
- **Component:** SSO
- **Feature:** SSO Login
- **Version:** NONE

## Problem Description
The customer enabled Single Sign-On (SSO) on their instance, which functioned correctly. However, they encountered an issue where non-super admin users could not access the local super user admin account, leading to a request to disable SSO from the backend.

## Environment Details
- The issue occurred after enabling SSO for the Netwrix Endpoint Protector platform.
- Users affected were not super admins, which restricted their access to the local admin login.

## Troubleshooting Steps
1. The support engineer confirmed the ability to remove the SSO option from the backend.
2. The SSO setting was disabled by the support engineer.
3. The customer was asked to attempt logging in again to verify if the issue was resolved.
4. The customer reported that they could still log in via SSO, prompting further discussion about completely removing the SSO configuration.
5. The support engineer confirmed the removal of the SSO settings and requested the customer to test the login again.

## Root Cause
The root cause of the issue was the enabling of SSO, which restricted access to the local super user admin account for non-super admin users. This configuration prevented the customer from accessing necessary administrative functions.

## Solution
The support engineer successfully removed the SSO configuration from the backend, allowing the customer to regain access to the local super user admin account. The customer confirmed that they could log in successfully after the changes were made.

## Notes
- It is important to ensure that all users who require access to administrative functions are designated as super admins before enabling SSO.
- Future implementations of SSO should include a review of user roles and access levels to prevent similar issues.
- The customer was advised to note the failover login URL for future reference and to set user permissions appropriately.