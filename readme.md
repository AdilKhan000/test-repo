Note: Upon retest, it was identified that the finding title and severity did not accurately reflect the actual vulnerability observed. This finding has been closed and superseded by a new finding which accurately describes the sensitive data exposure, associated impact, and revised severity. Please refer to the new finding for complete details

Abstract

"The test team observed that the application exposes sensitive backend configuration data in plaintext within the API response at /SEAESSAPI/v1/company. The response contains a full database connection string including the internal database server IP address, database name, username, and plaintext password.
In the current scenario, the test team extracted the following sensitive information directly from the API response:

Database Server IP: 
Database Name: 
Username: 
Password: 

The test team further confirmed that the database server is reachable from the internal network on port 1433, and that the exposed credentials were processed by the SQL Server authentication mechanism, confirming the validity of the exposed data."


Impact

"An attacker with access to the application can retrieve valid database credentials directly from the API response without any additional exploitation. The database server was confirmed to be reachable internally on port 1433. This allows an attacker operating from within the network perimeter to use the exposed credentials to authenticate directly to the backend database, potentially gaining access to all data stored within, including employee records, payroll information, and company configuration data."


Recommendation

"It is recommended to implement the following:

Immediately rotate the exposed database credentials and audit the database for any unauthorized access.
Modify the server-side API logic to explicitly filter out all sensitive configuration fields from the response before returning data to the client. Backend configuration objects should never be transmitted to the client under any circumstances.
Store database credentials in a secrets management solution such as Azure Key Vault or HashiCorp Vault rather than in application configuration files or database records.
Restrict database server access to application server IPs only using firewall rules, ensuring port 1433 is not accessible from general internal network ranges."
