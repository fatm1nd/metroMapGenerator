from tkinter import *

root = Tk()
root.title("Moscow Metro Map Editor")

canvas = Canvas(root, width=800, height=600, bg='white')
canvas.pack(fill=BOTH, expand=True)

def start_line(event):
    global line
    x, y = event.x, event.y
    line = canvas.create_line(x, y, x, y, fill="red", width=15)

def draw_line(event):
    global line
    canvas.coords(line, (canvas.coords(line)[0], canvas.coords(line)[1], event.x, event.y))

def end_line(event):
    global line
    canvas.coords(line, (canvas.coords(line)[0], canvas.coords(line)[1], event.x, event.y))

def create_station(event):
    x, y = event.x, event.y
    canvas.create_oval(x-25, y-25, x+25, y+25, fill="white", outline="red", width=5)

canvas.bind("<Button-1>", start_line)
canvas.bind("<B1-Motion>", draw_line)
canvas.bind("<ButtonRelease-1>", end_line)
canvas.bind("<Button-3>", create_station)

def save_map():
    canvas.postscript(file="map.ps", colormode="color")

def load_map():
    canvas.delete("all")

save_button = Button(root, text="Save Map", command=save_map)
save_button.pack(side=LEFT)
load_button = Button(root, text="Load Map", command=load_map)
load_button.pack(side=LEFT)

root.mainloop()
