

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
            sku_map[x] = skus.count(x)
        else:
            return -1
            
    total_checkout = 0
    for sku, num in sku_map.items():
        # discounts
        if sku == "A" and num % 3 == 0:
            total_checkout = (num // 3) * 130
            continue
            
        if sku == "B" and num % 2 == 0:
            total_checkout = (num // 2) * 45
            continue
        
        total_checkout = total_checkout + (num * price_for_sku[sku])

    return total_checkout