#dictionary 
e = {} #empty dictionary 
print("1.empty dictionary:e={}")
d={"aman":"c++",
   "rohan":"python"
   }
print("2.Element of dict")
for i in d:
    print(i)
a={
    "key":"value",
    "aman":"coding",
    "marks":"100",
    "list":[1,2,3]
}
print("3.length of dict.:",len(a))
print("4 print value of key :",a["key"])
print("5 value of list :",a["list"])
print("6.items in dict",a.items())#to print items of dictionary 
a.update({"marks":99})
print("7.udated value of marks",a["marks"])
a.update({"marks":"number"})#to update the value part
# a.update({"marks":"50"}) 
print(a)
a["number"]=a.pop("marks")
print(a)

#set 

s= {1,2,3,2,4,5,4}

e=set() #empty set 

print("10.empty set: e=set():",type(e))
s.pop()#pop random element
print("11.element after 2nd pop :",s.pop())# it takes updated value 
print(s)

s1=set()
s1.add(20.0)
s1.add("20")
s1.add(20)

print("13.",len(s1))
print("14.",s1)
