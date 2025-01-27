from products import Product
from warehouse import Warehouse


class Engine:

    def __init__(self):
        pass

    def menu(self):
        ok = True
        while(ok):
            print(" 1. Show inventory \n 2. Add product \n 3. Exit ")
            option = input("")
            match option:
                case "1":
                    print("Inventory")
                    ok = False
                    break
                case "2":
                    print("Add product")
                    ok = False
                    break
                case "3":
                    print("Bye bye")
                    ok = False
                    break
                case _:
                    print("Wrong option. Please repeat your option")
                    ok = True

        
    
    

            