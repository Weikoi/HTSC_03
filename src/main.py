from Product import *
from Inventory import *
from ProductSpec import *

if __name__ == '__main__':
    computer_spec_dict1 = {"brand": "ASUS", "price": "0-3999", "category": "game", "screen_size": "<11",
                           "CPU": "Intel_low"}
    computer_spec_dict2 = {"brand": "LENOVO", "price": "0-3999", "category": "light", "screen_size": "11",
                           "CPU": "Intel_low"}
    computer_spec_dict3 = {"brand": "ACER", "price": "0-3999", "category": "light", "screen_size": "14",
                           "CPU": "Intel_low"}
    computer_spec1 = ComputerSpec(computer_spec_dict1)
    computer_spec2 = ComputerSpec(computer_spec_dict2)
    computer_spec3 = ComputerSpec(computer_spec_dict3)

    inventory = Inventory()
    inventory.add_inventory(Computer(1, computer_spec1))
    inventory.add_inventory(Computer(2, computer_spec2))
    inventory.add_inventory(Computer(3, computer_spec3))

    search_spec = ComputerSpec(computer_spec_dict1)
    print(inventory.search(search_spec))
