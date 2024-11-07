Calculator with C Backend and Python (Tkinter) Frontend

Project Overview
This is a simple calculator application that demonstrates how to use a C-based backend for calculations while displaying a GUI built with Python's Tkinter.

Project Structure
calculations.c and calculations.h: These files contain the core logic for performing mathematical operations.
backend_interface.c: Acts as the bridge between the C backend (calculation files) and the Python frontend, allowing seamless interaction between them.
gui.py: Builds the graphical interface with Tkinter, providing buttons and input fields for the calculator.
main.py: Connects all components together to create the complete application.

How to Run
Compile the C files:

bash:

gcc -o backend_interface calculations.c backend_interface.c

Run main.py to start the calculator application.


Features:

Basic operations: Addition, subtraction, multiplication, and division.
User-friendly GUI created with Python's Tkinter.
C backend for optimized calculations.
