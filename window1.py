from tkinter import *


def btn_clicked():
    print("started")
    return "https://google.com"

def dialg():
    window = Tk()

    window.geometry("734x459")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=459,
        width=734,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(
        365.5, 223.5,
        image=background_img)

    img0 = PhotoImage(file=f"img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b0.place(
        x=438, y=291,
        width=196,
        height=57)

    window.resizable(False, False)
    window.mainloop()
