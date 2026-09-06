a = {1,2,3,2,3,2,"hello","hello","world","world"}

print("A = ", a) #prints  values of the set

a.add(67) #adds element to the set
a.add("bro") #adds element to the set

a.remove(1) #removes element from the set

(a.pop()) #removes random element from the set

print("A2 = ", a)
b = {1,2,3,4,5,6,7,8,9}
print("B = ", b)

print("A U B = ", a.union(b)) # combination of elements of both sets

print("A ∩ B = ", a.intersection(b)) #common element


