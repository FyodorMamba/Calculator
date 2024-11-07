import tkinter as tk
from tkinter import ttk
from backend_interface import add, subtract, multiply, divide

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern C-Powered Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)

        # Configure styles
        style = ttk.Style()
        style.configure("Display.TEntry",
                       padding=10,
                       font=('Arial', 20))
        
        style.configure("Calc.TButton",
                       padding=10,
                       font=('Arial', 14, 'bold'),
                       width=8)

        # Main display frame
        display_frame = ttk.Frame(root, padding="20 20 20 10")
        display_frame.pack(fill='x')

        # Calculator display
        self.display = ttk.Entry(display_frame,
                               justify='right',
                               font=('Arial', 24),
                               style="Display.TEntry")
        self.display.pack(fill='x', pady=5)

        # Previous calculation display
        self.prev_display = ttk.Label(display_frame,
                                    text="",
                                    font=('Arial', 12),
                                    foreground='gray')
        self.prev_display.pack(fill='x')

        # Button frame
        button_frame = ttk.Frame(root, padding="20 10 20 20")
        button_frame.pack(fill='both', expand=True)

        # Configure button layout
        buttons = [
            ('C', 0, 0), ('±', 0, 1), ('%', 0, 2), ('÷', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0, 2), ('.', 4, 2), ('=', 4, 3)
        ]

        # Create and configure grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        # Create buttons
        self.buttons = {}
        for btn_text, row, col, *span in buttons:
            columnspan = span[0] if span else 1
            button = ttk.Button(button_frame,
                              text=btn_text,
                              style="Calc.TButton",
                              command=lambda x=btn_text: self.button_click(x))
            button.grid(row=row, column=col, columnspan=columnspan,
                       padx=5, pady=5, sticky='nsew')
            self.buttons[btn_text] = button

        # Initialize calculator state
        self.current_num = ''
        self.first_num = None
        self.operation = None
        self.should_reset = False

    def button_click(self, value):
        if value.isdigit() or value == '.':
            if self.should_reset:
                self.current_num = ''
                self.should_reset = False
            self.current_num += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_num)

        elif value in ('+', '-', '×', '÷'):
            if self.first_num is None:
                self.first_num = float(self.current_num or '0')
            else:
                self.calculate()
            self.operation = value
            self.prev_display.config(text=f"{self.first_num} {value}")
            self.should_reset = True

        elif value == '=':
            self.calculate()
            self.operation = None
            self.first_num = None
            self.prev_display.config(text="")

        elif value == 'C':
            self.clear()

        elif value == '±':
            if self.current_num and self.current_num != '0':
                if self.current_num[0] == '-':
                    self.current_num = self.current_num[1:]
                else:
                    self.current_num = '-' + self.current_num
                self.display.delete(0, tk.END)
                self.display.insert(0, self.current_num)

    def calculate(self):
        if not self.operation or not self.first_num:
            return
        
        try:
            second_num = float(self.current_num or '0')
            if self.operation == '+':
                result = add(self.first_num, second_num)
            elif self.operation == '-':
                result = subtract(self.first_num, second_num)
            elif self.operation == '×':
                result = multiply(self.first_num, second_num)
            elif self.operation == '÷':
                if second_num == 0:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    return
                result = divide(self.first_num, second_num)

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.first_num = result
            self.current_num = str(result)
            self.should_reset = True

        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def clear(self):
        self.current_num = ''
        self.first_num = None
        self.operation = None
        self.should_reset = False
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')
        self.prev_display.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()