#TODO: 


######################################################
# All available database table functions for: Events #
######################################################

import mysql.connector
from mysql.connector import Error
from MySQL_Functions_Users import *
from MySQL_Functions_Connector import *

def createEvent(intUserId):
#Create Event Function:
## **Returns strOutput for command_processor.py**
## Active && Admin Users only
## No concurrent events (for now)...
    intEventId = 0
    strEventOutput = "createEvent.init"
    try:
        intEventId = insert_event(intUserId)
        if intEventId == 0:
            strEventOutput = "Sorry, something went wrong...createEvent.intEventId==0"
            print("FAILED: Unable to create Event for intUserId: "+str(intUserId))
        else:
            strEventOutput = "SUCCESS: Event created! EventId = "+str(intEventId)
            print("SUCCESS: Event ID: "+str(intEventId)+" created for UserId="+str(intUserId))
    except Error as error:
        strEventOutput = "Sorry, something went wrong...createEvent.except"
        print(error)
    finally:
        return strEventOutput

def insert_event(intUserId):
#Insert a new Event for an admin user only.
####Ex: insert_event(1001)
#Simple insert into Events w/ validation
#Returns intEventId (active / new / if error then 0)

    intEventId = 0
    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        #User Admin + Active Event Checks
        if isAdminUser(intUserId):

            query = "SELECT 1 FROM Events WHERE intUserId = %s and blnActiveEvent = 1;"
            args = (intUserId,)
            cursor.execute(query, args)

            if cursor.fetchone():
                intEventId = int(cursor.lastrowid)
                print('FAILED: Active Event found for intUserId='+str(intUserId)+' intEventId='+str(intEventId))
                raise Exception('FAILED: Active Event found for intUserId='+str(intUserId)+' intEventId='+str(intEventId))
        else:
            print('FAILED: Admin User not found. intUserId='+str(intUserId))
            raise Exception('FAILED: Admin User not found. intUserId='+str(intUserId))

        query = "INSERT INTO Events VALUES(0, %s, CURRENT_TIME(), 1, CURRENT_TIME());"
        args = (intUserId,)
        cursor.execute(query, args)
            
        intEventId = int(cursor.lastrowid)
        connection.commit()
        print('SUCCESS: Inserted intEventId='+str(intEventid)+' for intUserId='+str(intUserId))
              
    except Error as error:
        print(error)
        
    finally:
        closeConnection(cursor, connection)
        return intEventId

def update_activeEvent(intEventId, blnIsActive):
#Update an existing Events blnActiveEvents value
#Returns intEventId (active / new / if error then 0)

    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        if existsCheck(cursor,"Events", intEventId):
            query = "UPDATE Events SET blnActiveEvent = %s, dtmUpdatedWhen = CURRENT_TIME() WHERE intEventId = %s;"
            args = (blnIsActive, intEventId)
            cursor.execute(query, args)
            
            connection.commit()
            print("SUCCESS: Updated intEventId=" + str(intEventId) + " to blnActiveEvent=" + str(blnIsActive))
            
        else:
            print('FAILED: Event not found.')
            raise Exception('FAILED: Event not found.')
                
    except Error as error:
        print(error)

    finally:
        closeConnection(cursor, connection)
        return intEventId

def delete_event(intEventId):
#Delete Event Function:
####Ex: delete_event(1001)
#Simple delete from Events w/ exists check
    
    try:
        connection = newConnection()
        cursor = connection.cursor()
        
        if existsCheck(cursor,"Events", intEventId):
            query = "DELETE FROM Events WHERE intEventId = %s;"
            args = (intEventId,)
            cursor.execute(query, args)
            connection.commit()
            print("SUCCESS: Deleted intEventId=" + str(intEventId))
            
        else:
            print('FAILED: Event not found. intEventId='+str(intEventId))
            raise Exception('FAILED: Event not found. intEventId='+str(intEventId))
        
    except Error as error:
        print(error)
        
    finally:
        closeConnection(cursor, connection)
        return intEventId

####END####
