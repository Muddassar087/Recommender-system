from data import products

def search(item=""):
    cetagory = ""
    def itemsFilter(prod):
        if item in prod["name"]:
            return True

    searchResult = list(filter(itemsFilter, products))
    if searchResult.__len__() >= 1:
        cetagory = searchResult[0]["cetagory"]
        def itemswithcetagory(items):
            if cetagory == items['cetagory']:
                return True
        
        cetagoryRes = list(filter(itemswithcetagory, products))
        
        def deleteItem(item):
            ind = 0
            for i in range(len(cetagoryRes)):
                if cetagoryRes[i]['name'] == item:
                    ind = i
            cetagoryRes.pop(ind)
        if cetagoryRes.__len__() > 0:
            for i in searchResult:
                deleteItem(i['name'])

        for i in cetagoryRes: searchResult.append(i)
        
    return searchResult
