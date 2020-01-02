class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    #def switch_on(self):

kenwood = Kettle("Kenwood101", 12.88)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 23.99
print(kenwood.price)

kenwood2 = Kettle("Kenwood201", 14.99)