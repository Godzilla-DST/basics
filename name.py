def name() :
    import os
    import godzilla
    os.system("clear")
    user = input("user name : ")
    if user == "DST" : 
        godzilla.godzilla()
    else :
        os.system("exit")