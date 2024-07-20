'''def check(arr)  #divisible by 4 and 6
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            count+=1
    return count
arr=list(map(int,input().split()))
print('the count is:',check(arr))'''


#reverse the string
'''def string(s):
    rev=''
    for i in s:
        rev=i+rev
    print(type(rev))
    return rev
s="sreeja is good girl"
print(string(s))'''

#printing the letters in reverse order
'''def string(s):
    s=s.split()
    s=list(reversed(s))
    print(s)
s="sridevi womens engineering college"
string(s)'''

'''def string(s):
        print(s[::-1])
string("sridevi womens engineering college")'''


#printing the words in reverse order
'''def string(s):
    s=s.split()
    s=list(reversed(s))
    print(s)
    for i in s:
        rev=i[::-1]
        print(rev,end='')
s="sridevi womens engineering college"
string(s)'''


#fabnocii series
'''def check(n):
    n1=0
    n2=1
    print(n1,n2,end=' ')
    count=2
    while count<n:
        n3=n1+n2
        print(n3,end=' ')
        n1=n2
        n2=n3
        count+=1
check(10)'''

# calling the function with another function
'''arr=[5,9,13,6,17,3]
def check(ele):
    return ele%2==0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
print(increment(arr))'''

'''arr=[5,4,3,6,17,3]
def check(ele):
    return ele%2==0
def decrement(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
print(decrement(arr))'''

'''def check(ele):
    ele=str(ele)
    return ele==ele[::-1]
def increment(arr):
    count=0
    for ele in arr:
        if check(ele):
            print(ele)
            count+=1
    return count
arr=[21,70,212,702,1002]
print(increment(arr))  '''
  
  
  #to find palindrome b/w 1-50
'''1-50 palindrome number
def check(n):
    n=str(n)
    return len(n)>1 and n==n[::-1]
def increment(N):
    count=0
    for i  in range(1,N+1):
        if check(i):
            count+=1
            print(i)
    return count
N=50
print(increment(N)) '''



    
    

 
      
       
    