class Product(object):

    def __init__(self, serial_number, spec):
        self.serial_number = serial_number
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_spec(self):
        return self.spec

    def __repr__(self):
        kv_str = ""
        for k, v in self.spec.get_all_props():
            kv_str += str(k)
            kv_str += ":"
            kv_str += str(v)
            kv_str += " "
        return "serial_num:" + str(self.serial_number) + " ===== " + kv_str


class Computer(Product):
    def __init__(self, serial_number, computer_spec):
        Product.__init__(self, serial_number, computer_spec)


class Desktop(Product):
    def __init__(self, serial_number, desktop_spec):
        Product.__init__(self, serial_number, desktop_spec)


class Server(Product):
    def __init__(self, serial_number, server_spec):
        Product.__init__(self, serial_number, server_spec)
