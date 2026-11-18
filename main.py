import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=AAABATTERY;"
    "DATABASE=Library_CSI3450_GroupC;"
    "UID=aterr;PWD=3791;"
    "Encrypt=yes;TrustServerCertificate=yes;"
)
cursor = connection.cursor()

greeting = "Welcome to the library's inventory management system! Type a number to choose from the options below"
options = '''
1   View checked-out items
2   View the creator(s) with the most items in the library
3   Write a custom query (you must adhere to SQL syntax!)
0   Close the connection and end this session (your changes will be automatically committed)
'''
errorMsg = "An error occurred while executing the query. Try again or close the connection."

print(greeting)
print(options)
selected = int(input())

while selected != 0:
    match selected:
        case 1:
            try:
                cursor.execute("SELECT * FROM ITEM WHERE ITEM_ISOUT=1;")
                for row in cursor.fetchall():
                    print(row.ITEM_TITLE + " (ID: " + str(row.ITEM_ID) + ")")
            except:
                print(errorMsg)
        case 2:
            try:
                cursor.execute(
                                '''
                                SELECT C_FNAME, C_LNAME, C_NUMWORKS
                                FROM CREATOR, CREATOR_NUMWORKS
                                WHERE CREATOR.C_ID=CREATOR_NUMWORKS.C_ID AND C_NUMWORKS=(SELECT MAX(C_NUMWORKS) FROM CREATOR_NUMWORKS);
                                '''
                            )
                for row in cursor.fetchall():
                    if not row.C_LNAME:
                        print(row.C_FNAME + " (" + str(row.C_NUMWORKS) + " works)")
                    else:
                        print(row.C_FNAME, row.C_LNAME + " (" + str(row.C_NUMWORKS) + " works)")
            except:
                print(errorMsg)
        case 3:
            query = input()
            try:
                cursor.execute(query)
                for row in cursor.fetchall():
                    print(" ".join(row))
            except:
                print(errorMsg)
        case 0:
            break
    
    print(options)
    selected = int(input())

print("Committing changes...")
connection.commit()
print("Changes successfully committed. Goodbye!")
connection.close()