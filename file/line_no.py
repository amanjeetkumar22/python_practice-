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

##replacing words with "#" times of length of word 
for word in words:
    content=content.replace(word,"#"*len(word))

##change in word number 
# for i, word in enumerate(words):
    # content = content.replace(word,f"#WORD{i}#")

##again change in word     
# for i, word in enumerate(words):
    # content = content.replace(f"#WORD{i}#",word)


with open("line.txt","w") as f:
    f.write(content)