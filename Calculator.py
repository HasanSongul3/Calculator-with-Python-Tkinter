import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")

        self.screen = tk.Entry(master, width=25, font=('Arial', 16), justify='right')
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '*', 
            '7', '8', '9', '-',
            '0', '.', 'C', '+'
        ]

        # Döngüyle butonlar ekleniyor
        for i, button in enumerate(buttons):
            btn = tk.Button(master, text=button, width=5, height=2, font=('Arial', 12), command=lambda x=button: self.click(x))
            row = i // 4 + 1
            col = i % 4
            btn.grid(row=row, column=col, padx=5, pady=5)

        # '=' butonu
        equal_btn = tk.Button(master, text='=', width=5, height=2, font=('Arial', 12), command=self.calculate)
        equal_btn.grid(row=5, column=3, padx=5, pady=5)

    def click(self, key):
        if key == 'C':
            self.screen.delete(0, tk.END)
        else:
            self.screen.insert(tk.END, key)

    def calculate(self):
        try:
            result = eval(self.screen.get())
            self.screen.delete(0, tk.END)
            self.screen.insert(tk.END, str(result))
        except:
            self.screen.delete(0, tk.END)
            self.screen.insert(tk.END, "Error")

root = tk.Tk()
app = Calculator(root)
root.mainloop()
