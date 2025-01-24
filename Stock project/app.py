import tkinter as tk
from tkinter import ttk
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DATABASE_PATH = "Database.db"


def fetch_stock_data(stock_name):
    connection = sqlite3.connect(DATABASE_PATH)
    query = "SELECT Date, Price FROM stock_data WHERE Name = ? ORDER BY Date"
    df = pd.read_sql_query(query, connection, params=(stock_name,))
    connection.close()
    return df


def plot_stock():
    # Haal de geselecteerde aandeelnaam op
    stock_name = stock_selector.get()
    if not stock_name:
        status_label.config(text="Selecteer een aandeel!", foreground="red")
        return
    
    df = fetch_stock_data(stock_name)
    if df.empty:
        status_label.config(text="Geen data beschikbaar voor dit aandeel.", foreground="red")
        return

    # Maak een lijngrafiek
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df['Date'], df['Price'], marker='o', linestyle='-', color='blue')
    ax.set_title(f'Prijsontwikkeling van {stock_name}')
    ax.set_xlabel('Datum')
    ax.set_ylabel('Prijs')
    ax.grid(True)
    plt.xticks(rotation=45)

    for widget in graph_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    status_label.config(text=f"Grafiek voor {stock_name} weergegeven.", foreground="green")


root = tk.Tk()
root.title("Stock Data Visualization")
root.geometry("800x600")

# Titel
title_label = ttk.Label(root, text="Aandeleninformatie", font=("Helvetica", 16))
title_label.pack(pady=10)

# Dropdown voor aandeelselectie
stock_selector_label = ttk.Label(root, text="Selecteer een aandeel:")
stock_selector_label.pack(pady=5)

# Haal unieke aandelen uit de database voor de dropdown
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT Name FROM stock_data")
stock_names = [row[0] for row in cursor.fetchall()]
connection.close()

stock_selector = ttk.Combobox(root, values=stock_names, state="readonly")
stock_selector.pack(pady=5)

# Knop om grafiek te genereren
plot_button = ttk.Button(root, text="Toon Grafiek", command=plot_stock)
plot_button.pack(pady=10)

# Statuslabel
status_label = ttk.Label(root, text="", font=("Helvetica", 10))
status_label.pack(pady=5)

# Frame voor grafiek
graph_frame = ttk.Frame(root)
graph_frame.pack(fill=tk.BOTH, expand=True)

# Start GUI
root.mainloop()