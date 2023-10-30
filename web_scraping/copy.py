# import tkinter as tk
# from tkinter import scrolledtext
# import requests
# from bs4 import BeautifulSoup

# # Create a function to perform web scraping
# def scrape_website():
#     url = url_entry.get()
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         scraped_data = soup.get_text()
#         result_text.delete(1.0, tk.END)  # Clear previous text
#         result_text.insert(tk.INSERT, scraped_data)
#     else:
#         result_text.delete(1.0, tk.END)
#         result_text.insert(tk.INSERT, "Failed to fetch data from the URL.")

# # Create the main window
# window = tk.Tk()
# window.title("Web Scraping with Tkinter")

# # Create labels and entry fields
# url_label = tk.Label(window, text="Enter URL:")
# url_label.pack()
# url_entry = tk.Entry(window)
# url_entry.pack()

# # Create a button to trigger the scraping
# scrape_button = tk.Button(window, text="Scrape", command=scrape_website)
# scrape_button.pack()

# # Create a scrolled text widget to display the scraped data
# result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
# result_text.pack()

# # Start the main loop
# window.mainloop()
