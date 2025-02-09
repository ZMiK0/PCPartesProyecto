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

        This method show you the app menu.
        '''
        ok = False
        while not ok:
            clear()
            print("────────────────────────────────────")
            print("1. Show inventory \n2. Add product \n3. Search product \n4. Update product \n5. Remove product \n6. Filter products by price \n7. Show stats\n8. NEW: Sale Simulation \n0. Exit ")
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
                    self.warehouse.show_category()
                    category = input("Please, state the product category: ")
                    name = input("Please, state the product name: ")
                    print(self.warehouse.search_product(category, name))
                    input()
                case "4":
                    print("Update product")
                    self.warehouse.show_category()
                    category = input("Please, state the product category: ")
                    self.warehouse.update_product(category)
                case "5":
                    print("Remove product")
                    self.warehouse.show_category()
                    category = input("Please, state the product category: ")
                    print(self.warehouse.remove_product(category))
                case "6":
                    print("Filter products by price")
                    price = float(input("State the maximum price that you can buy: "))
                    print(self.warehouse.filter_prices(price))
                    input()
                case "7":
                    print("Shows stats")
                    print(self.warehouse.shows_stats())
                    input()
                case "8":
                    print("Sale Simulation")
                    self.sale_simulation()
                    input()
                case _:
                    print("Bye")
                    ok = True

  
    def add_menu(self):
        '''
        Add_menu method

        This method show you the options when you add a product in the inventory
        '''
        ok2 = False
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
            name = input("Name: ")
            brand = input("Brand: ")
            ok3 = False
            while(not ok3):
                stock = int(input("Stock: "))
                price = float(input("Price: "))
                if(stock <= 0 or price <= 0):
                    print("The stock and the price aren't negative numbers. Please try again")
                else:
                    ok3 = True
            print("────────────────────────────────────")
            
            if category != None:
                self.warehouse.add(category, name,brand,stock,price)
                input()

    def sale_simulation(self):
        '''
        sale_simulation Method

        This method simulates a real sale
        '''
        try:
            clear()
            self.warehouse.show_category()
            category = input("SELECT CATEGORY (by name): ")
            self.warehouse.show_category_product(category)
            product_index = int(input("SELECT PRODUCT (by index): "))
            quantity = int(input("STATE THE QUANTITY: "))
            self.warehouse.buy_product(category, product_index, quantity)
        except:
            print("--ERROR: WRONG INPUT--")
            input()



