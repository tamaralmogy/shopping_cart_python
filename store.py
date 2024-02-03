import yaml
from errors import TooManyMatchesError
from errors import ItemNotExistError
from item import Item
from shopping_cart import ShoppingCart

class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items
    
    # Returns the number of common hashtags of two lists
    # For use of func sorted in func search_by_name
    def common_hastags(self, l: list, m: list):
        total_sum = [l.count(x) for x in m if x in l]
        return sum(total_sum)
    
    # Returns a sorted list of item names not in shopping cart, that match the name given 
    def search_by_name(self, item_name: str) -> list:
        
        matching_list = [item for item in self._items if item not in self._shopping_cart.items if item_name in item.name]
        hashtags_shopping_cart = self._shopping_cart.get_hashtags()
        name_list = sorted(matching_list, key=lambda item: (-self.common_hastags(hashtags_shopping_cart,item.hashtags), item.name))

        return name_list

    # Returns a sorted list of item names not in shopping cart, that match the hashtag given 
    def search_by_hashtag(self, hashtag: str) -> list:
        matching_items = [item for item in self._items if item not in self._shopping_cart.items if hashtag in item.hashtags]
        hashtags_shopping_cart = self._shopping_cart.get_hashtags()
        hashtag_list = sorted(matching_items, key=lambda item: (-self.common_hastags(hashtags_shopping_cart,item.hashtags), item.name))

        return hashtag_list 
    
    # Adds an item from store to shopping cart
    def add_item(self, item_name: str):
        matching_item = [item for item in self._items if item_name in item.name]
        if len(matching_item) > 1:
            raise TooManyMatchesError
        if len(matching_item) == 0:
                raise ItemNotExistError
        else:
            self._shopping_cart.add_item(matching_item[0])

    # Removes an item from the shopping cart
    def remove_item(self, item_name: str): 
        matching_item = [item for item in self._shopping_cart if item_name in item.name]
        if len(matching_item) > 1:
            raise TooManyMatchesError
        if len(matching_item) == 0:
            raise ItemNotExistError
        else:
            self._shopping_cart.remove_item(matching_item[0].name)

    # Returns total sum of shopping cart
    def checkout(self) -> int:
        return self._shopping_cart.get_subtotal()
    

        
