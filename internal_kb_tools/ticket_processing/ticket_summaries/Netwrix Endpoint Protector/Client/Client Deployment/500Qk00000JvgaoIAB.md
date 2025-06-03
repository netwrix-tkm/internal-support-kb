## Ticket Metadata
- **Ticket ID:** 500Qk00000JvgaoIAB
- **Case Number:** 430780
- **Status:** Closed - Resolved
- **Account/Company:** DEKRA Brasil
- **Contact Name:** Lucas Cavalcante
- **Product:** Netwrix Endpoint Protector
- **Component:** Client
- **Feature:** Client Deployment
- **Version:** 1.0

## Problem Description
The customer, DEKRA Brasil, reported an urgent issue with deploying the Endpoint Protection Platform (EPP) through Group Policy Object (GPO) or SotiMobicontrol. They needed to ensure the correct packages were sent by December 31st, but faced challenges in deploying the EPP client with the required IP settings.

## Environment Details
- Deployment methods attempted: GPO and SotiMobicontrol
- EPP client installation package: Classic EPP MSI
- Command line parameters used for installation included WSIP and WSPORT.

## Troubleshooting Steps
1. Attempted to deploy the classic EPP MSI with the original name through both GPO and SotiMobicontrol.
2. Edited the MSI using an MSI editor to ensure the IP address was being applied correctly.
3. Executed the following command to apply parameters via command line:
   ```bash
   msiexec.exe /i "msiInstallerPath" WSIP="EPP_server_IP" WSPORT="443" /q REBOOT=ReallySuppress
   ```
4. Verified that manual installation of the EPP client worked successfully every time.

## Root Cause
The deployment of the EPP client through GPO was successful; however, the IP address was not being set correctly during the automated deployment process.

## Solution
To resolve the issue, the support team provided a change IP script along with detailed steps on how to run it. The script can be downloaded from the following link:
[Client IP Change Script](http://download.endpointprotector.com/Support_files/ClientIPChange.zip)

## Notes
- Ensure that the correct IP settings are applied during automated deployments to avoid similar issues in the future.
- Manual installation of the EPP client is a reliable workaround if automated methods fail.
- Always verify the deployment parameters and settings before executing the installation command.