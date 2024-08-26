from tkinter import *
import requests

def get_album():
    response = requests.get(url='https://taylor-swift-api.sarbo.workers.dev/albums')
    response.raise_for_status()
    data = response.json()

    def show_album(index=0):
        if index < len(data):
            album_name = data[index]['title'] 
            canvas.itemconfig(album_info, text=album_name)
            window.after(2000, show_album, index + 1)

    show_album()

window = Tk()
window.title("Taylor's Album")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
album_info = canvas.create_text(150, 207, text="Taylor Swift's Album Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylor.png")
taylor_button = Button(image=taylor_img, highlightthickness=0, command=get_album)
taylor_button.grid(row=1, column=0)

window.mainloop()





