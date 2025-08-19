from tkinter import messagebox
import csv

def check_balance(account_number):
    # open csv file
    csv_file= open(file="accounts.csv", mode="r")
    # read the csv content
    accounts= csv.DictReader(csv_file)
    for account in accounts:
        if account_number== account["account_number"]:
            # show balance with message
            messagebox.showinfo(title="check balance", message=f"your balance is{account["balance"]}")
            return
    # show user account not found
    messagebox.showerror(title="check balance", message=f"Account{account_number} does not not exist!")