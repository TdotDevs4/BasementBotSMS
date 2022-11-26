import mysql.connector

def newConnection():
    return mysql.connector.connect(host='localhost',
                                   database='dbNameHere',
                                   user='user-here',
                                   password='PASSWORD_HERE!')

def existsCheck(connectionCursor, strTable, intId):
    strPrimaryIdCol = "init.existsCheck"
    if strTable == "Users":
        strPrimaryIdCol = "intUserId"
    elif strTable == "Events":
        strPrimaryIdCol = "intEventId"
    else:
        print("FAILED: Table not found. strTable=" +strTable)
        raise Exception("FAILED: Table not found. strTable=" +strTable)

    connectionCursor.execute("SELECT 1 FROM "+strTable+" WHERE "+strPrimaryIdCol+" = %s;", (intId,))
    if connectionCursor.fetchone():
        return 1
    else:
        return 0

def closeConnection(connectionCursor, connection):
    connectionCursor.close()
    connection.close()
