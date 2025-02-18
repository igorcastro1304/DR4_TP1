clothes_catalog = {
    "t-shirt": 29.99,
    "dress": 89.99,
    "skirt": 69.99,
    "pants": 99.99
}

sold_products = {}

def add_clothing_price(product_name, price):
    updated_price = {product_name: price}

    clothes_catalog.update(updated_price)

    print(f"Roupa {product_name} - R$ {price} atualizada com sucesso.") 

def sell_clothing(product_name, quantity):
    if product_name not in clothes_catalog:
        print(f"Produto {product_name} não encontrado na lista de preços.")
        return

    if product_name not in sold_products:
        sold_products[product_name] = 0

    sold_products[product_name] += quantity

    total_price = clothes_catalog[product_name] * quantity
    print(f"{quantity} {product_name}(s) vendidos(as) por R$ {total_price:.2f}.")

def calc_profit():
    profit = 0
    for product, quantity in sold_products.items():
        profit += clothes_catalog[product] * quantity
    return profit

def remove_clothing(product_name):
    clothes_catalog.pop(product_name)

    print(f"Produto {product_name} removido com sucesso.")

add_clothing_price("glasses", 89.99)
add_clothing_price("jacket", 199.99)
sell_clothing("t-shirt", 50)
sell_clothing("skirt", 25)
sell_clothing("glasses", 50)

profit = calc_profit()
print(f"O lucro das vendas foi $ {profit:.2f}")

remove_clothing("pants")
print(clothes_catalog)