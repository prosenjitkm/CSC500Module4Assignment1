# ItemToPurchase class
class ItemToPurchase:
    # Default constructor
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        # Initialize with default values
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

# Helper method for printing
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
        return total_cost

# Helper function to prompt for item details
def get_item_details(item_number):
    print(f"Item {item_number}")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    return ItemToPurchase(name, price, quantity)

# Main function
def main():

    item1 = get_item_details(1)
    item2 = get_item_details(2)

    print("\nTOTAL COST")
    total_cost = item1.print_item_cost() + item2.print_item_cost()
    print(f"\nTotal: ${total_cost}")

main()
