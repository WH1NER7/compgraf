from tkinter import *


class Pen:
    def __init__(self, canvas, start_point, end_point, thickness=1, color="black", line_type=None):
        self.canvas = canvas
        self.start_point = start_point
        self.end_point = end_point
        self.thickness = int(thickness)
        self.color = color
        self.line_type = line_type

    def draw(self):
        self.canvas.create_line(self.start_point[0], self.start_point[1], self.end_point[0], self.end_point[1],
                                width=self.thickness, fill=self.color, dash=self.line_type)

    def erase(self):
        self.canvas.create_line(self.start_point[0], self.start_point[1], self.end_point[0], self.end_point[1],
                                width=self.thickness, fill=self.canvas["background"], dash=self.line_type)


class Ellipse:
    def __init__(self, canvas, center, radius_x, radius_y, outline_color="black", fill_color="white",
                 background_color="white"):
        self.canvas = canvas
        self.center = center
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.outline_color = outline_color
        self.fill_color = fill_color
        self.background_color = background_color

    def draw(self):
        x1 = self.center[0] - self.radius_x
        y1 = self.center[1] - self.radius_y
        x2 = self.center[0] + self.radius_x
        y2 = self.center[1] + self.radius_y
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.outline_color, fill=self.fill_color)

    def erase(self):
        x1 = self.center[0] - self.radius_x
        y1 = self.center[1] - self.radius_y
        x2 = self.center[0] + self.radius_x
        y2 = self.center[1] + self.radius_y
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.background_color, fill=self.background_color)


class Polygon:
    def __init__(self, canvas, points, outline_color="black", fill_color="white"):
        self.canvas = canvas
        self.points = points
        self.outline_color = outline_color
        self.fill_color = fill_color

    def draw(self):
        self.canvas.create_polygon(self.points, outline=self.outline_color, fill=self.fill_color)

    def erase(self):
        self.canvas.create_polygon(self.points, outline=self.canvas["background"], fill=self.canvas["background"])


def clear_canvas():
    canvas.delete("all")


# Создание окна
root = Tk()
root.title("Drawing Shapes")

# Создание холста для рисования
canvas = Canvas(root, width=400, height=400)
canvas.pack()

# Создание объекта Pen
pen = Pen(canvas, (50, 50), (200, 200), thickness=3, color="red", line_type=(4, 4))
pen.draw()  # Рисование линии
# pen.erase()  # Стирание линии

# Создание объекта Ellipse
ellipse = Ellipse(canvas, (300, 150), 50, 80, outline_color="blue", fill_color="green", background_color="white")
ellipse.draw()  # Рисование эллипса
# ellipse.erase()  # Стирание эллипса

# Создание объекта Polygon
polygon = Polygon(canvas, [(100, 200), (200, 200), (150, 300)], outline_color="black", fill_color="yellow")
polygon.draw()  # Рисование многоугольника
# polygon.erase()  # Стирание многоугольника

# Создание кнопки "Стереть все"
clear_button = Button(root, text="Стереть все", command=clear_canvas)
clear_button.pack()

# Запуск основного цикла окна
root.mainloop()