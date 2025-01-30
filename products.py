class Product:
    
    '''
    Product's builder

    Parameters:
    - name (str): its the name of the product
    - brand (str): its the brand of the product
    - stock (int): its the quantity of products that we have in the warehouse
    - price (float): its the price of the product

    Attributes:
    - self.name: its the same as name (parameters)
    - self.stock: its the same as stock (parameters)
    - self.price: its the same as price (parameters)
    - self.brand: its the same as brand (parameters)
    '''
    def __init__(self, name:str, brand:str, stock:int, price:float):
        self.name = name
        self.stock = stock
        self.price = price
        self.brand = brand

    '''
    __str__ Method

    This method returns a str chain
    '''
    def __str__(self):
        return f"Name: {self.name}, Brand: {self.brand}, Stock: {self.stock}, Price: {self.price}€"
    
    def getName(self):
        return self.name