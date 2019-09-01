

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    allowed_skus = "ABCDE"

    price_for_sku = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    sku_map = {}
    for x in skus:
        if x in allowed_skus:
            sku_map[x] = skus.count(x)
        else:
            return -1
            
    total_checkout = 0
    discount = 0
    for sku, num in sku_map.items():
        
        if sku == "A" and num >= 5:
            discount = 200 * (num // 5)
            if (num % 5) != 0:
                num_price = price_for_sku[sku] * (num % 5)
                total_checkout = total_checkout + discount + num_price
            else:
                total_checkout = total_checkout + discount
        
        elif sku == "A" and num >= 3:
            discount = 130 * (num // 3)
            if (num % 3) != 0:
                num_price = price_for_sku[sku] * (num % 3)
                total_checkout = total_checkout + discount + num_price
            else:
                total_checkout = total_checkout + discount
    
        elif sku == "B" and num >= 2:
            discount = 45 * (num // 2)
            if (num % 2) != 0:
                num_price = price_for_sku[sku] * (num % 2)
                total_checkout = total_checkout + discount + num_price
            else:
                total_checkout = total_checkout + discount
        else:
            total_checkout = total_checkout + price_for_sku[sku] * num

    return total_checkout
