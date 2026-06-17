CVSS 3.1 Score: 3.5
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:N/A:N
Severity: Low
Status: Closed
Classification: A05: Security Misconfiguration

Abstract
In the previous assessment, the test team observed that the application set an overly permissive Access-Control-Allow-Origin directive in the HTTP response headers.

In the current scenario during the retest, the test team observed that this issue has been successfully remediated. The server now validates the Origin header in the request and restricts the Access-Control-Allow-Origin response header to specific, trusted domains. Arbitrary or wildcard origin reflections are no longer permitted.

Impact
Because the Access-Control-Allow-Credentials header is not present, the immediate risk of cross-origin authenticated attacks is mitigated. However, the lack of strict origin validation introduces an information risk. The response could potentially be accessed by unauthorized or unintended third-party domains.

Affected Items
https://terminal.pl.staging.ehc.adp.com/4hr/prod/

Recommendation

Continue to restrict the Access-Control-Allow-Origin header to specific trusted domains instead of using wildcards or blindly reflecting the request origin.

Ensure CORS and other security headers are consistently applied across the application to prevent future regressions.
