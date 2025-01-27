from products import Product
from warehouse import Warehouse
import os

def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

class Engine:

    def __init__(self):
        self.warehouse = Warehouse()

    

    def menu(self):
        ok = False
        while not ok:
            clear()
            print("────────────────────────────────────")
            print("1. Show inventory \n2. Add product \n0. Exit ")
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
                case _:
                    print("Bye")
                    ok = True


    def add_menu(self):
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
            stock = int(input("Stock: "))
            price = float(input("Price: "))
            print("────────────────────────────────────")
            product = Product(name, brand, stock, price)
            if category != None:
                self.warehouse.add(category, product)
                input()