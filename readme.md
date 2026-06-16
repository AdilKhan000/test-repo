It is recommended to implement the following:

Disable detailed error messages and stack traces in production environments. Configure custom error pages that return generic error messages without exposing internal framework details, file paths, or version information.
In ASP.NET, set <customErrors mode="On"/> and <httpRuntime enableVersionHeader="false"/> in the web.config to suppress version disclosure and detailed error responses.
Upgrade the third-party software to their latest stable versions to remediate known vulnerabilities associated with the disclosed versions.
Configure the reverse proxy or Web Application Firewall to strip server-side headers such as Server, X-Powered-By, and X-AspNet-Version before sending responses over the network.

<customErrors mode="On"/>
<httpRuntime enableVersionHeader="false"/>
