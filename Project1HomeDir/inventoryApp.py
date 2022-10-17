"""Implements household inventory control features."""

from typing_extensions import Self
from homeInventory import HomeInventory
from subprocess import call
import os

# Frontend
class InventoryApp():

    def __init__(self):
        """Initializing objects"""
		# Constants
        self.NEW_INVENTORY='1'
        self.LOAD_INVENTORY='2'
        self.LIST_INVENTORY='3'
        self.ADD_ITEMS='4'
        self.SAVE_INVENTORY='5'
        self.SEARCH_INVENTORY='6'
        self.EXIT='7'
		# Fields
        self.menu_choice = 1
        self.keep_going = True
        self.home_inventory = HomeInventory()
        pass
        

    def clear_System(self):
        os.system('cls')

    def display_Menu(self):
        """Displaying the menu"""
        print('\t\t\tHousehold Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. List Inventory')
        print('\t\t4. Add Items')
        print('\t\t5. Save Inventory')
        print('\t\t6. Search Inventory')
        print('\t\t7. Exit')
        print()
        
    def process_Menu_Choices(self):
        """Process menu choices and execute corresponding methods"""
        self.menu_choice = input('Please enter menu item number: ')
        if __debug__:
            print(f'You entered: {self.menu_Choice}')
        match self.menu_choice:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.LOAD_INVENTORY:
                self.load_inventory()
            case self.LIST_INVENTORY:
                self.list_inventory()
            case self.ADD_ITEMS:
                self.add_items()
            case self.SAVE_INVENTORY:
                self.save_inventory()
            case self.EXIT:
                if __debug__:
                    print('Bye!')
                self.keep_going = False
                self.clear_System
            case _:
                print('Non-valid choice!')
                
    def new_inventory(self):
        """User creates a new inventory"""
        if __debug__:
            print('new_inventory() called')
        self.home_inventory.new_inventory()
        input('Press any key to continue...')
        self.clear_System()
        
    def load_inventory(self):
        if __debug__:
            print('load_inventory() called')
        self.home_inventory.load_inventory()
        input('Press any key to continue...')
        self.clear_System()
        
    def list_inventory(self):
        if __debug__:
            print('list_inventory() called')
        self.home_inventory.list_inventory()
        input('Press any key to continue...')
        self.clear_System()
        
    def save_inventory(self):
        if __debug__:
            print('save_inventory() called')
        self.home_inventory.save_inventory()
        input('Press any key to continue...')
        self.clear_System()
    
    def search_inventory(self):
        if __debug__:
            print('search_inventory() called')
        self.home_inventory.search_inventory()
        input('Press any key to continue...')
        self.clear_System()
        
    def add_items(self):
        if __debug__:
            print('add_items() called')
            keep_going = 'y'
        while keep_going[0] == 'y':
            item_name = input('Item name: ')
            item_count = input('Item count: ')
            self.home_inventory.add_items(item_name, item_count)
            keep_going = input('Add another (y/n): ')

    def start_Application(self):
        """Starts the application"""
		# Clear Screen
        while self.keep_going:
            self.clear_System()
            self.display_Menu()
            self.process_Menu_Choices()
