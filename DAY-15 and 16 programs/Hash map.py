my_map = {}
# putting a key value pair
my_map["key"] = "This is a value"
my_map[0] = "ZERO"
my_map[1.3] = "ONE.THREE"
my_map[0] = "UPDATED ZERO"

for key in my_map:
    print(my_map[key],end=" ")