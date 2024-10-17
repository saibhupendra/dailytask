"for multiples of three ,print 'fizz' instead of the number and for multiple of five ,print 'buzz'"
for i in range(1,100+1):
    if(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)  

