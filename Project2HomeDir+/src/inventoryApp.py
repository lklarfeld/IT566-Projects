# Louis Klarfeld
# This code is academic work and not to be used commercially
# 10/31/22
"""Implements household inventory control features."""

from homeInventory import HomeInventory
from subprocess import call
import os

# Frontend
class InventoryApp():

    def __init__(self):
        """Initializing objects"""
		# Constants
        self.NEW_INVENTORY='1'
        self.EXPORT_INV='3'
        self.LIST_INVENTORY='6'
        self.ADD_ITEMS='4'
        self.SAVE_INVENTORY='2'
        self.SEARCH_INVENTORY='6'
        self.EXIT='7'
		# Fields
        self.menu_choice = 1
        self.keep_going = True
        self.home_inventory = HomeInventory()
        self.password = None 
        pass
        

    def clear_System(self):
        os.system('cls')

    def display_Menu(self):
        """Displaying the menu"""
        print('\t\t\tHousehold Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Save Inventory')
        print('\t\t3. Export Inventory to File')
        print('\t\t4. Add Items')
        print('\t\t5. Search Inventory')
        print('\t\t6. Display Inventory')
        print('\t\t7. Exit')
        print()
        
    def process_Menu_Choices(self):
        """Process menu choices and execute corresponding methods"""
        self.menu_choice = input('Please enter menu item number: ')
        if __debug__:
            print(f'You entered: {self.menu_choice}')
        match self.menu_choice:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.EXPORT_INV:
                self.export_inv()
            case self.LIST_INVENTORY:
                self.list_inventory()
            case self.ADD_ITEMS:
                self.add_items()
            case self.SAVE_INVENTORY:
                self.save_inventory()
            case self.SEARCH_INVENTORY:
                self.search_inventory()
            case self.EXIT:
                print("Bye!!!")
                self.clear_System
                self.keep_going = False
            case _:
                print('Non-valid choice!')
                
    def new_inventory(self):
        """User creates a new inventory"""
        if __debug__:
            print('new_inventory() called')
        db_test = HomeInventory('localhost', 3306, 'home_inventory', 'home_inventory_user', self.password)
        self.tablename = input('Input new table name: ')
        self.table = self.tablename
        self.more_keys = True
        while self.more_keys == True:
            self.column = input('Enter key name type (CHAR or INT) and character limit (example: item CHAR(20))')
            self.table += ", " + self.column
            keep_going = input('add another key? y/n')
            if keep_going == "n":
                self.more_keys == False
        db_test.new_inventory(self.table)
        input('Press Enter to continue...')
        self.clear_System()
        
    def export_inv(self):
        if __debug__:
            print('load_inventory() called')
        db_test = HomeInventory('localhost', 3306, 'home_inventory', 'home_inventory_user', self.password)
        db_test.export_inv()
        input('Press Enter to continue...')
        self.clear_System()
        
    def list_inventory(self):
        if __debug__:
            print('list_inventory() called')
        db_test = HomeInventory('localhost', 3306, 'home_inventory', 'home_inventory_user', self.password)
        db_test.list_inventory()
        input('Press Enter to continue...')
        self.clear_System()
        
    def save_inventory(self):
        if __debug__:
            print('save_inventory() called')
        db_test = HomeInventory('localhost', 3306, 'home_inventory', 'home_inventory_user', self.password)
        db_test.save_inventory()
        input('Press Enter to continue...')
        self.clear_System()
    
    def search_inventory(self):
        if __debug__:
            print('search_inventory() called')
        db_test = HomeInventory('localhost', 3306, 'home_inventory', 'home_inventory_user', self.password)
        item = input('Enter the name of the desired item: ')
        db_test.search_inventory(item)
        input('Press Enter to continue...')
        self.clear_System()
        
    def add_items(self):
        if __debug__:
            print('add_items() called')
            db_test = HomeInventory('localhost', 3306, 'home_inventory', 'home_inventory_user', self.password)
            keep_going = 'y'
        while keep_going[0] == 'y':
            item_name = input('Item name: ')
            item_count = input('Item count: ')
            db_test.add_items(item_name, item_count)
            keep_going = input('Add another (y/n): ')

    def start_Application(self):
        """Starts the application"""
		# Clear Screen
        while self.keep_going:
            self.clear_System()
            self.display_Menu()
            self.process_Menu_Choices()
