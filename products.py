class Product:
    
    '''
    Product builder

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
    
    '''
    getName Method

    This method returns the product name
    '''
    def getName(self):
        return self.name
    
    '''
    getStock Method

    This method return the product stock
    '''
    def getStock(self):
        return self.stock
    
    '''
    getPrice Method

    This method return the product price
    '''
    def getPrice(self):
        return self.price
    
    '''
    setStock Method

    This method set a new stock in the product

    Paramaters:
    - stock (int): its the new stock
    '''
    def setStock(self, stock:int):
        self.stock = stock
    
    '''
    setPrice Method

    This method set a new price in the product

    Parameters:
    - price (float): its the new price
    '''
    def setPrice(self, price:float):
        self.price = price