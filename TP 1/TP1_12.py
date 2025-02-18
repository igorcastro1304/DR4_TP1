products_list = ["banana", "apple", "orange", "cider", "vinegar", "tangerine", "mango"]
products_set = set(products_list)

def check_disponibility(product_name):
    if product_name in products_set:
        print(f"O produto {product_name} está disponível no estoque")
    else:
        print(f"O produto {product_name} não está disponível no estoque")

check_disponibility("apple")
check_disponibility("wine")