Finding 1: Vulnerable Software Versions in Use (.NET Framework & ASP.NET)
CVSS: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H

Score: 8.1 — High

CWE: CWE-1104 — Use of Unmaintained Third-Party Components
Rationale for High:

AC:H because exploitation requires specific conditions (not a trivial one-click)
But C/I/A all High because confirmed RCE CVEs exist for these versions
This is your defensible middle ground — not a 9.8 which would be hard to justify without a working exploit, but High enough to be taken seriously

Observation:

"The test team observed that the application is running Microsoft .NET Framework version 4.0.30319 and ASP.NET version 4.8.4797.0. These software versions are associated with publicly disclosed vulnerabilities including remote code execution and denial of service. The following CVEs have been identified against these versions:
CVE-2020-1046 (RCE, CVSS 8.8), CVE-2020-1597 (DoS, CVSS 7.5), CVE-2018-8517 (DoS, CVSS 7.5), CVE-2023-29326 (RCE, CVSS 7.8), CVE-2023-24897 (RCE, CVSS 7.8)
The presence of these known vulnerabilities in a production environment poses a significant risk of unauthorized code execution and service disruption."


Finding 2: Stack Trace Disclosure Revealing Software Versions
CVSS: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N

Score: 5.3 — Medium

CWE: CWE-209 — Generation of Error Message Containing Sensitive Information
Rationale for Medium:

No auth required, low complexity, publicly triggerable
Direct impact is Low on its own — but it is the enabler of Finding 1
That chaining relationship is what you present to the client if challenged on why both exist as separate findings

Observation:

"The test team observed that the application returns detailed stack traces in HTTP error responses. The stack trace discloses internal software version information, specifically Microsoft .NET Framework version 4.0.30319 and ASP.NET version 4.8.4797.0. This information can be leveraged by an attacker to identify known vulnerabilities associated with these specific versions and tailor attacks accordingly. The disclosure of such information reduces the effort required for targeted exploitation."
