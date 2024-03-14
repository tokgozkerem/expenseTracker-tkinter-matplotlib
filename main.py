import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ExpenseTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expense_tracker = ExpenseTracker()

        self.create_widgets()

    def create_widgets(self):
        self.label_category = self.create_label("Category:", 0, 0)
        self.entry_category = self.create_entry(0, 1)

        self.label_amount = self.create_label("Amount:", 1, 0)
        self.entry_amount = self.create_entry(1, 1)

        self.button_add_expense = self.create_button("Add Expense", self.add_expense, 2)
        self.button_visualize_expenses = self.create_button(
            "Visualize Expenses", self.visualize_expenses, 3
        )

    def create_label(self, text, row, column):
        """
        Create a label widget with the specified text and place it in the specified row and column.

        :param text: The text to display on the label.
        :param row: The row in which the label will be placed.
        :param column: The column in which the label will be placed.
        :return: The created label widget.
        """
        label = ttk.Label(self.master, text=text)
        label.grid(row=row, column=column, padx=5, pady=5, sticky="e")
        return label

    def create_entry(self, row, column):
        """
        Create an entry widget and place it in the specified row and column.

        :param row: The row in which the entry will be placed.
        :param column: The column in which the entry will be placed.
        :return: The created entry widget.
        """
        entry = ttk.Entry(self.master)
        entry.grid(row=row, column=column, padx=5, pady=5)
        return entry

    def create_button(self, text, command, row):
        """
        Create a button widget and place it in the specified row.

        :param text: The text to display on the button.
        :param command: The function to call when the button is clicked.
        :param row: The row in which the button will be placed.
        :return: The created button widget.
        """
        button = ttk.Button(self.master, text=text, command=command)
        button.grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        return button

    def add_expense(self):
        """
        Add an expense based on the user input.
        If the amount is not a valid number, display an error message.
        """
        try:
            amount = float(self.entry_amount.get())
            category = self.entry_category.get()
            self.expense_tracker.add_expense(amount, category)
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def visualize_expenses(self):
        self.expense_tracker.visualize_expenses()


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        """
        Add an expense to the tracker.

        :param amount: The amount of the expense.
        :param category: The category of the expense.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.expenses.append({"amount": amount, "category": category})

    def categorize_expenses(self):
        """
        Categorize expenses by their categories.

        :return: A dictionary containing categories as keys and total amounts as values.
        """
        categories = {}
        for expense in self.expenses:
            category = expense["category"]
            if category not in categories:
                categories[category] = expense["amount"]
            else:
                categories[category] += expense["amount"]
        return categories

    def visualize_expenses(self):
        if not self.expenses:
            raise ValueError("No expenses to visualize.")
        categories = self.categorize_expenses()
        import matplotlib.pyplot as plt

        plt.bar(categories.keys(), categories.values())
        plt.xlabel("Categories")
        plt.ylabel("Amount")
        plt.title("Expense Distribution")
        plt.show()


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.title("Expense Tracker")
    center_window(root)  # Pencereyi ekranın ortasına yerleştir
    root.mainloop()


if __name__ == "__main__":
    main()
