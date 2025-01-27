from products import Product


class Warehouse:

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
        
        
    

    def add(self, category:str, product:Product):
        self.products[category].append(product)
        print("Product added")
        for i in self.products[category]:
            print(i)

    def remove(self):
        pass # A futuro

    def show_products(self):
        
        for i in self.products:
            print("─────────────────────────────────────────────────────────────────────────────────")
            print(f"{i}: ")
            print("")
            for j in self.products[i]:
                print(j)
        print("─────────────────────────────────────────────────────────────────────────────────")