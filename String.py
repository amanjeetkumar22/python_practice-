a=input("Enter your name:")
b=input("Enter Date:")
print("1.",a)
print(f"2.lenght in  {a}:",len(a))
print(f"3.capitalize of {a}",a.capitalize())

nameshort=a[0:6]
print("4.using slice of string[0:6]",nameshort)
print("5.a[0:4]",a[0:4])
print("6.a[-4:-2]",a[-4:-2])
print("7.a[1:6:2]",a[1:6:2])
print("8.",a.endswith("eet")) #to check string end with or not 
print(f"9.Good Morning,{a}")

Letter =""" Dear <|Name|> 
 You are  selected!
<|Date|>""" #\n for next line , \t  for space 

print("10.letter number where double space found:",Letter.find("  ")) #for dectecting space 
Letter=Letter.replace("  "," ") #replace double space with single space 
print("11.letter",Letter)

print("12.Letter:-",Letter.replace("<|Name|>","AMAN").replace("<|Date|>","3 DEC")) #chaining of .replacing 


#method 2 to replace the words 
# Letter=Letter.replace("<|Name|>", a)
# Letter=Letter.replace("<|Date|>", b)
# print("12.Letter:-",Letter)

