# Import required modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import requests
import datetime as dt

# Converting stuff
class CurrencyConverter:

    def __init__(self, url):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')

    def convert(self, amount, base_currency, des_currency):
        # based on EUR
        if base_currency != 'EUR':
            amount = amount/self.rates[base_currency]

        # Limiting the result to 2 decimal places
        amount = round(amount*self.rates[des_currency], 2)
        # Add comma every 3 numbers
        amount = '{:,}'.format(amount)
        return amount

# Main window
class Main(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.config(bg='#3A3B3C')
        self.CurrencyConverter = converter

        self.columnconfigure(0, weight=1, minsize=200)
        for i in range(4):
            self.rowconfigure(i, weight=1, minsize=80)

        for i in range(4, 6):
            self.rowconfigure(i, weight=1, minsize=40)
        # title label
        self.title_label = tk.Label(self, text='Currency Converter', bg='#3A3B3C', fg='white', font=('franklin gothic medium', 40), relief='sunken')
        self.title_label.grid(row=0, column=0, sticky="ew", padx=2, pady=2)

        # amount label
        self.amount = tk.Frame(self, bg='gray')
        self.amount.grid(row=1, column=0, sticky="ew", padx=2, pady=2)
        self.amount.columnconfigure(0, weight=1, minsize=100)

        self.amount_label = tk.Label(self.amount, text='Input Amount: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.amount_label.grid(row=0, column=0, sticky="w", padx=2, pady=3)
        self.amount_entry = tk.Entry(self.amount)
        self.amount_entry.config(width=25)
        self.amount_entry.grid(row=1, column=0, sticky="w", padx=2, pady=3)

        # 'from' label
        self.from_label = tk.Frame(self)
        self.from_label.grid(row=2, column=0, sticky="ew", padx=2, pady=5)
        self.from_label.columnconfigure(0, weight=1, minsize=100)
        self.base_currency_label = Label(self.from_label, text='From: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.base_currency_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # Create 'to' label
        self.to_label = Frame(self)
        self.to_label.grid(row=3, column=0, sticky="ew", padx=2, pady=5)
        self.to_label.columnconfigure(0, weight=1, minsize=100)
        self.destination_currency_label = Label(self.to_label, text='To: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.destination_currency_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # 'from' & 'to' dropdown menus
        self.currency_variable1 = StringVar(self)
        self.currency_variable2 = StringVar(self)
        self.currency_variable1.set('USD')
        self.currency_variable2.set('CNY')

        self.currency_combobox1 = ttk.Combobox(self.from_label, width=20, textvariable=self.currency_variable1, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox1.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.currency_combobox2 = ttk.Combobox(self.to_label, width=20, textvariable=self.currency_variable2, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # 'convert' & 'clear' button
        self.buttons = Frame(self)
        self.buttons.grid(row=4, column=0, sticky="ew", padx=2, pady=5)
        self.convert_button = Button(self.buttons, text='Convert', bg='white', fg='black', command=self.processed)
        self.convert_button.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.clear_button = Button(self.buttons, text='Clear', bg='white', fg='black', command=self.clear)
        self.clear_button.grid(row=0, column=1, sticky="w", padx=2, pady=5)

        # result field
        self.final_result = Label(self, text='', bg='#52595D', fg='white', font=('calibri', 12), relief='sunken', width=40)
        self.final_result.grid(row=5, column=0, sticky="ew", padx=2, pady=5)
    # Create clear function, to clear the amount field and final result field
    def clear(self):
        clear_entry = self.amount_entry.delete(0, END)
        clear_result = self.final_result.config(text='')
        return clear_entry, clear_result

    # Create a function to perform
    def processed(self):
        try:
            given_amount = float(self.amount_entry.get())
            given_base_currency = self.currency_variable1.get()
            given_des_currency = self.currency_variable2.get()
            converted_amount = self.CurrencyConverter.convert(given_amount, given_base_currency, given_des_currency)
            # Add comma every 3 numbers
            given_amount = '{:,}'.format(given_amount)

            self.final_result.config(text=f'{given_amount} {given_base_currency} = {converted_amount} {given_des_currency}')

        # Create warning message box
        except ValueError:
            convert_error = messagebox.showwarning('WARNING!', 'Please Fill the Amount Field (integer only)!')
            return convert_error


def main():
    converter = CurrencyConverter('https://api.exchangerate.host/latest')
    Main(converter)
    mainloop()
