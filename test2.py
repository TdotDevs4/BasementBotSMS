from MySQL_Functions_Users import *
from MySQL_Functions_Events import *
from MySQL_Functions_Connector import *

##Users testing
#insert_user("14044080221", 1)
#update_activeUser(1004, 0)
update_activeUser(1005, 1)
update_adminUser(1005, 0)
#update_adminUser(1004, 1)
#print(isAdminUser(1004))
#print(isAdminUser(1005))
#print(isAdminUser(1006))


#################################
##Events testing
#insert_user("18008675309", 0)

#print(insert_event(1005))
#insert_event(1005)

#print(isAdminUser(1004))
#print(createEvent(1004))

#print(update_activeEvent(1014, 0))
#print(update_activeEvent(1014, 1))

#delete_event(1014)
