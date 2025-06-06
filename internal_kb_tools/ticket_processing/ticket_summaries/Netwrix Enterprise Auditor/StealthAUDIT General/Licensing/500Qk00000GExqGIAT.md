## Ticket Metadata
- **Ticket ID:** 500Qk00000GExqGIAT
- **Case Number:** 422078
- **Status:** Closed - Resolved
- **Account/Company:** Central Bank of Trinidad and Tobago
- **Contact Name:** Ryan Tyson
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Licensing
- **Version:** 11.6

## Problem Description
The customer requested a live session to review the compliance objects of the Stealthbits application, specifically to confirm the count of Active Directory (AD) users for licensing purposes.

## Environment Details
- The customer is using Netwrix Enterprise Auditor version 11.6.
- Active Directory tools are required for the PowerShell scripts provided.

## Troubleshooting Steps
1. Conducted a live session with the customer to discuss the AD user counts.
2. Provided two PowerShell scripts to gather information on AD users:
   - A script to output enabled AD users to a text file.
   - A script to count active, inactive, and total AD users.
3. Discussed the implications of user counts on licensing with the customer.
4. Reviewed the results of the PowerShell scripts during the session.

## Root Cause
The issue stemmed from the need to confirm the counts of AD users for licensing purposes, which required accurate data extraction from the Active Directory environment.

## Solution
The issue was resolved by providing the customer with the following PowerShell scripts:
- **Script to output enabled AD users:**
  ```powershell
  get-aduser -filter * -Properties * | where {$_.enabled -eq "True"} | Sort-Object DistinguishedName | FT Name, DistinguishedName, Enabled -AutoSize | Tee-Object "c:tempEnabled_AD_Users_per_OU_2024_0927.txt"
  ```
- **Script to count active, inactive, and total AD users:**
  ```powershell
  Clear-Host
  $enabled = (get-aduser -filter * | where {$_.enabled -eq "True"}).count
  Write-host "Enabled users total =  $enabled" -f green
  $disabled = (get-aduser -filter * | where {$_.enabled -ne "False"}).count
  Write-host "Disabled users total =  $disabled" -f yellow
  $TotalADCount = (get-aduser -Filter *).count
  Write-host "All users total = $TotalADCount" -f red
  ```
- **Script to count users in Organizational Units:**
  ```powershell
  $OUs = Get-ADOrganizationalUnit -Filter *
  $results = @()
  foreach ($OU in $OUs) {
      $OUName = $OU.DistinguishedName
      $activeUsers = Get-ADUser -Filter {Enabled -eq $true} -SearchBase $OUName -SearchScope Subtree | Measure-Object | Select-Object -ExpandProperty Count
      $disabledUsers = Get-ADUser -Filter {Enabled -eq $false} -SearchBase $OUName -SearchScope Subtree | Measure-Object | Select-Object -ExpandProperty Count
      $results += [PSCustomObject]@{ OUName = $OUName; ActiveUsers = $activeUsers; DisabledUsers = $disabledUsers }
  }
  $results | Format-Table -AutoSize
  ```
- Confirmed that the customer could proceed with their licensing renewal based on the provided counts.

## Notes
- Ensure that the PowerShell scripts are run on a server with Active Directory tools installed.
- The licensing model is based on active user counts, and it is important to clarify with sales regarding the inclusion of non-user accounts in the counts.
- Future sessions should include a review of the AD inventory summary count to avoid confusion regarding user counts.