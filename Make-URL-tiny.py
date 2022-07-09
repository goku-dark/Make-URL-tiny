from tkinter import *
import paperclip
import pyshorteners

def url_shortner():
    shortener = pyshorteners.Shortener()
    url_short = shortener.tinyurl.short(main_url.get())
    
    #set the gloabal short_url
    short_url.set(url_short)

def copy_url():
    #copy short url on clipboard
    pyperclip.copy( short_url.get())

if __name__=="__main__":
    root = Tk()
    root.geometry("700x700")
    root.title("My URL Shortener App")
    root.configure(bg="#49A")

    main_url = StringVar()
    short_url= StringVar()
    
    Label(root, text="Enter The Main URL", font="poppins").pack(pady=5)
    Entry(root,textvariable=main_url, width =100).pack(pady=5)
    Button(root, text="Generate Short URL", command =url_shortner).pack(pady=5)

    Label(root, text="The Short URL ", font="poppins").pack(pady=5)
    Entry(root, textvariable= short_url, width=50).pack(pady=5)
    Button(root, text="Copy the Short URL", command= copy_url).pack(pady=5)
    root.mainloop()