def search_products(products, query, min_stock=10):
    """
    Search for products matching the query and enforce a minimum stock threshold.

    Args:
        products (list of dict): List of products with 'name' and 'stock'.
        query (str): Keyword to search in product names.
        min_stock (int): Minimum stock required to include the product.

    Returns:
        list of dict: Filtered product list.
    """
    query = query.lower()
    result = []

    for product in products:
        if query in product['name'].lower() and product['stock'] >= min_stock:
            result.append(product)

    return result

# Example
products = [
    {'name': 'Apple iPhone 15', 'stock': 20},
    {'name': 'Samsung Galaxy', 'stock': 5},
    {'name': 'Google Pixel', 'stock': 15}
]

print(search_products(products, "iphone"))
