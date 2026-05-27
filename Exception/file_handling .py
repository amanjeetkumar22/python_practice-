# f = open('file.txt','w')

# try:
#     f.write("Hello")

# finally:
#     f.close()

with open('file.txt','w') as f:
    f.write("Hellooo")