import tkinter as tk
from tkinter import font
from warehouse import Warehouse

home = tk.Tk()
home.title("Welcome to PCPartes!")
title_font = font.Font(family = "Oxanium Regular", size = 12, weight = "bold")
normal_font = font.Font(family = "Exo 2 Regular", size = 10, weight= "bold" )
warehouse = Warehouse()

# Hover methods
def on_enter(event):
   event.widget.config(bg = "#A9C61C")

def on_leave(event):
   event.widget.config(bg = "#FCFCF7")
   

def show_inventory():
   inventory = tk.Tk()
   home.withdraw() #Hide the window
   inventory.title("PCPartes warehouse")
   
   inventory.config(bg = "#C3C3C3")
   inventory.geometry("500x200")

   text = tk.Label(
      inventory,
      text = warehouse.show_products,
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      anchor = "center",
      justify = "center"
   )
   text.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   close_button = tk.Button(
        inventory,
        text = "Exit",
        width = 20,
        height = 1,
        fg = "#102323",
        bg = "#FCFCF7",
        relief = "flat", #Border style
        font = normal_font,
        command = inventory.destroy
   )
   close_button.grid(row = 1, column = 0, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   inventory.mainloop()


def add_product():
   print("Here you can add a product")

def search_product():
   print("Here you can search a product by name")

def update_product():
   print("Here you can update the stock or the price of the product")

def remove_product():
   print("Here you can delete a product")

def filter_product():
   print("Here you can filter a product by price")

def show_stats():
   print("Shows the shop stats")


# Home window configuration
home.config(bg = "#C3C3C3")
home.geometry("700x400")
home.columnconfigure(0, weight = 1)
home.columnconfigure(1, weight = 1)
home.columnconfigure(2, weight = 1)

title = tk.Label(
    home, 
    text ="Welcome to PCPartes! What do you want?",
    font = title_font,
    anchor = "center",
    justify = "center",
    fg = "#102323",
    bg = "#C3C3C3"
)
title.grid(row = 0, column = 0, columnspan = 3, pady = 20, sticky="nsew")

button_1 = tk.Button(
    home,
    text = "Show inventory",
    width = 20,
    height = 1,
    fg = "#102323",
    bg = "#FCFCF7",
    relief = "flat", #Border style
    font = normal_font,
    command = show_inventory
)
button_1.grid(row = 1, column = 0, padx = 10, pady = 10)
# Hover methods
button_1.bind("<Enter>", on_enter)
button_1.bind("<Leave>", on_leave)

button_2 = tk.Button(
   home,
   text = "Add product",
   width = 20,
   height = 1,
   fg = "#102323",
   bg = "#FCFCF7",
   relief = "flat",
   font = normal_font,
   command = add_product
)
button_2.grid(row = 1, column = 1, padx = 10, pady = 10)
button_2.bind("<Enter>", on_enter)
button_2.bind("<Leave>", on_leave)

button_3 = tk.Button(
   home,
   text = "Search product",
   width = 20,
   height = 1,
   fg = "#102323",
   bg = "#FCFCF7",
   relief = "flat",
   font = normal_font,
   command = search_product
)
button_3.grid(row = 1, column = 2, padx = 10, pady = 10)
button_3.bind("<Enter>", on_enter)
button_3.bind("<Leave>", on_leave)

button_4 = tk.Button(
   home,
   text = "Update product",
   width = 20,
   height = 1,
   fg = "#102323",
   bg = "#FCFCF7",
   relief = "flat",
   font = normal_font,
   command = update_product
)
button_4.grid(row = 2, column = 0, padx = 10, pady = 10)
button_4.bind("<Enter>", on_enter)
button_4.bind("<Leave>", on_leave)

button_5 = tk.Button(
   home,
   text = "Remove product",
   width = 20,
   height = 1,
   fg = "#102323",
   bg = "#FCFCF7",
   relief = "flat",
   font = normal_font,
   command = remove_product
)
button_5.grid(row = 2, column = 1, padx = 10, pady = 10)
button_5.bind("<Enter>", on_enter)
button_5.bind("<Leave>", on_leave)

button_6 = tk.Button(
   home,
   text = "Filter product",
   width = 20,
   height = 1,
   fg = "#102323",
   bg = "#FCFCF7",
   relief = "flat",
   font = normal_font,
   command = filter_product
)
button_6.grid(row = 2, column = 2, padx = 10, pady = 10)
button_6.bind("<Enter>", on_enter)
button_6.bind("<Leave>", on_leave)

button_7 = tk.Button(
   home,
   text = "Show stats",
   width = 20,
   height = 1,
   fg = "#102323",
   bg = "#FCFCF7",
   relief = "flat",
   font = normal_font,
   command = show_stats
)
button_7.grid(row = 3, column = 1,  padx = 10, pady = 10)
button_7.bind("<Enter>", on_enter)
button_7.bind("<Leave>", on_leave)

home.mainloop()