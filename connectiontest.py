import pymssql

try:
    conn = pymssql.connect(
        server='',
        port=,
        user='',
        password='',
        database=''
    )
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print(f"[+] Connected Successfully!")
    print(f"[+] Server Version: {row[0]}")
    conn.close()

except Exception as e:
    print(f"[-] Failed: {e}")
