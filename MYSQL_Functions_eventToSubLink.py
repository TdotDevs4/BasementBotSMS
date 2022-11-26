import sys
##################################################################
# All available database table functions for: eventToSubLink     #
##################################################################

def str_insert_SubLink(intEventId: int):
    
    query = f"INSERT INTO eventToSubLink VALUES(0, {intEventId}, '/event_sub_input.php?intEventId={intEventId}', 1, CURRENT_TIME(), CURRENT_TIME());"
    return query

def str_select_SubLink(intEventId: int):
    query = f"SELECT intEventId, strSubLink FROM eventToSubLink WHERE intEventId = {intEventId};"  
    return query

if __name__ == '__main__':
    if sys.argv[1] == 'select':
        print(str_select_SubLink(sys.argv[2]))
    elif sys.argv[1] == 'insert':
        print(str_insert_SubLink(sys.argv[2]))
    else:
        print(f'Invalid 1st argument: {sys.argv[1]}')