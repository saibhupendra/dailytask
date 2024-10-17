## set{}
## union()
## It will add two set elements without duplicates

s1={"nani","nagu",1,2,3,45}
s2={"prasad","ramadevi",2,3,4}
print(s1.union(s2))

##output
##{1, 2, 3, 'prasad', 4, 'nani', 45, 'ramadevi', 'nagu'}

##intersection()
##  > It will retuns only commom elements in the set
 
s1={"nagu","prasad",4,5,67}
s2={"nani","ramadevi",4,5,12}
print(s1.intersection(s2))

#output
#{4, 5}

##intersection_update()
## >>   It modify the set that are have only common elemnets in the both the sets

s1={"nagu","prasad",4,5,67}
s2={"nani","ramadevi",4,5,12}
s3=s1.intersection_update(s2)
print(s3)


##difference()
##  > returns s1 elements which are not present in s2

s1={"nagu","prasad",4,5,67}
s2={"nani","ramadevi",4,5,12}
print(s1.difference(s2))

##output
##{'nagu', 67, 'prasad'}
## 4,5 is present in the s1 and s2 also

## difference_update()
##   >It modifies the original set by removing elements that are present in another specified set

s1={"nagu","prasad",4,5,67}
s2={"nani","ramadevi",4,5,12}
print(s1.difference_update(s2))

## symetric_difference()
## >> It returns both s1 ans s2 which are not present in both the sets

s1={"nagu","prasad",4,5,67}
s2={"nani","ramadevi",4,5,12}
print(s1.symmetric_difference(s2))


#output
#{'ramadevi', 'prasad', 67, 12, 'nagu', 'nani'}

##symetric_diffrence_update()

s1={"nagu","prasad",4,5,67}
s2={"nani","ramadevi",4,5,12}
print(s1.symmetric_difference_update(s2))


##modifying of set elements
s={1,2,3,4,5,6,7}
l=list(s)
print(l)
l.append(9)
print(l)

