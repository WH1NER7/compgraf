from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, colorchooser

def load_image(file_path):
    image = Image.open(file_path)
    return image

def get_pixel_color(image, x, y):
    pixel = image.getpixel((x, y))
    return pixel

def get_pixel_brightness(image, x, y):
    pixel = image.getpixel((x, y))
    brightness = sum(pixel) / 3
    return brightness

def display_pixel_info(x, y, color_listbox, brightness_listbox):
    pixel_color = get_pixel_color(image, x, y)
    pixel_brightness = get_pixel_brightness(image, x, y)
    color_listbox.insert(tk.END, f"Pixel ({x}, {y}): RGB {pixel_color}")
    brightness_listbox.insert(tk.END, f"Pixel ({x}, {y}): Brightness {pixel_brightness}")

def select_color():
    selected_color = colorchooser.askcolor(title="Select Color")[0]
    color_var.set(selected_color)

def determine_color():
    x1 = int(x1_var.get())
    y1 = int(y1_var.get())
    pixel_color = get_pixel_color(image, x1, y1)
    pixel_brightness = get_pixel_brightness(image, x1, y1)
    color_listbox.insert(tk.END, f"Pixel ({x1}, {y1}): RGB {pixel_color}")
    brightness_listbox.insert(tk.END, f"Pixel ({x1}, {y1}): Brightness {pixel_brightness}")

def change_color_in_selection():
    x1 = int(x1_var.get())
    y1 = int(y1_var.get())
    x2 = int(x2_var.get())
    y2 = int(y2_var.get())
    target_color = color_var.get()

    target_color = tuple(map(int, target_color.replace('(', '').replace(')', '').split(',')))
    modified_image = modify_image(image, x1, y1, x2, y2, target_color)
    display_image(modified_image)

def modify_image(image, x1, y1, x2, y2, target_color):
    modified_image = image.copy()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            modified_image.putpixel((x, y), target_color)
    return modified_image

def display_image(image):
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.photo = photo

def on_canvas_click(event):
    x, y = event.x, event.y
    display_pixel_info(x, y, color_listbox, brightness_listbox)

def determine_pixel_color():
    x = int(pixel_x_var.get())
    y = int(pixel_y_var.get())
    pixel_color = get_pixel_color(image, x, y)
    pixel_brightness = get_pixel_brightness(image, x, y)
    color_listbox.insert(tk.END, f"Pixel ({x}, {y}): RGB {pixel_color}")
    brightness_listbox.insert(tk.END, f"Pixel ({x}, {y}): Brightness {pixel_brightness}")

root = tk.Tk()
root.title("Image Viewer")

# Load image
image_path = "img1.jpg"
image = load_image(image_path)

# Canvas to display the image
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.bind("<Button-1>", on_canvas_click)

# Listboxes to display pixel info
color_listbox = tk.Listbox(root)
color_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

brightness_listbox = tk.Listbox(root)
brightness_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Button to select color
color_button = ttk.Button(root, text="Select Color", command=select_color)
color_button.pack()

# Entry forms for rectangle coordinates
x1_label = ttk.Label(root, text="x1:")
x1_label.pack()
x1_var = tk.StringVar()
x1_entry = ttk.Entry(root, textvariable=x1_var)
x1_entry.pack()

y1_label = ttk.Label(root, text="y1:")
y1_label.pack()
y1_var = tk.StringVar()
y1_entry = ttk.Entry(root, textvariable=y1_var)
y1_entry.pack()

x2_label = ttk.Label(root, text="x2:")
x2_label.pack()
x2_var = tk.StringVar()
x2_entry = ttk.Entry(root, textvariable=x2_var)
x2_entry.pack()

y2_label = ttk.Label(root, text="y2:")
y2_label.pack()
y2_var = tk.StringVar()
y2_entry = ttk.Entry(root, textvariable=y2_var)
y2_entry.pack()

# Entry form for target color
color_label = ttk.Label(root, text="Target Color:")
color_label.pack()
color_var = tk.StringVar()
color_entry = ttk.Entry(root, textvariable=color_var)
color_entry.pack()

# Button to change color in selection
change_color_button = ttk.Button(root, text="Change Color", command=change_color_in_selection)
change_color_button.pack()

# Pixel color determination form
pixel_color_frame = ttk.Frame(root)
pixel_color_frame.pack(pady=10)

pixel_x_label = ttk.Label(pixel_color_frame, text="x:")
pixel_x_label.grid(row=0, column=0, sticky="e")
pixel_x_var = tk.StringVar()
pixel_x_entry = ttk.Entry(pixel_color_frame, textvariable=pixel_x_var)
pixel_x_entry.grid(row=0, column=1)

pixel_y_label = ttk.Label(pixel_color_frame, text="y:")
pixel_y_label.grid(row=1, column=0, sticky="e")
pixel_y_var = tk.StringVar()
pixel_y_entry = ttk.Entry(pixel_color_frame, textvariable=pixel_y_var)
pixel_y_entry.grid(row=1, column=1)

determine_pixel_button = ttk.Button(pixel_color_frame, text="Determine Color", command=determine_pixel_color)
determine_pixel_button.grid(row=2, column=0, columnspan=2)

# Display the initial image
display_image(image)

root.mainloop()
