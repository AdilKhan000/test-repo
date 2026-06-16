It is recommended to:

Implement CSRF protection tokens for the logout endpoint to ensure the request originates from the legitimate site. The token must be randomly generated, sufficiently long (minimum 128 bits), unique per session, and validated server-side on every state-changing request.
Change the logout method from GET to POST to prevent drive-by CSRF attacks via simple URL links or image tags.
Apply CSRF protection across all state-changing functionality within the application, not limited to the logout endpoint."
