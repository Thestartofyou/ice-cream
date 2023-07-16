class IceCreamShop:
    def __init__(self, name):
        self.name = name
        self.menu = {}
        self.orders = []

    def add_flavor(self, flavor, price):
        self.menu[flavor] = price

    def remove_flavor(self, flavor):
        if flavor in self.menu:
            del self.menu[flavor]
        else:
            print(f"{flavor} is not available in the menu.")

    def place_order(self, customer_name, flavor, quantity):
        if flavor in self.menu:
            order = {
                "customer_name": customer_name,
                "flavor": flavor,
                "quantity": quantity,
                "total_price": self.menu[flavor] * quantity
            }
            self.orders.append(order)
            print(f"Order placed by {customer_name}: {quantity} {flavor} ice cream(s).")
            print(f"Total price: {order['total_price']}")
        else:
            print(f"Sorry, {flavor} is not available in the menu.")

    def list_orders(self):
        if self.orders:
            print("List of Orders:")
            for order in self.orders:
                print(f"Customer Name: {order['customer_name']}")
                print(f"Flavor: {order['flavor']}")
                print(f"Quantity: {order['quantity']}")
                print(f"Total Price: {order['total_price']}")
                print("-------------------")
        else:
            print("No orders placed yet.")

    def list_menu(self):
        if self.menu:
            print("Ice Cream Menu:")
            for flavor, price in self.menu.items():
                print(f"{flavor}: ${price}")
        else:
            print("No flavors available in the menu.")


# Example usage
shop = IceCreamShop("My Ice Cream Shop")

shop.add_flavor("Chocolate", 2.5)
shop.add_flavor("Vanilla", 2.0)
shop.add_flavor("Strawberry", 3.0)

shop.list_menu()

shop.place_order("John", "Chocolate", 2)
shop.place_order("Alice", "Vanilla", 1)
shop.place_order("Bob", "Mint", 3)

shop.list_orders()

shop.remove_flavor("Mint")
shop.remove_flavor("Strawberry")

shop.list_menu()
