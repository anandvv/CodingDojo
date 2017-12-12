class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Bike's price: {}".format(self.price)
        print "Max Speed: {}".format(self.max_speed)
        print "Miles: {}".format(self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self


bike1 = Bike(10000, 250, 2500)
bike2 = Bike(20000, 300, 100)
bike3 = Bike(15000, 275, 500)

bike1.ride().ride().ride().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()


