import tkinter as tk

class CALCULATOR:
    def __init__(self, master):
        self.master = master
        master.title("CALCULATOR")

        self.expression = ""
        self.input_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.input_var, font=("Times New Roman", 20),
                              bd=10, insertwidth=10, width=16, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=5)

        # Creating buttons
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '=', '0', 'C', '/',
            
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # using keys via keyboard
        master.bind("<Key>", self.key_pressed)
        
        # assigning buttons

    def create_button(self, value, row, column):
        button = tk.Button(self.master, text=value, padx=20, pady=20, font=("Times New Roman", 16),
                           command=lambda: self.on_button_click(value))
        button.grid(row=row, column=column)

    def on_button_click(self, value):
        if value == 'C':
            self.expression = ""
        elif value == 'Backspace':
            self.expression = self.expression[:-1]  #assigning backspace
        elif value == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(value)
        self.input_var.set(self.expression)

    def key_pressed(self, event):
        key = event.char
        if key in '0123456789':
            self.on_button_click(key)
        elif key in '+-*/':
            self.on_button_click(key)
        elif key in ['c', 'C']:
            self.on_button_click('C')
        elif key in ['=', '\r']:
            self.on_button_click('=')
        elif event.keysym == 'BackSpace':  # Checking  backspace key
            self.on_button_click('Backspace')

if __name__ == "__main__":
    root = tk.Tk()
    CALCULATOR = CALCULATOR(root)
    root.mainloop()
