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

    search_spec_dict1 = {"screen_size": "15", "CPU": "Intel_low"}
    search_spec_dict2 = {"category":"game"}
    search_spec1 = ComputerSpec(search_spec_dict1)
    search_spec2 = ComputerSpec(search_spec_dict2)

    print("第一次检索结果：")
    print(inventory.search(search_spec1))
    print()
    print("第二次检索结果：")
    print(inventory.search(search_spec2))
