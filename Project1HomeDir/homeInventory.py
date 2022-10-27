"""Implements Home Inventory data structures and operations."""


import json
from datetime import date
from operator import index

# Backend
class HomeInventory():
    def __init__(self):
        """Initialize Home Inventory object."""
        self._Initialize_Home_Inventory_Dictionary()
        

    def new_inventory(self):
        """Initializing new dictionary to store inventory data based on input"""
        if(self.dictionary != None) and (bool(self.dictionary)):
            user_input = input('Save current inventory? (y/n): ')
            match user_input.lower():
                case 'y':
                    self.save_inventory()
                    self._Initialize_Home_Inventory_Dictionary()
                case 'n':
                    self._Initialize_Home_Inventory_Dictionary()
                case _:
                    self._Initialize_Home_Inventory_Dictionary()
        else:
            self._Initialize_Home_Inventory_Dictionary()
    
    def load_inventory(self):
        """User loads inventory from file"""
        try:
            file_path = self._get_file_path()
            """With is safe (this is for future refrence)"""
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.dictionary = json.loads(f.read())
        except OSError:
            print('Problem loading file. Please try again :)')
            
    def save_inventory(self):
        """Saves current inventory to file"""
        if self.dictionary != None:
            file_path = self._get_file_path()
            """again this is the safe way to open files!!!"""
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(json.dumps(self.dictionary))
    
    def search_inventory(self):
        """Searches current inventory based on user input"""
        searched = input('Enter item name: ')
        

    def list_inventory(self):
        for key, value in self.dictionary.items():
            if key == 'items':
                print('items:')
                for item in value:
                    print(f'\t {item["item"]:10} \t {item["count"]}')
            else:
                print(f'{key}: \t {value}')
    
    def add_items(self, item_name, item_count):
        assert self.dictionary != None
        self.dictionary['items'].append({'item': item_name, 'count': int(item_count)})

    def _get_file_path(self):
        """Gets file path from user"""
        f_path = input("Please enter path and filename: ")
        return f_path
    
    def _Initialize_Home_Inventory_Dictionary(self):
        self.dictionary = {}
        self.dictionary['type'] = 'Home Inventory'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['items'] = []
        if __debug__:
            print("New Home Inventory Initialized")