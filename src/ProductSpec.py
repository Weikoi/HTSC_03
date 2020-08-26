class ProductSpec(object):

    def __init__(self, prop_dict):
        self.prop_dict = prop_dict

    def get_prop(self, prop_name):
        return self.prop_dict[prop_name]

    def get_all_props(self):
        return self.prop_dict.items()

    # SRP 应用
    def match(self, other_spec):
        for k, v in other_spec.get_all_props():
            if self.prop_dict[k] != other_spec.get_prop(k):
                return False
        return True


class ComputerSpec(ProductSpec):
    def __init__(self, prop_dict):
        ProductSpec.__init__(self, prop_dict)


class DesktopSpec(ProductSpec):
    def __init__(self, prop_dict):
        ProductSpec.__init__(self, prop_dict)


class ServerSpec(ProductSpec):
    def __init__(self, prop_dict):
        ProductSpec.__init__(self, prop_dict)
