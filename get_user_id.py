import sys, os
###Get UserId to set on initial command input screen...
###This will eventually take in a phone number and return an id
###***For now it is just taking in strUserType[1000,1001,1002] and returning it

def getUserId(strPhoneNumber):
    dict={
        '1000' : 1000,
        '1001' : 1001,
        '1002' : 1002
        }

    return str(dict.get(strPhoneNumber, -1))

if __name__ == '__main__':
    print(getUserId(sys.argv[1]))
