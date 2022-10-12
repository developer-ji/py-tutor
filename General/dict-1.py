# Dictionary
# CRUD C:- Create R-Retrive, U:-Update, D:-Delete

# Create
data ={}
data ={"a":1, "b":2}
data = [('a',1), ('b',2)]
dict_data = dict(data)

# {"a":1, "b":2}
# Retrive
print(dict_data)
xl  = dict_data

# get value using key
key = 'a'
xl[key]
xl.get(key, 34)

# get all keys()
xl.keys()

# get all values()
xl.values()

# insert


# update 