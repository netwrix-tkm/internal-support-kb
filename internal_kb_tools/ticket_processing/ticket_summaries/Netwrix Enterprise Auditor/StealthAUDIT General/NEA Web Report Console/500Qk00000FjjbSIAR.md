# Ticket Metadata
- **Ticket ID:** 500Qk00000FjjbSIAR
- **Case Number:** 421006
- **Status:** Closed - Resolved
- **Account/Company:** Kerry Group Services International Limited
- **Contact Name:** Cameron Bowlds
- **Product:** Netwrix Enterprise Auditor
- **Component:** NEA Web Report Console
- **Feature:** Web Service REST API for Applications Accessing Data Remotely
- **Version:** 11.6

## Problem Description
The customer reported an issue with a vendor (Saviynt) attempting to connect to the Netwrix Enterprise Auditor (NEA) API to generate an access token. The customer was unsure about the required hostname and port for this connection.

## Environment Details
- **Netwrix Enterprise Auditor Version:** 11.6.0.92
- **Netwrix Access Information Center Version:** 11.6.0.23
- **Stealthbits Activity Monitor Version:** 6.0.1214

## Troubleshooting Steps
1. Confirmed the API connection details, including the client ID and client secret.
2. Attempted to generate an access token using PowerShell:
   ```powershell
   $body = @{
     client_id="****REDACTED***"
     client_secret="****REDACTED***"
     grant_type="client_credentials"
   }
   $response = Invoke-WebRequest -Method POST -uri https://TSUK2DAC01.ict.kerryad.com:8082/api/v1/token -Body $body -ContentType "application/json"
   $content = $response.Content | ConvertFrom-Json
   $access_token = $content.access_token;
   ```
3. Verified the API call to retrieve data from the SharePoint views.
4. Checked the configuration of the Netwrix Access Information Center (AIC) for Single Sign-On (SSO) settings.
5. Identified that the third-party tool was using the incorrect port (AIC Port) which does not support API calls.

## Root Cause
The issue was caused by the third-party tool attempting to connect using the Netwrix Access Information Center (AIC) port, which does not support API calls. Additionally, there was a partial configuration of SSO in the AIC.

## Solution
1. Confirmed that the REST API was functioning correctly with the created access.
2. Adjusted the configuration to ensure that the correct port (8082) was being used for the API calls.
3. Fixed the SSO configuration error in the AIC, ensuring it was fully set up for SSO.
4. Provided the customer with the correct API endpoint and instructions for generating the access token.

## Notes
- Ensure that the correct port (8082) is used for API calls to avoid similar issues in the future.
- Verify SSO configurations in both the Netwrix Enterprise Auditor and the AIC to ensure seamless access for third-party integrations.
- Document any changes made to the API access settings for future reference.