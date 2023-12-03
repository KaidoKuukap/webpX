import requests
from tkinter import *

def get_html_code():
    url = url_entry.get()
    try:
        response = requests.get(url)
        html_code = response.text
        text_box.delete(1.0, END)
        text_box.insert(1.0, html_code)
    except Exception as e:
        print(e)
        text_box.delete(1.0, END)
        text_box.insert(1.0, "Error retrieving HTML code.")

root = Tk()
root.title("htmlX")
root.geometry("800x600")

label = Label(root, text="Enter URL:", font=("Arial", 12))
label.pack()

url_entry = Entry(root, bd=2, width=50)
url_entry.pack()

button = Button(root, text="Get HTML Code", command=get_html_code)
button.pack()

text_box = Text(root, height=20, width=100, bd=2)
text_box.pack()

root.mainloop()
