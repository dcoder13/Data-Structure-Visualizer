import tkinter as tk
from tkinter import ttk
from src.sorting.mainFrame import mainFrame

def main():
    
    opt = int(input("1. Sorting\n2. DataStructure\n"))
    if opt == 1:
        sorting = mainFrame()
        sorting.run()
    elif opt == 2:
        print("DataStructure")
    else:
        print("invalid option")


if __name__ == "__main__":
    main()