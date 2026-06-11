1. Webserver Configuration - Rate Limiting (8.18)
The client wants exact thresholds, IP/Session tracking, and firewall details.

Recommendation:
It is recommended to implement a multi-layered rate limiting strategy on all transactional and state-changing endpoints:

Application-Level (Session-Based): Enforce strict rate limits tied to the authenticated user's session token (e.g., ASP.NET_SessionId). Limit actions such as payment process creations to a maximum of 5 to 10 requests per minute per user account.

Network/WAF-Level (IP-Based): Configure the Web Application Firewall (WAF) or edge load balancer to monitor and throttle excessive traffic from individual IP addresses. Implement a rule to temporarily block or issue a CAPTCHA challenge to any IP address exceeding 50 requests per minute to critical API endpoints.

Backend Validation: Ensure the backend system validates the uniqueness of the submitted data (e.g., preventing duplicate payment entries for the same transaction ID) to mitigate the impact if rate limits are temporarily bypassed.

2. Input validation
Implement Explicit Field Whitelisting (Prevent Mass Assignment): Do not blindly bind all incoming HTTP request parameters to backend database objects. The server must explicitly define a strict whitelist of fields that the user is permitted to modify in a given request (e.g., Phone Number, Address).

Enforce Immutable Fields Server-Side: Any data field that is disabled or marked as read-only in the frontend UI (such as Employee ID, Role, or Account Status) must be strictly configured as immutable on the backend. The backend logic or ORM must explicitly ignore or drop these parameters if they are maliciously injected into an update payload.

Reject Unauthorized Modifications: Configure the API endpoint to actively validate the incoming payload against the allowed schema. If the server detects an attempt to submit a parameter that the user is not authorized to alter, it should reject the entire request and return a 400 Bad Request or 403 Forbidden error, rather than silently processing the rest of the data.
HTML injection allows an attacker to manipulate the visual presentation and structure of the web application. By injecting unauthorized HTML tags, an attacker can deface the webpage or insert deceptive elements—such as malicious links or fake login forms—to conduct phishing attacks and deceive victims into revealing sensitive credentials.
