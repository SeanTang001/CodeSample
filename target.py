import requests
import pprint
import time
import json
import re
import io 
from fake_useragent import UserAgent
import pycurl

ua = UserAgent()
r = requests.Session()

def sortz(res):
    return sorted(res, key=lambda x: x["status"])[:5]

def get(x):
    r.headers = {'User-Agent': ua.random}
    return r.get(x).text

def score(items, instock, limitedstock):
    if (items==0):
        return 0
    x = 10/float(items)*instock + 10/float(items)*limitedstock
    return x

def search_item(item, count):
    x = get("https://redsky.target.com/v1/plp/search?keyword="+item+"&count="+str(count)+"&excludes=search_recommendations")
    res = json.loads(x)
    rez = []
    res = res["search_response"]["items"]["Item"]
    for i in range(len(res)):
        rez.append(res[i]["tcin"])
    return rez


def searchquery(itemtype, itemids, storeId, address):
    print("type: target id: "+storeId+"	itemtype: "+itemtype)
    items = ",".join(itemids)
    x = get("https://redsky.target.com/v2/pdp/tcin/"+items+"?excludes=in_store_location,taxonomy,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics,esp,available_to_promise_network&storeId="+storeId+"")
    rez = json.loads(x)
    res = []
    instock =0
    limitedstock = 0
    ofs=0
    for h in rez:
        try:
            status = h["product"]["available_to_promise_store"]["products"][0]["locations"][0]["availability_status"]
            if("IN_STOCK" in status):
                instock = instock+1
                status = "In Stock"
            if ("LIMITED_STOCK" in status): 
                limitedstock = limitedstock+0.5
                status = "Limited Stock"
            if (("DISCONTINUED" in status) or ("NOT_SOLD_IN_STORE" in status)):
                x=1/0
            if ("OUT_OF_STOCK" in status):
                ofs=ofs+1
                x=1/0
            quantity = h["product"]["available_to_promise_store"]["products"][0]["locations"][0]["onhand_quantity"]
        except:
            continue
        res.append({"tcin":h["product"]["available_to_promise_store"]["products"][0]["product_id"], "status":status, "quantity":quantity, "price":h["product"]["price"]["listPrice"]["price"], "name":h["product"]["item"]["product_description"]["title"]})
    if (len(res)==0):
        return None
    itemType = {}
    itemType["summaryTotal"] = {"quantityRank":score(len(res)+ofs, instock, limitedstock)}
    itemType["items"]=sortz(res)
    itemType["type"]="target"
    itemType["address"]=address
    itemType["storeId"] = storeId
    return itemType

def target(filename):
    items = json.load(open("item.json"))
    storeId = json.load(open("target_id.json"))	
    tcin = json.load(open("tcin.json"))
    pp = pprint.PrettyPrinter(indent=2)
    t = time.time()
    maindict = {}
    a = list(storeId.keys())

    for i in a:
        maindict[storeId[i][1]] = {}
    for i in a:
        maindict[storeId[i][1]][i] = {"address":storeId[i][0]}
        for x in items:
            print(x)    
            itemz = tcin[x]
            res = searchquery(itemz, i, storeId[i][0], x)
            maindict[storeId[i][1]][i][x] = res
        print(maindict)
    print(time.time()-t)
    x = open(filename, "w")
    x.write(json.dumps(maindict, indent=2))
    x.close()
    return maindict

if __name__ == "__main__":
    target("res1.json")
