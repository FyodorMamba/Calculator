from gui import Calculator
import tkinter as tk

def create_root_window():
    """Create the root window."""
    root = tk.Tk()
    root.title("Calculator")
    return root

def create_calculator(root):
    """Create the calculator."""
    return Calculator(root)

def main():
    """Create the main application window."""
    root = create_root_window()
    calculator = create_calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()