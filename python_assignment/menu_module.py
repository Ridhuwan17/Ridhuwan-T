def menu_boba():
    print("Welcome to Booba T!")
    print("Take a look at our menu and order by typing the desired alphabet!")
    
    menu_items = {
        "Milk Teas": [
            "(A) Original Pearl Milk Tea \t \t \t \t \t \t RM7.00",
            "(B) Signature Brown Sugar Pearl Milk Tea \t \t \t RM7.00",
            "(C) Classic Roasted Milk Tea with Grass Jelly \t RM7.00",
            "(D) Signature Milk Tea \t \t \t \t \t \t \t RM6.00"
        ],
        "Fruit Teas": [
            "(E) Passionfruit Green Tea \t RM8.00",
            "(F) Peach Oolong Tea \t \t \t RM8.00",
            "(G) Lychee Black Tea \t \t \t RM8.00",
            "(H) Grapefruit Green Tea \t \t RM8.50"
        ],
        "Coffee": [
            "(I) Signature Coffee \t RM9.00",
            "(J) Hazelnut Latte \t RM10.20",
            "(K) Americano \t \t RM10.00",
            "(L) Cappucino \t \t RM10.00",
            "(M) Mocha \t \t \t RM11.00"
        ]
    }

    max_name_length = max(len(item) for items in menu_items.values() for item in items)

    print("~" * (max_name_length + 12))
    print(f"{'Beverage':^{max_name_length + 2}}")
    print("~" * (max_name_length + 12))

    for category, items in menu_items.items():
        print(f"\n{category}:")
        for item in items:
            print(f"- {item:<{max_name_length}}")

    print("~" * (max_name_length + 12))
