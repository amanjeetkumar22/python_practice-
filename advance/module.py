def myFun():
    print("Hello")

# myFun()
# print("file name is " + __name__)

if(__name__ == "__main__"): ##if we want this piece of code is only run by "module" file 
    print("We are directly running this code")
    myFun()
    print("file name is " + __name__)
