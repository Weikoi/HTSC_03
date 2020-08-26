from Product import *


class Inventory(object):
    def __init__(self):
        self.inventory_list = []

    def __repr__(self):
        return self.inventory_list

    # def add_inventory(self, serial_number, spec):
    #     product = Product(serial_number, spec)
    #     self.inventory_list.append(product)

    def add_inventory(self, product):
        self.inventory_list.append(product)

    def get_product(self, serial_number):
        for product in self.inventory_list:
            if product.get_serial_number() == serial_number:
                return product
        return None

    def search(self, product_spec):
        match_list = []
        for product in self.inventory_list:
            if product.get_spec().match(product_spec):
                match_list.append(product)
        return match_list
