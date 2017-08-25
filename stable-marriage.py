
'''
stable marriage is if at least one of two pairs are happy with the arrangement
not stable if there are two pairs of who want to trade

1. buyer gets proposals from sellers; sellers also have proposals
2. buyer gives rejections to all except top sellers; top sellers now in tentative engagement
3. buyer can keep rejecting offers and getting new offers
4. seller  propses to new buyers

polygamous solution (many sellers to one buyer)
there enough sellers for each buyer (max 3),
    but the number of sellers is only equal to the sum of the number of preferred sellers for all buyers



Buyers want up to be matched with up to three sellers. Some want one, some two, 
some three. There are enough sellers to satisfy all the buyer's desired sellers but no more.

every buyer has been matched with their desired number of sellers and every seller is 
match with at exactly one buyer.

buyers only have as many preferences in their list as they want
the algorithm will try to get the preferred sellers on the list, but the number of sellers is more important
there may be buyers who do not have the sellers they asked for

'''


from customer import Customer
from vendor import Vendor

#===========================================================
#manually create lists of buyers and sellers so results can be easier to compare
buyersPref = {
    'a':['sellerA','sellerC','sellerE'],
    'b':['sellerC','sellerD','sellerA',],
    'c':['sellerA','sellerB'],
    # 'd':[],
    # 'e':[],
    }
# sellers = ["seller" + chr(x) for x in range(65, 65+len(buyers)*3)]
sellersPref = {
    'sellerA': ['c', 'b', 'a'],
    'sellerB': ['b', 'c', 'a'],
    'sellerC': ['a', 'c', 'b'],
    'sellerD': ['c', 'a', 'b'],
    'sellerE': ['b', 'a', 'c'],
    'sellerF': ['a', 'b', 'c'],
    'sellerG': ['a', 'c', 'b'],
    'sellerH': ['b', 'a', 'c'],
    }


#===========================================================

def matcher(buyerPref,sellerPref):
    matchBuyer = {}
    matchSeller = {}
    
    #set up buyers and sellers
    for buyer in buyerPref.keys():
        matchBuyer[buyer] = Customer(buyerPref[buyer])
    
    for seller in sellerPref.keys():
        matchSeller[seller] = Vendor(sellerPref[seller])
    
    
    for seller in matchSeller.keys():
        nowSeller = matchSeller[seller]
        counter = 1
        
        while not nowSeller.matched:
            for cust in nowSeller.prefs:
                nowSeller.visited.append(cust)
                nowCust = matchBuyer[cust]
                if not nowCust.full:
                    nowCust.addMatch(seller)
                    nowSeller.addMatch(cust)
                elif nowCust.full:
                    if nowCust.isPref(seller):
                        if nowCust.full:
                            delSeller = nowCust.removeNonPref()
                            matchSeller[delSeller].removeMatch()
                        nowCust.addMatch(seller)
                        nowSeller.removeMatch()
                        nowSeller.addMatch(cust)
                else:
                    break
            
            #now look through other buyers
            for cust in matchBuyer.keys():
                nowCust = matchBuyer[cust]
                if cust not in nowSeller.visited:
                    if not nowCust.full:
                        nowCust.addMatch(seller)
                        former = nowSeller.removeMatch(self)
                        matchBuyer[former].removeMatch(seller)
                        nowSeller.addMatch(cust)
            
    
    #print results
    for k in matchBuyer.keys():
        matchBuyer[k].seeAttr
    
    for k in matchSeller.keys():
        matchSeller[k].seeAttr
        
    
    
matcher(buyersPref, sellersPref)