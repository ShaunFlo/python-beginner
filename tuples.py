# tuples are list but cant be changed

tup = ("one", "two", "3" )
tup2 = ("one1", "two2", "3three" )

print(tup)

# splices index 0-2 not including 2
print(tup[0:2])

# add two
tup3 = tup + tup2
print(tup3)

# len function
a = len(tup3)
print(a)