# List - [], heterogenous elements, ordered, indexed, mutable (can change)
l=[12,54,32,'hello',True,3.43,'hi']
print(l)
print(type(l))

# slicing 
print(l[:])
print(l[:3])
print(l[1:8])
print(l[1:5:2])
print(l[1:6:-1])
print(l[5:1:-1])

print("-----")
l1=[45,32,11,10,4,78,66,54]
# l1.sort()
# print(l1)

print(l1)
# l1.insert(2,[44,33])
# print(l1)

l1.append(23)
# l1.append([33,21])
print(l1)

l1.extend([33,21])
print(l1)


# remove or pop 
# l1.pop(15) # by default last element remove 
# print(l1)
# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.

l1.remove(78) #Remove first occurrence of value, Raises ValueError if the value is not present.
print(l1)

print(l1.count(4))

for i in l1:
    print(i+5)
    
# zip function 
a=[3,4,5,6,7]
b=[1,2,3,5,6,10]

# for i in zip(a,b):
#     print(i)
# for i,j in zip(a,b):
#     print(i+j)

new=[]
for i in a:
    for j in b:
        if i==j:
            # print(i)
            new.append(i)
print(new)

for i in a:
    if i in b:
        print(i)
        

# string list 

l=["hello","how","are","you"]
print(l)

print("_".join(l))