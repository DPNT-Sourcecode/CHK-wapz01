

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
            
    if len(sku_map) == 0:
        return -1

    total_checkout = 0
    for sku, num in sku_map.items():
        # check for discounts.
        total_checkout = num * price_for_sku[sku]

    return total_checkout