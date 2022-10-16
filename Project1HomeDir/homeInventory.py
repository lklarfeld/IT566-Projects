"""Implements Home Inventory data structures and operations."""

import json
from datetime import date

# Backend
class HomeInventory():
    def __init__(self):
        """Initialize Home Inventory object."""
        self._Initialize_Home_Inventory_Dictionary()



    def _get_file_path(self):
        """Gets file path from user"""
        #f_path
    
    def _Initialize_Home_Inventory_Dictionary(self):
        if __debug__:
            print("Initializing new Home Inventory...")
        self.dictionary = {}
        self.dictionary['type'] = 'Home Inventory'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['items'] = []
        if __debug__:
            print("New Home Inventory Initialized")