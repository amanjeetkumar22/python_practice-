# f=open("files.txt") #open("file.txt","mode of opening") #read bydefault 
# data =f.read()
# print(data)
# f.close()

# st = """hello I am aman
#         kaise ho bhai """

# f=open("files.txt","w")#appending->"a" to add something in end 
# f.write(st) #write something in text file 
# f.close



# f=open("files.txt")

# # lines=f.readlines()#readlines return "list" ,next lines item is a new item in list 
# # print(lines)

# # line= f.readline()#line used to read single line 
# # print(line)

# # using while loop reading the txt file 
# line=f.readline()
# while(line != ""):
#     print(line)
#     line=f.readline()

# f.close()

# st=input("Enter what u want to write ")

with open("files.txt") as f:
        # f.write(st + "\n")
       print(f.read())
        # f.close # when we are using "with statement the no need of close statement"

# # f=open("files.txt","w")
# # # c=f.read()
# # # d=f.write()
# # lines = f.readlines()
# # print(lines,type(lines))

# # print(c)
# # f.close()






    
# f=open("files.txt")
# # f=open("string.txt")
# # lines = f.readlines()
# # print(lines,type(lines))
# # f.close()

