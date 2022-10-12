#Q1
x = {"a":
{"b":[("b", {"c":([{"name":{"nisha"}}])})]}
}  #dict me se nisha nikalna hai

y = x["a"]["b"]
# z = x["a"]["b"][0]
# kl = x["a"]["b"][0][1]
# xl = x["a"]["b"][0][1]["c"]
# k = x["a"]["b"][0][1]["c"][0]
# k2 = x["a"]["b"][0][1]["c"][0]["name"]
# #print(k2)
# k3 = list(k2)
# k4 = k3[0]
# print(k4) #out put = nisha


#Q2
_names = ['dashrath', ('ram', 'laxman', ('love', 'kush'))]

# kush nikalna tha

k = _names[1]
print(k)
kl = k[2]
print(kl)
xl = kl[1]
print(xl)
