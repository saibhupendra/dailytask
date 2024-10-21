## Functions:
##       >>It is a block of reuseble code excectes whenever we call the functions
##      >> we are passing a data to this functions as an arguments
##     >>functions are know as methods,procedures
#       >> function are two types:
##             1.bulit-in function
##             2.customised function(user define)


# declaration:
# def

def wish(name):
    print("happy birthday",name)
wish ("sai")



def add(s,s1):
    print(s+s1)
    print(s1-s1)
    print(s*s1)
    print(s/s1)
add(30,20)


def s(x,y):
    print(x+y)
s("nani","nani")    


## by adding marks for students:

def marks (math,physics,chemistry,english):
    
    total=math+physics+chemistry+english
    print(total)
    print((total/totalscore)*100)


math=91
physics=45
chemistry=45
english=60
totalscore=400
marks(math,physics,chemistry,english)

math=92
physics=47
chemistry=48
english=66
totalscore=400
marks(math,physics,chemistry,english)


### return >> it is used to send a value back from a function to where it was called.

def add(a,b):
    #print(a+b)
    return a+b
add(20,30)
print(add(20,30))
sum=add(10,20)
print(sum)

if sum %2==1:
    print("is even")
else:
    print("not a even")    



##hight frequency element
# 
def highest_frequency(l):
    max_count = 0
    most_frequent = None
    for i in l:
        count = l.count(i)
        if count > max_count:
            max_count = count
            most_frequent = i
    return most_frequent

s=highest_frequency([1, 3, 5, 2, 6, 2, 7, 2, 8])
print(s)
