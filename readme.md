1. Webserver Configuration - Rate Limiting (8.18)
The client wants exact thresholds, IP/Session tracking, and firewall details.

Recommendation:
It is recommended to implement a multi-layered rate limiting strategy on all transactional and state-changing endpoints:

Application-Level (Session-Based): Enforce strict rate limits tied to the authenticated user's session token (e.g., ASP.NET_SessionId). Limit actions such as payment process creations to a maximum of 5 to 10 requests per minute per user account.

Network/WAF-Level (IP-Based): Configure the Web Application Firewall (WAF) or edge load balancer to monitor and throttle excessive traffic from individual IP addresses. Implement a rule to temporarily block or issue a CAPTCHA challenge to any IP address exceeding 50 requests per minute to critical API endpoints.

Backend Validation: Ensure the backend system validates the uniqueness of the submitted data (e.g., preventing duplicate payment entries for the same transaction ID) to mitigate the impact if rate limits are temporarily bypassed.

2. Input Validation - Client-Side Bypass / IDOR (8.14)
The client wants you to expand on the typo "Add sever side validation" to explain exactly how that validation should work.

Recommendation:
It is recommended to:

Enforce Server-Side Access Controls: Never rely on frontend UI restrictions (such as disabled or hidden HTML input fields) for security. Treat all incoming HTTP requests as untrusted.

Implement Context-Aware Authorization: When the backend receives a request to modify a record (e.g., Modify Employee Details), it must actively verify the submitted Employee ID against the permissions of the currently authenticated user (via their .AspNet.Cookies token).

Strict Parameter Rejection: The backend must independently query the database to confirm if the active user holds the explicit organizational role required to alter the target Employee ID. If the authorization check fails, the server must reject the modification, log the unauthorized tampering attempt, and return a 403 Forbidden error.


HTML injection: 
Context-Aware Output Encoding (HTML Entities): At the point where user-controlled data is output into an HTTP response, explicitly encode the data for an HTML context. Convert all potentially dangerous characters into their safe HTML entity equivalents before rendering them in the browser.

Required Conversions: < to &lt;, > to &gt;, & to &amp;, " to &quot;, and ' to &#x27;.

Input Validation (Allow-listing): Filter all incoming user input on the server side using strict allow-lists. Accept only the expected data types, formats, and lengths, rejecting any input containing unneeded HTML markup.

Safe HTML Sanitization: If the application legitimately requires users to submit formatted HTML, do not rely on custom regex filters. Utilize an established, actively maintained sanitization library (such as DOMPurify) to strip malicious tags (like <script> or <iframe>) while preserving safe content.

Content Security Policy (CSP): Maintain a strict CSP as a defense-in-depth measure to mitigate the severity of any injection vulnerabilities that might bypass primary filters.

Impact HTML Injection: 
HTML injection allows an attacker to manipulate the visual presentation and structure of the web application. By injecting unauthorized HTML tags, an attacker can deface the webpage or insert deceptive elements—such as malicious links or fake login forms—to conduct phishing attacks and deceive victims into revealing sensitive credentials.
