def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices
products = ["apple", "banana", "apple", "orange", "apple", "grape"]
target = "apple"
result = linear_search_product(products, target)
print(result)
