thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
z = (thisdict.keys())
h = list(thisdict.values())
print(type(z))
print(z)
print(h)
items_1 = list(thisdict.items())
print(items_1)