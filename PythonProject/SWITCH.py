import tkinter as tk
import webbrowser
from tkinter import ttk
import streamlit as st
from PIL import Image, ImageTk
import subprocess

root = tk.Tk()
root.attributes('-fullscreen', True)

style = ttk.Style()
style.theme_use("clam")


def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)


root.bind('<Escape>', exit_fullscreen)

root.title("Account")

bg_color = "#111827"
fg_color = "#FFFFFF"
accent_color = "#3B82F6"

root.configure(bg=bg_color)

style.configure(
    "Main.TFrame",
    background=bg_color,
)
style.configure(
    "Title.TLabel",
    background=bg_color,
    foreground=fg_color,
    font=("Calibri", 20, "bold")
)
style.configure(
    "TButton",
    font=("Calibri", 12),
    foreground=fg_color,
    background=accent_color,
    padding=6,
)
style.configure(
    "TCombobox",
    fieldbackground="#1F2933",
    background="#1F2933",
    foreground=fg_color,)


def show_account_screen(loginpage):
    button2 = ttk.Button(root, text="Back", width=5, command=lambda: (exit_button_click(root)))
    button2.place(x=1060, y=5)


def exit_button_click(window):
    window.destroy()

def open_PROJECT():
    subprocess.Popen(["python", "PROJECT.py"])

def open_ACCOUNT():
    subprocess.Popen(["python", "ACCOUNT.py"])

def open_SITE():
    webbrowser.open("https://www.amazon.com/Nintendo-SwitchTM-Neon-Blue-Joy%E2%80%91ConTM-Switch/dp/B0BFJWCYTL/ref=sr_1_1?dib=eyJ2IjoiMSJ9.Q6e_3NgNcUvoh4Lw02lyGVXC3XKYi-fswzB8yQJGZB5GbHw407qdG-bBb_ys12Mn94th3xepK2ufEzW7n0WQ8SUKyP7VYqamJ_ks6Mdy5xQbTTgO92bs6UXkZ5LmreC8Bm-A2SwRGCBgR5U0Lwc9xqPxd8oXIft8lqYJYjONHJgxYpysA_yyHz0CjFMIjKkEtk0BG0ux8L7RDYIskpDmQH_Qfo14OMWoI_lX4X23Y04.8tbgXFKoq6DgwrSLs5Puc7XLwHsOrhmVAqgIoET7cPc&dib_tag=se&hvadid=657230199495&hvdev=c&hvexpln=0&hvlocphy=9026088&hvnetw=g&hvocijid=9732507121708029195--&hvqmt=e&hvrand=9732507121708029195&hvtargid=kwd-375876500148&hydadcr=26587_11751851&keywords=nintendo%2Bswitch%2B-&mcid=b5fec5d29dd43513b1a1e7edca5ae255&qid=1765393285&sr=8-1&th=1")


BORDER_WIDTH = 7
border = ttk.Frame(root, style="Main.TFrame", padding=20, borderwidth=BORDER_WIDTH, relief="ridge")
border.place(relx=0.5, rely=0.5, anchor="center", width=1530, height=862)


label = ttk.Label(root, text="Details", font=("Arial", 20))
label.place(x=5, y=5)

button = ttk.Button(root, text="Main Page", command=open_PROJECT)
button.place(x=950, y=5)

button2 = ttk.Button(root, text="Account", command=open_ACCOUNT)
button2.place(x=1150, y=5)

style = ttk.Style(root)
style.configure('TButton', font=('Arial', 12), foreground='blue')

combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack(pady=4000)

exit_button = ttk.Button(root, text="Exit", width=5, command=lambda: exit_button_click(root))
exit_button.place(x=1450, y=5)

item1 = ttk.Label(root, text="Nintendo Switch", font=("Arial", 12))
item1.place(x=400, y=95)
item1price = ttk.Label(root, text="$299.99    NEW", font=("Arial", 12))
item1price.place(x=400, y=135)

details = ttk.Label(root, text="Get started with Nintendo Switch", font=("Calibri", 19,))
details.place(x=400, y=195)
details = ttk.Label(root, text="Get to know the three different playmodes! Handheld, TV mode and Tabletop", font=("Calibri", 16))
details.place(x=400, y=240)
details2 = ttk.Label(root, text="Nintendo Switch is the way to play Super Mario Bros.™ Wonder, Mario Kart™ 8 Deluxe, and more games starring Mario and friends.", font=("Arial", 9))
details2.place(x=400, y=270)

info = ttk.Label(root, text="For More Information:", font=("Arial", 12))
info.place(x=400, y=295)
info2 = ttk.Label(root, text="https://www.nintendo.com/us/gaming-systems/switch/?srsltid=AfmBOormkOoDzawvOS4W1lddPweT83f3ralg4cjdEpx8ueeGNOnffJiq", font=("Arial", 12))
info2.place(x=400, y=325)

purchase_button = ttk.Button(root, text="Purchase", command=open_SITE)
purchase_button.place(x=400, y=380)

img = Image.open("switch pic1.jpg")
img = img.resize((300, 300))
img_tk = ImageTk.PhotoImage(img)
item1_pic = ttk.Label(root, image=img_tk)
item1_pic.image = img_tk
item1_pic.place(x=50, y=80)

img2 = Image.open("switch pic2.jpg")
img2 = img2.resize((300, 300))
img_tk = ImageTk.PhotoImage(img2)
item2_pic = ttk.Label(root, image=img_tk)
item2_pic.image = img_tk
item2_pic.place(x=50, y=450)

img3 = Image.open("switch pic3.jpg")
img3 = img3.resize((300, 300))
img_tk = ImageTk.PhotoImage(img3)
item3_pic = ttk.Label(root, image=img_tk)
item3_pic.image = img_tk
item3_pic.place(x=500, y=450)

combo.set("Select an option")


def on_combobox_selected(event):
    selected_value = combo.get()
    print(f"Selected: {selected_value}")


combo.bind("<<ComboboxSelected>>", on_combobox_selected)
root.mainloop()