x=int(input("enter number:"))
temp=x
rev=0
while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
if(temp==rev):
    print("true")
else:
    print("the number isn't a palindrome")
