"""Explicit main execution module."""

from getpass import getpass
from homeInventory import HomeInventory
from inventoryApp import InventoryApp


def main():
	"""Execute main program."""
	#password = getpass('Enter DB Password: ')
	home_inventory_app = InventoryApp()
	home_inventory_app.start_Application()


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()
