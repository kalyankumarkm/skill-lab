"""import keyword
print(keyword.kwlist)

a=None
print(a)


a=0
print(type(a))
print(bool(a))

print(bool([1.0]))
print(bool([0.0]))


a=3j+5
print(a)

a=6j
print(a)

'''List'''
a=[1,2,3,4,5,True,'hello']
print(a)

a.append(6)
print(a)
popped_value = a.pop()
print(popped_value)
popped_value = a.pop()
print(popped_value)

'''tuple'''
a=(1,2,3,4,5,True,'hello')
print(a)

a=(1,2,3,4,5,True,'hello',(1,2,3,4,5))
print(a)
a={'a':[10,20,30],'b':[40,50,60]}
print(a)

a='Hello'
print(a[2:4])
print(a[-3:2+1])

a="Good Morning"
print(a[7:11])
print(a[7:10+1])
print(a[1:5+1:2])
print(a[-7::3])
print(a[-2:-8:-3])

a=eval(input("Enter a number: "))
print(a,type(a))

a=int(input("Enter a number: "))
if(a%2==0):
    print("Even")
else:
    print("Odd")
a=eval(input("Enter a number: "))
if len(a)==5:
    print("Length is 5")
else:
    print("Length is not 5")
ch=input("Enter a character: ")
if("A"<=ch<="Z"):
    print("Uppercase")
elif("a"<=ch<="z"):
    print("Lowercase")
else:
    print("Not an alphabet")
i=25
while i<=50:
    if(i%2==0):
        print(i)
    i+=1
n=int(input("Enter a number: "))
rev=0
while(n>0):
    id=n%10
    rev=rev*10+id
    n=n//10
print("Reverse is: ",rev)
s=input("Enter a string: ")
output=""
for i in s:
    if "A"<=i<="Z":
        output+=chr(ord(i)+32)
    elif "a"<=i<="z":
        output+=chr(ord(i)-32)
print("Output is: ",output)
print("Hello World")
print('Hello World')
s=input("Enter a string: ")
rev=""
for i in s:
    rev=i+rev
print("Reverse is: ",rev)

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range(1,i+1):
        if(i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""


"""a='happy birthday'
print(a[-4:-7:-1])

def convert_to_uppercase(s):
    output=""
    for i in s:
        if "A"<=i<="Z":
            output+=chr(ord(i)+32)
        elif "a"<=i<="z":
            output+=chr(ord(i)-32)
    return output
print(convert_to_uppercase(input("Enter a string: ")))


def convert():
    s=input("Enter a string: ")
    output=""
    for i in s:
        if "A"<=i<="Z":
            output+=chr(ord(i)+32)
        elif "a"<=i<="z":
            output+=chr(ord(i)-32)
    return output
print(convert())


class college:
    def __init__(self, name,phone,usn):
        self.name=name

        self.phone=phone

        self.usn=usn
        
    def display(self):
        print(self.name,self.phone,self.usn)

s1=college("ABC",1234567890,"1ABCD1234")
s1.display()

s2=college("XYZ",9876543210,"1XYZD5678")
s2.display()"""

