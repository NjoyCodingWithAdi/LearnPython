# default argument can be passed to save us from error in future

def emailId(firstName="test", lastName="ok"):
    print("Your email id is:-", firstName +"."+ lastName +"@gmail.com")
    
emailId()