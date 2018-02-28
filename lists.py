import elifs

a = [3, 10, 45, "hello"]
print(a)

# add
a.append(1)
print(a)
a.append("bye")
print(a)

# remove at index
a.pop(0)
print(a)

# remove last
a.pop()
print(a)

# replace at index
a[0] = 67
print(a)