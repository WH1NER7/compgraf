import tkinter as tk
import numpy as np
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_graph():
    global canvas  # Объявляем canvas как глобальную переменную

    formula1 = formula_entry1.get()
    formula2 = formula_entry2.get()
    formula3 = formula_entry3.get()

    # Создание массива значений x
    x = np.linspace(-10, 10, 1000)

    try:
        # Создание массивов значений y для каждой формулы
        y1 = eval(formula1)
        y2 = eval(formula2)
        y3 = eval(formula3)

        # Создание графика
        figure = Figure(figsize=(6, 4), dpi=100)
        plot = figure.add_subplot(111)
        line1, = plot.plot(x, y1, 'r-', label=f'{formula1}')
        line2, = plot.plot(x, y2, 'g--', label=f'{formula2}')
        line3, = plot.plot(x, y3, 'b:', label=f'{formula3}')
        plot.legend()

        # Установка подписей для графиков
        line1.set_label(formula1)
        line2.set_label(formula2)
        line3.set_label(formula3)

        # Очистка предыдущего графика, если он был
        if canvas.get_tk_widget() is not None:
            canvas.get_tk_widget().destroy()

        # Создание нового холста для графика
        canvas = FigureCanvasTkAgg(figure, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        error_label.config(text=f"Ошибка: {str(e)}")


# Создание окна Tkinter
root = tk.Tk()
root.title("Построение графика")

# Создание форм для ввода формул
formula_label1 = tk.Label(root, text="Формула 1:")
formula_label1.pack()

formula_entry1 = tk.Entry(root)
formula_entry1.pack()

formula_label2 = tk.Label(root, text="Формула 2:")
formula_label2.pack()

formula_entry2 = tk.Entry(root)
formula_entry2.pack()

formula_label3 = tk.Label(root, text="Формула 3:")
formula_label3.pack()

formula_entry3 = tk.Entry(root)
formula_entry3.pack()

# Создание кнопки для построения графика
plot_button = tk.Button(root, text="Построить график", command=plot_graph)
plot_button.pack()

# Создание метки для отображения ошибок
error_label = tk.Label(root, fg="red")
error_label.pack()

# Создание холста для графика
figure = Figure(figsize=(6, 4), dpi=100)
plot = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack()

# Запуск основного цикла
root.mainloop()
