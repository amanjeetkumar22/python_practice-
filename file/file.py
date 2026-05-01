# f=open("files.txt","w")
# # c=f.read()
# # d=f.write()
# lines = f.readlines()
# print(lines,type(lines))

# print(c)
# f.close()






# st=input("Enter what u want to write ")

# st = "hello I am aman"

# f=open("string.txt","w")
# f.write(st)
# f.close


# with open("string.txt","a") as f:
#         f.write(st + "\n")
#         f.close
    
f=open("files.txt")
# f=open("string.txt")
# lines = f.readlines()
# print(lines,type(lines))
# f.close()

line=f.readline()
while(line != ""):
    print(line)
    line=f.readline()