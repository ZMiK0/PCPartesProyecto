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
        cpu0 = Product("Ryzen7 5600G", "AMD", 7, 140.32)
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
        
    def show_category(self):
        '''
        Shows every category
        '''
        print("─────────────────────────────────────────────────────────────────────────────────")
        index = 0
        for i in self.products:
            print(f"{index}: {i}")
            index += 1
        print("─────────────────────────────────────────────────────────────────────────────────")

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
    
    def show_products(self):
        '''
        Show_products method

        This method shows you completetly the dictionary
        '''
        chain = ""
        for i in self.products:
            print("─────────────────────────────────────────────────────────────────────────────────")
            print(f"{i}: ")
            print("")
            for j in range(len(self.products[i])):
                chain += (f"{j}: {self.products[i][j]}\n")
        print("─────────────────────────────────────────────────────────────────────────────────")
        print(chain)
        return chain
    
   
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
        if category in self.products:
            print("Category found")
            
            print("─────────────────────────────────────────────────────────────────────────────────")
            for j in range(len(self.products[category])):
                print(f"{j}: {self.products[category][j]}")
            print("─────────────────────────────────────────────────────────────────────────────────")
            index = int(input("State the product you want to update (by index number): "))
            product = self.products[category][index]
            print("Do you want to update the stock (1) or the price (2)")
            option = input("SELECT: ")
            match option:
                case "1":
                    stock = int(input("What's the new stock?: "))
                    product.setStock(stock)
                    print(f"The stock has been updated. Stock: {product.getStock()}")
                    input()
                    return ""
                case "2":
                    price = float(input("What's the new price?: "))
                    product.setPrice(price)
                    print(f"The price has been updated. Price: {product.getPrice()}€")
                    input()
                    return ""
                case _:
                    print("This option isn't correct, please try again")
                    return ""
        else:
            print("Category not found")
            input()

    def remove_product(self, category:str):
        '''
        Remove product method

        Removes the product of a category by index

        Parameters:
        - category (str): The category
        '''
        if category in self.products:
            print("─────────────────────────────────────────────────────────────────────────────────")
            for j in range(len(self.products[category])):
                print(f"{j}: {self.products[category][j]}")
            print("─────────────────────────────────────────────────────────────────────────────────")
            
            index:int = int(input("State the product to remove (by index number): "))
            try:
                self.products[category].remove(self.products[category][index])
                print("Product removed succesfully")
            except:
                print("Product not found")
            input("")
            return ""
        else:
            print("Category not found")
            input("")
            return ""

    def filter_prices (self, price:float):
        '''
        Filter prices method

        Shows you the products that are lower than the user price

        Parameters:
        - price (float): The user price
        '''  
        for key in self.products.keys():
            for product in self.products[key]:
                if(price >= product.getPrice()):
                    print(f"---- {key} ----")
                    print(product)
                    input()
                else:
                    pass
    
    def shows_stats(self):
        '''
        Shows stats method

        Shows you the total warehouse value, the total warehouse stock, the cheapest product and the most expensive product
        '''
        total = 0
        for key in self.products.keys():
            for product in self.products[key]:
                total += product.getPrice()
        print("---- Total warehouse value ----")
        print(f"{total}€")
        input()

        stock = 0
        for key in self.products.keys():
            for product in self.products[key]:
                stock += product.getStock()
        print("---- Total warehouse stock ----")
        print(f"{stock} products")
        input()

        box = []
        price = []

        for key in self.products.keys():
            for product in self.products[key]:
                box.append(product.getName())
                price.append(product.getPrice())
        print("---- The cheapest product ----")
        print(f"{box[price.index(min(price))]}: {min(price)}€")
        input()

        print("---- The expensive product ----")
        print(f"{box[price.index(max(price))]}: {max(price)}€")
        input()


            

