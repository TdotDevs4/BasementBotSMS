import sys

#### Sub-Command check function ####
def isSubCommand(strCommandHdr: str, strUserType: str, strCommand: str):

    if strCommandHdr == '':
        strSubCommandInput = strCommand
    elif '*' in strCommandHdr:
        strSubCommandInput = strCommandHdr[0:strCommandHdr.rfind('*')+1]
    else:
        strSubCommandInput = strCommandHdr+'_'+strCommand
        
    dict={
        'event' : '1001.c1',
        'event_create' : '1001.c2',
        'event_create_1*' : '1001.c3',
        'event_create_2*' : '1001.c3',
        'event_create_3*' : '1001.c3',
        'event_create_4*' : '1001.c0',
        'event_cancel' : '1001.c2',
        'event_cancel_1*' : '1001.c0',
        'unsub' : '1002.c1',
        'rcommand': '1001.c1',
        'rcommand_requests' : '1001.c0',
        'rcommand_add': '1001.c2',
        'rcommand_add_1*': '1001.c3',
        'rcommand_add_2*': '1001.c0'
        }
    
    strDefaultValue = '1000.c0'
    strSubMatch = str(dict.get(strSubCommandInput, strDefaultValue))

    ##Check user sub-command rights
    if strSubMatch[0:4] == strUserType:
        return strSubMatch[5:7]
    else:
        return strDefaultValue[5:7]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(isSubCommand(sys.argv[1], sys.argv[2], ''))
    elif len(sys.argv) == 4:
        print(isSubCommand(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        print('ERROR in sub_command_check ARGS: Exactly 3 arguments must be specified.')
        print(sys.argv)