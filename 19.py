##join a list of string into single string without using join() 
s=["hello","nani","nagu"]
c=""
for i in s:
    c+=i
c=c.strip()
print(c)