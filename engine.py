from products import Product
from warehouse import Warehouse
import os


def clear():
    '''
    Clear method 

    This method cleans all your console
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Engine:
    '''
    Engine class

    This class contains the logic of the app
    '''

    
    def __init__(self):
        '''
        Engine builder

        Attribute:
        - warehouse: it's an object of the Warehouse's class
        '''
        self.warehouse = Warehouse()

    
   
    def menu(self):
        '''
        Menu method

        This method show you the app menu. Option 1: Show the inventory. Option 2: Add a product into the inventory. Option 3: Exit the app
        '''
        ok = False
        while not ok:
            clear()
            print("────────────────────────────────────")
            print("1. Show inventory \n2. Add product \n3. Search product \n4. Update product \n0. Exit ")
            print("────────────────────────────────────")
            option = input("SELECT: ")
            match option:
                case "1":
                    print("Inventory")
                    self.warehouse.show_products()
                    input()
                case "2":
                    print("Add product")
                    self.add_menu()
                case "3":
                    print("Search a product")
                    category = input("Please, say the product category: ")
                    name = input("Please, say the product name: ")
                    self.warehouse.search_product(category, name)
                case "4":
                    print("Update product")
                    category = input("Please, say the product category: ")
                    self.warehouse.update_product(category)
                case _:
                    print("Bye")
                    ok = True

  
    def add_menu(self):
        '''
        Add_menu method

        This method show you the options when you add a product in the inventory
        '''
        ok2 = False
        ok3 = False
        while not ok2:
            clear()
            print("────────────────────────────────────")
            print("1. Cpu\n2. Gpu\n3. Motherboards\n4. Ram\n0. Exit")
            print("────────────────────────────────────")
            option2 = input("SELECT: ")

            
            match option2:
                case "1":
                    category = "Cpu"
                case "2":
                    category = "Gpu"
                case "3":
                    category = "Motherboards"
                case "4":
                    category = "Ram"
                case _:
                    category = None
                    ok2 = True
                    break
            #Queda comprobar si hay elementos repes
            name = input("Name: ")
            brand = input("Brand: ")
            while(not ok3):
                stock = int(input("Stock: "))
                price = float(input("Price: "))
                if(stock <= 0 or price <= 0):
                    print("The stock and the price aren't negative numbers. Please try again")
                else:
                    ok3 = True
            print("────────────────────────────────────")
            product = Product(name, brand, stock, price)
            if category != None:
                self.warehouse.add(category, product)
                input()