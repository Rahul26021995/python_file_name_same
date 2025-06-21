def search_shipped_orders(orders, customer_name):
    """
    Search shipped orders by customer name.

    Args:
        orders (list of dict): Each dict has 'customer', 'order_id', 'status'.
        customer_name (str): Customer name to search.

    Returns:
        list of dict: Orders that match the customer and are shipped.
    """
    name = customer_name.lower()
    return [
        order for order in orders
        if name in order['customer'].lower() and order['status'] == 'Shipped'
    ]

# Example
orders = [
    {'order_id': 101, 'customer': 'John Doe', 'status': 'Shipped'},
    {'order_id': 102, 'customer': 'Jane Smith', 'status': 'Pending'},
    {'order_id': 103, 'customer': 'Johnny', 'status': 'Shipped'}
]

print(search_shipped_orders(orders, 'john'))
