class SaveRegistration:
    def __init__(self, username, password):
        self.username= username
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password


class Group_c:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

    def set_group_id(self, group_id):
        self.group_id = group_id

    def get_group_id(self):
        return self.group_id

    def set_group_name(self, group_name):
        self.group_name = group_name
    def get_group_name(self):
        return self.group_name


class Product_c:
    def __init__(self, product_Id, product_name, price, min_stock, max_stock, group_id):
        self.product_Id = product_Id
        self.product_name = product_name
        self.price = price
        self.min_stock = min_stock
        self.max_stock = max_stock
        self.group_id = group_id

    def get_group_id(self):
        return self.group_id

    def set_group_id(self, group_id):
        self.group_id = group_id

    def get_product_Id(self):
        return self.product_Id
    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_product_name(self, product_name):
        self.product_name = product_name
    def get_product_name(self):
        return self.product_name

    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price

    def set_min_stock(self, min_stock):
        self.min_stock = min_stock
    def get_min_stock(self):
        return self.min_stock

    def set_max_stock(self, max_stock):
        self.max_stock = max_stock
    def get_max_stock(self):
        return self.max_stock




