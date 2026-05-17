
l=["Aman","Amit","1","2","3"]

d = "-".join(l)
print(d)

c="Aman"
e=303

###format

# n= "Hii {} kon room {} me hai".format(c,e)
# n= "Hii {1} kon room {0} me hai"
n= "Hii {0} kon room {1} me hai"
print(n.format(c,e))