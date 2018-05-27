# empty dictionary
d = {}
# also can do d = dict() and
d = {"george": 24, "tom": 54}

print(d)

d["shaun"] = 22
print(d)

d["shaun"] = 23
print(d)

# loop through dictionary
for key, value in d.items():
    print("key: " + key + ", the value is ")
    print(value)


# del dictName["key"] to delete
# OR
# .pop["key"]
