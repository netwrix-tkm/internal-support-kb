## Ticket Metadata
- **Ticket ID:** 500Qk00000GuyrYIAR
- **Case Number:** 423667
- **Status:** Closed - Resolved
- **Account/Company:** Millville Savings Bank
- **Contact Name:** Paul Maccarone
- **Product:** Netwrix Enterprise Auditor
- **Component:** StealthAUDIT General
- **Feature:** Credentials
- **Version:** 11.6

## Problem Description
The customer requested assistance in updating the admin password used by Stealth products due to an auditor's requirement. They sought documentation on all locations where the password needs to be updated and inquired about a script to facilitate this process.

## Environment Details
- **Netwrix Services:** Web Server, AIC, Vault
- **FSAA Proxy:** Not using LocalSystem
- **Monitored Hosts:** Includes NAS devices

## Troubleshooting Steps
1. Identified all locations where the admin password is typically stored:
   - **Global Settings:**
     - Connection Profiles (and User Credentials)
     - Notification settings (Mail Server and username)
     - Schedule (User Credentials)
     - ServiceNow (if enabled)
     - Storage (Authentication)
   - **NEA Environment:**
     - Netwrix Services (Web Server, AIC, Vault)
     - FSAA Proxy (if not using LocalSystem)
   - **Activity Monitor:**
     - Agent settings
     - Monitored Hosts (for NAS devices)
   - **Other Places (less likely to be used):**
     - NAM Agent & MH settings > Inactivity Alert
     - Global Settings > ServiceNow
     - Individual scheduled tasks
     - Job > Properties > AutoRetry

2. Provided the customer with a comprehensive list of all the locations and settings that required the password update.

## Root Cause
The need for a password update arose from an auditor's request, highlighting the importance of maintaining secure and updated credentials across all systems.

## Solution
The issue was resolved by providing the customer with detailed documentation outlining all the locations where the admin password needed to be updated. This included specific settings in Global Settings, NEA Environment, Activity Monitor, and other less common areas. The customer was also informed that there is no specific script available for automating this process, but the provided documentation serves as a guide for manual updates.

## Notes
- It is crucial to regularly review and update admin passwords to comply with security policies and audit requirements.
- Ensure that all relevant personnel are aware of the locations where credentials are stored to facilitate future updates.
- Consider implementing a password management solution to streamline the process of updating and managing credentials across multiple systems.