## Ticket Metadata
- **Ticket ID:** 500Qk00000NIwUwIAL
- **Case Number:** 439900
- **Status:** Closed - Resolved
- **Account/Company:** Dr. OK Wack Chemie
- **Contact Name:** Siaoyun Chen
- **Product:** Netwrix Endpoint Protector
- **Component:** Server
- **Feature:** Server Upgrade
- **Version:** Not specified

## Problem Description
The customer reported an issue while attempting to perform a system backup prior to updating their appliance. The backup process was stuck at the status "Generating" and did not progress.

## Environment Details
- The issue occurred on a Netwrix Endpoint Protector appliance.
- The customer was attempting to generate a backup using Backup V2.

## Troubleshooting Steps
1. Conducted a remote session (RS) with the customer to diagnose the issue.
2. Checked the usage of the `/var/eppfiles/` directory.
3. Identified that the innods were at 100% usage.
4. Cleared the innods from the `/shadows` folder.

## Root Cause
The root cause of the issue was identified as 100% usage of the innods in the `/var/eppfiles/` directory, which prevented the backup process from completing.

## Solution
After clearing the innods from the `/shadows` folder, the backup process was able to proceed successfully, and Backup V2 could be generated without further issues.

## Notes
- It is important to monitor the usage of innods in the `/var/eppfiles/` directory to prevent similar issues in the future.
- Regular maintenance of the shadows folder may help avoid backup failures related to innod usage.