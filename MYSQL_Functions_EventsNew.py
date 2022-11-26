import sys
##################################################################
# All available database table functions for: Events             #
##################################################################

def str_insert_Event(intUserId: int, strEventTitle: str, strEventLocation: str, strEventDateAndTime: str):
    #dtmEventDateTime = DateTimeParseFunctionHere(strEventDateandTime)
    #query = f"INSERT INTO Events VALUES(0, {intUserId}, '{strEventTitle}', '{strEventLocation}', '{strEventDateAndTime}', null, CURRENT_TIME(), CURRENT_TIME(), 0, DATE_ADD(CURRENT_TIME(), INTERVAL 2 DAY));"
    
    query = f"INSERT INTO Events SELECT 0, {intUserId}, '{strEventTitle}', '{strEventLocation}', '{strEventDateAndTime}', '/event_sub_input.php?intEventId=', CURRENT_TIME(), CURRENT_TIME(), 0, DATE_ADD(CURRENT_TIME(), INTERVAL 2 DAY) WHERE (SELECT COUNT(intEventId) FROM Events WHERE intUserId = {intUserId} AND dtmExpiration > CURRENT_TIME() AND blnExpired = 0) = 0;"
    return query
    
def str_select_ActiveUserEvents(intUserId: int):
    strCountSubQuery = f"(SELECT IFNULL(COUNT(s.intUserId), 0) FROM Events e, eventToSub s WHERE e.intEventId = a.intEventId AND s.intEventId = e.intEventId AND s.blnActiveSub = 1) as 'intSubCount'"
    query = f"SELECT a.intEventId, a.strEventTitle, a.strEventLocation, a.strEventDateAndTime, a.dtmExpiration, a.strEventSubLink, {strCountSubQuery} FROM Events a WHERE a.intUserId = {intUserId} AND a.blnExpired = 0 AND a.dtmExpiration > CURRENT_TIME();"  
    return query

def str_select_EventById(intEventId: int):
    #returns unexpired event info by id
    strCountSubQuery = f"(SELECT IFNULL(COUNT(s.intUserId), 0) FROM Events e, eventToSub s WHERE e.intEventId = {intEventId} AND s.intEventId = e.intEventId AND s.blnActiveSub = 1) as 'intSubCount'"
    query = f"SELECT intEventId, strEventTitle, strEventLocation, strEventDateAndTime, dtmExpiration, {strCountSubQuery}, strEventSubLink FROM Events WHERE intEventId = {intEventId} AND blnExpired = 0 AND dtmExpiration > CURRENT_TIME();"  
    return query

def str_update_CancelActiveUserEvents(intUserId: int):
    #updates blnExpired on all Active Events by intUserId
    query = f"UPDATE Events SET blnExpired = 1, dtmUpdatedWhen = CURRENT_TIME() WHERE intUserId = {intUserId} AND (blnExpired = 0 OR dtmExpiration < CURRENT_TIME())"
    return query

def str_update_EventSubLink(intEventId: int):
    #updates strEventSublink on an Event
    query = f"UPDATE Events SET strEventSubLink = CONCAT(strEventSublink, {intEventId}), dtmUpdatedWhen = CURRENT_TIME() WHERE intEventId = {intEventId};"
    return query

if __name__ == '__main__':
    if sys.argv[1] == 'select':
        print(str_select_ActiveUserEvents(sys.argv[2]))
    elif sys.argv[1] == 'get':
        print(str_select_EventById(sys.argv[2]))
    elif sys.argv[1] == 'insert':
        print(str_insert_Event(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    elif sys.argv[1] == 'cancel':
        print(str_update_CancelActiveUserEvents(sys.argv[2]))
    elif sys.argv[1] == 'sublink':
        print(str_update_EventSubLink(sys.argv[2]))    
    else:
        print(f'Invalid 1st argument: {sys.argv[1]}')