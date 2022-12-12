# Louis Klarfeld
# This code is academic work and not to be used commercially
# 10/31/22
"""Implements Home Inventory data structures and operations."""


import json
import mysql.connector
from mysql.connector import connect, Error
from datetime import date
from operator import index

# Backend
class HomeInventory():
    def __init__(self, db_host, db_port, db_name, db_user_name, db_password):
        """Initialize object properties."""
        # Fields
        self._db_port = db_port
        self._db_name = db_name
        self._db_host = db_host
        self._db_user_name = db_user_name
        self._db_password = db_password
        self.db_connection = None
		# Constants
        self.SELECT_ALL = 'SELECT id, item, count FROM items'
        self.SELECT = 'SELECT * FROM items WHERE item = %s'
        self.INSERT = 'INSERT INTO items (item, count) VALUES(%s, %s)'
        self.CREATE = 'CREATE TABLE `newitems` (`id` int(11) NOT NULL, `item` varchar(11) NOT NULL, `count` int(11) NOT NULL)'
                
        

    def new_inventory(self):##, table, columns):
        """Initializing new dictionary to store inventory data based on input"""
        try:
            with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
                cursor = connection.cursor()
                cursor.execute(self.CREATE)
                cursor.close()
        except Error as e:
            print(e)


    def export_inv(self):
        """Exports database to file"""
        try:
            with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
                cursor = connection.cursor()
                cursor.execute(self.SELECT_ALL)
                results = cursor.fetchall()
                cursor.close()
        except Error as e:
            print(e)
        try:
            f_path = input("Please enter path and filename: ")
            with open(f_path, 'w', encoding='UTF-8') as f: 
                f.write(json.dumps(results))
        except Error as e:
            print(e)
            
    def save_inventory(self):
        """Saves current inventory"""
        try:
            with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
                cursor = connection.cursor()
                connection.commit()
                cursor.close()
        except Error as e:
            print(e)
    
    def search_inventory(self, items):
        """Searches current inventory based on user input"""
        try:
            with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
                cursor = connection.cursor()
                cursor.execute(self.SELECT, (items,))
                print(cursor.fetchall())
                cursor.close()
        except Error as e:
            print(e)

    def list_inventory(self):
        """Displays Inventory"""
        try:
            with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
                cursor = connection.cursor()
                cursor.execute(self.SELECT_ALL)
                results = cursor.fetchall()
                cursor.close()
        except Error as e:
            print(e)
        print(results)

    
    def add_items(self, item, count):
        try:
            with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
                cursor = connection.cursor()
                cursor.execute(self.INSERT, (item, count))
                connection.commit()
                cursor.close()
        except Error as e:
            print(e)