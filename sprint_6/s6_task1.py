import json   

def dict_processing(data,key,l):
    if data.get(key):
        l.append(data[key]) if not isinstance(data[key],list) \
                            else l.extend(data[key]) 
    for k in data.values():
        if isinstance(k,dict) and k.get(key):
            l.append(k[key]) 
                   
def find(file, key):
    unique = []
    with open(file) as f:
        data = json.load(f)
        if type(data) == list:
            for i in data:
                dict_processing(i,key,unique)    
        else :
            dict_processing(data,key,unique)
    return  list(dict.fromkeys(unique)) 
