class Product:
    
    def __init__(self, name:str, brand:str, stock:int, price:float):
        self.name = name
        self.stock = stock
        self.price = price
        self.brand = brand

    def __str__(self):
        return f"Name: {self.name}, Brand: {self.brand}, Stock: {self.stock}, Price: {self.price}€"