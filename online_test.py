#To be continued 


class User:
    userID = 2341
    def __init__(self, username, email, password, address):
        self.username = username
        self.email = email
        self.password = password
        self.address = address
        self.cart = {}
        self.userId = User.userID
        User.userID += 1
    
    def set_user(self, new_username, new_email, new_password, new_address):
        self.username = new_username
        self.email = new_email
        self.password = new_password
        self.address = new_address

    def get_user(self):
        return self.userId, self.username, self.email, self.password, self.address

    def viewProducts(self):
         products = {'Clothes':'$69.99', 'Bags' :'$123.45', 'Food items':'$8.67', 'Books and Stationery' :'$149.84', 'Shoes':'$97.89', 'Accessories':'$95.23', 'Electrical Appliances': '$1236.99'}
         print('__Available products__ ')
         for i, product in enumerate(products, 1):
            print(f"{i}.{product}",products[product], sep =':')

    def addToCart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def viewCart(self):
        for product, quantity in self.cart.items():
            print(f"Product: {product}, Quantity: {quantity}")

class ShoppingCartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

   # def prod_uct(self) :
    #    self.product = []
    
    #def quant_ity(self) :
    #    self.quantity =[]
    
    


class Product: 
    def __init__(self):
        self.products = {
            'Clothes':'$69.99', 
            'Bags':'$123.45',
            'Food items':'$8.67', 
            'Books and Stationery':'$149.84' , 
            'Shoes':'$97.89',
            'Accessories':'$95.23',
            'Electrical Appliances':'$1236.99'}
        



class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.items = []
        self.total_amount = 0.0

    def calculateTotalPrice(self):
        for cart_item in self.items:
             if cart_item.product in self.user.products:
                self.total_amount += self.user.products[cart_item.product] * cart_item.quantity
        self.total_amount += cart_item.product.price * cart_item.quantity

class Checkout:
    def __init__(self, order):
        self.order = order

    def payprocess(self):
        try :
            while True:
                alert = int(input('Which payment method will you use?\n1 - Momo\n2 - Credit Card\n: '))
                if alert == 1 :
                    message = input('Give your momo number: ')
                    total = self.order.calculateTotalPrice()
                    print(f"Payment for ${total:.2f} will be deducted from {message}")
                    return True
                elif alert == 2:
                    message = input("Give your card details: ")
                    total = self.order.calculateTotalPrice()
                    print(f'Payment for ${total:.2f} will be deducted from {message}')
                    return True
                else:
                    print("Invalid choice, try again")
        except ValueError:
            print("Not valid")
            return False

    def complete_order(self):
        if self.payprocess():
            return f"Order placed successfully. Total amount: ${self.order.total_amount:.2f}"
        else:
            return "Payment processing failed. Order not placed."

class Payinfo:
    def __init__(self, paymethod, momo_number, card_number):
        self.paymethod = paymethod
        self.momo_number = momo_number
        self.card_number = card_number


def main():
    # Create a user
    user = User("John Doe", "johndoe@example.com", "password123", "123 Main St")

    # User views products
    user.viewProducts()

    # User adds items to the cart
    user.addToCart("Clothes", 3)
    user.addToCart("Shoes", 2)

    # User views the cart
    user.viewCart()

    # User places an order
    order = Order(1, user)
    order.items.append(ShoppingCartItem("Clothes", 3))
    order.items.append(ShoppingCartItem("Shoes", 2))

    checkout = Checkout(order)

    # User completes the order
    print(checkout.complete_order())


if __name__ == "__main__":
    main()
