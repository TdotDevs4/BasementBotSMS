import sys
##################################################################
# All available database table functions for: eventToSub         #
##################################################################

def str_insert_Sub(intEventId: int, intUserId: int):
    query = f"INSERT INTO eventToSub VALUES({intUserId}, {intEventId}, 1, CURRENT_TIME(), CURRENT_TIME());"
    return query

def str_select_UserSubs(intUserId: int):
    query = f"SELECT intEventid FROM eventToSub WHERE intUserId = {intUserId};"  
    return query

def str_select_EventSubs(intEventId: int):
    query = f"SELECT intUserId FROM eventToSub WHERE intEventId = {intEventId} AND blnActiveSub = 1;"   
    return query

if __name__ == '__main__':
    if sys.argv[1] == 'insert':
        print(str_insert_Sub(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == 'get_subs_by_user':
        print(str_select_UserSubs(sys.argv[2]))
    elif sys.argv[1] == 'get_subs_by_event':
        print(str_select_EventSubs(sys.argv[2]))    
    else:
        print(f'Invalid 1st argument: {sys.argv[1]}')