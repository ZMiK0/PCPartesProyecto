from products import Product


class Warehouse:

    '''
    Warehouse's builder

    Attributes:
    - cpu0: its an object of the product's class. Category (Key): Cpu
    - cpu1: its an object of the products's class. Category (Key): Cpu
    - gpu0: its an object of the product's class. Category (Key): Gpu
    - moth0: its an object of the product's class. Category (Key): Motherboards
    - ram0: its an object of the product's class. Category (Key): Ram

    - self.products: its a dictionary. The keys are the categories of the products and the values are the objects of the product's class
    '''
    def __init__(self):
        cpu0 = Product("Ryzen 7 5600G", "AMD", 7, 140.32)
        cpu1 = Product("i7 12400H", "Intel", 8, 199.99)
        gpu0 = Product("Dual GeForce RTX 4060", "Asus", 5, 319.95)
        moth0 = Product("B760M D3HP DDR4", "Gigabyte", 3, 99.99)
        ram0 = Product("Vengeance DDR5 6000MHz 32GB", "Corsair", 70, 137.99)

        self.products = {
                "Cpu": [cpu0,cpu1],
                "Gpu": [gpu0],
                "Motherboards": [moth0],
                "Ram": [ram0]
                }
        
        
    
    '''
    Add's method

    This method add a product in the dictionary.

    Paremeters:
    - category (str): its the category of the product. This is the key of the dictionary
    - product (Product): its the product object, contains all the information (name, brand, stock, price)
    '''
    def add(self, category:str, product:Product):
        self.products[category].append(product)
        print("Product added")
        for i in self.products[category]:
            print(i)

    def remove(self):
        pass # A futuro
    
    '''
    Show_products's method

    This method shows you completetly the dictionary
    '''
    def show_products(self):
        
        for i in self.products:
            print("─────────────────────────────────────────────────────────────────────────────────")
            print(f"{i}: ")
            print("")
            for j in self.products[i]:
                print(j)
        print("─────────────────────────────────────────────────────────────────────────────────")
    
    '''
    Search_product's method

    This method search a product in own warehouse, with the user category and name
    '''
    def search_product(self, category:str, name:str):
        for key in self.products.keys():
            if (category.lower() == key.lower()):
                print("Category's correct")
                for product in self.products[key]:
                    if(name.lower() == product.getName().lower()):
                        print(f"The product has been located: {product}")
                        input()
                        break
                    else:
                        print("The product hasn't been located")
                        input()
                        break
                
                    
