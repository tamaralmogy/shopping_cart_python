from item import Item
from errors import ItemAlreadyExistsError
from errors import ItemNotExistError

class ShoppingCart:
    
    def __init__(self):
        self.items = []
    
    def __iter__(self):
        
        self._index = 0
        return self

    def __next__(self):
        
        if self._index < len(self.items):
            current_item = self.items[self._index]
            self._index += 1
            return current_item
        else:
            raise StopIteration
    
    # Gets a flattened list of hastags of items in cart
    def get_hashtags(self):
        hashtag_list = [tag for item in self.items for tag in item.hashtags]
        return hashtag_list
    
    # Trys to add an item to shopping cart
    # If item already in cart, raises exception    
    def add_item(self, item: Item):
        if item in self.items:
            raise ItemAlreadyExistsError("Item already exists")
        
        else:
            self.items.append(item)
     
    # Trys to remove an item from shopping cart
    # If item not in cart, raises exception      
    def remove_item(self, item_name: str):
        for item in self.items:
            if item_name in item.name:
                self.items.remove(item)
                return
        else:
            raise ItemNotExistError("Item you are trying to remove does not exist") 
            
    
    # Returns the subtotal price of all the items currently in the shopping cart.
    def get_subtotal(self) -> int:
        return sum(item.price for item in self.items)
