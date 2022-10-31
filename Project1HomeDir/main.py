# Louis Klarfeld
# This code is academic work and not to be used commercially
# 10/31/22
"""Explicit main execution module."""
from inventoryApp import InventoryApp

def main():
	"""Execute when it's the main execution module."""
	home_inventory_app = InventoryApp()
	home_inventory_app.start_Application()



# Call main() if this is the main execution module
if __name__ == '__main__':
	main()