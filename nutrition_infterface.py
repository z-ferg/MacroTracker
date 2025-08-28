import tkinter as tk
from tkinter import *
from api_calling import make_item_request

"""""""""""""""""""""""""""""""""""
    BUTTON FUNCTION DEFINITIONS    
"""""""""""""""""""""""""""""""""""
def calculate_nutrition():
    ingredients = input_text.get("1.0", tk.END).strip().split("\n")
    num_servings = int(servings_spinbox.get())
    output_text.config(state="normal")
    # TODO -> Create new file for calculating nutritional info
    output_text.config(state="disabled")

def add_item():
    item_viewer = tk.Tk()
    item_viewer.title("Add Item to Database")
    item_viewer.geometry("300x400")
    item_viewer.resizable(False, False)
    
    item_viewer.rowconfigure(0, weight=1)
    item_viewer.rowconfigure(1, weight=2)
    item_viewer.rowconfigure(2, weight=1)
    
    value_output = tk.Text(item_viewer, wrap="word", font=("Arial", 12), width=40, height=20)
    value_output.grid(row = 1, column=0, pady=2)
    value_output.config(state="disabled")
    
    search_frame = tk.Frame(item_viewer)
    search_frame.grid(row=0, column=0, pady=2)
    
    search_bar = tk.Text(search_frame, wrap="word", font=("Arial", 12), width=30, height=2)
    search_bar.pack(side="left", padx=2)
    
    def term_print_anon():
        query = search_bar.get("1.0", tk.END).strip().split("\n")
        data = make_item_request(query)
        
        value_output.config(state="normal")
        
        if len(value_output.get("1.0", tk.END)) != 0:
            value_output.delete("1.0", tk.END)
            
        value_output.insert(tk.END, str(data) + "\n")
        value_output.config(state="disabled")
    
    search_button = tk.Button(search_frame, text="Search", command=term_print_anon)
    search_button.pack(side="right")
    
    add_item_button = tk.Button(item_viewer, text="Add Item", command=None)
    add_item_button.grid(row=2)
    
    item_viewer.mainloop()


"""""""""""""""""""""""""""""""""""
    MAIN WINDOW FUNCTIONALITY    
"""""""""""""""""""""""""""""""""""
root = tk.Tk()
root.title("Nutrition Calculator")
root.geometry("800x400")

# ------- Create Toolbar Functionality -------
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Misc", menu=subMenu)

subMenu.add_command(label="Add to Database", command=add_item)
subMenu.add_command(label="View Database", command=None)
subMenu.add_command(label="View Saved Meals", command=None)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=0)

input_label = tk.Label(root, text="Ingredients/Recipe", font=("Arial", 12))
input_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

input_label = tk.Label(root, text="Nutritional Information", font=("Arial", 12))
input_label.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

input_text = tk.Text(root, wrap="word", font=("Arial", 12))
input_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

output_text = tk.Text(root, wrap="word", font=("Arial", 12), state="normal")
output_text.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
output_text.config(state="disabled")

# ------- Create a Frame to hold bottom functionality -------
bottom_frame = tk.Frame(root)
bottom_frame.grid(row=2, column=0, columnspan=2, pady=10)

servings_label = tk.Label(bottom_frame, text="Servings:")
servings_label.pack(side="left", padx=5)

servings_spinbox = tk.Spinbox(bottom_frame, from_=1, to=20, width=5)
servings_spinbox.pack(side="left", padx=10)
servings_spinbox.delete(0, tk.END)
servings_spinbox.insert(0, "1")  # default value

calc_button = tk.Button(bottom_frame, text="Calculate Nutrition", command=calculate_nutrition)
calc_button.pack(side="left", padx=10)


root.mainloop()