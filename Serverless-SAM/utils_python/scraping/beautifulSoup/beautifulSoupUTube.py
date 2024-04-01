
# https://pypi.org/project/beautifulsoup4/
# https://www.educative.io/answers/how-to-find-element-by-id-using-beautiful-soup

# pip install beautifulsoup4

# Find number of subscribers of a YouTube user

import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_subscribers():
    channel_name = channel_entry.get()
    if not channel_name:
        messagebox.showwarning("Warning", "Please enter a channel name.")
        return

    url =   f"https://www.youtube.com/@{channel_name}"         # https://www.youtube.com/@aaaa
            # f"https://www.youtube.com/user/{channel_name}"
        
    try:
        site_content = requests.get(url).text
        soup = BeautifulSoup(site_content, "html.parser")
        
        # subscribers = soup.find(id="subscriber-count", recursive=True)
        subscribers = soup.find_all(id="subscriber-count", recursive=True)
        # subscribers = soup.find(attrs={'id':'subscriber-count'}, recursive=True)
        # subscribers = soup.find("yt-formatted-string", {"id": "subscriber-count"}, recursive=True).text
        # subscribers = soup.find("span", {"class": "yt-subscription-button-subscriber-count-branded-horizontal"}).text.strip()
        
        print("Subscribers: " , subscribers)
        subscriber_count = "0"
        if subscribers:
            subscriber_count = subscribers[0].text.strip()
        messagebox.showinfo("Subscribers", f"The number of subscribers for '{channel_name}' is {subscriber_count}")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("YouTube Subscribers Checker")

# Label and Entry for entering channel name
tk.Label(root, text="Enter Channel Name:").pack()
channel_entry = tk.Entry(root, width=40)
channel_entry.pack()

# Button to check subscribers
check_button = tk.Button(root, text="Check Subscribers", command=get_subscribers)
check_button.pack()

root.mainloop()
