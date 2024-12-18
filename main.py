import tkinter as tk
from tkinter import Canvas, Button
from PIL import Image, ImageDraw, ImageTk

def draw_bresenham_line(draw, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        draw.point((x1, y1), fill="black")
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def draw_flood_fill(image, x, y, new_color):
    width, height = image.size
    original_color = image.getpixel((x, y))
    if original_color == new_color:
        return

    pixels_to_check = [(x, y)]
    while pixels_to_check:
        x, y = pixels_to_check.pop()
        current_color = image.getpixel((x, y))
        if current_color == original_color:
            image.putpixel((x, y), new_color)
            if x > 0:
                pixels_to_check.append((x - 1, y))
            if x < width - 1:
                pixels_to_check.append((x + 1, y))
            if y > 0:
                pixels_to_check.append((x, y - 1))
            if y < height - 1:
                pixels_to_check.append((x, y + 1))

def display_image(canvas, image):
    canvas.image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image)

def on_bresenham_click():
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw_bresenham_line(draw, 50, 50, 350, 350)
    display_image(canvas, image)

def on_flood_fill_click():
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([100, 100, 300, 300], outline="black")
    draw_flood_fill(image, 200, 200, (255, 0, 0))
    display_image(canvas, image)

root = tk.Tk()
root.title("Raster Algorithms")

canvas = Canvas(root, width=400, height=400)
canvas.pack()

button1 = Button(root, text="Bresenham's Line", command=on_bresenham_click)
button2 = Button(root, text="Flood Fill", command=on_flood_fill_click)

button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)

root.mainloop()
