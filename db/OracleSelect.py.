import cx_Oracle

HOST = "host"
PORT = 1521
SID = "sid"
USER = "user"
PASSWORD = "password"

tns = cx_Oracle.makedsn(HOST, PORT, SID)
conn = cx_Oracle.connect(USER, PASSWORD, tns)

cur = conn.cursor()
cur.execute("SELECT sysdate FROM dual")

rows = cur.fetchall()

for r in rows:
    print("%s" % r[0])
