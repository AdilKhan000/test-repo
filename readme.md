Session Management - Missing HttpOnly Flag
CVSS 3.1 Score: 3.1
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
Severity: Low
Status: Open
Classification: A05: Security Misconfiguration

Abstract
The test team observed that the application issues cookies without the HttpOnly attribute set. This configuration makes the cookies accessible to client-side scripts, leaving them susceptible to theft through Cross-Site Scripting (XSS) attacks.

In the current scenario, during the retest, the test team observed that the vulnerability remains open. The application still sets the .DSS.Xsrf.Client and XSRF-TOKEN cookies without the HttpOnly flag.

Impact
If an attacker successfully exploits an XSS vulnerability on the application, they can use malicious JavaScript to read the contents of the cookies. This allows the attacker to steal session identifiers or security tokens, which can be used to hijack the user's session or bypass anti-CSRF protections.

Affected Items
Cookies:

.DSS.Xsrf.Client

XSRF-TOKEN

Recommendation
It is recommended to set the HttpOnly attribute on all sensitive session and security cookies. This instructs the browser to deny client-side scripts (like JavaScript) access to the cookie, effectively preventing attackers from stealing it via XSS vulnerabilities.
