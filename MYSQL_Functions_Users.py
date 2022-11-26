import sys
##################################################################
# All available database table functions for: Users             #
##################################################################

def str_UserExistsCheck(strPhoneNumber : str):
    query = f"SELECT intUserId FROM Users WHERE strPhoneNumber = '{strPhoneNumber}';"
    return query

def str_insert_activeUser(strPhoneNumber : str):
    query = f"INSERT INTO Users VALUES(0, {strPhoneNumber}, CURRENT_TIME(), 1, 0, CURRENT_TIME());"
    return query

def str_update_activeUser(intUserId: int, blnActiveUser: bool):
    if intUserId > 0:
        query = f"UPDATE Users SET blnActiveUser = {bool(blnActiveUser)}, dtmUpdatedWhen = CURRENT_TIME() WHERE intUserId = {intUserId};"
    return query

if __name__ == '__main__':
    if sys.argv[1] == 'check':
        print(str_UserExistsCheck(sys.argv[2]))
    elif sys.argv[1] == 'insert':
        print(str_insert_activeUser(sys.argv[2]))
    elif sys.argv[1] == 'active':
        print(str_update_activeUser(int(sys.argv[2]), bool(sys.argv[3])))
    else:
        print(f'Invalid 1st argument: {sys.argv[1]}')