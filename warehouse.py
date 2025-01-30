from products import Product


class Warehouse:

    
    def __init__(self):
        '''
        Warehouse builder

        Attributes:
        - cpu0: its an object of the product's class. Category (Key): Cpu
        - cpu1: its an object of the products's class. Category (Key): Cpu
        - gpu0: its an object of the product's class. Category (Key): Gpu
        - moth0: its an object of the product's class. Category (Key): Motherboards
        - ram0: its an object of the product's class. Category (Key): Ram

        - self.products: its a dictionary. The keys are the categories of the products and the values are the objects of the product's class
        '''
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
        
        
    
    
    def add(self, category:str, product:Product):
        '''
        Add method

        This method add a product in the dictionary.

        Paremeters:
        - category (str): its the category of the product. This is the key of the dictionary
        - product (Product): its the product object, contains all the information (name, brand, stock, price)
        '''
        found = False
        i = 0
        while not found and i != len(self.products[category]):
            if self.products[category][i].getName() != product.getName():
                i+=1
            else:
                print("Can't add the same product twice")
                found = True

        if not found:
            self.products[category].append(product)
            print("Product added")

        for i in self.products[category]:
            print(i)

    def remove(self):
        pass # A futuro
    
    
    def show_products(self):
        '''
        Show_products method

        This method shows you completetly the dictionary
        '''
        
        for i in self.products:
            print("─────────────────────────────────────────────────────────────────────────────────")
            print(f"{i}: ")
            print("")
            for j in self.products[i]:
                print(j)
        print("─────────────────────────────────────────────────────────────────────────────────")
    
   
    def search_product(self, category:str, name:str):
        '''
        Search_product method

        This method search a product in own warehouse, with the user category and name

        Parameters:
        - category (str): its the product category, its useful to search easily the product
        - name (str): its the product name, its useful to locate easily the product
        '''
        for key in self.products.keys():
            if (category.lower() != key.lower()):
                print("Category isn't correct")
                input()
                break
            else:
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
    
    
    def update_product(self, category:str):
        '''
        Update_product method

        This method update the stock or the price for a product in specific

        Parameters:
        - category (str): its the product category, its useful to search easily the product
        '''
        for key in self.products.keys():
            if(category.lower() != key.lower()):
                print("Category isn't correct")
                input()
                return
            else:
                print("Category's correct")
                name = input("What product do you want to update?")
                for product in self.products[key]:
                    if(name.lower() != product.getName().lower()):
                        print("The product hasn't been located")
                        input()
                        return
                    else:
                        print("Do you want to update the stock (1) or the price (2)")
                        option = input("SELECT: ")
                        match option:
                            case "1":
                                stock = int(input("What's the new stock?: "))
                                product.setStock(stock)
                                print(f"The stock has been updated. Stock: {product.getStock()}")
                                input()
                                return 
                            case "2":
                                price = float(input("What's the new price?: "))
                                product.setPrice(price)
                                print(f"The price has been updated. Price: {product.getPrice()}€")
                                input()
                                return 
                            case _:
                                print("This option isn't correct, please try again")
