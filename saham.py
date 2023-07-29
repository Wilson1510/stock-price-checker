import requests
import tkinter as tk
from tkinter import messagebox


def get_stock_price():
    symbol = entry.get()

    api_key = 'UNLTAYZBWWUVUHO7'
    base_url = 'https://www.alphavantage.co/query'

    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': api_key
    }
    print(params)

    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    if 'Global Quote' in data:
        stock_data = data['Global Quote']
        symbol = stock_data['01. symbol']
        price = stock_data['05. price']
        messagebox.showinfo("Harga Saham", f"Harga saham terkini {symbol}: ${price}")
    else:
        messagebox.showerror("Error", "Gagal mendapatkan data saham. Pastikan kode saham valid.")


# Membuat GUI
window = tk.Tk()
window.title("Pemantau Harga Saham")

label = tk.Label(window, text="Masukkan kode saham:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Cek Harga Saham", command=get_stock_price)
button.pack()

window.mainloop()
