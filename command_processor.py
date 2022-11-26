
#####################################
# Primary command processing logic. #
#####################################

import sys
import os

#Database functions
#from MySQL_Functions_Users import *
#from MySQL_Functions_Events import *

def commandsFileReturn(blnIsAdmin, strSubCommand):
#Returns commands/sub-commands files based on strSubCommand and blnIsAdmin.
    strOutput = "init_commandsfileReturn"
    strFilePath = '/var/www/basementbotsms.com/public_html/'
    
    if blnIsAdmin:
        strFilePath += 'admin_commands'
    else:
        strFilePath += 'user_commands'
    
    if strSubCommand:
        strFilePath += '_'+strSubCommand
        
    with open(strFilePath + '.txt') as f:
        strOutput = f.readlines()
        
    return strOutput

########MAIN COMMAND PROCESSING LOGIC#########
def process_command(strUserType, strCommand):
    strOutput = "init_process_command"
    #handling 1001=>1 and 1002=>0...php...
    if strUserType == "1001" or strUserType == 1001:
        blnIsAdmin = 1
    else:
        blnIsAdmin = 0
        
    #defaults empty input to "commands"
    if not strCommand: strCommand = "commands"
    #lower the command
    strCommandLower = strCommand.lower()

    ##Short-circuit, return appropriate commands list##
    if strCommandLower=="commands":
        strOutput = commandsFileReturn(blnIsAdmin, "")
        
    ##Friendly Commands##
    elif strCommandLower=="cbhskate69" or strCommandLower =="mufassa8941":
        strOutput = "Hey buddy, thanks for being un-apologetically yourself! -T"
        
    elif not(blnIsAdmin):
        #Non-Admin Commands#
        
        ##Functional commands##
        if strCommandLower=="me":
            strOutput = "USER: 1002, Active Events: 3.50, Total Event Count: 420."
        elif strCommandLower=="stop":
            strOutput = "Fine...USER: 1002 has been deactivated...bye!"
            
        #Invalid command else case
        else:
            strOutput = "Invalid Command: ["+strCommandLower+"]."
            strOutput = strOutput + str(commandsFileReturn(blnIsAdmin, ''))
    elif blnIsAdmin:
        #Admin Commands#
        
        ##Functional commands##
        if strCommandLower=="me":
            strOutput = "ADMIN: 1001, Event Status: ACTIVE: [Your Saucy Event], Sub Count: 69."
        elif strCommandLower=="event":
            strOutput = commandsFileReturn(blnIsAdmin, 'event')

        #Invalid command else case
        else:
            strOutput = "Invalid Command: ["+strCommandLower+"]."
            strOutput = strOutput + str(commandsFileReturn(blnIsAdmin, ''))

    #Final Return
    return str(strOutput)
#################


####MAIN IF STATEMENT TO VERIFY ARGS AND RUN PROCESSOR####
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(process_command(0, ""))
    elif len(sys.argv) == 2:
        print(process_command(sys.argv[1], ""))
    elif len(sys.argv) == 3:
        print(process_command(sys.argv[1], sys.argv[2]))
    else:
        print("ERROR in command_processor.py args if statement")
