## Ticket Metadata
- **Ticket ID:** 500Qk00000PMVhxIAH
- **Case Number:** 445665
- **Status:** Closed - Resolved
- **Account/Company:** IBM - Etihad Airways
- **Contact Name:** Praveen Huilgol
- **Product:** Netwrix Enterprise Auditor
- **Component:** Access Information Center
- **Feature:** Reports
- **Version:** 11.5

## Problem Description
The customer reported that auto-generated emails from the Access Information Center (AIC) console for Access Review were not displaying embedded images. Despite following a suggested workaround using Base64 encoding for images, the images were still not visible in the recipients' emails.

## Environment Details
- The issue occurred in the Netwrix Enterprise Auditor platform, specifically within the Access Information Center (AIC) console.
- The customer was using version 11.5 of the product.

## Troubleshooting Steps
1. Configured the auto email feature in the AIC console to send Access Review emails to end users.
2. Modified the AIC email template to include Base64-encoded images using the `<img>` HTML tag.
3. Sent a test email from the AIC console to end users.
4. Verified the recipient's email to check if images were displayed correctly or if the "Embedded Image" placeholder appeared instead.

## Root Cause
The root cause of the issue was not definitively identified. However, it was suspected that the problem may be related to the compatibility of the recipient's email client with Base64-encoded images. The AIC console was confirmed to send the HTML body of the email template correctly, but the email client might not support inline images in Base64 format.

## Solution
The customer ultimately requested to close the ticket without further investigation. No specific resolution was implemented, and the issue remains unresolved. For future reference, if the customer decides to revisit the issue, they should provide a copy of the problematic email and the debug log from the AIC console for further analysis.

## Notes
- The fallback mechanisms in the HTML template (e.g., "alt" text for images and download links for PDFs) were functioning correctly, but recipients did not see the images embedded in the email.
- It is important to clarify with customers whether the issue is related to the email client displaying fallback text instead of images.
- If similar issues arise, consider checking the compatibility of the email client with Base64-encoded images and suggest alternative methods for embedding images if necessary.