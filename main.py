import tkinter as tk
from commands import check_balance
# create main window
root=tk.Tk()

# add the tittle to main window
root.title("ATM SIMULATOR")
# Specify main window size
root.geometry("500x400")
# add account number entry
account_number_entry= tk.Entry(root, width=30)
account_number_entry.pack(side="top")

# add check balance button
check_balance_btn=tk.Button(root,text="check balance", command=lambda:check_balance(account_number_entry.get()))
check_balance_btn.pack(side="top")
deposit_btn=tk.Button(root, text="deposit")
deposit_btn.pack(side="top")
# open main window
root.mainloop()