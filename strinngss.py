# #string  - set of characters, numbers and some special characters

# naam="Manjot Singh"
# print(naam)
# print(len(naam))
# print(naam[2])


# # methods 
# print(naam.lower())
# print(naam.upper())
# print(naam.capitalize())
# print(naam.title())
# print(naam.swapcase())
# print(naam.endswith('gh')) # True or False answer
# print(naam.startswith('ma')) # True or False answer

# print("----------------")
# # replace in string
# n="Hello, how are you"
# print(n)
# print(n.replace('o','ui'))


# # Slicing 
# print(naam)
# print(naam[:]) # start:stop:step
# print(naam[:4]) # start:stop:step
# print(naam[1:15]) # start:stop:step
# print(naam[2:6]) # start:stop:step
# print(naam[2:6:1]) # start:stop:step
# print(naam[::-1]) # start:stop:step
# print(naam[10:1:-1]) 



s="Hello, how are you"
print(s)

#split
print(s.split(','))
print(s.split('o'))

s1="hewevwe#dfgbd#bfdbdf#jergejn#kjgbfgjj#kjdbjk"
print(s1.split('#'))

e="    hello     "
print(e.strip())
print(e.lstrip())
print(e.rstrip())

for i in s:
    print(i+"_")