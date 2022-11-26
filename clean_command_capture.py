import sys
##Same as clean_command except it retains casing and internal spaces....
####Remove defined special chars, nums and spaces using replace() 
####Only exactly one argument allowed.
def cleanCommand(strCommand):

    # print given command
    print ('Original Command : '+strCommand)
    

    ####I think sub-commands will use this syntax: [event_change_title || event_send_update]
    #### Will def allow that input for me and possibly allow for admins under the hood if they want.

    #Order matters here...
    #arrNums = ['0','1','2','3','4','5','6','7','8','9']  
    #arrSpaces = [' ']
    arrSpecialChars = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    arrUnderscores = ['__']

    arrRemoveFromCommand = arrSpecialChars + arrUnderscores
    strCommand = strCommand.strip()
    #strCommand = strCommand.lower()
        
    #iterate ordered array of characters to remove from the string
    for i in arrRemoveFromCommand: 
        strCommand = strCommand.replace(i, '')
    
    #remove leading '_'
    intCmdLen = len(strCommand)
    if strCommand[0:1] == '_':
        strCommand = strCommand[1:intCmdLen]
        intCmdLen = len(strCommand)        
    
    #remove trailing '_'
    if strCommand[(intCmdLen-1):intCmdLen] == '_':
        strCommand = strCommand[0:(intCmdLen-1)]
        intCmdLen = len(strCommand)        

    #print/return resulting command
    print ('Clean Command : ' + str(strCommand)+'\n')
    return strCommand

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(cleanCommand(sys.argv[1]))
    else:
        print('ERROR: Only exactly one argument allowed.')
        ##print(sys.argv)
