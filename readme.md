Abstract just needs the first line changed to:

"The test team observed that session cookies do not have the SameSite attribute set, making them susceptible to cross-site request forgery attacks."

In the current scenario, the test team observed that the application's session cookies are transmitted in cross-origin requests without any restriction. An attacker can host a malicious third-party page that silently sends requests to the application using the victim's active session cookies, performing actions on their behalf without any user confirmation or protection mechanism.

Impact (Revised)

"An attacker can perform cross-site request forgery attacks as the session cookies lack the SameSite attribute. Without this flag, the browser will include cookies in cross-origin requests, allowing a malicious third-party site to make authenticated requests on behalf of the logged-in user without their consent."


Recommendation (Revised)

"It is recommended to set the SameSite=Strict or SameSite=Lax attribute on all session cookies. This instructs the browser to only include cookies in requests originating from the same site, preventing cross-origin requests from carrying session credentials."
