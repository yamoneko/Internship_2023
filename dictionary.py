d_data = {"name":{
    "1st": "yamone",
    "2nd": "thwe",
    "3rd": "win"},  "age" :[12,13,14], "email": "ymko@gamil"}
print(d_data["name"]["2nd"])
x= d_data.copy()
print(x)
# y = ('k1', 'k2', 'k3')
# k= 4
# thisdict = dict.fromkeys(y)
# print(thisdict)
# thisdict = dict.fromkeys(y,k)
# print(thisdict)
y = d_data.get("price", 1500) #synt-> dictionary.get(keyname, value)
print(y)
#itmes() -> return dict's key-value pairs as tuple in a list //value update yin  change
#keys() ->keys of dictionary as  a list

#pop() -> remove specified item form dict -> dictionary.pop(keyname, defaultvalue)
#d_data.pop(("email"))

#print(d_data)
# x = d_data.pop("email") //the value of the removed item is the return value of pop()
# print(x)

#popitem()-> remove the last inserted key-value pair

#dictionary.setdefault(keyname,value)-> return the value of the item with specified key -> ma shi yin update pay
#d_data.setdefault("point",[23,4,5,6])

# d_data.update({"color": "white"})

#dictionary.values() -> return view object(the values of the dictionary as a list)
print(d_data.values())