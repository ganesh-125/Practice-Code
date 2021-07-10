# I/P -> [1,2,[3,4],[5,6]]]
# O/P -> [1,2,3,4]

list1= [1,2,[6,5,[1,4]]]
new_list = []
def islist(lis):
    for sublist in lis:
        if type(sublist) is list:
            return islist(sublist)
        new_list.append(sublist)
    return new_list
print(islist(list1))
