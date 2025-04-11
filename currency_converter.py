import tkinter as tk
from tkinter import *

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")


        self.label = tk.Label(root, text="Gib eine Zahl ein die du verändern willst!")
        self.label.pack(pady=10)


        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Anzeigen", command=self.anzeigen)
        self.button.pack(pady=10)


        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)


        self.currencies = ["EURO", "USD", "YEN"]
        self.exchange = [1.00, 0.93, 162]

        self.euro_button = IntVar()
        self.usd_button = IntVar()
        self.yen_button = IntVar()
        self.to_euro_button = IntVar()
        self.to_usd_button = IntVar()
        self.to_yen_button = IntVar()


        self.have_currency = tk.Label(root, text="Have Currency:")
        self.have_currency.pack()
        self.Button1 = Checkbutton(root, text="EURO", variable=self.euro_button, height=2, width=10)
        self.Button2 = Checkbutton(root, text="USD", variable=self.usd_button, height=2, width=10)
        self.Button3 = Checkbutton(root, text="YEN", variable=self.yen_button, height=2, width=10)
        self.Button1.pack()
        self.Button2.pack()
        self.Button3.pack()


        self.to_currency = tk.Label(root, text="To Currency:")
        self.to_currency.pack()
        self.Button4 = Checkbutton(root, text="EURO", variable=self.to_euro_button, height=2, width=10)
        self.Button5 = Checkbutton(root, text="USD", variable=self.to_usd_button, height=2, width=10)
        self.Button6 = Checkbutton(root, text="YEN", variable=self.to_yen_button, height=2, width=10)
        self.Button4.pack()
        self.Button5.pack()
        self.Button6.pack()

    def anzeigen(self):
        try:
            value = float(self.entry.get())
        except ValueError:
            self.output_label.config(text="Bitte gib eine gültige Zahl ein.")
            return

        from_index = None
        to_index = None


        if self.euro_button.get() == 1:
            from_index = 0
        elif self.usd_button.get() == 1:
            from_index = 1
        elif self.yen_button.get() == 1:
            from_index = 2


        if self.to_euro_button.get() == 1:
            to_index = 0
        elif self.to_usd_button.get() == 1:
            to_index = 1
        elif self.to_yen_button.get() == 1:
            to_index = 2

        if from_index is None or to_index is None:
            self.output_label.config(text="Bitte wähle Quell- und Zielwährung.", font=("Arial", 30))
            return

        if from_index == to_index:
            self.output_label.config(text=f"{value:.2f} {self.currencies[to_index]}")
            return


        amount_in_euro = value / self.exchange[from_index] 
        result = amount_in_euro * self.exchange[to_index]

        self.output_label.config(text=f"{result:.2f} {self.currencies[to_index]}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()
