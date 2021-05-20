# Imports
import tkinter as tk


# Functions

def start():
    global score_value
    global score
    file = open("cookie", "r")
    readfile = file.read()
    if readfile != "":
        score_value = int(readfile)
        score.set("Score: " + str(score_value))
    file.close()


def on_exit():
    file = open("cookie", "w")
    file.write(str(score_value))
    file.close()
    exit()


def plus():
    global score_value
    global score

    score_value += 1
    score.set("Score: " + str(score_value))


# Scene
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("450x700")
root.configure(bg="DarkOrchid3")
root.protocol("WM_DELETE_WINDOW", on_exit)

# Variables
score_value = 0
score = tk.StringVar(root, value="Score: " + str(score_value))

start()

# Design
AppName = tk.Label(text="Cookie Clicker", width=100, height=1, bg="DarkOrchid4", fg="white",
                   font=("font/main.ttf", 40)).pack(pady=20)

Cookie_Image = tk.PhotoImage(file="image/cookie.png")
Button = tk.Button(root, image=Cookie_Image, width=450, height=475, bg="DarkOrchid3",
                   activebackground="DarkOrchid3", borderwidth=0, highlightthickness=0, command=plus).pack()

Score = tk.Label(textvariable=score, width=100, height=1, bg="DarkOrchid4", fg="white",
                 font=("font/main.ttf", 35)).pack(pady=20)

# Mainloop
root.mainloop()
