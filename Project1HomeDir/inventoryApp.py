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
        self.menu_Choice = 1
        self.keep_Going = True
        self.home_Inventory = HomeInventory()
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
        print('\t\t7. Exit')
        print()

    def start_Application(self):
        """Starts the application"""
		# Clear Screen
        while self.keep_going:
            self.clear_screen()
            self.display_menu()
            self.process_menu_choice()