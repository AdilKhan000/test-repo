CVE-2026-41284, CVE-2026-43515, CVE-2026-43512, CVE-2026-43514, CVE-2026-43513, CVE-2026-42498


Unencrypted Communications (HTTP)
CVSS 3.1 Score: 4.3
CVSS Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
Severity: Medium
Classification: A02: Cryptographic failures

Abstract
During the assessment, it was observed that the application does not enforce Transport Layer Security (TLS). The web server allows communication over unencrypted HTTP, completely lacking encryption in transit.

In this scenario, the test team observed that the application dstiatvip.whc transmits all data in cleartext. As shown by the browser's "Not secure" warning, no SSL/TLS certificate is configured, leaving the connection entirely unprotected.

Impact
If an attacker establishes a Man-in-the-Middle (MitM) position on the internal network, they can easily intercept, read, and modify the cleartext traffic. This allows the attacker to directly capture sensitive data, including session cookies and internal application data, without needing to bypass any encryption mechanisms.

Affected Items
http://dstiatvip.whc/admin/#/implementations

Recommendation

Install a valid SSL/TLS certificate on the web server.

Enforce HTTPS across the entire application by configuring the server to automatically redirect all incoming HTTP requests to HTTPS (e.g., using a 301 redirect).

Implement HTTP Strict Transport Security (HSTS) headers to instruct browsers to exclusively interact with the application over secure connections.
