Impact
Exposing internal infrastructure details allows an attacker to map the backend network. Knowledge of specific internal IP addresses, hostnames, and application versions aids an attacker in identifying secondary internal targets and planning targeted exploits against the server.

Recommendation

Configure the API backend to strip internal configuration details from HTTP responses.

Ensure that internal IP addresses, server hostnames, and explicit application version numbers are removed or masked before the response reaches the client.

Implement a generic error-handling mechanism that does not leak stack traces or environment variables.
