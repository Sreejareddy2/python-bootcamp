# list is a collection of ordered elemnts & mutable in nature we cna perform operation like insert,update,delete
#to insert the elements
'''mobiles=['iphone','samsung','vivo']
print(mobiles)'''

#to remove
'''mobiles=['samsung','vivo','oppo']
mobiles.remove('vivo')
print(mobiles)'''

#to pop
'''mobiles=['samsung','vivo','oppo']
mobiles.pop(0)
print(mobiles)'''

#append
'''moblies=['samsung','oppo','vivo']
mobiles.append
print(mobiles)'''


#to replace a string
'''moblies=['iphone','samsung','oppo']
moblies[1]='blackberry'
print(moblies)'''


#to print the data
'''moblies=['iphone','samsung','vivo','oppo','nothing']
count=1
for ele in moblies:
    print(count,ele)
    count+=1'''
    
   #to print even  
'''moblies=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(moblies)):
     if i%2==0:
        print(moblies[i])'''
        
  #to reverse even position
'''moblies=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(moblies)):
     if i%2==0:
         print(moblies[::-1])
     else:    
        print(moblies[i])'''
          
     #to revese elements in even position   
'''moblies=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(moblies)):
     if i%2==0:
         rev=moblies[i]
         print(rev[::-1])
         print(moblies[::-1])
     else:    
        print(moblies[i])'''
        
        
 #       
'''arr=[1,2,3,4,5]
k=4
first=arr[k-1:] 
second=arr[:k-1]
print(first+second)'''

#
'''arr=[1,2,3,4,5]
k=3
#[5,4,3,2,1]
first=arr[k+1:k:-1]
print(first)'''



'''arr=[1,2,3,4,5,]
k=3
first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)'''

'''moblies=['iphone','samsung','vivo','oppo','nothing']
print(moblies)
del moblies
print(moblies)'''

'''arr=[1,2,3,4,5]
k=5              
if k<3:
    first=arr[k+1:k-2:-1]     
    second=arr[:k-1]
    print(first+second)'''





    

    
    
           
    
        