## Ticket Metadata
- **Ticket ID:** 500Qk00000ONOrtIAH
- **Case Number:** 442968
- **Status:** Closed - Resolved
- **Account/Company:** Los Angeles Unified School District
- **Contact Name:** Daniel Madrigal
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Install/Uninstall
- **Version:** NONE

## Problem Description
The customer, Daniel Madrigal from LAUSD IT Security, inquired about the licensing for the Netwrix Endpoint Protector. He wanted clarification on how licenses are counted for Windows and Mac devices, particularly regarding the installation process when the limit of 100 licenses is reached.

## Environment Details
- The customer is using Intune to deploy the Endpoint Protector client software to multiple Windows devices.

## Troubleshooting Steps
1. The support engineer, Ramon Torres, provided initial guidance on checking the licensing status via the System Configuration -> System Licensing section.
2. Explained that licenses are assigned on a first-in-first-served basis, with the first 100 devices being able to connect to the EPP appliance.
3. Clarified that while additional installations beyond 100 are possible, those devices would not receive policies or restrictions.
4. Suggested that the customer check with the super admin for license management and to be added as a System Administrator to view licensing details.

## Root Cause
The issue stemmed from a lack of understanding regarding how the licensing system works for the Endpoint Protector, specifically how devices are counted and what happens when the license limit is reached.

## Solution
The support engineer clarified that:
- The first 100 devices to connect to the EPP appliance would be assigned licenses.
- Additional devices can be installed, but they will not be able to enforce policies or restrictions due to the lack of available licenses.
- There are no additional charges for exceeding the license limit; the only consequence is that those devices will not be able to enforce any policies.

## Notes
- It is essential for users to have access to the System Licensing tab to manage licenses effectively. If access is not available, they should contact a system administrator to gain the necessary permissions.
- The customer confirmed understanding of the licensing process and requested to close the ticket after receiving the clarification.