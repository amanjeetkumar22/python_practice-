for i in range(1,10):
  pass #null statement // means do nothing 

for i in range(1,10):
    if(i==7):
        break
    print(i)
'''
output: 1,2,3,4,5,6 
'''
print()
for i in range(1,10,2): #(start,stop,step_size)
    if(i==6):
        continue
    print(i) 

'''
output: 1,2,3,4,5,7,8,9, 
'''      