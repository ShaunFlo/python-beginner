# empty dictionary
d = {}
# also can do d = dict() and
d = {"george": 24, "tom": 54}

print(d)

d["shaun"] = 22
print(d)

d["shaun"] = 23
print(d)

# keys usually strings or numbers

for key, value in d.items():
    print("key: " + key + ", the value is ")
    print(value)

