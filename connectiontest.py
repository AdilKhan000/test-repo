import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=IP;'
        'DATABASE=DATABASE;'
        'UID=UID;'
        'PWD='
        'Connect Timeout=10'
    )
    print("[+] Connected successfully")
    conn.close()

except pyodbc.OperationalError as e:
    print(f"[-] Connection failed - Server unreachable or port closed: {e}")

except pyodbc.InterfaceError as e:
    print(f"[-] Driver error: {e}")

except pyodbc.ProgrammingError as e:
    print(f"[-] Authentication failed or database not found: {e}")

except Exception as e:
    print(f"[-] Unexpected error: {e}")
