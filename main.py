import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=AAABATTERY;"
    "DATABASE=Library_CSI3450_GroupC;"
    "UID=aterr;PWD=3791;"
    "Encrypt=yes;TrustServerCertificate=yes;"
)

cursor = connection.cursor()

cursor.execute("SELECT PAT_FNAME, PAT_LNAME FROM PATRON")

for row in cursor.fetchall():
    print(row.PAT_FNAME, row.PAT_LNAME)

connection.close()