def doub(list):
    cleanlist = []
    
    for x in list:
        if list.count(x) >= 1 and x not in cleanlist:
            cleanlist.append(x)
    return cleanlist

list = [1, 1, 1, 2, 2, 3]
clean = doub(list)
print(clean)