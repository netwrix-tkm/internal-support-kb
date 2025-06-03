# Support Case Summary

## Ticket Metadata
- **Ticket ID:** 500Qk00000JScozIAD
- **Case Number:** 429798
- **Status:** Closed - Resolved
- **Account/Company:** Grant Thornton Business School
- **Contact Name:** Karl Halpin
- **Product:** Netwrix Endpoint Protector
- **Component:** Device Control
- **Feature:** Device Groups
- **Version:** Not specified

## Problem Description
The customer requested assistance in uninstalling all Endpoint Protector agents from all client machines. They inquired about the availability of a script or uninstallation executable that could be deployed via SCCM (System Center Configuration Manager) or another central management solution.

## Environment Details
- **Management Solution:** SCCM (System Center Configuration Manager)
- **Client Machines:** Multiple endpoints requiring agent uninstallation

## Troubleshooting Steps
1. Reviewed the customer's request for uninstallation methods.
2. Checked for existing scripts or executables that could facilitate the uninstallation process.
3. Provided guidance on how to deploy the uninstallation script through SCCM.

## Root Cause
The issue stemmed from the customer's need to efficiently remove Endpoint Protector agents from multiple client machines without manual intervention. There was no existing automated solution readily available for this specific request.

## Solution
The support team provided the customer with a custom uninstallation script that could be executed via SCCM. The script was designed to remove the Endpoint Protector agents from all specified client machines in a streamlined manner. The customer was guided on how to implement the script within their SCCM environment to ensure successful deployment.

## Notes
- Ensure that any uninstallation scripts are tested in a controlled environment before wide deployment to avoid unintended disruptions.
- Document any custom scripts created for future reference and potential reuse in similar cases.
- Advise customers to maintain a backup of their configurations before performing mass uninstalls.