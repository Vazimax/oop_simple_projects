class Order:

    def __init__(self,cart,customer):
            self.cart = cart
            self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __call__(self):
        print(str(self.customer))

    def __str__(self):
        return f"{self.customer} has bought : {self.cart}"

    def __repr__(self):
        return "Order(list of items , customer name)"

    def __bool__(self):
        return len(self.cart) > 0

    def __add__(self,other):
        self.cart.append(other)
        return self
    
    def __radd__(self,other):
        new_cart = self.cart.copy()
        new_cart.insert(5,other)
        return Order(new_cart,self.customer)

    def __getitem__(self,key):
        return self.cart[key]

    def __setitem__(self,key,value):
        self.cart[key] = value
        return self

order1 = Order(['books','laptops'],'Bakr El Habti')
order1 = 'mouse' + order1
order1[2] = 'VR'
print(order1.cart)
print(order1[1])



