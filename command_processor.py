
#####################################
# Primary command processing logic. #
#####################################

from genericpath import exists
from os import _exit
import sys
#import mariadb
#import mysql.connector
from sub_command_check import *
from MYSQL_Functions_commandRequestLog import *
#from MySQL_Functions_Connector import *
strUnderContruction = "...under construction..."

#Database functions
#from MySQL_Functions_Users import *
#from MySQL_Functions_Events import *

def isSauce(strCommandLower):
    dict={
        'sauce' : 1,
        'sawc' : 1,
        'saucy' : 1,
        'saucyy' : 1,
        'boss' : 1,
        'thesauce': 1
        }
    
    return dict.get(strCommandLower, 0) == 1

def isHello(strCommandLower):
    dict={
        'hey' : 1,
        'hi' : 1,
        'hello' : 1,
        'yo' : 1,
        'yoo' : 1,
        'yooo' : 1,
        'yoooo' : 1,
        'sup' : 1,
        'hola': 1,
        'suhdude' : 1,
        'sahdude' : 1,
        'supdude' : 1,
        'whatup' : 1,
        'whatsup' : 1,
        'wassup' : 1
        }
    
    return dict.get(strCommandLower, 0) == 1

def isFriend(strCommandLower):
    dict={
        'cbhskate69' : 1,
        'mufassa8941' : 1,
        'bondalan24' : 1,
        'commador' : 1,
        'drymeat' : 1
        }
    
    return dict.get(strCommandLower, 0) == 1

def commandsFileReturn(strUserType: str, strSubCommand: str, blnFunctional: bool):
#Returns commands/sub-commands files based on strSubCommand and strUserType.
    strOutput = 'init_commandsfileReturn'
    strFilePath = '/var/www/html/'
    
    if strUserType=='1001' or strUserType==1001:
        strFilePath += 'admin_commands'
    else:
        strFilePath += 'user_commands'
    
    if strSubCommand:
        strFilePath += '_'+strSubCommand

    strOutput = ''    
    with open(strFilePath + '.txt') as f:
        for line in f:
            strOutput += line

    if not blnFunctional:
        strOutput += '<br><br>'
        with open('friendly_commands.txt') as f:
            for line in f:
                strOutput += line
            
    #print(strOutput)
    return strOutput

##############################################
####### MAIN COMMAND PROCESSING LOGIC ########
##############################################
def process_command(strUserType: str,  intUserId: int, strCommandLvl: str, strCommandHdr, strCommand):
    strOutput = 'init_process_command'
    
    #handling 1001=>1 and 1002=>0...php...
    if strUserType == '1001' or strUserType == 1001:
        blnIsAdmin = 1
        strUserTypeLabel = 'ADMIN'
    else:
        blnIsAdmin = 0
        strUserTypeLabel = 'USER'
        
    #defaults empty input to 'commands'
    if not strCommand and not strCommandHdr: strCommand = 'commands'

    #########################################
    #### SHORT-CIRCUIT GLOBAL COMMANDS ######
    #########################################
    if strCommand=='commands' or strCommand=='fcommands':
        strOutput = commandsFileReturn(strUserType, '', strCommand[0:1]=='f')

    elif strCommand=='me':
        if strUserType=='1001':
            #Get applicable Event status/info
            strOutput = strUserTypeLabel+': '+str(intUserId)+', Event Status: ACTIVE: [Your Saucy Event], Sub Count: 69.'
        else:
            #Get Active/Total Events subbed
            strOutput = strUserTypeLabel+': '+str(intUserId)+', Active Events: 3.50, Total Event Count: 420.'
    elif strCommand=='stop':
        strOutput = 'Fine...'+strUserTypeLabel+': '+str(intUserId)+' has been deactivated...bye! (Not really tho)'
        
    ##Friendly Commands##
    elif isSauce(strCommand):
        strOutput = 'Sauce is the boss and I am the boss of the sauce.'
    elif isFriend(strCommand):
        strOutput = 'Hey buddy, thanks for being un-apologetically yourself! -T'
    elif isHello(strCommand):
        strOutput = 'Yooo, what up?! - T'
    elif strCommand=='beans':
        strOutput = 'Give it the beans! - Matt'
    elif strCommand=='beammeupscotty':
        strOutput = 'Butterscotch! - Yakov \n\nOR \n\n No. I want candy'
    elif len(strCommand) == 69:
        strOutput = 'You hit the character limit, congrats! Can you guess what the limit is?'
    elif strCommand=='makesomemorecommands' or strCommand=='makemorecommands':
        strOutput = strUnderContruction

    #### USER COMMANDS #######
    elif not(blnIsAdmin): ####
    ##########################
        
        ##Functional commands##
        if strCommand=='unsub':
            strOutput = strUnderContruction
            
        #Invalid command else case
        else:
            strOutput = 'Invalid Command: ['+strCommand+'].'
            #strOutput = strOutput + str(commandsFileReturn(blnIsAdmin, ''))


    ######################################
    #### ADMIN COMMANDS  #################
    elif blnIsAdmin:     #################
    ######################################
        if strCommandHdr:
            if '*' in strCommandHdr:
                strPreviousCommand = strCommandHdr[strCommandHdr.rfind('*')+2:len(strCommandHdr)]
                strCommandHdr = strCommandHdr[0:strCommandHdr.rfind('*')+1]
                strCommandWithHeader = strCommandHdr
            else:
                strCommandWithHeader = strCommandHdr+'_'+strCommand

            #### SUB-COMMANDS ####
            if strCommandLvl == 'c1':
                if strCommandHdr=='rcommand':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                elif strCommandHdr=='event':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                else:
                    strOutput = 'Invalid Sub-Command[c1]: ['+strCommandWithHeader+'].'

            elif strCommandLvl == 'c2':

                if strCommandHdr=='rcommand_add_1*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                elif strCommandHdr=='event_create_1*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                elif strCommandHdr=='event_cancel_1*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                else:
                    strOutput = 'Invalid Sub-Command[c2]: ['+strCommandWithHeader+'].'

            elif strCommandLvl == 'c3':
                
                if strCommandHdr=='rcommand_add_2*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                elif strCommandHdr=='event_create_2*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                elif strCommandHdr =='event_create_3*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                elif strCommandHdr =='event_create_4*':
                    strOutput = commandsFileReturn(strUserType, strCommandHdr, True)
                    arrInputs = strPreviousCommand.split('_')
                    strOutput += '\n\n'+f'Event Title: [{arrInputs[0]}]\n Event Location: [{arrInputs[1]}]\n Event Date & Time: [{strCommand}]\n\n'
                else:
                    strOutput = 'Invalid Sub-Command[c3]: ['+strCommandWithHeader+'].'

            elif strCommandLvl == 'c0':
                    
                if strCommandHdr=='rcommand_add_2*':
                    strRequestedCommand = strPreviousCommand
                    strDescription = strCommand
                    strOutput = 'SUCCESS: Your command was requested!\n\n'
                    strOutput += 'Command Request: ['+strRequestedCommand+'] <br>Command Function: ['+strDescription+']'

                elif strCommandHdr =='event_create_4*':
                    arrInputs = strPreviousCommand.split('_')
                    strOutput = f'\n\nSUCCESS: [{arrInputs[0]}] was confirmed!!'

                elif strCommandHdr =='event_cancel_1*':
                    
                    strOutput = f'SUCCESS: Your Event was cancelled.'
                elif strCommandWithHeader=='rcommand_requests':
                    strOutput = "\n--END--"
                elif strCommandWithHeader == 'event_create':
                    strOutput = 'Event in progress, one at a time please!'
                elif strCommandWithHeader == 'event_cancel':
                    strOutput = 'You do not have any active Events!'
                elif strCommandWithHeader == 'event_info':
                    strOutput = ""    
                
                else:
                    strOutput = 'Invalid Sub-Command[c0]: ['+strCommandWithHeader+'].'
            else:
                strOutput = 'Invalid Sub-Command[c]: ['+strCommandWithHeader+'].'
        else:
            ##Functional commands##
            if strCommand=='me':
                strOutput = 'ADMIN: '+str(intUserId)+', Event Status: ACTIVE: [Your Saucy Event], Sub Count: 69.'
            elif strCommand=='rcommand':
                strOutput = commandsFileReturn(strUserType, strCommand, True)
            ####Invalid command else case
            else:
                strOutput = 'Invalid Command[c0]: ['+strCommand+'].'
                #strOutput = strOutput + str(commandsFileReturn(blnIsAdmin, ''))

        
    #Final Return
    #print(str(strOutput))
    #return str(strOutput)
    return strOutput
##############################
## HELPER FUNCTIONS
#Inline-if value empty, return default value, else return value
def iif_empty(checkValue, defaultValue):
    if checkValue:
        return checkValue
    else:
        return defaultValue

#####################################################################
######## MAIN IF STATEMENT TO VERIFY ARGS AND RUN PROCESSOR #########
#####################################################################
##def process_command(strUserType: str,  intUserId: int, strCommandLvl: str, strCommandHdr: str, strCommand: str):
if __name__ == '__main__':
    if len(sys.argv) == 6:
        ##print(process_command(iif_empty(sys.argv[1], '1000'), iif_empty(sys.argv[2], 1000), iif_empty(sys.argv[3], 'c0'), iif_empty(sys.argv[4], ''), iif_empty(sys.argv[5], '')))
        print(process_command(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    else:
        print("\nERROR IN ARGS: RETURNING THE DEFAULT COMMANDS")
        # print(sys.argv)
        # print(len(sys.argv))
        # print('\n')
        print(process_command('1000', 0, 'c0', '', ''))
