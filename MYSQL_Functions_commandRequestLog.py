import sys
##################################################################
# All available database table functions for: commandRequestLog  #
##################################################################

def str_insert_commandRequest(intUserId: int, strCommandRequest: str, strDescription: str):
    
    query = f"INSERT INTO commandRequestLog VALUES(0, {intUserId}, '{strCommandRequest}', CURRENT_TIME(), CURRENT_TIME(), 0, '{strDescription}', null);"
    return query

def str_select_commandRequest(intUserId: int):
    query = f"SELECT intRequestId ,strCommandRequest, dtmSubmitted, strDescription FROM commandRequestLog WHERE intUserId = {intUserId};"  
    return query

if __name__ == '__main__':
    if sys.argv[1] == 'select':
        print(str_select_commandRequest(sys.argv[2]))
    elif sys.argv[1] == 'insert':
        print(str_insert_commandRequest(sys.argv[2], sys.argv[3], sys.argv[4]))
    else:
        print(f'Invalid 1st argument: {sys.argv[1]}')

##################################################################################
##import mysql.connector
# from mysql.connector import Error
# from MySQL_Functions_Connector import *

# def insert_commandRequest(intUserId: int, strCommandRequest: str, strDescription: str):
# #Insert a command request with a description
# ##Use update function after insert+validations to populate description
#     intRequestId = 0
#     connection = ''
#     try:
#         connection = newConnection()
#         cursor = connection.cursor()
#         query = "INSERT INTO commandRequestLog VALUES(%s,%s,%s, CURRENT_TIME(), CURRENT_TIME(), 0, %s, null);"
#         args = (intRequestId, intUserId, strCommandRequest, strDescription)
#         cursor.execute(query, args)
        
#         connection.commit()
#         intRequestId = cursor.lastrowid
#         print('SUCCESS: Inserted intRequestId='+str(intRequestId))
                
#     except Error as error:
#         intRequestId = -1
#         print(error)
#         return 'FAILED....'

#     finally:
#         if connection:
#             closeConnection(cursor, connection)

#     return intRequestId
   
####END####
