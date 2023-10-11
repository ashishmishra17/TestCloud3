#We have a nested object. We would like a function where you pass in the object and a key and get back the value.

def checkKeyValue(obj, key):
    keys = key.split("/")
    dict1 = obj
    for each in keys:
        if each in dict1:
            dict1 = dict1[each]
            if dict1 == None:
                return
    return dict1
    

obj = {'x':{'y':{'z':'a'}}}
key = "x/y/z"
print(checkKeyValue(obj=obj, key=key))
