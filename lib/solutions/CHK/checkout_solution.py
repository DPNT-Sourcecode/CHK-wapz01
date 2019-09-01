

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    allowed_skus = "ABCD"

    price_for_sku = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    sku_map = {}
    for x in skus:
        if x in allowed_skus:
            sku_map = {x: skus.count(x)}
        else:
            return -1
            
    total_checkout = 0
    for sku, num in sku_map.items():
        
        # discounts
        if sku == "A" and num == 3:
            total_checkout = num * 130
        
        if sku == "B" and num == 3:
            total_checkout = num * 130
        
        #total_checkout = num * price_for_sku[sku]

    return total_checkout
    

print(checkout("AAA"))
# - {"method":"checkout","params":[""],"id":"CHK_R1_002"}, expected: 0, got: -1
# - {"method":"checkout","params":["ABCa"],"id":"CHK_R1_009"}, expected: -1, got: 20
# - {"method":"checkout","params":["AxA"],"id":"CHK_R1_010"}, expected: -1, got: 100