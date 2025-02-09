class Product:
    
    def __init__(self, name:str, brand:str, stock:int, price:float):
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
        self.name = name
        self.stock = stock
        self.price = price
        self.brand = brand

    
    def __str__(self):
        '''
        __str__ Method

        This method returns a str chain
        '''
        return f"Name: {self.name}, Brand: {self.brand}, Stock: {self.stock}, Price: {self.price}€"
    
    
    def getName(self) -> str:
        '''
        getName Method

        This method returns the product name
        '''
        return self.name
    
   
    def getStock(self):
        '''
        getStock Method

        This method return the product stock
        '''
        return self.stock

    def addStock(self, n:int):
        '''
        addStock Method

        This method adds the stock a given number
        '''
        self.stock += n

    def sellStock(self, n:int):
        '''
        sellStock Method

        This method removes the stock by a given number
        '''
        self.stock -= n
    
    def getPrice(self):
        '''
        getPrice Method

        This method return the product price
        '''
        return self.price
    
    
    def setStock(self, stock:int):
        '''
        setStock Method

        This method set a new stock in the product

        Paramaters:
        - stock (int): its the new stock
        '''
        self.stock = stock
    
    
    def setPrice(self, price:float):
        '''
        setPrice Method

        This method set a new price in the product

        Parameters:
        - price (float): its the new price
        '''
        self.price = price