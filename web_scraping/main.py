import tkinter as tk
import requests as r
from bs4 import BeautifulSoup

def scrape():
    url = url_entry.get()
    

window = tk.Tk()
window.title("Web Scraping")
window.geometry("400x350")

url_label = tk.Label(window, text="Enter your URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_label.pack()

scrape_button = tk.Button(window, text="Scrape")
scrape_button.pack()

window.mainloop()