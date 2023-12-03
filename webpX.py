import tkinter as tk
from tkinter import ttk
import webbrowser

class WebpageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("webpX")

        # Label for the URL
        ttk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)

        # Entry for entering the URL
        self.url_entry = ttk.Entry(root, width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to load the webpage
        load_button = ttk.Button(root, text="Load Webpage", command=self.load_webpage)
        load_button.grid(row=0, column=2, padx=10, pady=10)

        # Web browser window
        self.browser_window = tk.Toplevel(root)
        self.browser_window.title("Webpage Display")
        self.browser_window.withdraw()  # Hide initially

    def load_webpage(self):
        url = self.url_entry.get()
        if url:
            # Open the webpage in the web browser window
            webbrowser.open_new(url)
            self.browser_window.deiconify()  # Show the web browser window

if __name__ == "__main__":
    root = tk.Tk()
    app = WebpageViewer(root)
    root.mainloop()
