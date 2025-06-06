## Ticket Metadata
- **Ticket ID:** 500Qk00000FaSvBIAV
- **Case Number:** 420611
- **Status:** Closed - Resolved
- **Account/Company:** Mizuho Americas Services LLC
- **Contact Name:** William Dang
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Configuration
- **Version:** 11.0

## Problem Description
The customer reported that their SSL certificate for the Access Information Center (AIC) was expiring and requested instructions on how to renew the certificate. The AIC is running on Netwrix web services and not IIS.

## Environment Details
- **Product Version:** 11.0
- **Build Number:** 194
- **AIC Version:** 11.6+

## Troubleshooting Steps
1. Identified the current SSL certificate details using PowerShell:
   ```powershell
   netsh http show sslcert
   Get-ChildItem -Path Cert:LocalMachineMy | Select-Object -Property * | Sort-Object NotAfter -Descending | Format-Table Thumbprint, Subject, FriendlyName, NotAfter -AutoSize
   ```
2. Deleted the old SSL certificate for the specified IP and port:
   ```powershell
   netsh http delete sslcert ipport=0.0.0.0:8082
   ```
3. Added the new SSL certificate using the new thumbprint:
   ```powershell
   $guid = "bdd5710f-7cbe-4f85-b8c1-da4bddf485a8"
   $certHash = "INSERT THUMBNAIL VALUE FROM STEP 2 BETWEEN QUOTES"
   $ip = "0.0.0.0"
   $port = "8082"
   "http add sslcert ipport=$($ip):$port certhash=$certHash appid={$guid}" | netsh
   ```
4. Repeated the deletion and addition for the second port (481):
   ```powershell
   netsh http delete sslcert ipport=0.0.0.0:481
   "http add sslcert ipport=$($ip):$port certhash=$certHash appid={$guid}" | netsh
   ```
5. Checked and updated URL ACLs if there were issues post-upgrade:
   ```powershell
   netsh http show urlacl
   netsh http delete urlacl url="http://+:8082/"
   netsh http add urlacl url=https://+:8082/ user="NT AUTHORITYLOCAL SERVICE" listen=yes delegate=no
   ```

## Root Cause
The issue was caused by the impending expiration of the SSL certificate used by the Access Information Center, which required renewal to maintain secure HTTPS connections.

## Solution
The issue was resolved by following the outlined steps to identify the old and new SSL certificate thumbprints, deleting the old SSL certificate, and adding the new one using the `netsh` command in PowerShell. The necessary URL ACLs were also checked and updated to ensure proper access.

## Notes
- Ensure to replace the placeholder `"INSERT THUMBNAIL VALUE FROM STEP 2 BETWEEN QUOTES"` with the actual thumbprint value obtained from the certificate details.
- It is recommended to monitor SSL certificate expiration dates proactively to avoid service interruptions.
- For future reference, consult the Netwrix documentation for any updates or changes in the process for SSL certificate management.