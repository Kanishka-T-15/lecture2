i=28
print(f"i is {i}")

f=2.8
print(f"f is {f}")

b=True
print(f"b is {b}")

n=None
print(f"n is {n}")

if i>0:
	print("i is positive" )

elif i<0:
	print("i is negative")	
#for loop
names=["Alice","Bob","Charlie"]
for name  in names:
		print(name)
#set
s=set()
s.add(1)
s.add(3)
s.add(5)
s.add(1)
print(s)

#dictionaries
ages={"Alice":22, "Bob": 27}
ages["Charlie"] =30
ages["Alice"]+=1

print(ages)