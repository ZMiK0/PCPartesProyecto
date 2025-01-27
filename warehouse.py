from products import Product


class Warehouse:

    def __init__(self):
        self.products = {
                "cpu": ["ryzen7","i7"],
                "motheboards": ["Asus"]
                }
        
        
    product1 = Product("Ryzen 7", 7, 140.32)

    def add (self, product:Product):
        pass