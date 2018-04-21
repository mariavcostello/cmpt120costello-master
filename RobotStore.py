#Maria Costello
#Intro to Programming
#Lab 9

productNames = [ "Ultrasonic range finder"
 , "Servo motor"
 , "Servo controller"
 , "Microcontroller Board"
 , "Laser range finder"
 , "Lithium polymer battery"
 ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def stock(self, count):
        if self.quantity >= int(count):
            return True
        else:
            return False

    def cost(self,count):
        cost = int(count) * self.price
        return cost

    def quantity(self,count):
        self.quantity = self.quantity - int(count)
        return self.quantity
        

        
def printStock(products):
    print()
    print("Available Products")
    print("------------------")
    n = 0
    for p in products:
        if p.quantity > 0:
            print(n, p.name, "$", p.price)
        n += 1
    print()
    
def main():
    products = [
        Product("Ultrasonic range finder", 2.50, 4),
        Product("Servo motor", 14.99, 10),
        Product("Servo controller", 44.95, 5),
        Product("Microcontroller Board", 34.95, 7),
        Product("Laser range finder", 149.99, 2),
        Product("Lithium polymer battery", 8.99, 8)
        ]

    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock(products)
        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodId = int(vals[0])
        product = products[prodId]
        count = int(vals[1])

        if product.stock(count):
            if cash >= product.cost(count):
                product.quantity(count)
                cash -= product.cost(count)
                print ("You purchased", count, product.name+".")
                print ("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.name)

main()
