#TODO: delete_user? (inactivate instead?)


#####################################################
# All available database table functions for: Users #
#####################################################

import mysql.connector
from mysql.connector import Error
from MySQL_Functions_Connector import *

def insert_user(strPhoneNumber,blnIsAdmin):
#Insert a new and active User by specifying blnIsAdmin and strPhoneNumber.
####Phone number format: '14044080221'
####Boolean format: 1 or 0 (nums)
####Ex: insert_user('14048675309', 0)
    intUserId = 0
    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        #Phone Number Format Validation
        if not (len(strPhoneNumber) > 4 and len(strPhoneNumber) < 16):
            print('FAILED: Invalid format for strPhoneNumber. Ex: "'"13214569870"'"')
            raise Exception('FAILED: Invalid format for strPhoneNumber. Ex: "'"13214569870"'"')

        #Duplicate Phone Number check
        cursor.execute("SELECT 1 FROM Users WHERE strPhonenumber = %s;", (strPhoneNumber,))
        row = cursor.fetchone()
        if not row:
            query = "INSERT INTO Users VALUES(0, %s, CURRENT_TIME(), 1, %s, CURRENT_TIME())"
            args = (strPhoneNumber,blnIsAdmin)
            cursor.execute(query, args)
            

            intUserId = cursor.lastrowid
            connection.commit()
            print('SUCCESS: Inserted intUserId='+str(intUserId)+' with blnIsAdmin ='+str(blnIsAdmin))
            
        else:
            print('FAILED: Duplicate Phone Number, use update_user function.')
            raise Exception('FAILED: Duplicate Phone Number, use update_user function.')
                
    except Error as error:
        print(error)

    finally:
        closeConnection(cursor, connection)
        return intUserId

def update_activeUser(intUserId, blnIsActive):
#Updates an existing Users blnActiveUser column with the intUserId.
####Phone number format: '14044080221'
####Boolean format: 1 or 0 (nums)
####Ex: update_ActiveUser(1001, 0)
    
    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        if existsCheck(cursor, "Users", intUserId):
            query = "UPDATE Users SET blnActiveUser = %s, dtmUpdatedWhen = CURRENT_TIME() WHERE intUserId = %s;"
            args = (blnIsActive, intUserId)
            cursor.execute(query, args)
            
            connection.commit()
            print("SUCCESS: Updated intUserId=" + str(intUserId) + " to blnIsActive=" + str(blnIsActive))
            
        else:
            print('FAILED: User not found. intUserId='+str(intUserId))
            raise Exception('FAILED: User not found. intUserId='+str(intUserId))
                
    except Error as error:
        intUserId = 0
        print(error)

    finally:
        closeConnection(cursor, connection)
        return intUserId        

def update_adminUser(intUserId, blnIsAdmin):
#Updates an existing Users blnIsAdmin column with the intUserId.
####Boolean format: 1 or 0 (nums)
####Ex: update_adminUser(1001, 1)
    
    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        if existsCheck(cursor, "Users", intUserId):
            query = "UPDATE Users SET blnAdminUser = %s, dtmUpdatedWhen = CURRENT_TIME() WHERE intUserId = %s;"
            args = (blnIsAdmin, intUserId)
            cursor.execute(query, args)
            
            connection.commit()
            print("SUCCESS: Updated intUserId=" + str(intUserId) + " to blnAdminUser=" + str(blnIsAdmin))
            
        else:
            print('FAILED: User not found. intUserId='+str(intUserId))
            raise Exception('FAILED: User not found. intUserId='+str(intUserId))
                
    except Error as error:
        intUserId = 0
        print(error)

    finally:
        closeConnection(cursor, connection)
        return intUserId

def isAdminUser(intUserId):
#Returns 0 or 1 indicating if the User is currently blnAdminUser.
####Ex: isAdminUser(1001)
    result = 0
    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        if existsCheck(cursor, "Users", intUserId):
            query = "SELECT 1 FROM Users WHERE intUserId = %s AND blnAdminUser = 1;"
            args = (intUserId,)
            cursor.execute(query, args)

            if cursor.fetchone():
                result = 1
                
        else:
            print('FAILED: User not found. intUserId='+str(intUserId))
            raise Exception('FAILED: User not found. intUserId='+str(intUserId))
                
    except Error as error:
        result = 0
        print(error)

    finally:
        closeConnection(cursor, connection)
        return result
        

####END####
