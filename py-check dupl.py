some_list=['a','b','c','d','d','e','f','f']
# duplicate=[]
# for alphebet in some_list:
#     if some_list.count(alphebet)>1:
#         if alphebet not in duplicate:
#           duplicate.append(alphebet)
# print(duplicate)

duplicate=list(set(x for x in some_list if some_list.count(x)>1))
print(duplicate)