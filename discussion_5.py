import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		the_stock = self.items[0].stock
		temp = self.items[0].name
		for item in self.items:
			if item.stock > the_stock:
				the_stock = item.stock
				temp = item.name
		return temp
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		the_price = self.items[0].price
		temp = self.items[0].name
		for item in self.items:
			if item.price > the_price:
				the_price = item.price
				temp = item.name
		return temp



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("a string a tring a ring"), 3)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		item_List = []
		item_List.append(self.item1)
		item_List.append(self.item2)
		item_List.append(self.item3)
		warehouse = Warehouse(item_List)
		warehouse.add_item(self.item5)
		self.assertEqual(warehouse.items[3], self.item5)

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		item_List = []
		item_List.append(self.item1)
		item_List.append(self.item2)
		item_List.append(self.item3)
		warehouse = Warehouse(item_List)
		max = warehouse.get_max_stock()
		self.assertEqual(max, "Water")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		item_List = []
		item_List.append(self.item1)
		item_List.append(self.item2)
		item_List.append(self.item3)
		warehouse = Warehouse(item_List)
		max = warehouse.get_max_price()
		self.assertEqual(max, "Beer")
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()