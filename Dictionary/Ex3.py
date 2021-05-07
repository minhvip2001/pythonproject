dict1 = {'color': {'attri':['Black']}, 'diameter': {'attri':['(300, 600)']}}
dict2 = {'size': {'op':'in'}, 'diameter': {'op':'range'}, 'color': {'op':'in'}}

dict3 = {n:{**dict1[n],**dict2[n]} for n in dict1}
print(dict3)