def search_employees(employees, query):
    """
    Search employees by name, returning only active ones.

    Args:
        employees (list of dict): List with 'name' and 'active' fields.
        query (str): Name or partial name to search.

    Returns:
        list of dict: List of active employees matching the query.
    """
    query = query.lower()
    return [
        emp for emp in employees
        if query in emp['name'].lower() and emp['active']
    ]

# Example
employees = [
    {'name': 'Alice Johnson', 'active': True},
    {'name': 'Bob Smith', 'active': False},
    {'name': 'Charlie', 'active': True}
]

print(search_employees(employees, 'ali'))
