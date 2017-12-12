class Product(object):
    def __init__(self, price, item_name, weight, brand, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.display_info()


    def sell(self):
        self.status = "sold"
        return self


    def add_tax(self, tax):
        sales_price = (self.price * tax) + self.price
        return sales_price


    def return_product(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "like new":
            self.status = "for sale"
        elif reason == "open box":
            self.status = "open box"
            self.price = self.price - (self.price * 0.20)
        return self


    def display_info(self):
        print "Price:", self.price
        print "Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self


p1 = Product(25, "Bluetooth mouse", 50, "Logitech")




