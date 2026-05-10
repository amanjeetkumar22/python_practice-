# with open ("files.txt") as f:
#     content= f.read()

# with open ("files_copy.txt","w") as f: #new txt file name is "files_copy.txt"
#     f.write(content)##to copy item in other file

 
with open ("files.txt") as f:
    content1= f.read()

with open ("files_copy.txt","r") as f: 
     content2=f.read()

if(content1==content2):
     print("Yes both are same.")

else:
     print("no they both are not same.")     