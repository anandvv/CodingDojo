from Product import Product

class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner


    def add_product(self, product):
        self.products.append(product)
        return self

    
    def remove_product(self, productName):
        i = 0
        found = False

        for product in self.products:
            if product.item_name == productName:
                found = True
                break
            i += 1

        if found == True:
            del self.products[i]

        return self


    def inventory(self):
        for product in self.products:
            print product.item_name
            print product.price
            print " "


p1 = Product(25, "Bluetooth mouse", 50, "Logitech")
p2 = Product(10, "Mousepad", 20, "Microsoft")
p3 = Product(15, "Trackpad", 30, "Zen Design")

s = store([p1, p2], "San Jose", "Shak")
s.add_product(p3)
s.inventory()
s.remove_product("Mousepad")
print "===================="
s.inventory()





