import tkinter as tk
import pymongo

# Connect to mongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyChat"]
message_col = db["messages"]


# Tkinter GUI
root = tk.Tk()
root.title("PyChat")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def send_message():
    if entry.get():
        message_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)
        


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

messages_label = tk.Label(root, text="Messages:\n", justify="left")
messages_label.pack()



# Steg 1 Stage code = git add .
# Steg 2 Commit code = git commit -m"Added new shit"
# Steg 3 Push Code = git push


root.mainloop()