def succeed():
    print "You've successfully log in,enjoy."
    exit(0)

def passwd_check():
    print "Please enter your password."
    index =raw_input(">")

    if index=="tianyi":
        succeed()
    else :
        log_in()

def acount_check():
    print "Please enter your acount."
    index=raw_input(">")

    if index=="110120":
        passwd_check()
    else :
        log_in()

def log_in():

    print "Welcome, please log in your acount."
    acount_check()

log_in()
