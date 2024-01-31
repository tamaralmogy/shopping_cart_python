from item import Item
from errors import ItemAlreadyExistsError, ItemNotExistError

class ShoppingCart:
    
    def __init__(self):
        self.items = []
        
    # Adds the given item to the shopping cart.
    # Arguments: the current instance of ShoppingCart and an instance of Item.
    # Exceptions: if the item name already exists in the shopping cart, raises ItemAlreadyExistsError.
    
    def add_item(self, item: Item):
        try:
            if any(existing_item.name == item.name for existing_item in self.items):
                raise ItemAlreadyExistsError("Item already exists in shopping cart")
            else:
                self.items.append(item)
        except ItemAlreadyExistsError as e:
            print(f"Caught an ItemAlreadyExistsError: {e}")
        
    # Removes the item with the given name from the shopping cart
    # Aguments: the current instance of ShoppingCart and an instance of str.
    # Exceptions: if no item with the given name exists, raises ItemNotExistError.
    def remove_item(self, item_name: str):
        try: 
            if item_name not in self:
                raise ItemNotExistError("Item you are trying to remove does not exist") 
            else:
                self.remove(item_name)
        except ItemNotExistError as e:
            print(f"Caught an ItemNotExistError: {e}")
    
    # Returns the subtotal price of all the items currently in the shopping cart.
    def get_subtotal(self) -> int:
        return sum(item.price for item in self)
