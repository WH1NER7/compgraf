import sys
import numpy as np
from PIL import Image
import OpenGL.GL as gl
import OpenGL.GLUT as glut

# Загрузка файла с символами "0" и "1"
file_path = "input.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

# Определение размеров изображения
image_height = len(lines)
image_width = len(lines[0].strip())

# Создание пустого изображения
image_data = np.zeros((image_height, image_width, 3), dtype=np.uint8)

# Преобразование символов в цвета пикселей
for y, line in enumerate(lines):
    line = line.strip()
    for x, char in enumerate(line):
        if char == "0":
            image_data[y, x] = [0, 0, 0]  # Черный цвет для "0"
        elif char == "1":
            image_data[y, x] = [255, 255, 255]  # Белый цвет для "1"

# Создание объекта Image из данных изображения
image = Image.fromarray(image_data)

# Сохранение изображения в формате BMP
output_path = "output.bmp"
image.save(output_path)

# Функция отображения
def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glRasterPos2i(-1, -1)
    gl.glDrawPixels(image_width, image_height, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image_data)
    glut.glutSwapBuffers()

# Функция изменения размеров окна
def reshape(width, height):
    gl.glViewport(0, 0, width, height)


# Инициализация GLUT
glut.glutInit(sys.argv)
glut.glutInitDisplayMode(glut.GLUT_RGB | glut.GLUT_DOUBLE | glut.GLUT_DEPTH)
glut.glutInitWindowSize(image_width, image_height)
glut.glutCreateWindow("Image Viewer")

# Задание функций отображения и изменения размеров окна
glut.glutDisplayFunc(display)
glut.glutReshapeFunc(reshape)

# Запуск основного цикла GLUT
glut.glutMainLoop()
