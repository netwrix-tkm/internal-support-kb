## Ticket Metadata
- **Ticket ID:** 500Qk00000KLjbKIAT
- **Case Number:** 431409
- **Status:** Closed - Resolved
- **Account/Company:** Deutsche Telekom Digital Labs India PVT LTD
- **Contact Name:** Ankit Kumar
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Access Error
- **Version:** NONE

## Problem Description
The customer configured the Single Sign-On (SSO) settings in the Endpoint Protector Dashboard. Upon testing the configuration, they were logged out and received an error message stating "SSO is not configured properly." This issue prevented them from logging back into the dashboard to revert the settings or obtain the Failover URL.

## Environment Details
- **Platform:** Netwrix Endpoint Protector
- **Collector Code:** Server

## Troubleshooting Steps
1. Customer attempted to test the SSO configuration, which resulted in being logged out and receiving an error.
2. Customer was unable to log back into the Endpoint Protector Dashboard to revert the SSO settings or retrieve the Failover URL.
3. A remote session was initiated to address the issue.
4. During the remote session, the support technician removed the SSO configuration via the backend.

## Root Cause
The root cause of the issue was an improper configuration of the SSO settings, which led to the error message and subsequent inability to access the dashboard.

## Solution
The issue was resolved during a remote session where the support technician removed the faulty SSO configuration from the backend. After this, the customer was able to log into the Endpoint Protector Server and reconfigure the SSO settings correctly, ensuring to note down the Failover URL for future reference.

## Notes
- It is crucial to verify the SSO configuration settings thoroughly before testing to avoid being locked out of the dashboard.
- Always document the Failover URL when configuring SSO to facilitate recovery in case of similar issues in the future.