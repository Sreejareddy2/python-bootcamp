#to find product of given string with numbers
'''s=input()
prod=1
for i in range(0,len(s)):
    if s[i].isdigit():
        prod*=int(s[i])
print(prod)'''


#to count number of digits in input
'''s=input()
count=0
for i in range(0,len(s)):
    if s[i].isdigit():
        count+=1
print(count)'''



#string palindrome or not
'''s = 'racecar'
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
if(s1==s):
    print('palindrome')
else:
    print('not')   '''
    
#to count vowels in a given string
'''s='sreeja'
vowels=['a','e','i','o','u']
count=0
for c in s:
    if c in vowels:
        count+=1
print(count)'''


#no of characters
'''s='sreeja64857394'
count=0
for c in s:
    if c in s:
        count+=1
print(count)'''


#to check the data
'''data=[1,8,'apple','mango','carrot']
fruits=['apple','mango','watermelon']
for i in data:
    if i not in fruits:
        print(i)


data=[1,8,'apple','mango','carrot']
fruits=['apple','mango','watermelon']
vegies=['onion','brinjal','tamato','carrot']
for i in data:
    if i in  vegies and i not in fruits:
        print(i)'''
        
        

'''s="he is playing football but not playing cricket"
s=s.split()
print(s)
print(len(s))
print(s.count("he"))'''

#to print the given data
'''def greetings(branch):
   return ("hello good morning",branch)
print(greetings("cse"))
print(greetings("it"))
print(greetings("ece"))
'''

#to check given num is even or odd
'''n=13
def evenodd(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"
print(evenodd(n))'''

