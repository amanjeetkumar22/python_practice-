# word="python"
words=["Aman","Jeet","Kalwar"]
with open ("line.txt","r") as f:
    content=f.read()

##to search ->"Word" in text file 
# if("python" in content):
#     print("Yes found")
# else:
#     print("not found")

##to replace word that is stored in list with # 
# for word in words:
#     content=content.replace(word,"#"*len(word))

# with open("line.txt","r")as f:
#     content=f.read()
#     if("###" in content):
#         content=content.replace("###",words)


# for i, word in enumerate(words):
#     content = content.replace(word, f"#WORD{i}#")


for i, word in enumerate(words):
    content = content.replace(f"#WORD{i}#", word)


with open("line.txt","w") as f:
    f.write(content)