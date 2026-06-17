7.X Broken Authentication
FieldValueCVSS 3.1 Score8.5CVSS VectorCVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:LSeverityHighClassificationA07: Identification and Authentication Failures
Abstract
The test team observed that the application fails to properly validate session tokens on the server side, allowing requests to be replayed without authentication cookies.
In this scenario, the test team observed that an authenticated request was captured using Burp Suite. Upon removing all session cookies from the request and replaying it, the application accepted the request without any issue, granting access to the resource as if the session was still valid. This indicates that the server does not properly enforce session-based authentication checks.
Impact
This flaw allows an attacker to bypass authentication controls and gain unauthorized access to application functionality. Malicious users can access sensitive data or perform actions without valid session credentials, potentially compromising data confidentiality and integrity.
Affected Items
[Insert affected endpoint URLs here]
Recommendation
It is recommended to:

Implement robust server-side session validation for every request
Ensure that requests without valid session tokens are explicitly rejected by the server
Invalidate sessions on the server side upon logout and enforce strict session expiry policies


7.X Content Security Policy (CSP) Misconfiguration
FieldValueCVSS 3.1 Score8.5CVSS VectorCVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:LSeverityHighClassificationA05: Security Misconfiguration
Abstract
The test team observed that the application has improper Content Security Policy (CSP) configuration across different endpoints, leaving the application exposed to client-side attacks such as Cross-Site Scripting (XSS).
Case 1 — For one of the application URLs (identified under the benefits hub endpoint: benefitshub-iat.nj.adp.com), the CSP header is present but misconfigured. As seen in the response, the policy includes style-src 'self' 'unsafe-inline', which permits inline styles and weakens the CSP protection. Additionally, the policy is missing critical directives such as frame-ancestors and object-src, which are necessary to prevent clickjacking and plugin-based attacks.
Case 2 — For another URL within the application scope, the CSP header is entirely absent. Without a CSP header, the browser applies no content restrictions, leaving the application fully exposed to injection-based attacks with no mitigation in place.
Impact
This flaw allows for a complete compromise of data confidentiality and integrity. Malicious users can steal sensitive PII, financial data, or proprietary information of other companies. They can also maliciously alter or destroy cross-tenant data.
Affected Items
[Insert affected endpoint URLs here]
Recommendation
It is recommended to:
Case 1:

Remove 'unsafe-inline' from the style-src directive and replace inline styles with external stylesheets
Add missing directives such as frame-ancestors 'self' and object-src 'none' to strengthen the policy

Case 2:

Implement a Content Security Policy header on all application endpoints
Enforce strict CSP directives to restrict resource loading to trusted sources only
