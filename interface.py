import tkinter as tk
from tkinter import font
from warehouse import Warehouse

home = tk.Tk()
home.title("Welcome to PCPartes!")
warehouse = Warehouse()

# Hover methods
def on_enter(event):
   event.widget.config(bg = "#A9C61C")

def on_leave(event):
   event.widget.config(bg = "#FCFCF7")

# Placeholder methods
def on_focus_in(event):
    if event.widget.get() == "Enter your text...":
        event.widget.delete(0, tk.END)

def on_focus_out(event):
    if event.widget.get() == "":
        event.widget.insert(0, "Enter your text...")
   

def show_inventory():
   '''
   Aquí falta agregar la categoria. Una buena idea sustituir el numerito por la categoria
   '''
   inventory = tk.Toplevel()
   home.withdraw() #Hide the window
   inventory.title("PCPartes warehouse")
   
   inventory.config(bg = "#C3C3C3")
   inventory.geometry("550x300")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      inventory,
      text = "List of products",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   text = tk.Label(
      inventory,
      text = warehouse.show_products(),
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify="left"
   )
   text.grid(row = 1, column = 0, pady = 20)

   close_button = tk.Button(
      inventory,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat", #Border style
      font = normal_font,
      command=lambda: (home.deiconify(), inventory.destroy())
   )
   close_button.grid(row = 2, column = 0, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   inventory.mainloop()

def add_product():
   product = tk.Toplevel()
   home.withdraw()
   product.title("Add product in PCPartes warehouse")

   product.config(bg = "#C3C3C3")
   product.geometry("550x300")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      product,
      text = "State the product",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   category_text = tk.Label(
      product, 
      text = "Category",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
   )
   category_text.grid(row = 1, column = 0, pady = 10)

   category = tk.Entry(product)
   category.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   category.grid(row = 1, column = 1, pady = 10, padx = 10)
   category.insert(0, "Enter your text...")
   category.bind("<FocusIn>", on_focus_in)
   category.bind("<FocusOut>", on_focus_out)

   name_text = tk.Label(
      product,
      text = "Name",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   name_text.grid(row = 1, column = 2, pady = 10)

   name = tk.Entry(product)
   name.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   name.grid(row = 1, column = 3, pady = 10, padx = 10)
   name.insert(0, "Enter your text...")
   name.bind("<FocusIn>", on_focus_in)
   name.bind("<FocusOut>", on_focus_out)

   brand_text = tk.Label(
      product,
      text = "Brand",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   brand_text.grid(row = 2, column = 0, pady = 10)

   brand = tk.Entry(product)
   brand.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   brand.grid(row = 2, column = 1, pady = 10, padx = 10)
   brand.insert(0, "Enter your text...")
   brand.bind("<FocusIn>", on_focus_in)
   brand.bind("<FocusOut>", on_focus_out)

   stock_text = tk.Label(
      product,
      text = "Stock",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   stock_text.grid(row = 2, column = 2, pady = 10)

   stock = tk.Entry(product)
   stock.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   stock.grid(row = 2, column = 3, pady = 10, padx = 10)
   stock.insert(0, "Enter your text...")
   stock.bind("<FocusIn>", on_focus_in)
   stock.bind("<FocusOut>", on_focus_out)

   price_text = tk.Label(
      product,
      text = "Price",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   price_text.grid(row = 3, column = 0, pady = 10)

   price = tk.Entry(product)
   price.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   price.grid(row = 3, column = 1, pady = 10, padx = 10)
   price.insert(0, "Enter your text...")
   price.bind("<FocusIn>", on_focus_in)
   price.bind("<FocusOut>", on_focus_out)

   add_button = tk.Button(
      product,
      text = "Add product",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command =lambda: warehouse.add(category.get(),name.get(),brand.get(),stock.get(),price.get())
   )
   add_button.grid(row = 3, column = 2, columnspan = 2, pady = 10, padx = 10)
   add_button.bind("<Enter>", on_enter)
   add_button.bind("<Leave>", on_leave)

   close_button = tk.Button(
      product,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command=lambda: (home.deiconify(), product.destroy())
   )
   close_button.grid(row = 4, column = 0, columnspan = 4, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   product.mainloop()

def show_result(category, name, result):
   result.config(text = warehouse.search_product(category, name))

def search_product():
   search = tk.Toplevel()
   home.withdraw()
   search.title("Seach a product in PCPartes warehouse")

   search.config(bg = "#C3C3C3")
   search.geometry("700x300")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      search,
      text = "State the category and the name",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   category_text = tk.Label(
      search, 
      text = "Category",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
   )
   category_text.grid(row = 1, column = 0, pady = 10)

   category = tk.Entry(search)
   category.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   category.grid(row = 1, column = 1, pady = 10, padx = 10)
   category.insert(0, "Enter your text...")
   category.bind("<FocusIn>", on_focus_in)
   category.bind("<FocusOut>", on_focus_out)

   name_text = tk.Label(
      search,
      text = "Name",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   name_text.grid(row = 1, column = 2, pady = 10)

   name = tk.Entry(search)
   name.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   name.grid(row = 1, column = 3, pady = 10, padx = 10)
   name.insert(0, "Enter your text...")
   name.bind("<FocusIn>", on_focus_in)
   name.bind("<FocusOut>", on_focus_out)

   result = tk.Label(
      search,
      text = "",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   result.grid(row = 3, column = 0, columnspan = 4, pady = 10, padx = 10)

   search_button = tk.Button(
      search,
      text = "Search product",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command = lambda: show_result(category.get(), name.get(), result)
   )
   
   search_button.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10)
   search_button.bind("<Enter>", on_enter)
   search_button.bind("<Leave>", on_leave)

   close_button = tk.Button(
      search,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command=lambda: (home.deiconify(), search.destroy())
   )
   close_button.grid(row = 3, column = 0, columnspan = 4, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)
   search.mainloop()

def method_update(category, name, radio_var, number, result):
   type = "price" if radio_var == "Price" else "stock"
   result.config(text = warehouse.update_product(category, name, type, number))


def update_product():
   update = tk.Toplevel()
   home.withdraw()
   update.title("Update a product in PCPartes warehouse")

   update.config(bg = "#C3C3C3")
   update.geometry("1000x300")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      update,
      text = "State the category and the price or the stock",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   category_text = tk.Label(
      update,
      text = "State the category",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   category_text.grid(row = 1, column = 0, pady = 10)

   category = tk.Entry(update)
   category.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   category.grid(row = 1, column = 1, pady = 10, padx = 10)
   category.insert(0, "Enter your text...")
   category.bind("<FocusIn>", on_focus_in)
   category.bind("<FocusOut>", on_focus_out)

   name_text = tk.Label(
      update,
      text = "State the name",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   name_text.grid(row = 2, column = 0, pady = 10)

   name = tk.Entry(update)
   name.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   name.grid(row = 2, column = 1, pady = 10, padx = 10)
   name.insert(0, "Enter your text...")
   name.bind("<FocusIn>", on_focus_in)
   name.bind("<FocusOut>", on_focus_out)

   option_text = tk.Label(
      update,
      text = "Please select the price or the stock",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   option_text.grid(row = 1, column = 2, pady = 10)

   radio_var = tk.StringVar(value="Opción 1")
   radio1 = tk.Radiobutton(update, text="Price", variable=radio_var, value="Price", command="")
   radio2 = tk.Radiobutton(update, text="Stock", variable=radio_var, value="Stock", command="")
   radio1.grid(row = 1, column = 3, pady = 10, padx = 10)
   radio2.grid(row = 2, column = 3, pady = 10, padx = 10)

   number_text = tk.Label(
      update,
      text = "State the quantity",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center",
      anchor = "center"
   )
   number_text.grid(row = 3, column = 0, pady = 10)

   number = tk.Entry(update)
   number.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   number.grid(row = 3, column = 1, pady = 10, padx = 10)
   number.insert(0, "Enter your text...")
   number.bind("<FocusIn>", on_focus_in)
   number.bind("<FocusOut>", on_focus_out)

   result = tk.Label(
      update,
      text = "",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323"
   )
   result.grid(row = 4, column = 0, columnspan= 4, pady = 10, padx = 10)

   update_button = tk.Button(
      update,
      text = "Update product",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command = lambda: method_update(category.get(), name.get(), radio_var.get(), number.get(), result)
   )
   update_button.grid(row = 3, column = 2, pady = 10, padx = 10)
   update_button.bind("<Enter>", on_enter)
   update_button.bind("<Leave>", on_leave)

   close_button = tk.Button(
      update,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command=lambda: (home.deiconify(), update.destroy())
   )
   close_button.grid(row = 5, column = 0, columnspan = 4, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   update.mainloop()

def method_remove(category, name, result):
   result.config(text = warehouse.remove_product(category, name))

def remove_product():
   removew = tk.Toplevel()
   home.withdraw()
   removew.title("Remove a product")

   removew.config(bg = "#C3C3C3")
   removew.geometry("600x400")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      removew,
      text = "Remove a product",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   category_name = tk.Label(
      removew,
      text = "State the category",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   category_name.grid(row = 1, column = 0, pady = 10)

   category = tk.Entry(removew)
   category.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   category.grid(row = 1, column = 1, pady = 10, padx = 10)
   category.insert(0, "Enter your text...")
   category.bind("<FocusIn>", on_focus_in)
   category.bind("<FocusOut>", on_focus_out)

   name_text = tk.Label(
      removew,
      text = "State the name",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   name_text.grid(row = 2, column = 0, pady = 10)

   name = tk.Entry(removew)
   name.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   name.grid(row = 2, column = 1, pady = 10, padx = 10)
   name.insert(0, "Enter your text...")
   name.bind("<FocusIn>", on_focus_in)
   name.bind("<FocusOut>", on_focus_out)

   result = tk.Label(
      removew,
      text = "",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   result.grid(row = 3, column = 0, pady = 10)

   remove_button = tk.Button(
      removew,
      text = "Remove product",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command = lambda: method_remove(category.get(), name.get(), result)
   )
   remove_button.grid(row = 4, column = 0, pady = 10, padx = 10)
   remove_button.bind("<Enter>", on_enter)
   remove_button.bind("<Leave>", on_leave)

   close_button = tk.Button(
      removew,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat", #Border style
      font = normal_font,
      command=lambda: (home.deiconify(), removew.destroy())
   )
   close_button.grid(row = 4, column = 1, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   removew.mainloop()

def method_filter(price, result):
   result.config(text = warehouse.filter_prices(float(price)))

def filter_product():
   filterw = tk.Toplevel()
   home.withdraw()
   filterw.title("Filter a product by price")

   filterw.config(bg = "#C3C3C3")
   filterw.geometry("600x400")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      filterw,
      text = "PCParts filter products",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   price_text = tk.Label(
      filterw,
      text = "State the maximum product",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   price_text.grid(row = 1, column = 0, pady = 10)

   price = tk.Entry(filterw)
   price.config(
      bg = "#C3C3C3",
      fg = "#102323",
      font = normal_font
   )
   price.grid(row = 1, column = 1, pady = 10, padx = 10)
   price.insert(0, "Enter your text...")
   price.bind("<FocusIn>", on_focus_in)
   price.bind("<FocusOut>", on_focus_out)

   result = tk.Label(
      filterw,
      text = "",
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   result.grid(row = 3, column = 0, pady = 10)

   filter_button = tk.Button(
      filterw,
      text = "Filter products",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat",
      font = normal_font,
      command = lambda: method_filter(price.get(), result)
   )
   filter_button.grid(row = 1, column = 2, pady = 10, padx = 10)
   filter_button.bind("<Enter>", on_enter)
   filter_button.bind("<Leave>", on_leave)

   close_button = tk.Button(
      filterw,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat", #Border style
      font = normal_font,
      command=lambda: (home.deiconify(), filterw.destroy())
   )
   close_button.grid(row = 2, column = 0, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   filterw.mainloop()

def show_stats():
   stats = tk.Toplevel()
   home.withdraw() #Hide the window
   stats.title("PCPartes stats")
   
   stats.config(bg = "#C3C3C3")
   stats.geometry("300x350")
   title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
   normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

   title = tk.Label(
      stats,
      text = "PCPartes Stats",
      font = title_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify = "center"
   )
   title.grid(row = 0, column = 0, pady = 20, sticky = "nsew")

   text = tk.Label(
      stats,
      text = warehouse.shows_stats(),
      font = normal_font,
      bg = "#C3C3C3",
      fg = "#102323",
      justify="left"
   )
   text.grid(row = 1, column = 0, pady = 20)

   close_button = tk.Button(
      stats,
      text = "Exit",
      width = 20,
      height = 1,
      fg = "#102323",
      bg = "#FCFCF7",
      relief = "flat", #Border style
      font = normal_font,
      command=lambda: (home.deiconify(), stats.destroy())
   )
   close_button.grid(row = 2, column = 0, pady = 10, padx = 10)
   close_button.bind("<Enter>", on_enter)
   close_button.bind("<Leave>", on_leave)

   stats.mainloop()


# Home window configuration
home.config(bg = "#C3C3C3")
home.geometry("700x400")
home.columnconfigure(0, weight = 1)
home.columnconfigure(1, weight = 1)
home.columnconfigure(2, weight = 1)
title_font = font.Font(family = "Oxanium", size = 12, weight = "bold")
normal_font = font.Font(family = "Exo 2", size = 10, weight= "bold" )

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