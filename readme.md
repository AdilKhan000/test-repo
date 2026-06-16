Abstract just needs the first line changed to:

"The test team observed that session cookies do not have the SameSite attribute set, making them susceptible to cross-site request forgery attacks."

Impact (Revised)

"An attacker can perform cross-site request forgery attacks as the session cookies lack the SameSite attribute. Without this flag, the browser will include cookies in cross-origin requests, allowing a malicious third-party site to make authenticated requests on behalf of the logged-in user without their consent."


Recommendation (Revised)

"It is recommended to set the SameSite=Strict or SameSite=Lax attribute on all session cookies. This instructs the browser to only include cookies in requests originating from the same site, preventing cross-origin requests from carrying session credentials."
